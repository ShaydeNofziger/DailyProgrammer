"""
Description:
I had the other day in my possession a label bearing the number 3 0 2 5 in large figures. This got accidentally torn in half, so that 3 0 was on one piece and 2 5 on the other. 
On looking at these pieces I began to make a calculation, when I discovered this little peculiarity. 
If we add the 3 0 and the 2 5 together and square the sum we get as the result, the complete original number on the label! 
Thus, 30 added to 25 is 55, and 55 multiplied by 55 is 3025. Curious, is it not?
Now, the challenge is to find another number, composed of four figures, all different, which may be divided in the middle and produce the same result.
Bonus:
Create a program that verifies if a number is a valid torn number.
"""

def main():
	curr_num = 1000
	while curr_num < 10000:
		if isValid(curr_num):
			print(curr_num)
		curr_num += 1


def isValid(number):
	if checkAllDifferent(number):
		first_num = int(str(number)[0:2])
		second_num = int(str(number)[2:4])
		result = (first_num + second_num)**2
		if result == number:
			return True
	return False


def checkAllDifferent(number):
	result = set()
	for i in str(number):
		result.update(i)
	if len(result) != 4:
		return False
	return True

main()