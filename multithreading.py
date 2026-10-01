import threading
import time

# def walk_dog(name):
#     time.sleep(5)
#     print(f"walked {name}")

# def pick_trash():
#     time.sleep(2)
#     print("took trash")

# def check_mail():
#     time.sleep(4)
#     print("checked mail")

# t1=threading.Thread(target=walk_dog,args=("scoobey",))
# t1.start()
# t2=threading.Thread(target=pick_trash)
# t2.start()
# t3=threading.Thread(target=check_mail)
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# print("All tasks done!")



# def cook(dish,t):
#     print(f"item {dish} cooking..")
#     time.sleep(t)
#     print(f"item {dish} cooked!")

# items=[("biriyani",5),("noodles",2)]
# l=[]
# for i in items:
#     t=threading.Thread(target=cook, args=i)
#     l.append(t)
#     t.start()
# for i in l:
#     i.join()
# print("all done!")


def cook_biriyani(dish,t):
    print(f"item {dish} cooking..")
    time.sleep(t)
    print(f"item {dish} cooked!")

def cook_noodles(dish,t):
    print(f"item {dish} cooking..")
    time.sleep(t)
    print(f"item {dish} cooked!")

items=[cook_biriyani,("biriyani",5)],[cook_noodles,("noodles",2)]
l=[]
for i,j in items:
    t=threading.Thread(target=i, args=j)
    l.append(t)
    t.start()
for i in l:
    i.join()
print("all done!")