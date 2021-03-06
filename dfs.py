# DEPTH-FIRST-SEARCH

# A graph is searched depth first by visiting an initial
# vertex and then visiting one of its neighbours. After
# visiting this neighbour you visit one of its neighbours
# and so on. If you come to a vertex with no neighbors you
# backtrack one stage and visit another neighbour of the 
# previous vertex.

# The algorithm
# ------------------------------------------------------
# set the colour of v to black
# ITERATE over all w that are neighbours of v
# 	IF the colour of w is white
# 		depth first search of G from w
# ------------------------------------------------------

def dfs(v, g):
	g[v]['colour'] = 'black'
	for w in g[v]['neighbours']:
		if g[w]['colour'] is 'white':
			dfs(w, g)


# An algorithm traversing the vertices of a graph needs 
# some way in which to detect when a vertex has already 
# been visited, or it might continue endlessly revisiting 
# vertices and never terminate. The traditional way to 
# record when a vertex has been visited is to give each 
# vertex a colour, white or black. Unvisited vertices are 
# coloured white. When a vertex is visited, its colour is 
# changed to black and black vertices are not revisited.
def chatty_dfs(vertex, graph):
	v = vertex
	g = graph

	print( "Visited: ", v)

	g[v]['colour'] = 'black'

	for w in g[v]['neighbours']:
		if g[w]['colour'] is 'white':
			g = chatty_dfs(w, g)

	return g


graph1 = {
	1 : { 'colour' : 'white', 'neighbours' : [2, 3, 4] },
	2 : { 'colour' : 'white', 'neighbours' : [1, 4, 5] },
	3 : { 'colour' : 'white', 'neighbours' : [1, 4] },
	4 : { 'colour' : 'white', 'neighbours' : [1, 2, 3] },
	5 : { 'colour' : 'white', 'neighbours' : [2]}
}

print( graph1 )
print( chatty_dfs(3, graph1) )
