two_digit_number = input("Type a two digit number: ") #data type is currently STRING

#Then we convert the two numbers into an interger
num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])

#We complete the sum of both numbers
sum = num1 + num2

#We convert again the data into string so that we can concatenate
new_sum = str(sum)

#Finally, we print the sum
print("The sum of the two numbers is: " + new_sum)