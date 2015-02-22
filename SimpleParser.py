
class SimpleParser:
	"""A Simpple Parser Class"""
	def __init__(self, filename):
		self.filename= filename
		self.xs = []
		self.total = 0	
	def parse(self):
		with open(self.filename) as openfileobject:
    			for line in openfileobject:
				x = line.replace('\n','').split(',')
				self.total = self.total + len(x) - 1
        			self.xs.append(x[1:])
		print( "total: " + str(self.total))		
		return self.xs	
	def contains(self,small, big):
		for x in small:
			if( (x in big) == False ): 
				return False
			#big.remove(x)
		return True

	def support(self, ys):
		ss = map(lambda row: self.contains(ys,row), self.xs)
		#ss = map(lambda row: set(ys).issubset(row), self.xs)
		return ss.count(True)
		

				



