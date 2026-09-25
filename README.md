# Snip

A small tool that lets you save long commands under short nicknames so you copy them to your clipboard whenever you want.


## Why

I can't remember long commands that I use almost daily, maybe its just because i am lazy. So instead of finding and writing those long commands over and over again, i can just save them under a nickname once and then all i have to remember is the small nickname i gave it. 

## Features
* `snip add <name> <command>` - for saving a command under a nickname
* `snip get <name>` - for copying a saved command directly to clipboard
* `snip list` - for showing all saved snippets/commands
* `snip delete <name>` - for deletng a saved snippet/command

## Installing
\```bash
pip install snip-cli
\```

## Usage
\```bash
snip add gitpush "git push origin main"
snip get gitpush
# git push origin main is now on your clipboard

snip list
snip delete gitpush
\```

## Built with
-Python
-`argparse` for the command line interface
-`json` for storing commands locally
-`pyperclip` for system's clipboars support

