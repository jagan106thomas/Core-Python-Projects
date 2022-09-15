employee_id=[11,12,13,14,15,16,17,18,19]
project1={11,12,13,14,15,16}
project2={14,15,16,17,18}
project3=set()
while True:
    ask=input("Do you want to assign employee Type Yes or No")
    if ask.lower()=="yes":
        ID=int(input("Enter the Employee ID to Assign from {}".format(employee_id)))
        if ID in employee_id:
            emply_id={ID}
        else:
            print("Enter a Valid Employee ID")
            emply_id = set()
    elif ask.lower()=='no':
        exit()
    else:
        print("Enter Yes or No Please")
        emply_id = set()

    if project1.intersection(emply_id) and project2.intersection(emply_id):
        print("Already working in other Project")
    else:
        project3=project3.union(emply_id)
        print("The Project3 Has this many people",project3)
