import jinja2 
import os 
import webapp2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_vars = {
            "page_title": "My First Web Page",
            "greeting": "Aloha"
        }
        template = jinja_environment.get_template('hello.html')
        self.response.out.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
