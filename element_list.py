import json


class ElementList:
    def read(self):
        """Reads a json file
        Returns the list of elements in the file
        """
        with open('elements.json') as elements:
            element = json.load(elements)
            return element

    def print_element(self, element):
        """Takes an argument (element)
        Prints out all the details of that element
        """
        print('{}: {}'.format(element['Number'], element['Name']))
        print('-' * 15)
        print('Kemisk symbol: {}'.format(element['Symbol']))
        print('Protoner: {}'.format(element['Protons']))

        if element['Neutrons'] is not None:
            print('Neutroner: {}'.format(element['Neutrons']))
        else:
            print('Neutroner: ---')

        print('Elektroner: {}'.format(element['Electrons']))

        if element['Weight'] is not None:
            print('Vægt: {}'.format(element['Weight']))
        else:
            print('Vægt: ---')

        if element['NobleGas'] is True:
            print('- Ædelgas')

        if element['IsMetal'] is True:
            print('- Metal')
        else:
            print('- Ikke Metal')

        if element['IsLanthanide'] is True:
            print('- Lanthanide')

        if element['IsActinides'] is True:
            print('- Actinide')

    def search(self, key, value):
        """Takes two arguments (key, value)
        Loops through the list of elements returned by read()
        If element[key] matches value then prints the details of that element
        """
        elements = self.read()
        elements_found = 0
        for element in elements:
            if element[key] == value:
                self.print_element(element)
                elements_found += 1
                print('\n')
        if elements_found == 0:
            print('Sorry, could not find "{}: {}"\n'. format(key, value))

    def all(self):
        """Prints a full list of all elements returned by read()"""
        elements = self.read()
        for element in elements:
            self.print_element(element)
            print('\n')
