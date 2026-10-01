# class School:
#     n=0
#     total=0
#     def __init__(self,name,cgpa):
#         self.name=name 
#         self.cgpa=cgpa
#         School.n+=1
#         School.total+=cgpa

#     @classmethod
#     def avg(cls):
#         return School.total/School.n

# try:
#     n=input("Enter the name:")
#     c=float(input("enter cgpa:"))

#     s=School(n,c)
    
# except Exception as e:
#     print(f"{e} error has occured")


# # except IndexError
# # except TypeError   \\Operation applied to an incompatible data type	eg:"age: " + 25\\
# # except ValueError 
# # except FileNotFoundError
# # except ZeroDivisionError
# # except KeyError
# # except Exception as e 

class AgeRestrictionError(Exception):
    pass

class OutOfStorageError(Exception):
    pass

class AppStore:
    n=0
    def __init__(self,app_name,storage_required,min_age):
        self.app_name=app_name
        self.storage_required=storage_required
        self.min_age=min_age

    def download(self,age,storage):
        if age<self.min_age:
            raise AgeRestrictionError("Your age should be greater than 13")
        elif storage<self.storage_required:
            raise OutOfStorageError("Insufficient Storage")
        else:
            print("app downloaded !")
            AppStore.n+=1

app=AppStore("PES",2.5,13)

attempts=[(13,1),(15,2.1),(18,7)]
for age,storage in attempts:
    try:
        app.download(age,storage)
    except AgeRestrictionError as e:
        print(e)
    except OutOfStorageError as e2:
        print(e2)

print(f"No. of downloads is : {AppStore.n}")
































     