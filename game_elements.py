import time

# class to set up each team
class Team(object):

	# initialize team with player 1 and player 2
	def __init__(self, p1, p2):
		self.player1 = p1
		self.player2 = p2
		self.resource = 20

	# return player 1 of the team
	def getPlayer1(self):
		return player1

	#return player 2 of the team
	def getPlayer2(self):
		return player2

	def gain_resource(self, a):
		self.resource += a

	def lose_resource(self, a):
		self.resource -= a

# parent class for game elements
class GameElement(object):

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

	# checks if player has vision of the element
	def hasVision(self, u):
		if u in self.vision:
			return true
		else:
			return false

	# checks if player has control of the element
	def hasControl(self, u):
		if u in self.control:
			return true
		else:
			return false

	# check the health of the element
	def getHealth(self):
		return self.health

# parent class for structures
class Structures(GameElement):

	def __init__(self, t, all_t, x, y, h, r, a):
		self.armour = a 				# armour value to reduce damage
		super(Structures, self).__init__(t, all_t, x, y, h, r):

	# reduces health based on damage taken
	def takeDamage(self, d):
		if d > self.armour:
			self.health = self.health - (d - self.armour)
		else:
			self.health -= 1

# parent class for units
class Units(GameElement):

	def __init__(self, t, all_t, x, y, h, r, m):
		self.move_speed = m 			# time to move one grid unit
		super(Units, self).__init__(t, all_t, x, y, h, r):

	# reduces health based on damage taken
	def takeDamage(self, d):
		self.health -= d

	# moves the unit one block if possible
	def move(self, u, x, y):
		x_diff = x - x_location
		y_diff = y - y_location
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

class Farm(Structures):

	def __init__(self, t, all_t, x, y):
		super(Farm, self).__init__(self, t, all_t, x, y, 100, "cow", 1)

	def 

class Barn(Structures):

	def __init__(self, t, all_t, x, y):
		super(Farm, self).__init__(self, t, all_t, x, y, 150, "cow", 2)
		self.units = {"builder" : {"time" : 15, "resource" : 20}, "fighter" : {"time" : 23, "resource" : 30}, "magic" : {"time" : 27, "resource" : 20}}

	def makeCow(self, u, t):
		if super(Barn, self).hasControl(u):
			if self.belong.resource >= self.units[t]["resource"]:
				self.belong.lose_resource(self.units[t]["resource"])
				time.sleep(self.units[t]["time"])
				