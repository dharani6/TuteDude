try:
    with open ('Sample1.txt','r') as fob:
        for i,line in enumerate(fob, start =1):
          print(f"\033[91mline{i}\033[0m:{line.strip()}")
except FileNotFoundError:
    print("File not found ERROR")
except Exception as e:
    print(e)
        



