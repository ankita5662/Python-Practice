'''Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers 
in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)'''


def fib(n):
    fib_list = [0,1]
    for i in range (2,n):
      next_num = fib_list[i-1] + fib_list[i-2]
      fib_list.append(next_num)
    return fib_list[:n]    

n = int(input("Enter number of terms: "))
print(fib(n))
