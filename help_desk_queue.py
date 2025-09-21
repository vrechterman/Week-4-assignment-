# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    # Delete the following line and implement your Queue class
    pass
    


def run_help_desk():
    # Create an instance of the Queue class
    

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            
            
            print(f"{name} added to the queue.")
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            pass # delete this line


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            pass # delete this line


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()


'''
Memo: 
For this week’s assignment we learned what stacks, queues, and 
when to use a stack or a queue. A stack is a linear data that 
follows a last in, first out order. The last value added is the 
first one removed. Now for, is the queues, queues is a linear data 
structure that follows a first in, first out order. In a queue, 
the first value added is the first one removed. Now that stacks 
and queues have been explained, it is time to explain when to 
use them. Stacks are used when the most recent action should be 
handled first. On the other hand, queues are used when the first 
request should be handled first. Stacks are effective for this type 
of assignment with us doing undo/ redo systems because it aligns better 
with this type of coding. And for queues, it is better used for help
 desk ticketing, it is the best thing to be able to take the costumers 
 requests for a help desk scenario. For this assignment, building this 
 code by using the stacks and queues using linked nodes, along with the 
 pop and push, as well as the enqueue, it will make the performance run a lot smoother. 
 '''