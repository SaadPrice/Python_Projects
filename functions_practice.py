# functions_practice.py

def hello():
    print("Greetings!")

def pack(apple, banana, sandwich):
    return [apple, banana, sandwich]

def eat_lunch(lunch_items):
    if not lunch_items:
        print("My lunchbox is empty!")
    else:
        print("First I eat", lunch_items[0])
        for item in lunch_items[1:]:
            print("Next I eat", item)

# Test your file by calling the functions and printing the output of pack() in the terminal.
if __name__ == "__main__":
    # Call the functions
    hello()
    packed_items = pack("apple", "banana", "sandwich")
    eat_lunch(["salad", "soup", "bread"])

    # Print the output of pack()
    print("Packed items:", packed_items)



