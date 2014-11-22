from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.api import channel
from google.appengine.ext import db
from google.appengine.api import background_thread

import webapp2

class GamePage(webapp2.RequestHandler):

	def get(self):
		user = users.get_current_user()
		if user:
			self.response.headers.add_header('Access-Control-Allow-Origin', '*')
			self.response.headers.add_header('Access-Control-Allow-Methods', 'GET, POST, PUT')
			self.response.headers['Content-Type'] = 'text/html'
			self.response.out.write(template.render("main.html", {}))
		else:
			self.redirect(users.create_login_url(self.request.uri))

application = webapp2.WSGIApplication([
	('/', GamePage),
], debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()