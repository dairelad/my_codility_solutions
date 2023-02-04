def perm_missing_elem(A):
    if A:
        a_sorted = sorted(A)
        for i in range(len(a_sorted)):
            if a_sorted[i] != i+1:
                return i+1
        return len(A)+1
    else:
        return 1


if __name__ == '__main__':
    print(perm_missing_elem([1,2,3,4,6]))