import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # This gets the result of ?name=value when appended to the end of the
        # URL request. For example, if the URL requesting this page was
        # http://localhost:8080?name=victoria, name_value would be 'victoria'.
        name_value = self.request.get('name')
        exclamations_value = self.request.get('exclamations')

        # If there is no 'name' parameter, it is an empty string.
        # An empty string in Python is "falsey" and therefore returns false.
        # We set name_value to 'world' if there's no query parameter.
        if not name_value:
            name_value = 'world'

        punct_count = int(exclamations_value)
        if not exclamations_value:
            punct_count = 1
        punct = punct_count * "!"
        
        self.response.write('<!DOCTYPE html>')
        self.response.write('<title>My First Web Page</title>')
        self.response.write('<p>My First Web Page</p>')
        self.response.write('<p>Hello, {}{}</p>'.format(name_value, punct))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
