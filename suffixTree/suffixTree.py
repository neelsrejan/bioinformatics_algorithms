class TrieNode():
	
	def __init__(self,num):
                self.name = num
                self.children = []

class TrieEdge():

	def __init__(self, char, idx, u, v):
                self.path = char
		self.idx = idx
                self.u = u
                self.v = v

class SuffixTrie():
	
	def __init__(self):
                self.root = TrieNode(-1)
                self.size = 0

        def add(self, words):
		for i in range(len(words[0])):
			currNode = self.root
			text = words[i]
			#print(i)
			#print(text)
			for j in range(i,len(text)+i):
				currSymbol = text[j-i]
				allChildren = []
                                for child in currNode.children:
                                        allChildren.append(child.path)
				if currSymbol in allChildren:
					nextNodeIdx = allChildren.index(currSymbol)
					order = str(currNode.children[nextNodeIdx].u.name) + "->" + str(currNode.children[nextNodeIdx].v.name) + ":" + str(currNode.children[nextNodeIdx].path)+ ":" + str(currNode.children[nextNodeIdx].idx) + "\n"
                                        #print(order)
					prevNode = currNode.children[nextNodeIdx].u
                                        currNode = currNode.children[nextNodeIdx].v
				else:
					self.size = self.size + 1
					if currSymbol == "$":
						newNode = TrieNode(i)
						newEdge = TrieEdge(currSymbol, j, currNode, newNode)
						currNode.children.append(newEdge)
						order = str(newEdge.u.name) + "->" + str(newEdge.v.name) + ":" + str(newEdge.path)+ ":" + str(newEdge.idx) + "\n"
						#print("Here5")
						#print(order)
					else:
						newNode = TrieNode(-1)
                                                newEdge = TrieEdge(currSymbol, j, currNode, newNode)
                                                currNode.children.append(newEdge)
						order = str(newEdge.u.name) + "->" + str(newEdge.v.name) + ":" + str(newEdge.path)+ ":" + str(newEdge.idx) + "\n"
						#print(order)
						currNode = newNode
                #print(orderNodes)
class SuffixNode():
	
	def __init__(self, num):
		self.name = num
		self.children = []

class SuffixEdge():
	
	def __init__(self, idx, length, u, v):
		self.idx = idx
		self.length = length
		self.u = u
		self.v = v

