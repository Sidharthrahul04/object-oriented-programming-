import json
import csv

#txt file
# file_text=["alphonse","yechuri","sebastian","munir","salahuddin","ragesh","sahadevan","2025"]  #only string can be written

# file_path="C:/Users/rahul/OneDrive/Desktop/output.txt"   #relative file we can also add an absolute file path too

# try:
#     with open(file_path,"w") as file:
#         for i in file_text:
#             file.write(f"{i} \n")
#         print("written")
# except Exception as e:
#     print("file already exists")


#json file
# employee={"clerk":"azhikode",
#           "cook":"lavakusha",
#           "driver":"manikuttan"
#          }

# path="C:/Users/rahul/OneDrive/Desktop/test.json"

# try:
#     with open(path,"x") as file:
#         json.dump(employee,file)
#         print("written")
# except Exception as e:
#     print(e)


#csv file
employee=[["Squidword",24],["patrick",33],["spongebob",37]]

path="C:/Users/rahul/OneDrive/Desktop/test.csv"

try:
    with open(path,"w") as file:
        writer=csv.writer(file)
        writer.writerow(employee)
        print("written")
except Exception as e:
    print(e)
