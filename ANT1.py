from random import randint
from scipy import stats
import matplotlib.pyplot as plt

def Construct(tau, adj):
	numvert = len(adj[1])
	path = [0]
	dist = 0
	#visited[i] = 0 means vertex i not visited, 1 means visited
	visited = [0 for x in range(numvert)]
	visited[0] = 1
	path[0] = 0
	curvertex = 0
	while(0 in visited):
		phertotal = 0
		verpher = [0 for x in range(numvert)]
		for vert in range(numvert):
			if(vert!=curvertex and visited[vert] == 0):
				phertotal = phertotal + tau[curvertex][vert]
				verpher[vert] = tau[curvertex][vert]
		normverpher = [x / float(phertotal) for x in verpher]
		distrib = stats.rv_discrete(values = (range(numvert), normverpher))
		nextvertex = int(distrib.rvs(size=1))
		visited[nextvertex] = 1
		dist = dist + adj[curvertex][nextvertex]
		path.append(nextvertex)
		curvertex = nextvertex
	dist = dist + adj[curvertex][0]
	path.append(dist)
	return path

	
def Update(tau, P):
	numvert = len(tau[0])
	rho = 1/float(3)
	newtau = [[0 for j in range(0,len(tau[0]))] for i in range(0, len(tau[0]))]
	isinpath = [[0 for j in range(0,len(P))] for i in range(0, len(P))]
	for i in range(len(P)-1):
		isinpath[P[i]][P[i+1]] = 1
	isinpath[P[len(P)-1]][P[0]] = 1
	for i in range(len(tau[0])):
		for j in range(len(tau[0])):
			if(i!=j):
				if(isinpath[i][j] == 1):
					newtau[i][j] = min(((1-rho)*tau[i][j] + rho)/(1 - rho + 2*numvert*rho),(numvert-1)/float(2*(numvert**2)))
				else:
					newtau[i][j] = max(((1-rho)*tau[i][j])/(1 - rho + 2*numvert*rho),(1)/float(2*(numvert**2)))
	return newtau

	
def PlotRoute(points, path):
	for i in range(len(points)):
		plt.plot(points[i][0], points[i][1], marker='o')
	for i in range(len(path)-1):
		plt.plot([points[path[i]][0], points[path[i+1]][0]],[points[path[i]][1], points[path[i+1]][1]], color = 'b')
	figManager = plt.get_current_fig_manager()
	figManager.window.showMaximized()
	plt.show()


testinput = [[0,0],[0,1],[1,0],[2,2],[5,5],[4,4],[2,3],[1,0],[20,20],[5,6],[17,17]]
adj = [[0 for j in range(0,len(testinput))] for i in range(0, len(testinput))]
pher = [[0 for j in range(0,len(testinput))] for i in range(0, len(testinput))]
for i in range(len(adj[1])):
	for j in range(len(adj[1])):
		if(i!=j):
			adj[i][j] = ((testinput[i][0] - testinput[j][0])**2 + (testinput[i][1] - testinput[j][1])**2)**.5
			adj[j][i] = adj[i][j]

#Assume we have an adjaceny matrix "adj" where adj[i][j] = distance from vertex i to vertex j
#Assume graph is fully connected
#Assume undirected
numvert = len(adj[1])
numedge = numvert*(numvert-1)/2
#Initialize pheromones. pher[i][j] SHOULD ALWAYS EQUAL pher[j][i]
for i in range(numvert):
	for j in range(numvert):
		if i!=j:
			pher[i][j] = 1/float(numedge)
		elif i==j:
			pher[i][j] = 0
#Construct initial path
bestpath = [0 for x in range(numvert)]
bestdist = 0
proppath = [0 for x in range(numvert)]
propdist = 0

firstpath = Construct(pher,adj)
bestdist = firstpath.pop()
bestpath = firstpath
pher = Update(pher, firstpath)
print bestdist
print bestpath
PlotRoute(testinput,bestpath)
for i in range(1000):
	proppath = Construct(pher,adj)
	propdist = proppath.pop()
	if(propdist < bestdist):
		bestdist = propdist
		print bestdist
		print bestpath
		bestpath = proppath
		pher = Update(pher, bestpath)
		PlotRoute(testinput,bestpath)

PlotRoute(testinput,bestpath)

