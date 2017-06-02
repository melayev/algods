# DIJKSTRA


# The algorithm
# ------------------------------------------------------
# create priority queue
# set dist to 0 for v and dist to infinity for all other vertices
# add all vertices to priority queue
# ITERATE whilte priority queue is not empty
# 	remove u from the front of the queue
# 	ITERATE over w in the neighbours of u
# 		set new distance to dist u + length of edge from u to w
# 		IF new distance is less than distw
#			set dist w to new distance
#			change priority(w, new distance)

from priorityqueue import PriorityQueue

infinity = 100 # :) oh well that's the world we're are living in here

graph1 = {
	'u': { 'dist': infinity, 'edgeTo': { 'v': 1, 'w': 2 }},
	'v': { 'dist': infinity, 'edgeTo': { 'u': 1, 'x': 2, 'y': 5, 'z': 6 }},
	'w': { 'dist': infinity, 'edgeTo': { 'u': 2, 'x': 2, 'z': 4}},
	'x': { 'dist': infinity, 'edgeTo': { 'v': 6, 'w': 2, 'y': 3}},
	'y': { 'dist': infinity, 'edgeTo': { 'x': 3, 'v': 5, 'z': 1 }},
	'z': { 'dist': infinity, 'edgeTo': { 'v': 6, 'w': 4, 'y': 1 }}
}


# The objective is to find the shortest path from the source to each
# of the other vertices. To do this, we record against each vertex 
# the length of the shortest path to it found so far. As the algorithm 
# progresses this value is updated whenever a shorter path is discovered.
#
# Initially, the distance to the source's vertex is 0 (it's zero distance 
# from itself). We have no information yet about the other distances, so we 
# set them all to some suitably large value, conventionally called 'infinity'.
# We then add all the vertices to a priority queue, sorted by currrent 
# distance, The sourcehas the smallest distance (zero versus infinity for 
# all the others) so it will be at the front.
#
# While the priority queue is not empty we repeat these steps
# 	- Remove the vertex at the front of the queue
# 	- Locate its neighbours. For each neighbour, compute a new distance by 
# 		adding together the base distance and the length of the edge going to 
# 		that neightbour
# 	- If the new distance is less than the neightbour's current distance, we 
# 		have found a shorter path to the neighbour. So replace the neighbour's 
#		distance with the new distance

def dijkstra(source, graph):
	pQueue = PriorityQueue()
	graph[source]['dist'] = 0

	for v in graph:
		pQueue.enqueue((graph[v]['dist'], v))

	while not pQueue.isEmpty():
		u = pQueue.dequeue()
		baseDist = graph[u]['dist']
		for w in graph[u]['edgeTo']:
			edgeLen = graph[u]['edgeTo'][w]
			newDist = baseDist + edgeLen
			currentDist = graph[w]['dist']
			if newDist < currentDist:
				graph[w]['dist'] = newDist
				pQueue.changePriority(w, newDist)

	distanceList = []
	for v in graph:
		distanceList.append((v, graph[v]['dist']))

	return distanceList


print( "Distance from 'u' to other vertices:" )
print( dijkstra('u', graph1) )