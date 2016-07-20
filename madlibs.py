from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """asking user if they want to play."""

    yes_no = request.args.get("answer")

    if yes_no == "yes":
        return render_template("game.html", answer=yes_no)
    else:
        return render_template("goodbye.html", answer=yes_no)


@app.route('/madlibs')
def show_madlibs_form():
    """route to madlib."""

    person_name = request.args.get("person")
    chosen_color = request.args.get("color")
    chosen_noun = request.args.get("noun")
    chosen_adjective = request.args.get("adjective")

    return render_template("madlibs.html", person=person_name, color=chosen_color,
        noun=chosen_noun, adjective=chosen_adjective)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
