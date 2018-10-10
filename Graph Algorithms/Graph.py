class Vertex(object):
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}

	def addNeighbor(self, nbr, weight=0):
		self.connectedTo[nbr] = weight

	def getConnections(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self,nbr):
		return self.connectedTo[nbr]

	def __str__(self):
		return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])


class Graph(object):
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0

	def addVertex(self,key):
		self.numVertices += 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex

	def getVertex(self, n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None

	def addEdge(self,fro,to,cost=0):
		if fro not in self.vertList:
			nv = self.addVertex(fro)
		if to not in self.vertList:
			nv = self.addVertex(to)

		self.vertList[fro].addNeighbor(self.vertList[to], cost)

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())

	def __contains__(self):
		return n in self.vertList
