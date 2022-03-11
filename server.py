from math import remainder
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def tables():
    users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]   
    user_length = len(users)
    return render_template("index.html",users = users, user_length = user_length )

if __name__=="__main__":
    app.run(debug=True)