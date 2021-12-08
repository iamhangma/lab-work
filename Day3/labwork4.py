#
list_1 = []
num = int(input("Enter number of element in last"))
#iteratingtill num to append element in list
for i in range(1, num+1):
    e=int(input("Enter element:"))
    list_1.append(e)
# print maximum element 
print("Smallest element is:", min(list_1))