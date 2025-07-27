task = input("Enter your task: ")
priority = input("Priority (high, medium, low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task!"
        if time_bound == "yes":
            reminder += " that requires immediate attention."
        else: 
            reminder += "."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
        if time_bound == "yes":
            reminder += " Please address it soon."
        else:
            reminder += " You can handle it later."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."
        if time_bound == "yes":
            reminder += " Please try to finish it this week."
        else:
            reminder += " You can complete it whenever you have time."
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low." 
        if time_bound == "yes":
            reminder += " Note that time-bound tasks should be prioritized."
        else:
            reminder += " Non-time-bound tasks can be scheduled flexibly."

print()
print(reminder)
print("Have a productive day!")