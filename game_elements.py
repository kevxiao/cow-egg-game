from google.appengine.api import background_thread
from google.appengine.ext import db

import time

class Player(db.Model):
	name = db.StringProperty()
	status = db.StringProperty()

# class to set up each team
class Team(object):

	# initialize team with player 1 and player 2
	def __init__(self, p1, p2):
		self.player1 = p1
		self.player2 = p2
		self.resource = 20

	# return player 1 of the team
	def getPlayer1(self):
		return self.player1

	# return player 2 of the team
	def getPlayer2(self):
		return self.player2

	# increase resource for the team
	def gainResource(self, a):
		self.resource += a

	# decrease resource for the team
	def loseResource(self, a):
		self.resource -= a

class Map(object):

	def __init__(self, size):
		map_grid = [[None for x in range(5)] for x in range(5)]

# parent class for game elements
class GameElement(object):

	# initialize team with team, all teams in game, x position, y position, health and race
	def __init__(self, t, all_t, x, y, h, r):
		self.belong = t
		self.vision = {}				# dictionary of players with vision
		self.control = {}				# dictionary of players with control
		self.vision[t.getPlayer1()] = t.getPlayer1()	# add one team's player 1 to players with vision
		self.control[t.getPlayer1()] = t.getPlayer1()	# add one team's player 1 to players with control
		for teams in all_t:				# add all other teams' player 2 to players with vision
			self.vision[teams.getPlayer2()] = teams.getPlayer2()
		self.x_location = x 			# set the starting x location
		self.y_location = y 			# set the starting y location
		self.health = h 				# set the health
		self.race = r 					# set the race

	# check the team that the element belongs to
	def belongsTo(self):
		return self.belong

	# checks if player has vision of the element
	def hasVision(self, u):
		if u in self.vision:
			return True
		else:
			return False

	# checks if player has control of the element
	def hasControl(self, u):
		if u in self.control:
			return True
		else:
			return False

	# check the health of the element
	def getHealth(self):
		return self.health

# parent class for structures
class Structures(GameElement):

	# initialize structure with everything from game element plus armour value
	def __init__(self, t, all_t, x, y, h, r, a):
		self.armour = a 				# armour value to reduce damage
		super(Structures, self).__init__(t, all_t, x, y, h, r)

	# reduces health based on damage taken
	def takeDamage(self, d):
		if d > self.armour:
			self.health = self.health - (d - self.armour)
		else:
			self.health -= 1

# parent class for units
class Units(GameElement):

	# initialize unit with everything from game element plus move speed value
	def __init__(self, t, all_t, x, y, h, r, m):
		self.move_speed = m 			# time to move one grid unit
		super(Units, self).__init__(t, all_t, x, y, h, r)

	# reduces health based on damage taken
	def takeDamage(self, d):
		self.health -= d

	# moves the unit one block if possible
	def move(self, u, x, y):
		x_diff = x - self.x_location
		y_diff = y - self.y_location
		if super(Units, self).hasControl(u):
			if self.y_location % 2 == 0:
				if abs(y_diff) == 1 and x_diff == -1:
					raise MoveError("Move location is too far")
			else:
				if abs(y_diff) == 1 and x_diff == 1:
					raise MoveError("Move location is too far")
			if abs(y_diff) > 1 or abs(x_diff) > 1:
				raise MoveError("Move location is too far")
			time.sleep(self.move_speed)
			self.x_location += x_diff
			self.y_location += y_diff
		else:
			raise MoveError("User does not have control")

# class for farm structure (resource producing structure for cow race)
class Farm(Structures):

	# initialize farm with team, all teams in game, x position and y position
	def __init__(self, t, all_t, x, y):
		super(Farm, self).__init__(self, t, all_t, x, y, 100, "cow", 1)
		p = background_thread.start_new_background_thread(target=self.gatherResource)

	# increase resources 
	def gatherResource(self):
		while True: 
			time.sleep(2)
			self.belong.gainResource(5)

# class for barn structure (unit making structure for cow race)
class Barn(Structures):

	# dictionary of all units that the barn makes with their corresponding build time and resource cost
	units = {"builder" : {"time" : 15, "resource" : 20}, "fighter" : {"time" : 23, "resource" : 30}}

	# initialize barn with team, all teams in game, x position and y position
	def __init__(self, t, all_t, x, y):
		super(Farm, self).__init__(self, t, all_t, x, y, 150, "cow", 2)

	# makes a new unit
	def makeCow(self, u, t):
		if super(Barn, self).hasControl(u):
			if self.belong.resource >= self.units[t]["resource"]:
				self.belong.loseResource(self.units[t]["resource"])
				time.sleep(self.units[t]["time"])
				# insert code to put unit on map

# class for the builder unit
class Builder(Units):

	# dictionary of all structures that the builder makes with their corresponding build time and resource cost
	structures = {"Farm" : {"time" : 15, "resource" : 20}, "Barn" : {"time" : 25, "resource" : 25}}

	# initialize builder with team, all teams in game, x position and y position
	def __init__(self, t, all_t, x, y):
		super(Builder, self).__init__(self, t, all_t, x, y, 40, "cow", 1.5)

	# make a new structure
	def makeStruct(self, u, t):
		if super(Builder, self).hasControl(u):
			if self.belong.resource >= self.structures[t]["resource"]:
				self.belong.loseResource(self.structures[t]["resource"])
				time.sleep(self.structures[t]["time"])
				# insert code to put structure on map

# class for the fighter unit
class Fighter(Units):

	# initialize fighter with team, all teams in game, x position and y position
	def __init__(self, t, all_t, x, y):
		super(Fighter, self).__init__(self, t, all_t, x, y, 70, "cow", 1.2)
		self.damage = 10

	# attack enemies on the same location
	def attack(self, u):
		# for all units on the same location
			if u.belongsTo() != self.belongs:
				u.takeDamage(self.damage)