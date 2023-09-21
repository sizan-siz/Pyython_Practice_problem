#Write a code to check whether a given number is a palindrome.


#code:
# a=input("Enter 1st number")
# b=a[::-1]
# if a==b:
#     print("Palindom")
# else:
#     print("Not palindom")



# #Write a code to find the sum of numbers divisible by 4.The code must allow the user to accept a number and add it to the sum if it is divisible by 4. It should continue accepting numbers as long as the user wants to provide an input and should display the final sum.Ex: given a number 11, here 1 to 11 only 4 and 8 are disible by 4 so sum will be 4+8=12
# num=int(input("Enter a number "))
# sum=0
# i=0
# while i<=num:
#     n=i%100
#     if n%4==0:
#         sum=sum+n
#         i=i+1
#     else:
#         i=i+1
#         continue

# print("Sum is ",sum)
#A three digit number is said to be an “Armstrong number” if the sum of the third power of its individual digits is equal to the number itself.Write a program to check whether a number is armstrong or not.
num = int(input("Enter a number: "))


sum = 0


temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp=temp//10


if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
