import os
import datetime
from flask import Flask, render_template
# using https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application

# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)

#color = os.environ.get('APP_COLOR')
color = "red"
current_utc_dt=datetime.datetime.utcnow()

# The route() function of the Flask class is a decorator which tells the application which URL should call the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():
  print(color, current_utc_dt)
  #return render_template("index.html", color=color)
  #return render_template('index.html', utc_dt=datetime.datetime.utcnow())
  return render_template('index.html', color="red", utc_dt=datetime.datetime.utcnow())
  #return render_template('index.html')

@app.route('/about/')
def about():
  return render_template('about.html')

@app.route('/comments/')
def comments():
  comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
             ]

  return render_template('comments.html', comments=comments)

# main
if __name__ == '__main__':
  # run() method of Flask class runs the application on the local development server.
  #app.run(debug=True)   # default port is 5000
  app.run(host="0.0.0.0", port="8080")
