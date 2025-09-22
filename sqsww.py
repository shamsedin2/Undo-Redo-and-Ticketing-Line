class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
from node import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        return None if not self.top else self.top.value

    def print_stack(self):
        current = self.top
        if not current:
            print("(empty)")
            return
        while current:
            print(f"- {current.value}")
            current = current.next


def run_undo_redo():
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action: ")
            undo_stack.push(action)
            redo_stack = Stack()  # clear redo
            print(f"Action performed: {action}")

        elif choice == "2":
            action = undo_stack.pop()
            if action:
                redo_stack.push(action)
                print(f"Undid action: {action}")
            else:
                print("No actions to undo")

        elif choice == "3":
            action = redo_stack.pop()
            if action:
                undo_stack.push(action)
                print(f"Redid action: {action}")
            else:
                print("No actions to redo")

        elif choice == "4":
            print("Undo Stack:")
            undo_stack.print_stack()

        elif choice == "5":
            print("Redo Stack:")
            redo_stack.print_stack()

        elif choice == "6":
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    run_undo_redo()
from node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.rear:  # empty queue
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        value = self.front.value
        self.front = self.front.next
        if not self.front:  # queue became empty
            self.rear = None
        return value

    def peek(self):
        return None if not self.front else self.front.value

    def print_queue(self):
        current = self.front
        if not current:
            print("(empty)")
            return
        while current:
            print(f"- {current.value}")
            current = current.next


def run_help_desk():
    queue = Queue()

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
            queue.enqueue(name)
            print(f"{name} added to the queue.")

        elif choice == "2":
            customer = queue.dequeue()
            if customer:
                print(f"Helped: {customer}")
            else:
                print("No customers in queue.")

        elif choice == "3":
            customer = queue.peek()
            if customer:
                print(f"Next customer: {customer}")
            else:
                print("No customers in queue.")

        elif choice == "4":
            print("Waiting customers:")
            queue.print_queue()

        elif choice == "5":
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    run_help_desk()
