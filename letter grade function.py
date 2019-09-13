grade=int(input("What is your grade?"))
def letterGrade(grade):
    x=grade
    if x <60:
        print("F")
    elif 60 <=x and x <=69:
        print("D")
    elif 70 <=x and x<=79:
        print("C")
    elif 80 <=x and x <=89:
        print("B")
    elif 90 <=x and x<=100:
        print("A for Awsome.")
print(letterGrade(grade))
