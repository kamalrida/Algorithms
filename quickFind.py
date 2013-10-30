class quickFind(object):
	"""docstring for quickFind"""

	def __init__(self, N):
		self.id=list(range(N))
	def connected(self, p, q):
		return self.id[p]==self.id[q]
	def union(self, p, q):
		if self.connected(p,q):
			return
		pid=self.id[p]
		qid=self.id[q]
		for i in range(len(self.id)):
			if self.id[i]==pid:
				self.id[i]=qid
		return self.id

"""
USAGE:
>>> qf=quickFind(8)
>>> qf.id
[0, 1, 2, 3, 4, 5, 6, 7]
>>> qf.union(2,4)
[0, 1, 4, 3, 4, 5, 6, 7]
>>> qf.union(1,5)
[0, 5, 4, 3, 4, 5, 6, 7]
>>> qf.union(5,3)
[0, 3, 4, 3, 4, 3, 6, 7]
>>> qf.union(0,7)
[7, 3, 4, 3, 4, 3, 6, 7]
>>> qf.union(0,1)
[3, 3, 4, 3, 4, 3, 6, 3]
>>> qf.union(4,6)
[3, 3, 6, 3, 6, 3, 6, 3]
"""
