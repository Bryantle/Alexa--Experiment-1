from flask import Flask, render_template, App
from flask_ask import question, session, Ask, statement, convert_errors, version, request, context

app = Flask(__name__)
ask = Ask(app, "/")

@ask.launch
def launched():
    return question('Welcome to Foo').reprompt("I didn't get a response. I said welcome to foo.")

@ask.intent('HelloIntent')
def hello(firstname):
    message = render_template('hello', firstname = firstname)
    return statement(message).simple_card('Hello', message)

@ask.intent('HelloWorld')
def helloworld():
    message = 'Hello World'
    return statement(message)

@ask.intent('WeatherIntent', mapping= {'city': 'City'})
def weather(city):
    return statement('I predict great weather for {}'.format(city))

@ask.intent('AddIntent', convert = {'x':int, 'y':int})
def adder(x,y):
    z = x + y
    return statement('{} plus {} equals {}'.format(x,y,z))

@ask.intent('AgeIntent', convert = {'age': int})
def say_age(age):
    if age in convert_errors:
        return question('Please repeat your age.')
    else:
        return statement('Your age is {}'.format(age))

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    app.run(debug = True)
