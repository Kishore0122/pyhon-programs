def second_max(num):
    if len(num)<2:
        return "less than 2 elements"
    sorted_num=sorted(num)
    return sorted_num[-2]
num=input("enter set of numbers with sapce:")
num_list=list(map(int,num.split()))
result=second_max(num_list)
print("second max=",result)
