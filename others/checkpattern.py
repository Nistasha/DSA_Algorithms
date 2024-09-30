def solution(panel, codes):
    results = []
    
    for code in codes:
        # Iterate over possible split points
        for x in range(1, len(code)):  # Start from 1 to ensure index is not empty
            index = code[:x]  # Everything before x
            pattern = code[x:]  # Everything from x to the end
            
            # Convert the index to an integer
            int_index = int(index)  
            
            # Check if the index is out of bounds
            if int_index >= len(panel):  
                results.append("not found")
                continue
            
            # Calculate the end position of the substring in panel
            substring_end = int_index + len(pattern)
            
            # Extract the substring and compare
            if panel[int_index:substring_end] == pattern:
                results.append(pattern)
            else:
                results.append("not found")
    
    return results

# Example usage
panel = "2311453915"
codes = ["0211", "639"]
result = solution(panel, codes)
print(result)  # Expected output: ["not found", "11", "not found", "39", "not found"]
