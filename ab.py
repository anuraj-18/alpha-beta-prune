import numpy as np
import random
import pdb

#pdb.set_trace()

MIN = 0
MAX = 1

INF = 10000
NINF = -10000

class Node:
    def __init__(self, parent, m):
        self.val = NINF
        self.alpha = NINF
        self.beta = INF
        self.children = []
        self.agent = m
        self.parent = parent

    def resetValues(self):
    	self.val = NINF
    	self.alpha = NINF
    	self.beta = INF
    	self.children = []
    	self.agent = MAX
    	self.parent = None
    	self.ind = 0

    def evaluate(self):
    	self.val = random.randint(0, 20)

class GameTree:
	def __init__(self, root):
		self.root = root
	
	def getOptimumValue(self, dep):
		depth = 0
		k = dep
		bf = 5
		newVal = NINF
		# self.root.resetValues()
		curr = self.root
		bestIndArr = []
		while self.root.val == NINF:
			if depth == k:
				curr.evaluate()
				newVal = curr.val
				depth -= 1
				curr = curr.parent
				continue

			if newVal > NINF:
				if curr.agent == MIN:
					if (newVal < curr.beta and len(curr.children) > 1) or len(curr.children) == 1:
						curr.beta = newVal
				else:
					if (newVal >= curr.alpha and len(curr.children) > 1) or len(curr.children) == 1:
						if curr == self.root:
							if curr.alpha < newVal:
								bestIndArr = []
								bestIndArr.append(len(curr.children) - 1)
							if curr.alpha == newVal:
								bestIndArr.append(len(curr.children) - 1)
						curr.alpha = newVal
						
				newVal = NINF

			if curr.alpha >= curr.beta:
				if curr.agent == MIN:
					curr.val = curr.beta
				else:
					curr.val = curr.alpha
				depth -= 1
				newVal = curr.val
				curr = curr.parent
			else:
				l = len(curr.children)
				if l < bf:
					curr.children.append(Node(curr, 1-curr.agent))
					curr = curr.children[l]
					curr.alpha = curr.parent.alpha
					curr.beta = curr.parent.beta
					depth += 1
				else:
					if curr.agent == MIN:
						curr.val = curr.beta
					else:
						curr.val = curr.alpha
					newVal = curr.val
					curr = curr.parent; depth -= 1

		return self.root.val, bestIndArr


root = Node(None, MAX)

gt = GameTree(root)

print(gt.getOptimumValue(3))



