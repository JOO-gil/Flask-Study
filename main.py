from flask import Flask, request, render_template

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
  return render_template('form.html')
  
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