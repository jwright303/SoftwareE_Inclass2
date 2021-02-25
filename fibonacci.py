def fibCalc(fibN):
	start = 0
	first = 1
	fibS = 1
 
	if fibN < 0 :
		print("error invalid input given")
		return
	elif fibN == 0:
		return start
	else:
		for i in range(1, fibN):
			fibS = start + first
			start = first
			first = fibS
		return fibS
	return fibS

def factCalc(facN):
	facP = 1
	#if facN == 0:
	#       return 1
	if facN > 0:
		while facN > 0:
			facP = facP * facN
			facN = facN - 1
	#print(facP)
	return facP
