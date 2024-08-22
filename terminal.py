import os
import sys

# Define the current directory relative to where terminal.py is located
current_dir = os.path.dirname(os.path.abspath(__file__))

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_prompt():
    """Displays the command prompt."""
    hostname = "localhost"
    home_dir = "~"
    prompt = f"{os.getlogin()}@{hostname}:{home_dir}/{os.path.basename(current_dir)}$ "
    return prompt

def save_command_history(command):
    """Saves the command to history."""
    with open('history.txt', 'a') as f:
        f.write(command + '\n')

def load_command_history():
    """Loads the command history."""
    if os.path.exists('history.txt'):
        with open('history.txt', 'r') as f:
            return f.read().splitlines()
    return []

def create_directory(directory):
    """Creates a new directory."""
    path = os.path.join(current_dir, directory)
    try:
        os.makedirs(path)
        print(f"Directory created: {directory}")
    except FileExistsError:
        print(f"Directory already exists: {directory}")

def create_file(file):
    """Creates a new file."""
    path = os.path.join(current_dir, file)
    with open(path, 'w') as f:
        pass
    print(f"File created: {file}")

def remove_file(file):
    """Removes a file."""
    path = os.path.join(current_dir, file)
    try:
        os.remove(path)
        print(f"File removed: {file}")
    except FileNotFoundError:
        print(f"File not found: {file}")

def remove_directory(directory):
    """Removes an empty directory."""
    path = os.path.join(current_dir, directory)
    try:
        os.rmdir(path)
        print(f"Directory removed: {directory}")
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
    except OSError:
        print(f"Directory not empty: {directory}")

def display_file(file):
    """Displays the contents of a file."""
    path = os.path.join(current_dir, file)
    try:
        with open(path, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File not found: {file}")

def process_command(command):
    """Processes commands entered by the user."""
    global current_dir  # Declare current_dir as global
    
    if command.startswith("mkdir "):
        create_directory(command[6:].strip())
    elif command.startswith("touch "):
        create_file(command[6:].strip())
    elif command.startswith("rm "):
        remove_file(command[3:].strip())
    elif command.startswith("rmdir "):
        remove_directory(command[6:].strip())
    elif command.startswith("cat "):
        display_file(command[4:].strip())
    elif command == "ls":
        print(" ".join(os.listdir(current_dir)))
    elif command.startswith("cd "):
        new_dir = command[3:].strip()
        new_path = os.path.join(current_dir, new_dir)
        if os.path.isdir(new_path):
            current_dir = new_path
        else:
            print(f"Directory not found: {new_dir}")
    elif command == "clear":
        clear_screen()
    elif command == "history":
        for idx, cmd in enumerate(load_command_history()):
            print(f"{idx}: {cmd}")
    elif command == "help":
        print("Available commands:")
        print("mkdir <dir> - Create a new directory")
        print("touch <file> - Create a new file")
        print("rm <file> - Remove a file")
        print("rmdir <dir> - Remove an empty directory")
        print("cat <file> - Display the contents of a file")
        print("ls - List files in the current directory")
        print("cd <dir> - Change the current directory")
        print("clear - Clear the terminal screen")
        print("history - Show command history")
        print("help - Show this help message")
    else:
        print(f"Command not found: {command}")

def main():
    """Main function to run the terminal."""
    while True:
        try:
            prompt = display_prompt()
            command = input(prompt).strip()
            if command.lower() in ["exit", "quit"]:
                print("Exiting terminal...")
                break
            if command:
                save_command_history(command)
                process_command(command)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt caught. Exiting...")
            break

if __name__ == "__main__":
    main()
