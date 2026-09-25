import argparse
import json
import os
import pyperclip

SNIPPETS_FILE = "snippets.json"

def load_snippets():
    if not os.path.exists(SNIPPETS_FILE):
        return{}
    with open(SNIPPETS_FILE, "r") as f:
        return json.load(f)

def save_snippets(snippets):
    with open(SNIPPETS_FILE, "w") as f:
        json.dump(snippets, f, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Snip- save and recall terminal commands")
    subparsers = parser.add_subparsers(dest="action")

    add_parser  = subparsers.add_parser("add", help="save a new command under a nickname")
    add_parser.add_argument("name", help="short nickname for the command")
    add_parser.add_argument("command", help="the actual command to be remembered")

    get_parser = subparsers.add_parser("get", help="look up a saved command by nickname")
    get_parser.add_argument("name", help='the nickname to look up')

    args = parser.parse_args()

    if args.action == "add":
        snippets = load_snippets()
        snippets[args.name] = args.command
        save_snippets(snippets)
        print(f"Got it, saving '{args.command}' under the name '{args.name}'")
    elif args.action == 'get':
        snippets = load_snippets()
        if args.name in snippets:
            command = snippets[args.name]
            pyperclip.copy(command)
            print(f"Copied to clipboard: {command}")
        else:
            print(f"No snippet found called '{args.name}'")
    else:
        print("snip is alive! Try: snip.py add <name> <command>")

if __name__ == "__main__":
    main()