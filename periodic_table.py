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
        """Clearing the console"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_options(self, options):
        """Shows a list of options"""
        for option in options:
            print('{}: {}'.format(option[0], option[1]))

    def search(self):
        """Prints a list a search options
        Asking the user what he/she wants to search for
        Prints out detail for the element searched for
        """
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
                self.element_list.search('Name', name)
                self.show_options(search_options)
            elif choice == 'number':
                while True:
                    try:
                        number = int(input('Enter number: '))
                    except ValueError:
                        print('Please enter a number.')
                        continue
                    else:
                        if number > 0 and number <= 116:
                            self.clear_screen()
                            self.element_list.search('Number', number)
                            self.show_options(search_options)
                            break
                        else:
                            print('Please only enter a number between 1 and 116.')
                            continue
            else:
                print('That is not a valid input.')

    def run(self):
        """Keeps the program running until the user enter 'quit'"""
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
