import SimpleParser
import sys
from itertools import chain, combinations

def powerset(iterable):
  xs = list(iterable)
  # note we return an iterator rather than a list
  return list(chain.from_iterable( combinations(xs,n) for n in range(len(xs)+1) ))

def main():
	parser = SimpleParser.SimpleParser("data/transaction2.txt")
  	parser.parse()
	items = ["1","2","3","4","5","6","7","8","9"]
	#t = ["1","2","3","4"]	
	#print list(combinations(t,2))

	#items = [["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"]]
	ps = powerset(items)
	for p in ps:
		sup = parser.support( list(p) )
		if sup > 0:
			print str(list(p)) + ":"+ str(sup ) 
	
if __name__ == '__main__':
   main()



