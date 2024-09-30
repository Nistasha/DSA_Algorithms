def count_key_changes(recording):
    # Normalize the recording to lower case, so that case doesn't matter
    normalized_recording = [key.lower() for key in recording]
    
    # Initialize the count of changes
    change_count = 0

    # Iterate through the recording and compare consecutive entries
    for i in range(1, len(normalized_recording)):
        # Check if the current key is different from the previous key
        if normalized_recording[i] != normalized_recording[i-1]:
            change_count += 1
    
    return change_count


# Test examples
recording1 = ['w', 'W', 'a', 'A', 'a']
recording2 = ['w', 'a', 'W', 'w']

print(count_key_changes(recording1))  # Output: 1
print(count_key_changes(recording2))  # Output: 2
