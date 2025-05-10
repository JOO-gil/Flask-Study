from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

ERROR_EMPTY = '⚠️ WRITE TILTE AND CONTENTS ⚠️'

posts = []

@app.route('/')
def home():


    return redirect(url_for('board'))  # root → board

@app.route('/board')
def board():
    return render_template('board.html', posts=posts)  # list posts

@app.route('/write', methods=['GET'])
def write_form():
    return render_template('write.html', error=None)  # show form


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



