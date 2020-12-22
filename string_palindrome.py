#to find given string is palindrome or not
string=input("Enter string:")
if(string==string[::-1]):
   print(string,"string is a palindrome")
else:
   print(string,"string isn't a palindrome")