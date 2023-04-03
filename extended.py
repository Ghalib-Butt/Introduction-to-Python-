from functools import partial
from utility import clearTerminal
  
# A normal function
def f(a, b, c, x):
    return 1000*a + 100*b + 10*c + x
# A partial function that calls f with
# a as 3, b as 1 and c as 4.
g = partial(f, 3, 1, 4) 
# Calling g()


# Check if a string is pladinrome using recurssion
def palindromeQuestion():
    word = input("Enter a string: ")
    size = len(word)
    isPalindrome(word, 0, size-1)
    
def isPalindrome(word, start, end):
    if start > end or start == end:
        print("Given word is plaindrome.")
    elif word[start] == word[end]:
        isPalindrome(word, start+1, end-1)
    else:
        print("Given word in not a plaindrome.")

def main():
    print(g(5))
    palindromeQuestion()
    clearTerminal()

main()
