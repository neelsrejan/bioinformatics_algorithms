class TrieNode():
	
	def __init__(self,num):
		self.name = num
		self.children = []

class Edge():	

	def __init__(self, char, u, v):
		self.path = char
		self.u = u
		self.v = v
	
class Trie():
	def __init__(self):
		self.root = TrieNode(0)
		self.size = 0

	def add(self, words):
		orderNodes = []
		for word in words:
			currNode = self.root
			for letter in word:
				allChildren = []
                		for child in currNode.children:
                        		allChildren.append(child.path)
				if letter not in allChildren:
					self.size = self.size + 1
					newNode = TrieNode(self.size)
					newEdge = Edge(letter, currNode, newNode)
					currNode.children.append(newEdge)
					currNode = newNode
					orderNodes.append(str(newEdge.u.name) + "->" + str(newEdge.v.name) + ":" + str(newEdge.path))
				else:
					nextNodeIdx = allChildren.index(letter)
					currNode = currNode.children[nextNodeIdx].v
		return orderNodes
def main():
	input = open("input51.txt","r")
	output = open("output51.txt","w")
	
	words = []
	for line in input:
		line = line.strip()
		words.append(line)
	
	trie = Trie()
	order = trie.add(words)
	
	for i in order:
		output.write(i) 
		output.write("\n")
			
	output.close()
	input.close()	
if __name__ == "__main__":
	main()
