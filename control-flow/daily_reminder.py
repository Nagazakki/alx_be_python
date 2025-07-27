task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " and should be handled with urgency."
        else:
            reminder += " It requires immediate attention!"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
        if time_bound == "yes":
            reminder += " Please address it soon unless something more urgent comes up."
        else:
            reminder += " You can handle it at your convenience."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."
        if time_bound == "yes":
            reminder += " Consider completing it when you have free time."
        else:
            reminder += " It can wait until you have more time."
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

print()
print(reminder)
