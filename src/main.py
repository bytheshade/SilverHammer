import curses
from curses import wrapper
import matplotlib as plt
import numpy as np
import sympy as sp
from m1.m1_src import *

# center = (curses.LINES // 2, curses.COLS // 2)
def print_menu(stdscr: 'curses.window', selected_row_idx, menu):
    stdscr.erase()
    stdscr.box()
    
    h, w = stdscr.getmaxyx()  # Get the screen dimensions
    
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2  # Center the text horizontally
        y = h // 2 - len(menu) // 2 + idx  # Center the menu vertically
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))  # Turn on highlighting
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))  # Turn off highlighting
        else:
            stdscr.addstr(y, x, row)  # Normal menu option
    
    stdscr.refresh()
   
def yonly(stdscr: 'curses.window'):
    stdscr.clear()
    stdscr.box()
    
    user_input = ''
    
    while True:
        stdscr.clear()  # Clear the window at the start of each loop
        stdscr.box()  # Re-draw the box after clearing

        # Display the user input in bold
        stdscr.attron(curses.A_BOLD)  # Turn on bold attribute
        stdscr.addstr(curses.LINES // 2, curses.COLS // 2 - len(user_input) // 2, user_input)
        stdscr.attroff(curses.A_BOLD)  # Turn off bold attribute

        stdscr.refresh()  # Refresh the screen to show changes

        # Get user input
        _ = stdscr.getch()

        if _ == 27:  # ESC key to exit
            break

        # Append the character to user_input, only if it is a printable character
        if 32 <= _ <= 126:  # ASCII printable range
            user_input += chr(_)
        
    

def main(stdscr):
    # Initialize curses
    stdscr = curses.initscr()
    stdscr.box()
    curses.curs_set(0)  # Hide the cursor
    stdscr.keypad(True)  # Enable arrow keys
    curses.start_color()  # Enable colors
    
    # Define color pair for highlighting
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    # Menu options
    menu = ['Y VALUES ONLY', 'X & Y VALUES', 'LEARN MORE', 'EXIT']
    
    # Index of the currently selected row
    current_row = 0
    
    # Main loop
    while True:
        # Print the menu with the current selection highlighted
        print_menu(stdscr, current_row, menu)
        
        # Wait for user input
        key = stdscr.getch()
        
        # Handle user input
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1  # Move the selection up
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1  # Move the selection down
        elif key == ord('q'):
            current_row = len(menu) - 1
        elif key == ord('\n'):  # Enter key to select the option
            if current_row == len(menu) - 1:
                break  # Exit the program if "Exit" is selected
            elif menu[current_row] == 'Y VALUES ONLY':
                yonly(stdscr)
            else:
                stdscr.erase()
                stdscr.box()
                text = f"You selected '{menu[current_row]}'"
                stdscr.addstr(curses.LINES // 2, curses.COLS // 2 - len(text) // 2, text)
                stdscr.refresh()
                
                while True:
                    _ = stdscr.getch()
                    if _ == ord('q'):
                        break
                        
    stdscr.erase()
    stdscr.refresh()

    
wrapper(main)