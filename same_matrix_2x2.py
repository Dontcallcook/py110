""" 
[1, 2, 3, 4] Comparison

[3, 1, 4, 2] if array1[0] == array2[1] and array1[1] == array2[3] and array1[2] == array2[0]

[4, 3, 2, 1] if array1[0] == array2[3] and array1[1] == array2[2] and array1[2] == array2[1]

[2, 4, 1, 3] if array1[0] == array2[2] and array1[1] == array2[0] and array1[2] == array2[3] 

"""


def count_different_matrices(matrices):
    unique_matrices = set()

    for matrix in matrices:
        a, b, c, d = matrix
        
        rotations = [
            (a, b, c, d),
            (c, a, d, b),
            (d, c, b, a),
            (b, d, a, c)
        ]

        min_rotation = min(rotations)
        unique_matrices.add(min_rotation)

    return len(unique_matrices)


""" 
count_different_matrices([[1, 2, 3, 4],
                [3, 1, 4, 2],
                [4, 3, 2, 1],
                [2, 4, 1, 3]]) """

print(count_different_matrices([[5, 1, 2, 6], [5, 4, 3, 5], [2, 5, 6, 1]]))
