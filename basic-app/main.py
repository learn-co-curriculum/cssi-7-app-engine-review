import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<!DOCTYPE html>')
        self.response.write('<title>My First Web Page</title>')
        self.response.write('<p>My First Web Page</p>')
        self.response.write('<p>Hello, World!</p>')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
