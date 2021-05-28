#Name: Chenyu Song
#Course: CS362
#Description: fizzbuzz implementation
#Date: 5/28/2021

def fizzbuzz(num):
    if(num%3 == 0):
        return "Fizz" 
    if(num%5 == 0):
        return "Buzz"
    if(num%15 == 0):
        return "FizzBuzz"
    
    return num

def main():
    for num in range (1,100):
        print(fizzbuzz(num))

if __name__ == "__main__":
    main()