class SuffixTree():
	
	def __init__(self):
		self.root = SuffixNode(-1)
	
	def makeInnerNodes(self, trieRoot, sufRoot, trie, length):
		currNodeTrie = trieRoot
		currNodeSuf = sufRoot
		cycle = -1
		while len(currNodeTrie.children) != 0:
			nextEdgeTrie = currNodeTrie.children.pop()
			nextNodeTrie = nextEdgeTrie.v
			beginIdx = nextEdgeTrie.idx
			length = 1
			cycle = cycle + 1
			if len(nextNodeTrie.children) == 0:
				newNodeSuf = SuffixNode(nextNodeTrie.name)
				currEdgeSuf = SuffixEdge(beginIdx, length, currNodeSuf, newNodeSuf)
                                currNodeSuf.children.append(currEdgeSuf)		
			elif len(nextNodeTrie.children) == 1:
				while len(nextNodeTrie.children) == 1:
					nextEdgeTrie = nextNodeTrie.children.pop()
					nextNodeTrie = nextEdgeTrie.v
					length = length + 1
					if len(nextNodeTrie.children) == 0:
						newNodeSuf = SuffixNode(nextNodeTrie.name)
        	        	                currEdgeSuf = SuffixEdge(beginIdx, length, currNodeSuf, newNodeSuf)
	        	                        currNodeSuf.children.append(currEdgeSuf)
						#print(str(currNodeSuf.children[cycle].idx) + ":"+ str(currNodeSuf.children[cycle].length) + " " + str(currNodeSuf.children[cycle].u.name) + "->" + str(currNodeSuf.children[cycle].v.name))
					elif len(nextNodeTrie.children) > 1:
						newNodeSuf = SuffixNode(nextNodeTrie.name)
                                                currEdgeSuf = SuffixEdge(beginIdx, length, currNodeSuf, newNodeSuf)
                                                currNodeSuf.children.append(currEdgeSuf)
						self.makeInnerNodes(nextNodeTrie, newNodeSuf, trie,length)
						
			elif len(nextNodeTrie.children) > 1:
				newNodeSuf = SuffixNode(nextNodeTrie.name)
                                currEdgeSuf = SuffixEdge(beginIdx, length, currNodeSuf, newNodeSuf)
                                currNodeSuf.children.append(currEdgeSuf)
                             	self.makeInnerNodes(nextNodeTrie, newNodeSuf, trie,length)
				 


	def makeTreeNodes(self, root, trie, length):
		currNodeTrie = root
		currNodeSuf = SuffixNode(-1)
		while len(currNodeTrie.children) != 0:
               		nextEdgeTrie = currNodeTrie.children.pop()
	                nextNodeTrie = nextEdgeTrie.v
			beginIdx = nextEdgeTrie.idx
			length = 1
			lenNext = len(nextNodeTrie.children)
			if lenNext == 0:
				newNodeSuf = SuffixNode(nextNodeTrie.name)
				currEdgeSuf = SuffixEdge(beginIdx, length, currNodeSuf, newNodeSuf)
                                currNodeSuf.children.append(currEdgeSuf)
				#print(str(currNodeSuf.children[lenNext].idx) + ":"+ str(currNodeSuf.children[lenNext].length) + " " + str(currNodeSuf.children[lenNext].u.name) + "->" + str(currNodeSuf.children[lenNext].v.name))	
			elif lenNext == 1:
				while len(nextNodeTrie.children) == 1:
					nextEdgeTrie = nextNodeTrie.children.pop()
					nextNodeTrie = nextEdgeTrie.v
					length = length + 1
					if len(nextNodeTrie.children) == 0:
						newNodeSuf = SuffixNode(nextNodeTrie.name)
        	        	                currEdgeSuf = SuffixEdge(beginIdx, length, currNodeSuf, newNodeSuf)
	        	                        currNodeSuf.children.append(currEdgeSuf)
						#print(str(currNodeSuf.children[lenNext].idx) + ":"+ str(currNodeSuf.children[lenNext].length) + " " + str(currNodeSuf.children[lenNext].u.name) + "->" + str(currNodeSuf.children[lenNext].v.name))
					elif len(nextNodeTrie.children) > 1:
						newNodeSuf = SuffixNode(nextNodeTrie.name)
                                                currEdgeSuf = SuffixEdge(beginIdx, length, currNodeSuf, newNodeSuf)
                                                currNodeSuf.children.append(currEdgeSuf)
						#print(str(currNodeSuf.children[lenNext].idx) + ":"+ str(currNodeSuf.children[lenNext].length) + " " + str(currNodeSuf.children[lenNext].u.name) +     "->" + str(currNodeSuf.children[lenNext].v.name))
						self.makeInnerNodes(nextNodeTrie, newNodeSuf, trie,length)
			elif lenNext > 1:
				newNodeSuf = SuffixNode(-1)
                                currEdgeSuf = SuffixEdge(beginIdx, length, currNodeSuf, newNodeSuf)
                                currNodeSuf.children.append(currEdgeSuf)
				#print(str(currNodeSuf.children[lenNext].idx) + ":"+ str(currNodeSuf.children[lenNext].length) + " " + str(currNodeSuf.children[lenNext].u.name) + "->" + str(currNodeSuf.children[lenNext].v.name))	
				self.makeInnerNodes(nextNodeTrie, newNodeSuf, trie,length) 
		return currNodeSuf


def preorderPrint(root):
	order = []
	newOrder = printArr(order, root)
	#print("\n")
	substrings = []
	for i in newOrder:
		substrings.append((i.idx, i.length))
		#print(str(i.idx) + ":" + str(i.length) + " " + str(i.u.name) + "->" + str(i.v.name))
	return substrings

def printArr(order, root):
	if len(root.children) == 0:
		return order 
	while len(root.children) > 0:
		Edge = root.children.pop()
		nextNode = Edge.v
		order.append(Edge)
		printArr(order,nextNode) 
	return order

def main():
	input = open("input53.txt","r")
	output = open("output53.txt","w")
	
	text = next(input).strip()
	suffixes = []
	for i in range(len(text)):
		suffix = text[i:]
		suffixes.append(suffix)

	trie = SuffixTrie()
	trie.add(suffixes)
	
	tree = SuffixTree()
	root = tree.makeTreeNodes(trie.root, trie, 1)
	
	substring = preorderPrint(root)

	for i in substring:
		#print(i)
		partOfText = text[i[0]:i[0]+i[1]]
		output.write(partOfText)
		output.write("\n")

	output.close()
	input.close()
if __name__ == "__main__":
	main()
