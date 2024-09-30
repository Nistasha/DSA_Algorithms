def count_fish_caught(fish, baits):
    total_fish_caught = 0

    for bait in baits:
        # Find fish greater than the bait
        fish_to_catch = [f for f in fish if f > bait]
        
        # Catch up to 3 fish
        fish_caught = fish_to_catch[:3]
        
        # Remove the caught fish from the pond
        for caught_fish in fish_caught:
            fish.remove(caught_fish)
        
        # Increase the total count of fish caught
        total_fish_caught += len(fish_caught)

    return total_fish_caught


# Test examples
fish3 = [1, 2, 3, 4, 5]
baits3 = [1, 2]
print(count_fish_caught(fish3, baits3))  # Output: 5
