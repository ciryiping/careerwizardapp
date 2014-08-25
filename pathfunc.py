#my modified Dijkstra's algorithm
from priodict import priorityDictionary
from math import log
def Dijkstra(G,start,end=None,option="length"):
    """
    Modified from David Eppstein's codes.
    G: graph object form snap.py
    start: nid of the start node (int)
    end: nid of the end node (int)
    option can be "length", "time" and "prob"
    
    Find shortest paths from the start vertex to all
    vertices nearer than or equal to the end.

    The output is a pair (D,P) where D[v] is the distance
    from start to v and P[v] is the predecessor of v along
    the shortest path from s to v.
    
    Dijkstra's algorithm is only guaranteed to work correctly
    when all edge lengths are positive. This code does not
    verify this property for all edges (only the edges seen
    before the end vertex is reached), but will correctly
    compute shortest paths even for some graphs with negative
    edges, and will raise an exception if it discovers that
    a negative edge has caused it to make a mistake.
    """

    D = {}  # dictionary of final distances
    P = {}  # dictionary of predecessors
    Q = priorityDictionary()   # est.dist. of non-final vert.
    Q[start] = 0
    
    for v in Q:
        D[v] = Q[v]
        if v == end: break
        NI = G.GetNI(v)
        for Id in NI.GetOutEdges():#w in G[v]:
            eid = G.GetEId(v, Id)
            #if eid == -1: raise
            if option == "length":
                edgeweight = 1
            elif option == "time":
                edgeweight = G.GetIntAttrDatE(eid, "AveTime")
            elif option == "prob":
                prob = G.GetFltAttrDatE(eid, "Prob")
                if prob <= 0.001:
                    prob = 0.001
                edgeweight = -  log(prob)
            vwLength = D[v] +  edgeweight#G[v][w]
            if Id in D:
                if vwLength < D[Id]:
                    raise ValueError, \
  "Dijkstra: found better path to already-final vertex"
            elif Id not in Q or vwLength < Q[Id]:
                Q[Id] = vwLength
                P[Id] = v

    return (D,P)


def shortestPath(G,start,end,option="length"):
    """
    Find a single shortest path from the given start vertex
    to the given end vertex.
    The input has the same conventions as Dijkstra().
    The output is a list of the vertices in order along
    the shortest path.
    """

    D,P = Dijkstra(G,start,end,option)
    Path = []
    while 1:
        Path.append(end)
        if end == start: break
        if end not in P.keys():
            return "NONE"
        else:
            end = P[end]
    Path.reverse()
    return Path

 
 

def namedpath(G,path):
    named=list(G.GetStrAttrDatN(value, "Name") for value in path)
    #return '/'.join(named)
    return named
     


def yearspath(G,path):
    years = 0.0
    for i in range(len(path)-1):
        
         
        NId = path[i]
        NId2 = path[i+1]
        eid = G.GetEId(NId, NId2)
        years += G.GetIntAttrDatE(eid, "AveTime")
        #print G.GetIntAttrDatE(eid, "AveTime")
    
    return "%0.0f years" % (years/float(12))



def probpath(G,path):
    prob = 1
    for i in range(len(path)-1):
        NId = path[i]
        NId2 = path[i+1]
        eid = G.GetEId(NId, NId2)
        prob *= G.GetFltAttrDatE(eid, "Prob")
    #return "one out of %d " % int(1/prob)
    if float(prob)>0.01:
        result = "Difficulty: easy"
    elif float(prob)>0.001:
        result = "Difficulty: moderate"
    else:
        result = "Difficulty: hard"
    return result
    

def nodesummary(G,nid):
    NI = G.GetNI(nid)
    result = []
    problist = [0]
    for Id in NI.GetOutEdges():
        #print "edge (%d %d)" % (NI.GetId(), Id)
        
        eid = G.GetEId(nid, Id)
            #if eid == -1: raise    
        AveTime = G.GetIntAttrDatE(eid, "AveTime")     
        AveT = "%0.0f years" % (AveTime/float(12))
        Prob = G.GetFltAttrDatE(eid, "Prob")
        Prob_str = "{0:.0f}%".format(float(Prob)* 100)
        #print Prob
        CompChange = G.GetStrAttrDatE(eid, "CompChange")
        CompChange = "{0:.0f}%".format(float(CompChange)* 100)
        if Prob>=0.02:
            nextname = G.GetStrAttrDatN(Id, "Name")
            for i in range(len(problist)):
                if Prob>problist[i]:
                    problist.insert(i,Prob)
                    result.insert(i, {"nextnode":nextname,"AveTime":AveT,"Prob":Prob_str,"CompChange":CompChange})
                    break        
       # print "{0:.0f}%".format(float(Prob)* 100)
    return result
                