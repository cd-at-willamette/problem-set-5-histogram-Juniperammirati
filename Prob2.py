##################################################
# Name: Juniper Ammirati
# Collaborators:
# Estimate of time spent (hr): 1.5
##################################################

def is_magic_square(array:list[list[int]]) -> bool:
    #pass
    # Check if rows have the same length as the outer list
    if not array or any(len(row) != len(array) for row in array):
        return False
    
    n = len(array)  # Size of magic square 
    Target_sum = sum(array[0])  # The firsts rows sum  is equal to the target sum

    # Checks the sum of each row
    for row in array:
        if sum(row) != Target_sum:
            return False

    # Checks sum of each column
    for col in range(n):
        if sum(array[row][col] for row in range(n)) != Target_sum:
            return False

    # Checks sum of the main diagonal
    if sum(array[i][i] for i in range(n)) != Target_sum:
        return False

    # Check sum of the anti-diagonal
    if sum(array[i][n - 1 - i] for i in range(n)) != Target_sum:
        return False

    return True
not_magic = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
small = [[8,1,6],[3,5,7],[4,9,2]]
print(is_magic_square(small))
print(is_magic_square(not_magic))

