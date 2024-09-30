def find_indices(a, b):
    n = len(a)  # Assuming both arrays are of the same length
    for i in range(n):
        for j in range(i, n):  # Ensure I <= J
            if a[i] - b[j] == b[i] - a[j]:
                return i, j  # Return the first pair of indices that satisfies the condition
    return None  # If no such pair is found

# Test examples
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]

result = find_indices(a, b)
if result:
    print(f"Indices found: I = {result[0]}, J = {result[1]}")
else:
    print("No such indices found.")
