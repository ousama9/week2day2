
def numbers_less_than_ten(l):
    l1 = []
    for i in l:
        if i<10:
            l1.append(i)
        return(l1)

            
print(numbers_less_than_ten([1,11,14,5,8,9]))






l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def Merge(l_1, l_2):
    final_list = l_1 + l_2
    final_list.sort()
    return(final_list)
print(Merge(l_1, l_2))



