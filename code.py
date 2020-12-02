import time
db={}
def create(key,value,timeout=0):
    if key in db:
        print("error:key already exists")
    else:
        if(key.isalpha()):
            if len(db)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32:
                    db[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error:key should not contain special characters & numbers")

def read(key):
    if key not in db:
        print("error:key does not exists in database..Please enter a valid key")
    else:
        b=db[key]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(key)+":"+str(b[0])
                return stri
            else:
                print("error:time-to-live of",key,"has expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri

def delete(key):
    if key not in db:
        print("error:key does not exist in database. Please enter a valid key")
    else:
        b=db[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del db[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            del db[key]
            print("key is successfully deleted")


create("ruby",25)
create("dinesh",70,3600)
create("rr123",50)
read("ruby")
read("dinesh")
create("ruby",50)
print(db)
delete("ruby")
print(db)

