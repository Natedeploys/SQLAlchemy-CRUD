#Take advantage of functionality
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

#Use to decipher message sent from the server
import cgi

# import CRUD Operations
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#Handler class
#Indicate what code to execute

class WebServerHandler(BaseHTTPRequestHandler):

    #Handle all get requests our web server receives
    def do_GET(self):
        #get the url sent by the client, look for /hello
        if self.path.endswith("/hello"):
            #Response with a successful status code
            self.send_response(200)
            #Reply with text in html
            self.send_header('Content-type', 'text/html')
            #Blank line indicating http headers
            self.end_headers()
            message = ""
            message += "<html><body>Hello!"
            message += """<form method='POST' enctype='multipart/form-data'
            action='hello'><h2>What would you like to say?</h2>
            <input name='message' type='text' ><input type='submit'
            value='Submit'></form>"""
            message += "</body></html>"
            #Send message to client
            self.wfile.write(message)
            #Show in our terminal
            print message
            #Exit statement with return command
            return
        #get the url sent by the client, look for /hello
        elif self.path.endswith("/hola"):
            #Response with a successful status code
            self.send_response(200)
            #Reply with text in html
            self.send_header('Content-type', 'text/html')
            #Blank line indicating http headers
            self.end_headers()
            message = ""
            message += "<html><body>Hola <a href='/hello'>Return</a>"

            message += """<form method='POST' enctype='multipart/form-data'
            action='hello'><h2>What would you like to say?</h2>
            <input name='message' type='text' ><input type='submit'
            value='Submit'></form>"""
            message += "</body></html>"
            #Send message to client
            self.wfile.write(message)
            #Show in our terminal
            print message
            #Exit statement with return command
            return

        elif self.path.endswith("/edit"):
            #grab the id number from the url, split values by slash get the 3rd in index
            restaurantIDPath = self.path.split("/")[2]
            #Get the restaurant with the id
            myRestaurantQuery = session.query(Restaurant).filter_by(id =
                restaurantIDPath).one()
            #if not empty then continue
            if myRestaurantQuery != [] :
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()
                message = "<html><body>"
                message += "<h1>%s</h1>" % myRestaurantQuery.name
                #Pass in the id to post data to the url
                message += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>" % restaurantIDPath
                message += "<input name = 'NewRestaurant' type='text' placeholder = '%s'>" % myRestaurantQuery.name
                message += "<input type = 'submit' value='Rename'>"
                message += "</form>"
                message += "</body></html>"

                self.wfile.write(message)

        #Objective 1 - Restaurant
        #get the url sent by the client, look for /hello
        elif self.path.endswith("/restaurants"):
            #Response with a successful status code
            self.send_response(200)
            #Reply with text in html
            self.send_header('Content-type', 'text/html')
            #Blank line indicating http headers
            self.end_headers()
            message = ""
            message += "<html><body><a href='/restaurants/new'>Make a New Restaurant Here</a>"

            #Query database and return a single restaurant name
            items = session.query(Restaurant).all()
            for item in items:
                message += "<p>%s</p>" % item.name
                message += "<a href='/restaurants/%s/edit'>Edit</a>" % item.id
                message += "<a href='/restaurants/%s/delete'>Delete</a><br>" % item.id

            message += "</body></html>"
            #Change to return all restaurant names and add to html
            #using a for loop

            #Send message to client
            self.wfile.write(message)
            #Show in our terminal
            print message
            #Exit statement with return command
            return

        elif self.path.endswith("/restaurants/new"):
            #Response with a successful status code
            self.send_response(200)
            #Reply with text in html
            self.send_header('Content-type', 'text/html')
            #Blank line indicating http headers
            self.end_headers()
            message = ""
            message += "<html><body>Add Restaurant -<a href='/restaurants'> Go Back</a>"

            message += """<form method='POST' enctype='multipart/form-data'
            action='/restaurants/new'><h2>What would you like to say?</h2>
            <input name='NewRestaurant' type='text' placeholder='New Restaurant Name'>
            <input type='submit' value='Create'></form>"""
            message += "</body></html>"
            #Change to return all restaurant names and add to html
            #using a for loop

            #Send message to client
            self.wfile.write(message)
            #Show in our terminal
            print message
            #Exit statement with return command
            return

        elif self.path.endswith("/delete"):
            #grab the id number from the url, split values by slash get the 3rd in index
            restaurantIDPath = self.path.split("/")[2]
            #Get the restaurant with the id
            myRestaurantQuery = session.query(Restaurant).filter_by(id =
                restaurantIDPath).one()
            #if not empty then continue
            if myRestaurantQuery != [] :
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()
                message = "<html><body>"
                message += "<h1>Are you sure to you want to delete %s?</h1>" % myRestaurantQuery.name
                #Pass in the id to post data to the url
                message += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete'>" % restaurantIDPath
                message += "<input type = 'submit' value='Delete'>"
                message += "</form>"
                message += "</body></html>"
                #write back output to client
                self.wfile.write(message)

        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                #extract information from the form
                if ctype == 'multipart/form-data':
                    #collect all fields in the form
                    fields=cgi.parse_multipart(self.rfile, pdict)
                    #get the value of a specific field passed in by form
                    messagecontent = fields.get('NewRestaurant')
                    #grab the id number from the url, split values by slash get the 3rd in index
                    restaurantIDPath = self.path.split("/")[2]

                    #perform query to find object with matching id
                    myRestaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()

                    if myRestaurantQuery != [] :
                        myRestaurantQuery.name = messagecontent[0]
                        session.add(myRestaurantQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        #redirect to restaurants homepage
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

            if self.path.endswith("/delete"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                #grab the id number from the url, split values by slash get the 3rd in index
                restaurantIDPath = self.path.split("/")[2]

                #perform query to find object with matching id
                myRestaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()

                if myRestaurantQuery != [] :
                    session.delete(myRestaurantQuery)
                    session.commit()
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    #redirect to restaurants homepage
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            #look for the path
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                #extract information from the form
                if ctype == 'multipart/form-data':
                    #collect all fields in the form
                    fields=cgi.parse_multipart(self.rfile, pdict)
                    #get the value of a specific field passed in by form
                    messagecontent = fields.get('NewRestaurant')

                    # Create new Restaurant Object
                    newRestaurant = Restaurant(name=messagecontent[0])
                    session.add(newRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    #redirect to restaurants homepage
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

        except:
            pass


#Main method

#Instantiate our server and specify what port to listen on

def main():

    try:
        #Specify port to listen on
        port = 8080
        #Define webserverHandler above
        server = HTTPServer(('', port), WebServerHandler)
        print "Web Server running on port %s" % port
        #Keep server constantly listening until interrupted
        server.serve_forever()

    #Triggered when user presses ctrl+c on the keyboard
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

#Entry point in the code tell it to immediate run main
if __name__ == '__main__':
    main()