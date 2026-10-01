import os

def exists(path):
    print( os.path.exists(path))
    print(os.path.isdir(path))
    print(os.path.isfile(path))
    print(os.path.basename(path))
    print(os.path.dirname(path))

    # os.path.join("sample","test2.py")

    for i in os.listdir("."): #current folder  --"."
        print(i)

(exists("test.py"))