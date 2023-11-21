# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from linked_list import SingleLinkedList

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


list = SingleLinkedList()
list.insertLast(1)
list.insertLast(2)
list.insertLast(3)
list.printList()
# list.insertAfter(list.find(2), 98)
# list.printList()
# list.deleteNode(list.find(2))
# list.printList()
# list.insertBefore(list.find(98), 76)
# list.printList()
# list.deleteNode(list.find(1))
# list.printList()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
