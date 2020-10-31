def inverse_matrix(matrix):
    l = len(matrix)
    for i in matrix:
        if len(i) != l:
            return None
        
    for i in l:
        for j in l:
            if i != j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    return matrix

if "__name__" == "__main__":
    print(f"Inverse of the matrix is inverse_matrix([[1,2,3],[9,8,7],[6,4,5]])")
