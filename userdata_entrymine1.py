import json

def fxn1():
    fh=open("entrydata1.txt","r")
    data=fh.read()
    data=json.loads(data)
    fh.close()
    print("file exists and is setup ")
    return data
    
def fxn2():
    fh=open("entrydata1.txt","w+")
    startdata=dict()
    data=json.dumps(startdata)
    fh.write(data)
    fh.close()
    print("exception block")
    return fxn1()
    
def fxn6():
    name=input("Enter names : ")
    email=input("Enter email : ")
    skills=input("Enter skill : ")
    exp=input("Enter years of expeience : ")
    phone=input("Enter phone number :")
    location= input("Enter location of residence: ")

    entry = dict()
    entry[email]={
    'name':name,
    'email':email,
    'skills':skills,
    'exp':exp,
    'phone':phone,
    'location':location
    }
    return entry
    
def fxn3(data):
    fh = open("entrydata1.txt","w")
    entry = fxn6()
    data.update(entry)
    data = json.dumps(data)
    fh.write(data)
    fh.close()
    print("data updated!")
    
def fxn4():
    fh = open("entrydata1.txt","r")
    data = fh.read()
    data = json.loads(data)
    for  x in data:
        print(x)
        print(data[x])
        print("==========================")
    fh.close()
    print(f"Total entries: {len(data)}")
    
        
def fxn_search():
    fh=open("entrydata1.txt","r")
    data=fh.read()
    data=json.loads(data)
    fh.close()
    
    choice=input("search by (1)email or (2)phone?")
    
    if choice=="1":
        email= input("Enter email")
        if email in data:
            print (data[email])
        else:
            print("Entry not found.")
            
    elif choice=="2":
        phone=input("Enter phone number:")
        found=False
        for x in data:
            if data [x].get("phone")== phone:
                print(data[x])
                found= True
                break
        if not found:
            print("Entry not found")
    
def doostart():
    inp = input(" Enter 1 for entry, 2 to display, 3 to search: ")
    if inp =="1":
        try:
            data= fxn1()
            fxn3(data)
        except:
            data= fxn2()
            fxn3(data)
    elif inp == "2":
        fxn4()
    elif inp == "3":
        fxn_search()
    else:
        print("Invalid input.")
        
doostart()