import os

class Flashcards:
    def __init__(self):
        self.flashcard_dict = {}
        self.num_cards = 0


    def add_new_card(self):
        self.num_cards += 1

        term = input(f'The card:\n')

        while True:
            try:
                if term not in self.flashcard_dict.keys():
                    break
                else:
                    term = input(f'The card "{term}" already exists. Try again:\n')
            except ValueError:
                print("Provide an valid term for card...")
                continue

        definition = input(f'The definition of the card:\n')
        while True:
            try:
                if definition not in self.flashcard_dict.values():
                    break
                else:
                    definition = input(f'The definition "{definition}" already exists. Try again:\n')
            except ValueError:
                print('Provide an valid definition for card...')
                continue

        self.flashcard_dict[term] = definition
        print(f'The pair ("{term}":"{definition}") has been added.\n')


    def remove_card(self):
        card_to_remove = input('Which card?\n')

        if card_to_remove in self.flashcard_dict:
            del self.flashcard_dict[card_to_remove]
            print('The card has been removed.\n')
        else:
            print(f'Can\'t remove "{card_to_remove}": there is no such card.\n')


    def import_file(self):
        file_name = input('File name:\n')

        try:
            user_file = open(file_name, 'r')
        except FileNotFoundError:
            print('File not found.\n')
            return
        except Exception as e:
            print(f'Exception: {e}')
            return

        contents = user_file.read()

        result = contents.split('\n')

        num_imports = len(result)

        for i, n in enumerate(result):
            if n:
                key_value = n.split(',')
                self.flashcard_dict[key_value[0]] = key_value[1]
            else:
                num_imports -= 1

        print(f'{num_imports} cards have been loaded.')
        user_file.close()


    def export_file(self):
        file_name = input('File name:\n')

        try:
            user_file = open(file_name, 'w')
        except Exception as e:
            print(f'Exception: {e}')
            return

        for key in self.flashcard_dict:
            user_file.write(key)
            user_file.write(',')
            user_file.write(self.flashcard_dict[key])
            user_file.write('\n')

        print(f'{len(self.flashcard_dict)} cards have been saved.\n')

        user_file.close()


    def test(self):

        num_terms = int(input('How many times to ask?\n'))

        dict_keys = list(self.flashcard_dict.keys())

        for i in range(num_terms):

            answer = input(f'Print the definition of "{dict_keys[i % len(dict_keys)]}":\n')

            if answer == self.flashcard_dict[dict_keys[i % len(dict_keys)]]:
                print('Correct!')
            elif answer in self.flashcard_dict.values():
                print(
                    f'Wrong. The right answer is "{self.flashcard_dict[dict_keys[i % len(dict_keys)]]}", but your definition is correct for "{list(self.flashcard_dict.keys())[list(self.flashcard_dict.values()).index(answer)]}".')
            else:
                print(f'Wrong. The right answer is "{self.flashcard_dict[dict_keys[i % len(dict_keys)]]}".')

            if i+1 == num_terms:
                return


        for i, term in enumerate(self.flashcard_dict):
            answer = input(f'Print the definition of "{term}":\n')

            if answer == self.flashcard_dict[term]:
                print('Correct!')
            elif answer in self.flashcard_dict.values():
                print(
                    f'Wrong. The right answer is "{self.flashcard_dict[term]}", but your definition is correct for "{list(self.flashcard_dict.keys())[list(self.flashcard_dict.values()).index(answer)]}".')
            else:
                print(f'Wrong. The right answer is "{self.flashcard_dict[term]}".')

            if i+1 == num_terms:
                return


def main():

    flashcards = Flashcards()

    while True:
        action = input('Input the action (add, remove, import, export, ask, exit):\n')

        if action == 'add':
            flashcards.add_new_card()
        elif action == 'remove':
            flashcards.remove_card()
        elif action == 'import':
            flashcards.import_file()
        elif action == 'export':
            flashcards.export_file()
        elif action == 'ask':
            flashcards.test()
        elif action == 'exit':
            print('Bye bye!')
            exit()


if __name__ == '__main__':
    main()

