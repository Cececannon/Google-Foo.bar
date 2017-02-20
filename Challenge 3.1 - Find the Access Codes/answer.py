def answer(l):
    divisor_list = []
    index_list = []
    for i,n in enumerate(l):
        temp_index_list = []
        count = 0
        for j,o in enumerate(l[:i]):
            if n % o == 0:
                count += 1
                temp_index_list.append(j)
        index_list.append(temp_index_list)
        divisor_list.append(count)
    sum_list = [divisor_list[i] for sublist in index_list for i in sublist]   
    return sum(sum_list)
