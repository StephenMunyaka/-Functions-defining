def main():
    number = get_number()
    come(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n  # Return n if it's greater than 0
        else:
            print("Please enter a positive integer.")

def come(n):
    for _ in range(n):
        print("come")

main()





