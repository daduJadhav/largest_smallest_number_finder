# Largest no. finder

list = [1,2,3,4,5,6,7,8,9,10,11,12,33,56,77]

def largest_no_finder(no_List):
    max = no_List[0]

    for i in range(1, len(no_List)):
        if no_List[i] > max:
            max = no_List[i]

    print('largest no is  : ',max)

largest_no_finder(list)