def main():
    number = get_number()
    meow(number)
def get_number():
    while True:
        n = int(input("what's n?  "))
        if n > 0:
            return n
        else:
            print("please enter a positive number")
def meow(n):
        for _ in range(n):
           print("meow")

main()
