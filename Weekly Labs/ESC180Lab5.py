#Problem 1
def list1_start_with_list2(list1, list2):
    if len(list1) >= len(list2):
        for i in range(len(list2)):
            if list1[i] != list2[i]:
                return False
        return True
    else:
        return False


#Problem 2
def match_pattern(list1, list2):
    if len(list1) >= len(list2):
        for i in range(len(list1) - len(list2)):
            if list1[i] == list2[0]:
                position = i
                for j in range(len(list2)):
                    if list1[position] == list2[j]:
                        position += 1
                        if j == len(list2) -1:
                            return True
                    else:
                        break
        return False
    else:
        return False

def match_pattern2(list1, list2):
    for i in range(len(list1) + 1 - len(list2)):
        if list1[i:i + len(list2)] == list2:
            return True
    return False

list1 = [0, 1, 2, 3, 4 ,5]
list2 = [3, 4, 5]


#Problem 3
def repeats(list0):
    for i in range(len(list0) - 1):
        if list0[i] == list0[i + 1]:
            return True
    return False


#Problem 4A
def print_matrix_dim(M):
    return (str(len(M)) + " x " + str(len(M[0])))


#Problem 4B
def mult_M_v(M, v):
    newVector = []
    dotproduct = 0
    if len(M[0]) == len(v):
        for i in range(len(M)):
            dotproduct = 0
            for j in range(len(M[i])):
                dotproduct += M[i][j] * v[j]
            newVector.append(dotproduct)
        return newVector
    else:
        return "Multiplication not possible"

#Problem 4C
def mult_M1_M2(M2, M1):
    newMatrix = []
    for z in range(len(M1)):
        newMatrix.append([])

    if len(M1[0]) == len(M2):
        #rows M1
        for i in range(len(M1)):
            #row M1
            for j in range(len(M1)):
                dotproduct = 0
                #rows M2
                for k in range(len(M2)):
                    dotproduct += M1[j][k] * M2[k][i]
                newMatrix[j].append(dotproduct)
        return newMatrix
    else:
        return "Multiplication not possible"

def mult_M1_M2_two(M1, M2):
    newMatrix = []
    for z in range(len(M1)):
        newMatrix.append([])

    if len(M1[0]) == len(M2):
        for i in range(len(M1)):
            for j in range(len(M2[0])):
                dotproduct = 0
                for k in range(len(M2)):
                    dotproduct += M1[j][k] * M2[k][i]
                newMatrix[i][j].append(dotproduct)
        return newMatrix
    else:
        return "Multiplication not possible"

if __name__ == '__main__':
    listA = [0, 1, 2, 3, 4, 5, 7, 6, 6]
    listB = [2, 4, 4, 5]

    matrix2 = [[5,  6],
               [0, 6],
               [4, 6]]

    matrix1 = [[2, 5, 4],
               [8, 3, 0]]

    matrixi = [[1, 0, 0],
               [0, 1, 0],
               [0, 0, 1]]



    vector1 = [2, 3]

    #Problem 1
    print(list1_start_with_list2(listA, listB))

    #Problem 2
    print(match_pattern(listA, listB))

    #Problem 3
    print(repeats(listA))

    #Problem 4A
    print(print_matrix_dim(matrix1))

    #Problem 4B
    print(mult_M_v(matrix1, vector1))

    #Problem 4C
    print(mult_M1_M2_two(matrixi, matrix2))