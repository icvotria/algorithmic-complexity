import random

def shuffle(lst):

    indexes = [i for i in range(len(lst))]
    
    new_index_order = []
    new_lst = []
    
    while(len(indexes) > 0):
        rand = random.choice(indexes)
        new_index_order.append(rand)
        indexes.remove(rand)

    for item in lst:
        index = lst.index(item)
        new_index = new_index_order[index]
        x = lst[new_index]
        new_lst.append(x)