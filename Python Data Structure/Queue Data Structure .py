# Queue Implementatiion :

queue = []

def Enqueue():
    element = input("Enter the element : ")
    queue.append(element)
    print(queue," is added the queue ")

def Dequeue():
    if not queue:
        print("queue is Empty")
    else:
        e = queue.pop(0)
        print("removed element : ",e)
        print(queue)
def show():
    print(queue)
while True:
    print("Select the Operation :  1.Enqueue  2.Dequeue  3.show 4.Quit ")
    choice = int(input())

    if choice == 1 :
        Enqueue()

    elif choice == 2 :
        Dequeue()

    elif choice == 3:
        show()
    elif choice == 4:
        break
    else:
        print("Enter the currect operetion !")
