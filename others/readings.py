def solution(readings, k):
    count = 0  # Initialize the counter
    
    for num in readings:
        #original_num = num   Keep track of the original number for comparison
        # Continue dividing num by k while it's divisible by k
        while num % k == 0:
            num //= k  # Integer division
        
        # If num is reduced to 1, original_num is a power of k
        if num == 1:
            count += 1
    
    return count  # Return the total count

readings = [2, 4, 7, 8, 16, 32, 120]
k = 2
print(solution(readings, k))  # Output: 5

readings = [10201, 101, 1030301, 101, 101]
k = 101
print(solution(readings, k))  # Output: 5
