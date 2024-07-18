import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict
import datetime 

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
	print("Running in test mode")
	mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
	mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),user=os.getenv("MYSQL_USER"),
                     password=os.getenv("MYSQL_PASSWORD"),host=os.getenv("MYSQL_HOST"),
                     port=3306)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = mydb
mydb.connect()
mydb.create_tables([TimelinePost])

print(mydb)
@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellows", url=os.getenv("URL"))

@app.route('/MatthewChang')
def mc():
    return render_template('mc.html', title="Matthew Chang", url=os.getenv("URL"))

@app.route('/VuongHo')
def vh():
    return render_template('vh.html', title="Vuong Ho", url=os.getenv("URL"))

@app.route('/Hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"))

@app.route('/testing')
def tt():
    return render_template('mc.html', title="testing")

@app.route('/timeline')
def timelines():
    print("accessed")
    return render_template('timeline.html',title="Timeline")

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form.get('name','')
    email = request.form.get('email','')
    content = request.form.get('content','')
    if name == '':
        return jsonify({'error':'Invalid name'}), 400
    elif '@' not in email or email == '':
        return jsonify({'error':'Invalid email'}), 400
    elif content == '':
        return jsonify({'error':'Invalid content'}), 400
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post/del', methods=['DELETE'])
def del_timeline_post(id):
    TimelinePost.delete_by_id(id)
    return "Deleted Successfully"

