from flask import Flask, request

# Initialize the Flask application
app = Flask(__name__)

#For home page
@app.route('/')
def home():
  return 'Hello, World!'

#For about page
@app.route('/about')
def about():
  return 'This is About page.'

#For contact page
@app.route('/contact')
def contact():
  return 'This is the Contact page.'

#For form page (using HTML in here)
@app.route('/form')
def form():
  return '''
  <html>
  <head>
    <style>
      body {
          text-align: center;
          font-family: Arial, sans-serif;
          margin-top: 50px;
      }
      input[type="text"] {
          padding: 10px;
          font-size: 1rem;
          width:200px;
          margin-bottom: 20px;
      }
      button {
          padding: 10px 20px;
          font-size: 1rem;
          margin-bottom: 20px;
      }
      form {
          display: inline-block;
      }
    </style>
  </head>
  <body>
    <form method="POST" action="/submit">
    <input type="text" name="username" placeholder="Enter your name"><br>
    <button type="submit">Submit</button>
    </form>
  </body>
  </html>
  '''
#For handling form submission
@app.route('/submit', methods=['POST'])
def submit():
  # Retrieve the submitted username from the form
  name = request.form['username']
  # Display a greeting message using the submitted username
  return f'<h2>Hello, {name}!</h2>'

# Start the Flask server
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3000)