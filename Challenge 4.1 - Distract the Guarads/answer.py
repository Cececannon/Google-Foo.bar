import math

def is_a_solution(original_l, max_sol, req_sol):
    return max_sol >= req_sol

def common_factor(big,small):
    while(small!=0):
        r = small
        small = big % r
        big = r
    return big

def construct_candidates(new_list):
    output = []
    k = new_list[0]
    for i,x in enumerate(new_list[1:]):
        big = max(x,k)
        small = min(x,k)
        divisor = common_factor(big,small)  
        big = big / divisor
        small = small / divisor
        if x!=k and not math.log(big + small,2).is_integer():
            output.append(i+1)
    return output

def make_move(listy, i):
    return listy[1:i] + listy[i+1:]

def is_a_solution_possible(listy,n_sol,max_sol):
    return len(listy)/2 + n_sol <= max_sol
        
def backtrack(banana_list, original_l, n_sol, req_sol, max_solutions):  
    global max_sol
    max_sol = max_solutions
    #check if complete solution is found
    if is_a_solution(original_l, max_sol,req_sol):
        return original_l/2
    if is_a_solution_possible(banana_list,n_sol,max_sol):
        return max_sol
    #else proceed with backtrack
    if len(banana_list) > 1:
        n_candidates = construct_candidates(banana_list)
        for i in n_candidates:
            if backtrack(make_move(banana_list, i), original_l, n_sol + 1, 
                         req_sol, max(max_sol, n_sol+1)) >= req_sol:
                return max_sol
        if len(n_candidates)== 0:
            if backtrack(banana_list[1:], original_l, 
                         n_sol, req_sol, max_sol) >= req_sol:
                return max_sol
    return max_sol

def prune(banana_list, n_solutions, req_solutions):
    #count of infinite pairs
    n_sol = n_solutions
    req_sol = req_solutions
    #sort by even and odd
    even_list = []
    odd_list = []
    for x in banana_list:
        if x % 2 == 0:
            even_list.append(x)
        else:
            odd_list.append(x)
    if len(even_list) > 0 and len(odd_list) > 0:
        if len(even_list)==len(odd_list):
            n_sol += len(even_list)
            return ([], n_sol, req_sol)
        elif len(even_list)>len(odd_list):   
            n_sol += len(odd_list)
            return prune(even_list, n_sol, req_sol)
        elif len(even_list)<len(odd_list):   
            n_sol += len(even_list)
            return prune(odd_list, n_sol, req_sol)
    elif len(even_list) > 0:
        return prune([x/2 for x in even_list], n_sol, req_sol)
    return (odd_list, n_sol, req_sol)

def answer(banana_list):
    prune_list,n_sol,req_sol = prune(banana_list, 0, len(banana_list)/2) 
    return len(banana_list) - backtrack(
            prune_list, len(banana_list), n_sol, req_sol , n_sol) * 2
