import SimpleParser
import sys

def main():
	p = SimpleParser.SimpleParser("data/transaction1.txt")
	list = p.parse()
	#print(list)
	items = [["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"]]
	t = 0	
	for i in items:
		t = t + p.support(i)
		print str(i) + ":"+ str(p.support(i))
	print t

if __name__ == '__main__':
   main()



