from flask import Flask, request
#Import Flask framework and 'request' to handle form data

app = Flask(__name__)
#Create a new Flask web application

#Handles the root URL '/' (when user first visits the site)
@app.route('/')
def index():
    return '''
      <form method="POST" action="/submit">
        <input type="text" name="username" placeholder="Enter your name">
        <button type="submit">Submit</button>
        </form>
        '''
#Handles the form submission (POST request to '/submit')
@app.route('/submit', methods=['POST'])
def submit():
    #Get the value entered by the user from the form
    name = request.form['username']#From the input field

    #Send a response with the user's name
    return f'<h2>Hello, {name}!</he>'

app.run(host='0.0.0.0', port=3000)