'''This file contains my solutions to the lessons on Codility
'''

def binary_gap(N):
    '''
    find longest sequence of zeros in binary representation
    of an integer
    '''
    bin_N = bin(N).replace("0b", "")
    bin_gap = 0
    current_gap = 0
    start_count = False
    for i in bin_N:
        if i == '1':
            start_count = True
        if i == '0' and start_count:
            current_gap += 1
        if i == '1' and start_count:
            bin_gap = max(current_gap,bin_gap)
            current_gap = 0
    return bin_gap

def cyclic_array(A, K):
    '''
    rotate an array to the right by a given number of steps
    '''
    output_array = [None] * (len(A))
    for i in range(len(A)):
        new_index = (i+K)%len(A)
        output_array[new_index] = A[i]
    return output_array

def frog_jump(X,Y,D):
    '''
    count the minimal number of jumps from position X to Y
    '''
    distance = Y-X
    jumps = distance//D + bool(distance%D)
    return jumps

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
        element_freq.update({elem:element_freq.get(elem,0)+1})

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

    # inefficent solution O(n*n), but very concise:
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

def frog_river_one(X, A): #todo: improve efficiency
    '''
    find the earliest time when a frog can jump to the other side of a river.
    '''
    time = 0
    hops_left = X
    leaves_fallen = []
    for pos in A:
        if pos not in leaves_fallen:
            leaves_fallen.append(pos)
            hops_left -= 1
        if hops_left == 0:
            return time
        time += 1
    return -1

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
    # brute force solution:
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

def genomic_range_query(S, P, Q):
    '''
     Find the minimal nucleotide from a range of sequence DNA.
     '''

def triangle():
    '''
    Determine whether a triangle can be built from a given set of edges.
    '''

def distinct(A):
    '''
    Compute number of distinct values in an array.
    '''
    return len(set(A))

def maxProductOfThree(A):
    '''
    Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).
    '''
    N = len(A)
    for i in range(len(a)):
        p = i; q = i+1; r = i+2
        triplet = bool(0 <= p < q < r < N)

        #if triplet:

if __name__ == '__main__':
    # todo: add more test cases for each question to account for edge cases
    print('binary gap:')
    print(binary_gap(1041))

    print('\ncyclic array:')
    print(cyclic_array([3,8,9,7,6],3))

    print('\nfrog jump:')
    print(frog_jump(1,5,2))
    print(frog_jump(0,0,2))

    print('\nperm missing element:')
    print(perm_missing_elem([1,2,3,4,6]))

    print('\nodd occurences:')
    print(odd_occurences_array([1,1,1,2,2,3,3,3,3,4]))

    print('\ntape equilibrium:')
    print(tape_equilibrium([3,1,2,4,3]))

    print('\nfrog river one:')
    print(frog_river_one(5,[1,3,1,4,2,3,5,4]))
    print(frog_river_one(5,[3]))

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
    print(count_div(6,11,2))

    print('\ngenomic range query:')
    print(genomic_range_query(6,11,2))

    print('\ndistinct:')
    print(distinct([2,1,1,2,3,1]))