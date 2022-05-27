

#Print hello world

print('hello world')

#Addition of two numbers

first_number=float(input('Enter first number: '))
second_number=float(input('Enter second number: '))
sum_of_two_number=first_number+second_number

print('Sum of two number is:',sum_of_two_number)

#Swapping of two number

first_number=float(input('Enter first number: '))
second_number=float(input('Enter second number: '))

temp=first_number
first_number=second_number
second_number=temp

print('After swapping the first number is: ',first_number)
print('After swapping the second number is: ',second_number)

#Swapping of two number without third variable

first_number=float(input('Enter first number: '))
second_number=float(input('Enter second number: '))

first_number, second_number=second_number, first_number

print('After swapping the first number is: ',first_number)
print('After swapping the second number is: ',second_number)

#Take a number wheather it is greater than 100 or not

number=float(input('Enter the number: '))

if(number>100):
  print('This number',number,'is greater than 100')
else:
  print('This number',number,'is not greater than 100')