task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
        if time_bound == "yes":
            reminder += " It should be handled with urgency."
        print(reminder)
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
        if time_bound == "yes":
            reminder += " Please address it soon unless something more urgent comes up."
        print(reminder)
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."
        if time_bound == "yes":
            reminder += " Consider completing it when you have free time."
        print(reminder)
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

print()
print(reminder)
