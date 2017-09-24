import os
import sys

from element_list import ElementList


class PeriodicTable:
    options = (
        ('all', 'Shows all the elements'),
        ('search', 'Search for an element'),
        ('quit', 'Exit the program')
    )
    element_list = ElementList()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_options(self, options):
        for option in options:
            print('{}: {}'.format(option[0], option[1]))

    def search(self):
        search_options = (
            ('name', 'Search by name'),
            ('number', 'Search by number'),
            ('cancel', 'Go back to start')
        )
        self.show_options(search_options)

        while True:
            choice = input('\nWhat do you want to search by? ').lower().strip()

            if choice == 'cancel':
                break
            elif choice == 'name':
                name = input('What element are you looking for? ').capitalize().strip()

                self.clear_screen()
                self.element_list.search_name(name)
                self.show_options(search_options)
            else:
                print('That is not a valid input.')

    def run(self):
        self.clear_screen()
        self.show_options(self.options)

        while True:
            choice = input('\nWhat do you want to do? ').lower().strip()

            if choice == 'quit':
                sys.exit(0)
            elif choice == 'all':
                self.clear_screen()
                self.element_list.all()
                self.show_options(self.options)
            elif choice == 'search':
                self.clear_screen()
                self.search()
                self.clear_screen()
                self.show_options(self.options)
            else:
                print('That is not a valid input.')


if __name__ == '__main__':
    periodic = PeriodicTable()
    periodic.run()
