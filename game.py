from google.appengine.api import users
from google.appengine.ext.webapp import template

import webapp2
import os

class GamePage(webapp2.RequestHandler):

    def get(self):
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(template.render("main.html", {}))

application = webapp2.WSGIApplication([
    ('/', GamePage),
], debug=True)