graph1 = {
	1 : { 'colour' : 'white', 'neighbours' : [2, 3, 4] },
	2 : { 'colour' : 'white', 'neighbours' : [1, 4, 5] },
	3 : { 'colour' : 'white', 'neighbours' : [1, 4] },
	4 : { 'colour' : 'white', 'neighbours' : [1, 2, 3] },
	5 : { 'colour' : 'white', 'neighbours' : [2]}
}


def dfs(vertex, graph):
	v = vertex
	g = graph

	g[v]['colour'] = 'black'

	for w in g[v]['neighbours']:
		if g[w]['colour'] is 'white':
			dfs(w, g)
	return g


print( dfs(3, graph1) )
