# დავალება 1.

# ლექციაზე განხილულ კოდებს, დააწერეთ კომენტარები თუ რა დროს 
# რა ხდება

#########################################
#1.Node კლასი წარმოადგენს ერთ კვანძს, რომელიც გამოიყენება ერთმანეთთან დაკავშირებულ სტრუქტურებში (მაგ. ლისტი, სტეკი).
#data მოიცავს ინფორმაციას, ხოლო next მიუთითებს მომდევნო კვანძზე.

class Node:
    def __init__(self, data=None):
        self.data = data # ინახავს მონაცემს
        self.next = None # მიუთითებს მომდევნო კვანძზე

#######################################
# 2.LinkedList კლასი - ესაა ლინკური ლისტი, რომელიც შედგება 
# კვანძებისგან (Nodes), რომელიც ერთმანეთთანაა დაკავშირებული.

class LinkedList:
    def __init__(self):
        self.head = None #   # ლისტის პირველი კვანძი
#############################
# 3.append ამატებს ახალ კვანძს ლინკურ ლისტში. თუ ლისტი 
# ცარიელია, ახალი კვანძი ხდება head. თუ არა, ბოლო კვანძს 
# უკავშირდება ახალი კვანძი.
    def append(self, data):
        new_node = Node(data) # ახალი კვანძის შექმნა

        if self.head is None: #თუ ცარიელია ლისტი
            self.head = new_node #ახალი კვანძი ხდება პირველი
            return

        last_node = self.head ## ლისტის ბოლო კვანძზე გადასვლა

        while last_node.next:# სანამ ბოლო კვანძზე მივალთ
            last_node = last_node.next

        last_node.next = new_node  # კვანძის დაკავშირება ლისტში


#############################
# 4.remove_at - ამოიღებს კვანძს კონკრეტული პოზიციიდან.
# პირველი ინდექსი ამოიღებს head-ს, სხვანაირად, გადასვლით 
# პოულობს კვანძს და შლის მას.
    def remove_at(self, index):
        if index < 0 or self.head is None:# თუ ინდექსი არასწორია ან ლისტი ცარიელია
            return

        if index == 0:  # თუ პირველი კვანძია ამოსაღები
            self.head = self.head.next
            return

        current_node = self.head # ინდექსით კვანძის ძებნა
        current_position = 0

        while current_node.next and current_position < index - 1:
            current_node = current_node.next
            current_position += 1

        if current_node.next: # კვანძის ამოღება ლისტიდან
            current_node.next = current_node.next.next
########################
# 5.display - ეკრანზე გამოაქვს ყველა კვანძის მონაცემები.
    def display(self):
        current_node = self.head # ლისტის კვანძებზე გადასვლა და მონაცემის ჩვენება

        while current_node is not None: 
            print(current_node.data, end=" -> ")
            current_node = current_node.next


linked_list = LinkedList()
linked_list.append("Hello")
linked_list.append(10)
linked_list.append(True)
linked_list.append(5.5)
linked_list.display()
print()
linked_list.remove_at(2)
linked_list.remove_at(0)
linked_list.display()

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
############################
# 6.Stack კლასი წარმოადგენს სტეკს, რომელიც იყენებს 
# Node კლასის კვანძებს და არის LIFO სტრუქტურა (ბოლო 
# შემოსული პირველი გამოდის).

class Stack:
    def __init__(self):
        self.top_node = None # სტეკის ზედა კვანძი
        self.length = 0  # კვანძების რაოდენობ
##########################
# 7.empty ამოწმებს ცარიელია თუ არა სტეკი.
    def empty(self):
        return self.length == 0 # აბრუნებს True-ს თუ სტეკი ცარიელია

##############################
# 8.size აბრუნებს სტეკის ზომას.
    def size(self):
        return self.length
################################
# 9. push ამატებს ახალ კვანძს სტეკის ზედა ნაწილში.
    def push(self, data):
        new_node = Node(data) # ახალი კვანძის შექმნა
        new_node.next = self.top_node # ახალი კვანძი ხდება ზედა და აკავშირებს ძველს
        self.top_node = new_node
        self.length += 1
##############################
# 10. top აბრუნებს ზედა კვანძის მონაცემს, თუ სტეკი ცარიელია, 
# აბრუნებს შეცდომას.
    def top(self):
        if not self.empty(): # აბრუნებს ზედა კვანძის მონაცემს
            return self.top_node.data
        else:
            raise IndexError("Stack Is Empty")


############################
# 11. pop ამოიღებს და აბრუნებს ზედა კვანძის მონაცემს სტეკიდან.
    def pop(self):
        if not self.empty():
            popped_item = self.top_node.data
            self.top_node = self.top_node.next
            self.length -= 1
            return popped_item
        else:
            raise IndexError("Stack Is Empty")


stack = Stack()

print(f"Stack Is Empty: {stack.empty()}")
print(f"Stack Size: {stack.size()}")

stack.push(10)
stack.push(5)
stack.push(20)
stack.push(50)

print(f"Stack Is Empty: {stack.empty()}")
print(f"Stack Size: {stack.size()}")

print(stack.pop())
print(f"Stack Size: {stack.size()}")
print(stack.pop())
print(f"Stack Size: {stack.size()}")
print(stack.pop())
print(f"Stack Size: {stack.size()}")
print(stack.pop())
print(f"Stack Size: {stack.size()}")

print(stack.top())

# დავალება 2.

# დაწერეთ value გადაწოდების შედეგად ამოშლის ლოგიკა 
# დაკავშირებულ სიებში
class Node:
    def __init__(self, data=None):
        self.data = data  # კვანძის მონაცემი
        self.next = None  # კვანძის მიმთითებელი მომდევნო კვანძზე

class LinkedList:
    def __init__(self):
        self.head = None  # ლინკური ლისტის პირველი კვანძი

    def append(self, data):
        new_node = Node(data)  # ახალი კვანძის შექმნა
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def remove_by_value(self, value):
        # ამოწმებს არის თუ არა ლისტი ცარიელი
        if self.head is None:
            return

        # თუ ამოსაღები კვანძი არის პირველი კვანძი
        if self.head.data == value:
            self.head = self.head.next
            return

        # მოძებნის კვანძს რომლის მომდევნო შეიცავს აღნიშნულ მნიშვნელობას
        current_node = self.head
        while current_node.next and current_node.next.data != value:
            current_node = current_node.next

        # თუ ასეთი კვანძი მოიძებნა, ამოიღებს მას
        if current_node.next:
            current_node.next = current_node.next.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  # ლისტის დასასრული


# ლინკური ლისტის შექმნა და ფუნქციების ტესტირება
linked_list = LinkedList()
linked_list.append("Hello")
linked_list.append(10)
linked_list.append(True)
linked_list.append(5.5)

print("Before removing the link list:")
linked_list.display()

# წაშლის პირველი მნიშვნელობით "True" კვანძს
linked_list.remove_by_value(True)
print("Link list after removing True:")
linked_list.display()

# წაშლის პირველი მნიშვნელობით "Hello" კვანძს
linked_list.remove_by_value("Hello")
print("Link list after removing hello")
linked_list.display()

# წაშლის პირველი მნიშვნელობით 100 კვანძს (არაფერს არ გააკეთებს)
linked_list.remove_by_value(100)
print("Link list after removing 100:")
linked_list.display()
