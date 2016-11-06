import logging

from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def start():
    name = "Bobby"
    welcome_msg = render_template('welcome', firstname=name)
    session.attributes['name'] = name
    return question(welcome_msg)

@ask.intent("QuestionIntent")
def prompt_user():
    prompt = render_template('question')
    return question(prompt)

@ask.intent("AnswerIntent")
def get_pills():
    with open("pills.txt", "r") as file:
        data = file.readlines()
    data = list(map(lambda x:x.replace('\n', ''), data))
    list_message = render_template('list', list=data)
    return statement(list_message)

@ask.intent("AddToListIntent")
def add_to_list(pill):
    with open("pills.txt", "a") as file:
        file.write(pill + '\n')
    add_message = render_template('add')
    return question(add_message)

if __name__ == '__main__':
    app.run(debug=True)