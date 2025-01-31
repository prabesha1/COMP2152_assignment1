"""
Author: Prabesh Shrestha
Student ID: 101538718
Course: Open Source Development COMP 2152
CRN: 50332
Assignment: #1
"""

# Creating Variables
# gym_member: str
gym_member = "Alex Alliton"

# preferred_weight_kg: float
preferred_weight_kg = 20.5

# highest_reps: int
highest_reps = 25

# membership_active: bool
membership_active = True

# favorite_exercise: str
favorite_exercise = "Deadlifts"  # Favorite workout activity

# Dictionary: Stores workout minutes for each friend
workout_stats = {
    "Alex": (30, 45, 20),       # (yoga, running, weightlifting)
    "Rakesh": (40, 30, 50),     # (yoga, running, weightlifting)
    "Amir": (25, 35, 45),       # (yoga, running, weightlifting)
    "Safal": (23, 31, 46)       # (yoga, running, weightlifting)
}

# Calculate total workout minutes and store separately
total_minutes_dict = {friend: sum(activities) for friend, activities in workout_stats.items()}

# Nested list: Extract workout minutes for each activity
# workout_list: list of lists
workout_list = [list(activities) for activities in workout_stats.values()]

# Slicing workout_list
# Yoga and running minutes for all friends
print("Yoga and Running Minutes:")
for row in workout_list:
    print(row[:2])

# Weightlifting minutes for the last two friends
print("\nWeightlifting Minutes for Last Two Friends:")
for row in workout_list[-2:]:
    print(row[2:])

# Check if any friend has total workout minutes >= 120
for friend, total in total_minutes_dict.items():
    if total >= 120:
        print(f"Great job staying active, {friend}!")

# Allow user to input a friend's name instead of hardcoding
friend_name = input("\nEnter a friend's name to check their workout stats: ")

if friend_name in workout_stats:
    print(f"Workout minutes for {friend_name}: Yoga={workout_stats[friend_name][0]}, "
          f"Running={workout_stats[friend_name][1]}, Weightlifting={workout_stats[friend_name][2]}.")
    print(f"Total workout minutes: {total_minutes_dict[friend_name]}.")
else:
    print(f"Friend {friend_name} not found in the records.")

# Find friend with highest and lowest total workout minutes
highest_friend = max(total_minutes_dict, key=total_minutes_dict.get)
lowest_friend = min(total_minutes_dict, key=total_minutes_dict.get)

print(f"\nFriend with highest workout minutes: {highest_friend} ({total_minutes_dict[highest_friend]} minutes)")
print(f"Friend with lowest workout minutes: {lowest_friend} ({total_minutes_dict[lowest_friend]} minutes)")
