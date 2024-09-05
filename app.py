from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/about')
def about():
    return render_template('/about.html')

@app.route('/blog')
def blog():
    return render_template('/blog.html')

@app.route('/projects')
def projects():
    return render_template('/project.html')

@app.route('/contact_me')
def contact_me():
    return render_template('/contact_me.html')

if __name__== '__main__':
    app.run(debug=True)