class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self):
        x = input("Enter a Sentence: ")
        new = Node(x)
        if self.top is None:
            self.top = new
            self.top.next = None
        else:
            new.next = self.top
            self.top = new

    def pop(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            print("Popped Element is  : ", self.top.data)
            print("------------------------------------")
            self.top = self.top.next

    def palindrome_checker(self):
        self.display()
        # Gets the index of the sentence to be checked for palindrome
        sentence_index = int(input("Enter the Sentence's Index to be Checked: ")) - 1
        temp = self.top
        if temp is None:
            print("Stack is Empty")
        else:
            # Traverse the stack to reach the specified index
            for _ in range(sentence_index):
                if temp := temp.next:
                    pass
                else:
                    print("Invalid Index")
                    break
                # Convert the data at the specified index to a cleaned string for palindrome check
            else:
                pal = ''.join(e.lower() for e in (temp.data if temp else '') if e.isalnum())
                print("The Sentence is a palindrome!" if pal == pal[::-1] else "The Sentence is not a palindrome.")

    def display(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            temp = self.top
            index = 1
            while temp:
                print(f"Sentence {index}: {temp.data}")
                temp = temp.next
                index += 1
            print("Top of the Stack is:", self.top.data)

s = Stack()
while True:
    print("Enter option Below")
    print("\t 1 - Enter Sentence \n\t 2 - Display Sentences \n\t 3 - Palindrome Checker \n\t 4 - Exit")
    option = int(input())
    if option == 1:
        print("---ADD--A--SENTENCE---")
        s.push()
    elif option == 2:
        print("------DISPLAY------")
        s.display()
    elif option == 3:
        print("---PALINDROME-----CHECKER---")
        s.palindrome_checker()
    elif option == 4:
        break

'''
Reflection:
Developing the code presented a challenge as I needed to integrate the functionalities of push, display, and the palindrome checker 
within the menu structure to ensure seamless interaction. Initially, I struggled to comprehend the workings of the palindrome checker. 
Eventually, I sought guidance by exploring existing palindrome checker code, which provided a step-by-step breakdown. 
This resourceful approach significantly aided my understanding, enabling me to eventually create the palindrome checker.
'''
