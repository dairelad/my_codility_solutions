def perm_missing_elem(A):
    '''
    returns the missing element in an array
    '''
    if A:
        a_sorted = sorted(A)
        for i in range(len(a_sorted)):
            if a_sorted[i] != i+1:
                return i+1
        return len(A)+1
    else:
        return 1

def odd_occurences_array(A):
    '''
    returns the odd occurences in an array
    '''
    element_freq = dict()
    for elem in A:
        if elem in element_freq.keys():
            freq = element_freq.get(elem) + 1
            element_freq.update({elem:freq})
        else:
            element_freq.update({elem:1})

    odd_occurences = []
    for key, value in element_freq.items():
        if value % 2 != 0:
            odd_occurences.append(key)
    return odd_occurences

def tape_equilibrium(A):
    '''
    returns the minimum sum of adjacent
    numbers in an array
    '''
    results = [0] * (len(A) -1)

    # inefficent solution O(n*n): but very succint
    # lhs = rhs = 0
    # for i in range(len(A)-1):
    #     lhs = sum(A[:i+1])
    #     rhs = sum(A[i+1:])
    #     results.append(abs(lhs-rhs))
    # return min(results)

    # efficient algorithm
    lhs_sums =[0] * len(A)
    rhs_sums =[0] * len(A)
    sum_r = 0
    sum_l = 0
    for i in range(len(A)-1):
        sum_l = sum_l + A[i]
        lhs_sums[i] = sum_l
        sum_r = sum_r + A[len(A)-1-i]
        rhs_sums[len(rhs_sums)-1-i] = sum_r

    del(lhs_sums[-1])
    del(rhs_sums[0])

    for i in range(len(lhs_sums)):
        sum = abs(rhs_sums[i] - lhs_sums[i])
        results[i] = sum
    return results

def perm_check(A):
    '''
    returns 1 if the input array is a permutation.
    (sequence of unique integers from 1-N) Else 0
    '''
    if A:
        a_sorted = sorted(A)
        for i in range(len(a_sorted)):
            if a_sorted[i] != i+1:
                return 0
        return 1

def max_counter(A, N): #todo: improve performance O(N*M)
    '''
    count occurences in an array according to the max
    counter method, N being the max counter
    '''
    counts = {}
    max_c = 0
    for i in range(N):
        counts.update({i+1:0})

    for i in range(len(A)):
        if A[i] <= N:
            freq = counts.get(A[i])
            counts.update({A[i]:freq+1})
        elif A[i] > N:
            max_c = max(list(counts.values()))
            counts = {x:max_c for x in counts}

    result =[]
    for key, value in counts.items():
        result.append(value)
    return result

def missing_int(A): #todo: improve correctness
    '''
    returns the smallest positive integer that does not occur
    in a given sequence.
    '''
    a_sorted = sorted(set(A))
    if len(a_sorted) < 1:
        return 1
    elif a_sorted[-1] < 0:
        return 1
    elif len(a_sorted) == 1:
        return a_sorted[0] + 1
    else:
        for i in range(len(a_sorted)-1):
            # ignore negative values and zero
            if a_sorted[i+1] <= 0:
                continue
            elif a_sorted[i+1] - a_sorted[i] != 1:
                return a_sorted[i] + 1
        return a_sorted[-1] + 1

def passing_cars(A): #todo: improve performance O(N**2)
    '''
    count the number of passing cars on the road.
    '''
    cars_passing = 0
    for i in range(len(A)):
        count = 0
        if A[i] == 0:
            for x in range(len(A)-1):
                x = i + x + 1 # start counting from the next car onwards
                if x < len(A):
                    if A[x] == 1:
                        count += 1
                else:
                    break
            cars_passing += count
    return cars_passing

def count_div(A, B, K):
    '''
    compute number of integers divisible by k in range [a..b].
    '''
    # brute force:
    # count = 0
    # if A == 0 and B == 0:
    #     return 1
    # else:
    #     for i in range(A,B):
    #         if i % K == 0:
    #             count += 1
    #     return count

    # efficient solution:
    if A == 0 and B == 0:
        return 1
    else:
        while A % K != 0:
            A += 1
        while B % K != 0:
            B -= 1
        return ((B - A) // K) + 1

if __name__ == '__main__':
    # todo: add more test cases for each question to account for edge cases
    print('perm missing element:')
    print(perm_missing_elem([1,2,3,4,6]))

    print('\nodd occurences:')
    print(odd_occurences_array([1,1,1,2,2,3,3,3,3,4]))

    print('\ntape equilibrium:')
    print(tape_equilibrium([3,1,2,4,3]))

    print('\nperm check:')
    print(perm_check([3,1,2,4,3]))

    print('\nmax counter:')
    print(max_counter([3,4,4,6,1,4,4],5))

    print('\nmissing int:')
    print(missing_int([-1, -3]))
    print(missing_int([1,3,6,4,1,2]))
    print(missing_int([3,6,4,2]))
    print(missing_int([113415135]))
    print(missing_int([-3,-1,-2,1,2,4]))

    print('\npassing cars:')
    print(passing_cars([0,1,0,1,1]))
    print(passing_cars([0]))
    print(passing_cars([0,1,1,1,1]))

    print('\ncount div:')
    print(passing_cars(6,11,2))