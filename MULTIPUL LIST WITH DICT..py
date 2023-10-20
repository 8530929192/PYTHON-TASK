key=input("enter keys sepreted by space:-").split()
num=int(input("enter the number of value list:-"))
result_dict={}
for i in range(num):
    values=input(f"enter values sepreted by space for key {key[i]}:-").split()
    result_dict[key[i]]=values
print("\nCreated dicyonary:-")
print(result_dict)
    
    