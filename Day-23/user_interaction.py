# Simple interactive assistant

name = input("What is your name? ").strip()
print(f"Assistant: Nice to meet you, {name}.")

choice = input("Would you like to check your tasks? yes/no: ").strip().lower()

if choice == "yes":
    tasks = ["Practice Python", "Review SQL", "Update GitHub"]
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
else:
    print("Assistant: No problem.")
