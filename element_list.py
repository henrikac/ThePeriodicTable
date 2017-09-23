import json


class ElementList:
    def read(self):
        with open('elements.json') as elements:
            element = json.load(elements)
            return element

    def all(self):
        element = self.read()
        for ele in element:
            print('{}: {}'.format(ele['Number'], ele['Name']))
            print('-' * 15)
            print('Kemisk symbol: {}'.format(ele['Symbol']))
            print('Protoner: {}'.format(ele['Protons']))

            if ele['Neutrons'] is not None:
                print('Neutroner: {}'.format(ele['Neutrons']))
            else:
                print('Neutroner: ---')

            print('Elektroner: {}'.format(ele['Electrons']))

            if ele['Weight'] is not None:
                print('Vægt: {}'.format(ele['Weight']))
            else:
                print('Vægt: ---')

            if ele['NobleGas'] is True:
                print('- Ædelgas')

            if ele['IsMetal'] is True:
                print('- Metal')
            else:
                print('- Ikke Metal')

            if ele['IsLanthanide'] is True:
                print('- Lanthanide')

            if ele['IsActinides'] is True:
                print('- Actinide')

            print('\n')
