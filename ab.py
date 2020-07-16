import numpy as np
import random

MIN = 0
MAX = 1

MINVAL = 10000
MAXVAL = -10000

class Node:
    def __init__(self, parent, m):
        self.val = MAXVAL
        self.alpha = MAXVAL
        self.beta = MINVAL
        self.children = []
        self.agent = m
        self.parent = parent

    def resetValues(self):
    	self.val = MAXVAL
    	self.alpha = MAXVAL
    	self.beta = MINVAL
    	self.children = []
    	self.agent = MAX
    	self.parent = None

    def evaluate(self):
    	self.val = random.randint(1, 20)

class GameTree:
	def __init__(self, root):
		self.root = root
	
	def getOptimumValue(self, dep):
		depth = 0
		k = dep
		bf = 2
		newVal = MAXVAL
		self.root.resetValues()
		curr = self.root

		while self.root.val == MAXVAL:
			if depth == k:
				curr.evaluate()
				newVal = curr.val
				depth -= 1
				curr = curr.parent
				continue

			if newVal > MAXVAL:
				if curr.agent == MIN:
					if newVal < curr.beta and len(curr.children) > 1:
						curr.beta = newVal
					elif len(curr.children) == 1:
						curr.beta = newVal
				else:
					if newVal > curr.alpha and len(curr.children) > 1:
						curr.alpha = newVal
					elif len(curr.children) == 1:
						curr.alpha = newVal
				newVal = MAXVAL

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

		print(root.val)

root = Node(None, MAX)
gt = GameTree(root)

gt.getOptimumValue(3)


