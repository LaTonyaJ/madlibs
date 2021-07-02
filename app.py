from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Tink870$'
debug = DebugToolbarExtension(app)


@app.route('/homepage')
def show_form():
    """Shows the story form"""
    prompts = story.prompts
    return render_template('homepage.html', prompts=prompts)


@app.route('/story')
def show_story():
    """Show story"""
    text = story.generate(request.args)
    return render_template('story.html', text=text)


@app.route('/')
def landing_page():
    """Clear Not Found Error"""
    return"""
    <h1>Welcome to MadLIBS!!!</h1>
    <p>I'll ask a couple questions and you'll make a story.....</p>
    """
