# Convert natural-looking commands into actions

def process_command(command):
    command = command.strip().lower()

    if command == "show balance":
        return "Your current balance is ₹12,500."
    if command == "show orders":
        return "You have 4 active orders."
    if command == "help":
        return "Available: show balance, show orders, help, exit"
    return "Unknown command."

commands = ["show balance", "show orders", "help", "something else"]
for command in commands:
    print(">", command)
    print(process_command(command))
