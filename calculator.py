
def main():
	firstnumber = input("Enter the first number:")
	secoundnumber = input("Enter the second number:")
	operat = input("Choose the operation (+, -, /, *):")
	if (firstnumber.isdigit())and(secoundnumber.isdigit()):
		if operat == "+":
			print("The answer is "+ str(int(firstnumber)+int(secoundnumber)))
		elif operat == "-":
			print("The answer is "+ str(int(firstnumber)-int(secoundnumber)))
		elif operat == "/":
			print("The answer is "+ str(int(firstnumber)/int(secoundnumber)))
		elif operat == "*":
			print("The answer is "+ str(int(firstnumber)*int(secoundnumber)))
		else:
			print("The operation is not valid")
	else:
		print("The numbers were invalid")




if __name__ == '__main__':
	main()
