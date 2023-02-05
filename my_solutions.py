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

def tape_equilibrium(A): #todo: revisit for max marks
    '''
    returns the minimum sum of adjacent
    numbers in an array
    '''
    lhs = 0
    rhs = 0
    results = []

    for i in range(len(A)-1):
        lhs = sum(A[:i+1])
        rhs = sum(A[i+1:])
        results.append(abs(lhs-rhs))
    return min(results)

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

def max_counter(A, N): #todo: revisit for max marks
    '''
    count occurences in an array according to the max
    counter method, N being the max counter
    '''
    counts = {}
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

def missing_int(A): #todo: revisit for max marks
    '''
    returns the smallest positive integer that does not occur
    in a given sequence.
    '''
    a_sorted = sorted(set(A))
    if a_sorted[-1] <= 0:
        return 1
    else:
        for i in range(len(a_sorted)):
            if a_sorted[i] != i+1:
                return i+1
        return A[-1] + 1

if __name__ == '__main__':
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
    print(missing_int([1,3,6,4,1,2]))