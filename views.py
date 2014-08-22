from flask import render_template, request
from app import app
from flask.json import jsonify
import pymysql as mdb
import pickle
import snap as snap
from pathfunc import * 
f=open('nodename','rb')
nodename = pickle.load(f)

FIn = snap.TFIn("test.graph")
G2 = snap.TNEANet.Load(FIn)

#db= mdb.connect(user="root", host="localhost", db="world_innodb", charset='utf8')

@app.route("/career")
def careerpage():
	return render_template("newbootstrap.html")
#@app.route("/index")
#def cities_page_fancy():
#  with db:
#    cur = db.cursor()
#    cur.execute("SELECT Name, CountryCode, Population FROM city ORDER BY Population LIMIT 15;")
#    query_results = cur.fetchall()
#  cities = []
#  for result in query_results:
#    cities.append(dict(name=result[0], country=result[1], population=result[2]))
#  user = { 'nickname': 'Kevin' } # fake user
#  return render_template('starter.html', user=user) 

@app.route("/")
def homepage():
  	return render_template("index.html")
@app.route("/summary")
def summary():
	print request.args.get('title_start', '')
	title_start = request.args.get('title_start', '')
	title_start = str(title_start)
	start = nodename[title_start] 
	NextNode_list = nodesummary(G2,start)
	result = '<ul>'
	for i in range(len(NextNode_list)):
		if i>=6:
			break
		NextNode=NextNode_list[i]
		result += '<div class="nodeblock"><h4>' + NextNode['nextnode'] + \
		'</h4> <h5 style="display: none">' + NextNode['AveTime'] +', \n' + \
		str(NextNode['Prob']) +title_start + 's become this.' +'</h5></div>'
		#+ NextNode['CompChange'] + ' change companies
			
	result = result + '</ul>' 
	return  result
	
@app.route("/path")

def fastest_path():

	print request.args.get('title_start', '')
	title_start = request.args.get('title_start', '')
	print request.args.get('title_end', '')
	title_end = request.args.get('title_end', '')
	start = nodename[title_start]  
	end = nodename[title_end]  #EXECUTIVE DIRECTOR

	path = shortestPath(G2,start,end,"time")
	path_named = namedpath(G2,path)
	# '&#8594'.join(path_named)
	result = '<h2>Fastest Path </h2>\
  	<h4 class="nodeinpath">' + '&#8594'.join(path_named) + '</h4> \
  	<h4>It takes ' + yearspath(G2,path) + '.</h4> \
  	<h4>' + probpath(G2,path) + ' </h4>' 
  	#<h4>' + probpath(G2,path) +' '+title_start +'s follows this path. </h4>' 
  	
	return result
@app.route("/path2")

def shortest_path():

	print request.args.get('title_start', '')
	title_start = request.args.get('title_start', '')
	print request.args.get('title_end', '')
	title_end = request.args.get('title_end', '')
	start = nodename[title_start]  
	end = nodename[title_end]  #EXECUTIVE DIRECTOR

	path = shortestPath(G2,start,end,"length")
	path_named = namedpath(G2,path)
	# '&#8594'.join(path_named)
	result = '<h2>shortest Path </h2>\
  	<h4 class="nodeinpath">' + '&#8594'.join(path_named) + '</h4> \
  	<h4>It takes ' + yearspath(G2,path) + '.</h4> \
  	<h4>' + probpath(G2,path) +' </h4>' 
  	#<h4>' + probpath(G2,path) +' '+title_start +'s follows this path. </h4>' 
  	
	return result
 	

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


