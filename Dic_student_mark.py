stud_mark = {"Vishakan":90,"Alex":85,"Janani":88,"Tharan":66,"Dharani":77}
try:
    name = input("Enter Student Name:")
    if name in stud_mark:
        print(stud_mark[name])
    else:
        print("Enter Name is not in list")
except KeyError:
    print("Key ERROR is seen, enter Name correctly ")
