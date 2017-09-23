import os
import sys

from element_list import ElementList


class PeriodicTable:
    options = (
        ('all', 'Shows all the elements'),
        ('quit', 'Exit the program')
    )
    element_list = ElementList()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_options(self):
        for option in self.options:
            print('{}: {}'.format(option[0], option[1]))

    def run(self):
        self.clear_screen()
        self.show_options()

        while True:
            choice = input('\nWhat do you want to do? ').lower().strip()

            if choice == 'quit':
                sys.exit(0)
            elif choice == 'all':
                self.clear_screen()
                self.element_list.all()
                self.show_options()
            else:
                print('That is not a valid input.')


if __name__ == '__main__':
    periodic = PeriodicTable()
    periodic.run()
