task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match (priority):
    case ("high"):
        if time_bound == "yes":
            print(f"Reminder:  '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: You have a high-priority task '{task}'. Please address it as soon as possible.")
    case ("medium"):
        if time_bound == "yes":
            print(f"Reminder:  '{task}' is a medium priority task that is time-bound. Please plan to complete it soon.")
        else:
            print(f"Note: You have a medium-priority task '{task}'. Please address it when you can.")
    case ("low"):
        if time_bound == "yes":
            print(f"Reminder:  '{task}' is a low priority task that is time-bound. Please try to complete it in due time.")
        else:
            print(f"Note: You have a low-priority task '{task}'. Please address it when you have free time.")