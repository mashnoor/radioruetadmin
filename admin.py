from flask import Flask, render_template, request
import peewee
from peewee import *
import datetime, time

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
#db.create_table(OnlineMsg)

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


@app.route('/setonlinemsg', methods=['POST'])
def setonlinemsg():
    name = request.form.get('name')
    department = request.form.get('department')
    series = request.form.get('series')
    message = request.form.get('message')
    onlnmsg = OnlineMsg(name=name, department=department, series=series, message=message)
    onlnmsg.save()
    return "Saved"

@app.route('/setsecretmsg', methods=['POST'])
def setsecretmsg():

    message = request.form.get('message')
    curr_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    scrtmsg = SecretMsg(msg=message, time=curr_time)
    scrtmsg.save()
    return "Saved"



if __name__=="__main__":
    app.run(port=5000)