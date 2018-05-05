from stack import Stack

def divdeBy8(octalNumber):
	remstack = Stack()

	while octalNumber > 0:
		rem = octalNumber % 8
		remstack.push(rem)
		octalNumber = octalNumber // 8

	binString = ""
	while  not remstack.is_empty():
		binString = binString + str(remstack.pop())
	
	return binString

print(divdeBy8(668))	
	