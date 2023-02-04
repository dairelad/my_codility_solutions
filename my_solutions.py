def perm_missing_elem(A):
    if A:
        a_sorted = sorted(A)
        for i in range(len(a_sorted)):
            if a_sorted[i] != i+1:
                return i+1
        return len(A)+1
    else:
        return 1

def odd_occurences_array(A):
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
    lhs = 0
    rhs = 0
    results = []

    for i in range(len(A)-1):
        lhs = sum(A[:i+1])
        rhs = sum(A[i+1:])
        results.append(abs(lhs-rhs))
    return min(results)

if __name__ == '__main__':
    print('perm missing element:')
    print(perm_missing_elem([1,2,3,4,6]))

    print('\nodd occurences:')
    print(odd_occurences_array([1,1,1,2,2,3,3,3,3,4]))

    print('\ntape equilibrium:')
    print(tape_equilibrium([3,1,2,4,3]))