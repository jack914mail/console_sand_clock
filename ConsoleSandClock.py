def printer(a):
    row_number = 0
    left_star_index = 0
    right_star_index = a-1
    if a % 2 == 0:
        height = a-1
    else:
        height = a

    while row_number < height:
        row_number = row_number + 1
        
        # drawing top part of sand clock
        if row_number <= round((height+1)/2):
            for j in range(a):
                if j >= left_star_index and j <= right_star_index:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
            if row_number == round((height+1)/2):
                continue
            left_star_index = left_star_index + 1
            right_star_index = right_star_index - 1

        # drawing button part of sand clock
        else:
            left_star_index = left_star_index - 1
            right_star_index = right_star_index + 1
            for j in range(a):
                if j >= left_star_index and j <= right_star_index:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()


your_number = int(input())
printer(your_number)
