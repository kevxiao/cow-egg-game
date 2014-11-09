from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.api import channel
from google.appengine.ext import db

import webapp2
import os

class GamePage(webapp2.RequestHandler):

    def get(self):
    	user = users.get_current_user()

        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(template.render("main.html", {}))
        self.response.out.write('Hello, ' + user.nickname())

application = webapp2.WSGIApplication([
    ('/', GamePage),
], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()