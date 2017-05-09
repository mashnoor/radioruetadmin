from flask import Flask, render_template
import peewee
from peewee import *

db = MySQLDatabase('radioruet_api', user='root', passwd='92702689')

class OnlineMsg(peewee.Model):
    name = CharField()
    department = CharField()
    series = CharField()
    message = CharField()

    class Meta:
        database = db

class SecretMsg(peewee.Model):
    msg = CharField()
    time = DateTimeField()
    class Meta:
        database = db

#db.create_table(SecretMsg)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/onlinemessages')
def onlinemessage():
    onlinemsgs = OnlineMsg.select()
    return render_template("onlinemessages.html", messages=onlinemsgs)

@app.route('/secretmessages')
def secretmessage():
    secretmsgs = SecretMsg.select()
    return render_template("secretmessages.html", messages=secretmsgs)

@app.route('/archive')
def archive():
    return "Archive"

@app.route('/statistics')
def statistics():
    return "Statistics"

@app.route('/logout')
def logout():
    return "Logout"


if __name__=="__main__":
    app.run(port=5001)