# Mini virtual assistant project

from datetime import datetime

def respond(command):
    command = command.strip().lower()

    if command in {"hi", "hello"}:
        return "Hello! What can I do for you?"
    if "time" in command:
        return f"The current time is {datetime.now().strftime('%I:%M %p')}"
    if "date" in command:
        return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}"
    if command == "help":
        return "Try: hello, time, date, help, exit"
    return "I could not understand that request."

print("Assistant started. Type 'exit' to stop.")

while True:
    command = input("You: ")
    if command.strip().lower() == "exit":
        print("Assistant: Goodbye.")
        break
    print("Assistant:", respond(command))
