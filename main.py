from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user

app = Flask(__name__)
# Set secret key for login session
app.secret_key = "my_secret_key"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

users = {}
posts = []

ERROR_EMPTY = '⚠️ WRITE TILTE AND CONTENTS ⚠️'

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def get_id(self):
        return str(self.id)

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)
    

@app.route('/')
def home():
    return redirect(url_for('board'))  # root → board

@app.route('/board')
def board():
    return render_template('board.html', posts=posts)  # list posts

@app.route('/write', methods=['GET'])
def write_form():
    return render_template('write.html', error=None) # show form

@app.route('/write', methods=['POST'])
def write_post():
    title = request.form.get('title', '').strip()
    content = request.form.get('content', '').strip()

    if not title or not content:
        # Server-Side Validation Error Messages
        return render_template('write.html', error=ERROR_EMPTY)  
       

        # simple error massage
    posts.append({
        'id':       len(posts) + 1,
        'title':    title,
        'content':  content

    })  # add post


    return redirect(url_for('board'))  # back to board

# User register page
@app.route('/register', methods=['GET', 'POST'])
def register():

    
    if request.method == 'POST':
        # Get input values
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        print(f"[DEBUG] username: {username}, password: {password}")

        # Check if fields are empty
        if not username or not password:
            return render_template('register.html', error="Please enter all fields")
        
        # Check if username is already taken
        for u in users.values():
            if u.username == username:
                return render_template('register.html', error="The username already exists")

        # Save new user
        user_id = len(users) + 1
        user = User(id=user_id, username=username, password=password)
        users[str(user_id)] = user
        
        # Auto login after register
        login_user(user)
        return redirect(url_for('board'))
    
    # Show register form
    return render_template('register.html', error=None)

# User login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("📥 A POST request received")

        # Get input values
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        # Check if user info is correct
        for user in users.values():
            if user.username == username and user.password == password:
                login_user(user)
                flash('✅ Login successful', 'success')
                return redirect(url_for('board'))

        # If login failed
        flash('❌ Invalid username or password', 'error')

    # Show login form
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



