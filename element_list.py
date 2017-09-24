import json


class ElementList:
    def read(self):
        with open('elements.json') as elements:
            element = json.load(elements)
            return element

    def print_element(self, element):
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

    def search_name(self, name):
        elements = self.read()
        for element in elements:
            if element['Name'] == name:
                self.print_element(element)
                print('\n')

    def search_number(self, number):
        elements = self.read()
        for element in elements:
            if element['Number'] == number:
                self.print_element(element)
                print('\n')

    def all(self):
        elements = self.read()
        for element in elements:
            self.print_element(element)
            print('\n')
