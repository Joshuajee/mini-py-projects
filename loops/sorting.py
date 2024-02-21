my_list = [2, 30, 5, 50, 10, 2, 11, 6]

sorted_list = []

for i in range(len(my_list)):

    for j in range(i + 1, len(my_list)):
        
        if my_list[i] > my_list[j]:
            temp = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = temp
else:
    print("DONE")    
    print(my_list)

print(my_list)

"""
    Iteration X
        1st iteration x = 2
        Iteration Y
            1st iteration of y 2
            1st iteration of y 30
            1st iteration of y 5
            .
            .
            .
            last iteration of y 6
        2st iteration x = 30
        Iteration Y
            1st iteration of y 2
            1st iteration of y 30
            1st iteration of y 5
            .
            .
            .
            last iteration of y 6
"""