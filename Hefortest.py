list1 = [1,2,3,4]
list2 = [320,430,975]
reuslt = 430
x = 0
    
print(list1)
print(list2)



def find_number_in_list(list1,thing_to_search,list2):
    for firstconfirm in list1:
        if firstconfirm == reuslt:
            listposition = list1.index(thing_to_search)
            listnumber = list2[listposition]
            return listnumber


print(find_number_in_list(list2,reuslt,list1))
