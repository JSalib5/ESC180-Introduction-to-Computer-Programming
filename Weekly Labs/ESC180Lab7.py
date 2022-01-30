from numpy import *

#problem 1
def print_matrix(M_lol):
    print(array(M_lol))
    

#problem 2
def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0: 
            return i
    return len(row)

# #problem 2.5
# def get_back_ind(row):
#     for i in range(len(row) - 1, 0, -1):
#         if row[i] != 0: 
#             return i - 1
#     return len(row) - 1

#problem 3
def get_row_to_swap(M, start_i):
    leading_coefficients = []
    for i in range(start_i, len(M)):
        leading_coefficients.append(get_lead_ind(M[i]))
    smallest = min(leading_coefficients)
    return leading_coefficients.index(smallest) + start_i 

#problem 4
def add_rows_coefs(r1, c1, r2, c2):
    add_rows = [0]*len(r1)
    for i in range(len(r1)):
        add_rows[i] = r1[i] * c1 + r2[i] * c2
    return add_rows

#problem 5
def eliminate(M, row_to_sub, best_lead_ind):
    newMatrix = [[0]* len(M[0])] * len(M)
    eliminate_coefficient = M[row_to_sub][best_lead_ind]
    for i in range(row_to_sub +1, len(M)):
        c2 = M[i][best_lead_ind]/eliminate_coefficient 
        newMatrix[i] = add_rows_coefs(M[i],1,M[row_to_sub],(-c2))
    for i in range(row_to_sub+1):
        newMatrix[i] = M[i]
    return newMatrix
#line 43 can use M[i] to avoid using a new matrix

#problem 6
def forward_step(M):
    for i in range(len(M)-1):
        M[i], M[get_row_to_swap(M, i)] = M[get_row_to_swap(M, i)], M[i]
        M_array = array(M) 
        M_array[[i, get_row_to_swap(M, i)]] = M_array[[get_row_to_swap(M, i), i]]
        M = M_array.tolist()
        M = eliminate(M, i, get_lead_ind(M[i]))
        print_matrix(M) 
        print("")
    return M

#problem 7
def backward_step(M):
    for i in range(len(M)-1, 0, -1):
        newMatrix = [[0]* len(M[0])] * len(M)
        eliminate_coefficient = M[i][i]
        for j in range(i):
            c2 = M[j][i]/eliminate_coefficient 
            newMatrix[j] = add_rows_coefs(M[j],1,M[i],(-c2))
        for j in range(i, len(M)):
            newMatrix[j] = M[j]
        M = newMatrix
    print(print_matrix(M))
    print("")
    for i in range(len(M)):
        reduced_rows = []
        for j in range(len(M[i])):
            reduced_rows.append(M[i][j] / M[i][i])
        M[i] = reduced_rows
    print_matrix(M)
    print("")
    return M
    
def solve(M, b):
    for i in range(len(M)):
        M[i].append(b[i])
    M = forward_step(M)
    M = backward_step(M)
    x = []
    for i in range(len(M)):
        x.append(M[i][len(M)])
    return x
    

if __name__ == '__main__':
    M = [[ 1, -2, 3],
         [ 3, 10, 1],
         [ 1, 5, 3]]
    b = [1, 2, 3]

    print(solve(M, b))
    
    #check
    M = array([[1,-2,3],[3,10,1],[1,5,3]])
    x = array([-0.51785714,0.28571429,0.6964285714285714])
    b = dot(M,x)        
    print(b)