# A small command-line assistant

print("Assistant: Hello! Type help to see commands.")

while True:
    command = input("You: ").strip().lower()

    if command == "hello":
        print("Assistant: Hello! How can I help?")
    elif command == "help":
        print("Commands: hello, status, exit")
    elif command == "status":
        print("Assistant: Everything is running normally.")
    elif command == "exit":
        print("Assistant: Goodbye!")
        break
    else:
        print("Assistant: I don't know that command yet.")
