from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.api import channel
from google.appengine.ext import db
from google.appengine.api import background_thread
#from game_elements import *

import webapp2
import json

class GamePage(webapp2.RequestHandler):

	def get(self):
		self.response.headers.add_header('Access-Control-Allow-Origin', '*')
		self.response.headers.add_header('Access-Control-Allow-Methods', 'GET, POST, PUT')
		self.response.headers['Content-Type'] = 'text/html'
		self.response.out.write(template.render("main.html", {}))

	def post(self):
		row = self.request.get('row')
		col = self.request.get('col')

class StartGame(webapp2.RequestHandler):

	def post(self):
		self.request.get('start')
		user = users.get_current_user()
		if user:
			player = Player.get_by_key_name(user.user_id())
			if not player:
				player = Player(key_name = user.user_id(),
								name = user. user_id(),
								status = 'off')
			player.status = 'waiting'
			

application = webapp2.WSGIApplication([
	('/', GamePage),
	('/start', StartGame)
], debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()