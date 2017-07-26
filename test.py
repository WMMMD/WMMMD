def collatz(number):
	if (number%2==0):
		num=number//2
		return print(num,number)
	elif (number%2!=0):
		numb=3*number+1
		return print(numb)
#fenggexian
print('Please enter number:')
number=input()
number=int(number)
collatz(number)
