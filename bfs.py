# BREADTH-FIRST-SEARCH

# Visit an initial vertex, and then visit every one of its
# neighbours. Only when every neighbour vertex has been 
# visited then move to a neighbour of a neighbour. Each time
# the seach comes to a new vertex it visits all of its
# neighbours before visiting any that are further from the 
# start

# The algorithm
# ------------------------------------------------------
# create queue
# add v to the back of the queue
# ITERATE while queue is not empty
# 	remove u from the front of the queue
# 	set the colour of the u to black
# 	ITERATE over all w that are neighbours of u
# 		IF the colour of w is white
# 			set the colour of w to grey
#			add w to the back of the queue
# ------------------------------------------------------

def bfs(v, g):
	queue = []
	queue.append(v)

	while len(queue) > 0:
		u = queue.pop(0)
		g[u]['colour'] = 'black'
		for w in g[u]['neighbours']:
			if g[w]['color'] is 'white':
				g[w]['colour'] = 'grey'
				queue.append(w)	


# The idea is that we keep a todo list of vertices we are 
# aware of but have not visited yet. The list is a queue so
# the next vertex to visit, will always be at the front of 
# the queue. As in DFS, we colour the vercies but in BFS 
# there are three colours:
# 	- black for a vertex that has been visited
# 	- grey for a vertex waiting to be visitied
#	- while for a vertex we have not reached yet
# While the todo list is not empty, we repeat these steps:
# 	- Remove the vertex at the front of the queue
# 	- Locate its neighbours. Those coloured white are 
#		coloured grey and added to the back of the queue
def chatty_bfs(vertex, graph):
	g = graph
	v = vertex

	queue = []
	queue.append(v)

	while len(queue) > 0:
		u = queue.pop(0)
		g[u]['colour'] = 'black'
		print( "Visited: ", u )
		for w in g[u]['neighbours']:
			if g[w]['colour'] is 'white':
				g[w]['colour'] = 'grey'
				queue.append(w)
	return g	

graph1 = {
	1 : { 'colour' : 'white', 'neighbours' : [2, 3, 4] },
	2 : { 'colour' : 'white', 'neighbours' : [1, 4, 5] },
	3 : { 'colour' : 'white', 'neighbours' : [1, 4] },
	4 : { 'colour' : 'white', 'neighbours' : [1, 2, 3] },
	5 : { 'colour' : 'white', 'neighbours' : [2]}
}

print( graph1 )
print( chatty_bfs(3, graph1) )
