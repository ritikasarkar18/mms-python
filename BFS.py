import pickle

def ShortestPath(head): 
	visited = [] 
	
	queue = [[head]] 
	
	while queue: 
		path = queue.pop(0) #store the queue after pop first element
		node = path[-1]  #store node to traverse
		#print(node)
	
		if node not in visited: 
			neighbours = node.neighbours #access neighbours of node
			#print(neighbours)

			for neighbour in neighbours: 
				new_path = list(path) 
				new_path.append(neighbour) 
				#print(new_path)
				queue.append(new_path)
				#print(queue)
				
				
				if neighbour.isEnd: 
					print("Shortest path = ")
					return new_path
			
			visited.append(node) 

	print("Connecting path doesn't exist") 
	return


if __name__ == "__main__": 
	head = pickle.load(open("HeadNode.p", "rb"))

        print(ShortestPath(head)) 
