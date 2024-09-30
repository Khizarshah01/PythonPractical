def pract1():
    #Q1
    a = [1,2,3,4,6,7]
    print(a)
    print("Created By khizar shah Roll no 86 :>")

def pract2():
    #Q2
    s1 = "khizar"
    s2 = "shah"
    s3 = s1+" "+s2
    print(s3)
    print("accesss substring" +" "+ s3[4:11])
    print("Created By khizar shah Roll no 86 :>")

def pract3():
    #Q3
    # createing list in python\
    list = [1,2,3,4,56]
    print (list)

    # remove
    list.remove(4)
    print(list)

    # append
    list.append(99)
    print(list) 
    print("Created By khizar shah Roll no 86 :>")
    
def pract4():
    #Q4
    # tuple is a structure where element can not ne create , delete, update after the decleration
    a = (1,2,3,45)
    print(a)
    print("Created By khizar shah Roll no 86 :>")

def pract5():
    #Q6 
    # dictionary is similar to maping a key to value like a map in many programiun language 
    dic = {"a" : "khizar",
        "b" : "arshad"}
    print(dic)
    print("Created By khizar shah Roll no 86 :>")

def practical(i):
    if i == 1:
        print(":>")
        print("practical one")
        
        print()
        pract1()
    elif i == 2:
        print(":>")
        print("practical two")
        print()
        pract2()
    elif i == 3:
        print(":>")
        print("practical three")
        print()
        pract3()
    elif i == 4:
        print(":>")
        print("practical four")
        print()
        pract4()
    elif i == 5:
        print(":>")
        print("practical five")
        print()
        pract5()
    else : 
        print(">>>>> You enter wrong input <<<<")
while True:
    
    prac = input("Enter practical number:  ")
    if prac == "00":
        break
    idx = int(prac) 
    practical(idx)
    
    
