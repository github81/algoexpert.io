
class btree:

	def __init__(self,val):
		self.val = val
		self.right = None
		self.left = None
		
		
#		3
#	  /   \
#    2     7
#   / \     \
#  4  -2 	 5	
		
def breadthFirstPrint(root):	
	q = [root]
	while len(q) > 0:
		currentNode = q.pop(0)
		print(currentNode.val)
		if currentNode.left:
			q.append(currentNode.left)
		if currentNode.right:
			q.append(currentNode.right)


def depthFirstPrint(root):
	s = [root]
	while len(s) > 0:
		currentNode = s.pop()
		print(currentNode.val)
		if currentNode.right:
			s.append(currentNode.right)
		if currentNode.left:
			s.append(currentNode.left)

	
def depthFirstPrintRecursion(root):
	if not root:
		return
	print(root.val)
	depthFirstPrintRecursion(root.left)
	depthFirstPrintRecursion(root.right)
	
	
def sumTree(root):
	s = [root]
	sum = 0
	while len(s) > 0:
		currentNode = s.pop()
		#print(currentNode.val)
		sum += currentNode.val
		if currentNode.right:
			s.append(currentNode.right)
		if currentNode.left:
			s.append(currentNode.left)
			
	return sum

# t - O(n), s - O(n)
def sumTreeRecursion(root):
	if not root:
		return 0
	return sumTreeRecursion(root.left) + root.val + sumTreeRecursion(root.right)
	# 0 + 4 + 0 + 2 + 0 + -2 + 0 + 3 + 0 + 7 + 0 + 5 + 0
	
def countTree(root):	
	if not root:
		return 0
	return 1 + countTree(root.left) + countTree(root.right)
	
if __name__ == '__main__':
	root = btree(3)
	root.left = btree(2)
	root.right = btree(7)
	root.left.left = btree(4)
	root.left.right = btree(-2)
	root.right.right = btree(5)
	
	#breadthFirstPrint(root)
	#depthFirstPrint(root)
	#print(sumTreeRecursion(root))
	#depthFirstPrintRecursion(root)
	#print(countTree(root))
	print(sumTree(root))