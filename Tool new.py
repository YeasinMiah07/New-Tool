#!/usr/bin/env python3
# Example Tool Installer Script

import os

def list_tools():
    print("1: 2008-2009")
    print("2: 2010-2011")
    print("3: 2012-2015")
    print("x: Exit")

def install_tool(tool_name):
    os.system(f"apt-get install {tool_name}")

def main():
    while True:
        list_tools()
        choice = input("Enter the number of the tool you want to install: ")
        if choice == '1':
            install_tool('tool-a-package-name')
        elif choice == '2':
            install_tool('tool-b-package-name')
        elif choice == '3':
            install_tool('tool-c-package-name')
        elif choice.lower() == 'x':
            break
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()
