import time

# class to set up each team
class Team(object):

	# initialize team with player 1 and player 2
	def __init__(self, p1, p2):
		self.player1 = p1
		self.player2 = p2

	# return player 1 of the team
	def getPlayer1(self):
		return player1

	#return player 2 of the team
	def getPlayer2(self):
		return player2


# parent class for
class GameElement(object):

	def __init__(self, t, all_t, x, y, h, r):
		self.vision = {}				# dictionary of players with vision
		self.control = {}				# dictionary of players with control
		self.vision[t.getPlayer1] = t.getPlayer1	# add one team's player 1 to players with vision
		self.control[t.getPlayer1] = t.getPlayer1	# add one team's player 1 to players with control
		for teams in all_t:				# add all other teams' player 2 to players with vision
			self.vision[teams.getPlayer2] = teams.getPlayer2
		self.x_location = x 			# set the starting x location
		self.y_location = y 			# set the starting y location
		self.health = h 				# set the health
		self.race = r 					# set the race

	def hasVision(self, u):
		if u in self.vision:
			return true
		else:
			return false

	def hasControl(self, u):
		if u in self.control:
			return true
		else:
			return false

	def getHealth(self):
		return self.health

	def takeDamage(self, d):
		self.health -= d

class Structures(GameElement):

	def __init__(self, t, all_t, x, y, h, r, a):
		self.armour = a 				# armour value to reduce damage
		super(Structures, self).__init__(t, all_t, x, y, h, r):

	def takeDamage(self, d):
		if d > self.armour:
			self.health = self.health - (d - self.armour)
		else:
			self.health -= 1

class Units(GameElement):

	def __init__(self, t, all_t, x, y, h, r, m):
		self.move_speed = m 			# time to move one grid unit
		super(Units, self).__init__(t, all_t, x, y, h, r):

	def takeDamage(self, d):
		self.health -= d

	def move(self, u, x_diff, y_diff):
		if super.hasControl(u):
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

class Barn(Structures):

	def __init__(self, t, all_t, x, y):
		super(Barn, self).__init__(self, t, all_t, x, y, 100, "cow", 1)

	def 