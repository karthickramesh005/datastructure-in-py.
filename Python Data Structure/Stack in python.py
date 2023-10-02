# Stack Implementatiion :

stack = []

def push():
    element = input("Enter the element : ")
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("Stack is Empty")
    else:
        e = stack.pop()
        print("removed element : ",e)
        print(stack)

while True:
    print("Select the Operation :  1.Push  2.Pop  3.Quit ")
    choice = int(input())

    if choice == 1 :
        push()

    elif choice == 2 :
        pop_element()

    elif choice == 3:
        break
    else:
        print("Enter the currect operetion !")
