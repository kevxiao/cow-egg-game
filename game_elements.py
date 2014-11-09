from abc import ABCMeta, abstractmethod

# class to set up each team
class Team(object):

	# initialize team with player 1 and player 2
	def __init__(self, p1, p2):
		self.player1=p1
		self.player2=p2

	# return player 1 of the team
	def getPlayer1(self):
		return player1

	#return player 2 of the team
	def getPlayer2(self):
		return player2


# parent class for
class GameElement(object):

	__metaclass__ = ABCMeta

	@abstractmethod
	def setVision(self, users):
		self.vision=users

	@abstractmethod
	def setControl(self, user):
		self.control=user

	@abstractmethod
	def hasVision(self, user):
		if user in self.vision:
			return true
		else:
			return false

	@abstractmethod
	def hasControl(self, user):
		if user == self.control:
			return true
		else:
			return false

class Structures(GameElement):

	__metaclass__ = ABCMeta

	@abstractmethod
	def 