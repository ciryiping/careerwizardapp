from flask import render_template, request, Flask
#from app import app
from flask.json import jsonify
#import pymysql as mdb
import pickle
import snap as snap
from pathfunc import * 

app = Flask(__name__)

f=open('nodename','rb')
nodename = pickle.load(f)

FIn = snap.TFIn("test.graph")
G2 = snap.TNEANet.Load(FIn)


@app.route("/")
@app.route("/career")
def careerpage():
	return render_template("newbootstrap.html")
 
 
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
		'</h4> <h5 style="display: none">' +str(NextNode['Prob']) +' ' +title_start + 's make this transition.</h5> <h5 style="display: none">' + \
		  'It takes ' + NextNode['AveTime'] +' on average.</h5></div>'
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
	if path == "NONE":
		return '<h4 class="nodeinpath">No path in the database. Be creative!</h4>'
	path_named = namedpath(G2,path)
	# '&#8594'.join(path_named)
	result = '<h2>Fastest Path </h2>\
  	<h4 class="nodeinpath">' + '&#8594'.join(path_named) + '</h4> \
  	<h5>It takes ' + yearspath(G2,path) + '.</h5> \
  	<h5>' + probpath(G2,path) + ' </h5>' 
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
	if path == "NONE":
		return '<h4 class="nodeinpath">No path in the database. Be creative!</h4>'
	path_named = namedpath(G2,path)
	# '&#8594'.join(path_named)
	result = '<h2>shortest Path </h2>\
  	<h4 class="nodeinpath">' + '&#8594'.join(path_named) + '</h4> \
  	<h5>It takes ' + yearspath(G2,path) + '.</h5> \
  	<h5>' + probpath(G2,path) +' </h5>' 
  	#<h4>' + probpath(G2,path) +' '+title_start +'s follows this path. </h4>' 
  	
	return result
 	

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000,debug = True)


