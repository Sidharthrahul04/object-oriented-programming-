import json
import csv


#txt file
# file_text=["alphonse","yechuri","sebastian","munir","salahuddin","ragesh","sahadevan","2025"]  #only string can be written

# file_path="C:/Users/rahul/OneDrive/Desktop/output.txt"   #relative file we can also add an absolute file path too

# try:
#     with open(file_path,"r") as file:
#         content=file.read()
#         print(content)
# except Exception as e:
#     print("file already exists")


#json file
# employee={"clerk":"azhikode",
#           "cook":"lavakusha",
#           "driver":"manikuttan"
#          }

# path="C:/Users/rahul/OneDrive/Desktop/test.json"

# try:
#     with open(path,"r") as file:
#         content=json.load(file)
#         print(content["clerk"])
# except Exception as e:
#     print(e)



#csv file
# employee=[["Squidword",24],["patrick",33],["spongebob",37]]

# path="C:/Users/rahul/OneDrive/Desktop/test.csv"

# try:
#     with open(path,"r") as file:
#         content=csv.reader(file)
#         for i in content:
#             print(i)
# except Exception as e:
#     print(e)