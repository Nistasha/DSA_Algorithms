def solution(laps):
    best_times = {}  # Dictionary to store the best time for each driver
    eliminated_drivers = []  # List to store the order of eliminations

    # Step 1: Initialize the best times after the first lap
    first_lap = laps[0]
    for entry in first_lap:
        name, time = entry.split()  # Split the string to extract name and time
        best_times[name] = int(time)  # Store the best time in the dictionary

    # Step 2: Loop through the rest of the laps to update best times and eliminate drivers
    for lap in laps[1:]:
        # Update each driver's best time based on the current lap
        for entry in lap:
            name, time = entry.split()
            time = int(time)
            if name in best_times:
                # Update best time if the current lap time is faster
                best_times[name] = min(best_times[name], time)
            print("best_times in each loop",best_times)

        # Step 3: Find the driver(s) with the slowest best time (maximum time)
        slowest_time = max(best_times.values())  # Find the slowest best time
        to_eliminate = [name for name, time in best_times.items() if time == slowest_time]  # Get all drivers with that time

        # Step 4: Eliminate the driver(s) with the slowest time
        to_eliminate.sort()  # Sort their names alphabetically if there's a tie
        eliminated_drivers.extend(to_eliminate)  # Add to the elimination order

        # Remove the eliminated drivers from the race
        for driver in to_eliminate:
            del best_times[driver]

    # Add the last remaining driver(s) to the elimination list
    remaining_drivers = sorted(best_times.keys())  # In case more than one remains (tie)
    eliminated_drivers.extend(remaining_drivers)
    
    return eliminated_drivers
laps = [
    ["Gina 155", "Eddie 160", "Joy 161", "Harold 161"],
    ["Harold 151", "Gina 153", "Joy 160", "Eddie 160"],
    ["Harold 149", "Joy 150", "Gina 152", "Eddie 154"],
    ["Harold 148", "Gina 150", "Eddie 151", "Joy 155"]
]

print(solution(laps))
