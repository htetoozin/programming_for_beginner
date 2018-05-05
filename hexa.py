from stack import Stack

def divdeBy16(hexNumber):
	remstack = Stack()

	while hexNumber > 0:
		rem = hexNumber % 16
		if rem == 10:
			 rem = "A"
		elif rem == 11:
			 rem = "B"	
		elif rem == 12:
			 rem = "C"
		elif rem == 13:
			 rem = "D" 
		elif rem == 14:
			 rem = "E" 
		elif rem == 15:
			 rem = "F"	
		else: 
			 rem = rem	

		remstack.push(rem)
		hexNumber = hexNumber // 16

	binString = ""
	while not remstack.is_empty():
		binString = binString + str(remstack.pop())

	return binString

print(divdeBy16(668))			