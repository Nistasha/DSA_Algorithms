def solution(state, operations):
    for operation in operations:
        if operation == "L":
            # Find the first index where the value is 0 and set it to 1
            for i in range(len(state)):
                if state[i] == 0:
                    state[i] = 1
                    break
        elif operation[0] == "C":
            # Extract the index from the "C<index>" operation
            index = int(operation[1:])
            state[index] = 0
    
    # Convert the state list to a binary string and return it
    return ''.join(map(str, state))

# Example usage:
state = [0, 0, 0, 0, 0]
operations = ["L", "L", "C0", "L", "C3", "L"]
print(solution(state, operations))  # Output: "1110000000"
