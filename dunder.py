class Student:
    def __init__(self,members):
        self.members=members

    def __len__(self):
        return len(self.members)

    def __repr__(self):
        return repr(self.members)   

    def __getitem__(self, key):
        return self.members[key]

    def __setitem__(self, key, value):
         self.members[key]=value

    def __eq__(self, other):
        return self.members==other.members

def main():
    s1=Student(["akil","sugu"])
    s2=Student(["valverde","sugu"])

    print(len(s1))
    s1[0]="valverde"
    print(s1[0])
    print(s1[0]==s2[0])
    print(s1)

if __name__=='__main__':
    main()

        
        