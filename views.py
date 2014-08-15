from flask import render_template, request
from app import app
from flask.json import jsonify
import pymysql as mdb


db= mdb.connect(user="root", host="localhost", db="world_innodb", charset='utf8')

@app.route("/career")
def careerpage():
	return render_template("newbootstrap.html")
@app.route("/index")
def cities_page_fancy():
#  with db:
#    cur = db.cursor()
#    cur.execute("SELECT Name, CountryCode, Population FROM city ORDER BY Population LIMIT 15;")
#    query_results = cur.fetchall()
#  cities = []
#  for result in query_results:
#    cities.append(dict(name=result[0], country=result[1], population=result[2]))
  user = { 'nickname': 'Kevin' } # fake user
  return render_template('starter.html', user=user) 

@app.route("/")
def homepage():
  return render_template("home2.html")

#@app.route("/result")
#def resultpage():
#  print request.args.get('func')
  
#  return render_template("result.html")

@app.route("/jquery")
def index_jquery():
  return render_template('index_js.html')
  
@app.route("/db_json")
def cities_json():
    with db:
        cur = db.cursor()
        cur.execute("SELECT Name, CountryCode, Population FROM city ORDER BY Population DESC;")
        query_results = cur.fetchall()
    cities = []
    for result in query_results:
        cities.append(dict(name=result[0], country=result[1], population=result[2]))
    return jsonify(dict(cities=cities))


