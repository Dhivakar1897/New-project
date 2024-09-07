# How to get input from user
a=int(input("Enter The Number A:"))
b=int(input("Enter The Number B:"))
c=a+b
print(c)
print("-----------------------------")
name1,name2,name3=input("Enter The 3 Names:").split()
print("Name1:",name1)
print("Name2:",name2)
print("Name3:",name3)
print("-----------------------------")
name1,name2,name3=input("Enter The 3 Names With Comma:").split(',')
print("Name1:",name1)
print("Name2:",name2)
print("Name3:",name3)
print("-----------------------------")
# Get Multiline input from user(paragraph)
para=[]
print("Enter The Paragraph:")
while True:
    user=input()
    if user:
        para.append(user)
    else:
        print("Your Para!")
        break
out='\n'.join(para)
print(out)
# Creating list using element from user input
print("Create Your List:")
list=[]
n=int(input("How Many Element Do You Want?:"))
print("Enter Your Element One by One!")
for i in range(n):
    user=int(input("Enter Your Element:"))
    list.append(user)
print("Your List:",list)
print("-----------------------------")
# While Loop using
print("Create Your List:")
list1=[]
print("Enter Your Element One by One!")
while True:
    user1=int(input("Enter The Element:"))
    list1.append(user1)
    choise=input("If you want finish,put 'yes', otherwise put enter to continue:")
    if choise=='yes':
        break
print("Your List:",list1)
