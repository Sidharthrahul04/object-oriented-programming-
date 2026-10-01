import os

def file_read_write(file_name):
    try:
        if not os.path.exists(file_name):
            file_content=input("enter the file content:")
            with open(file_name,"x") as file:
                file.write(file_content)
        with open(file_name,"r") as file:
            content=file.read()
            print(f"the content inside{file_name} is ->")
            print(content)
    except Exception as e:
        print(e)


file_name=input("enter the file name/path:")  #if file name provided it creates a relative file else an absolute file.
file_read_write(file_name)
