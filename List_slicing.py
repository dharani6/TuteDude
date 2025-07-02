lst = [i for i in range(10+1)]
#print(lst)

req_len = len(lst)//2

new_lst =[lst[i] for i in range((req_len),0,-1)] # range(limties,incrementer)
print(new_lst)