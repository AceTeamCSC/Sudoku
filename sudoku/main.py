import curses
import time

from sudoku import Sudoku

menu = ["Rules", "Play", "Exit"]
submenu = ["Easy", "Hard", "Exit"]


def intro_message():
    welcome_message = """
    Welcome to Sudoku
    Rules:
    All rows should have the digits 1-9, without repition.
    All columns should have the digits 1-9, without repition.
    All 9 sub-matrices should have the digits 1-9, without repition.
    To play, enter the row, column, and answer at the command prompt. The
    Format is: <row> <column> <value>
    Type exit to leave
    Please note this game uses 0 indexing
    Good luck!\n
    """
    return welcome_message


def print_subject(stdscr, w, text):
    text_x = w // 2 - len(text) // 2
    stdscr.addstr(5, text_x, text)


def print_menu(stdscr, curr_row, curr_menu, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    title_x = w // 2 - len(text) // 2
    stdscr.addstr(5, title_x, text)
    for idx, row in enumerate(curr_menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == curr_row:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def sub_menu(stdscr):
    # Requirement 2.0.0
    submenu_row = 0
    print_menu(stdscr, submenu_row, submenu, "Pick a Difficulty")

    while True:
        sub_key = stdscr.getch()

        if sub_key == curses.KEY_UP and submenu_row > 0:
            submenu_row -= 1
        elif sub_key == curses.KEY_DOWN and submenu_row < len(submenu) - 1:
            submenu_row += 1
        if sub_key == sub_key in [10, 13]:
            if submenu[submenu_row] == "Easy":
                print_center(stdscr, "'{}' selected".format(submenu[submenu_row]))
                start_game(submenu[submenu_row])
            elif submenu[submenu_row] == "Hard":
                print_center(stdscr, "'{}' selected".format(submenu[submenu_row]))
                start_game(submenu[submenu_row])
            elif submenu[submenu_row] == "Exit":
                print_center(stdscr, "'{}' selected".format(submenu[submenu_row]))
                return

        print_menu(stdscr, submenu_row, submenu, "Pick a Difficulty")


def start_game(difficulty):
    time.sleep(1)
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    Sudoku.run(difficulty)


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row = 0
    print_menu(stdscr, current_row, menu, "Sudoku!")

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == key in [10, 13]:
            if menu[current_row] == "Rules":
                stdscr.addstr(5, 5, intro_message())
                stdscr.getch()
            elif menu[current_row] == "Play":
                sub_menu(stdscr)
            elif menu[current_row] != "Exit":
                print_center(stdscr, "'{}' selected".format(menu[current_row]))
                stdscr.getch()
            if current_row == len(menu) - 1:
                break

        print_menu(stdscr, current_row, menu, "Sudoku!")


if __name__ == "__main__":
    curses.wrapper(main)
