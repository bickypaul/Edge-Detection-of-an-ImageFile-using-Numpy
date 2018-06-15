#importing the numpy library
import numpy as np

def vert_edge(w,h,big_matrix):
    try:
        size_of_square_matrix = 3 #standard size of the submatrix
        vef = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
        #Calculating the total number of possible square submatrices can be formed from the given matrix and the output matrix.
        no_of_square_matrices = ((w-size_of_square_matrix)+1)*((h-size_of_square_matrix)+1)
        sosm=size_of_square_matrix
        row=(h-size_of_square_matrix)+1                     #It is the number of rows it will cover to find out the desired output.
        column=(w-size_of_square_matrix)+1                  #It is the number of columns it will cover to find out the desired output.
        max_val=0
        result = []
        r = (h-3)+1                                         #row value of horizontal edge filter
        c = (w-3)+1                                         #column value of horizontal edge filter

        for i in range(row):
            for j in range(column):
                sq = big_matrix[i:i+sosm,j:j+sosm]
                sum = 0
                for k in range(3):
                    for l in range(3):
                        sum += (sq[k,l] * vef[k,l])
                result.append(sum)
        result_matrix = np.asarray(result).reshape(r,c)     #reshaping the resultant matrix
        return result_matrix

    except Exception as e:
        print("Invalid Input, Try again",str(e))
