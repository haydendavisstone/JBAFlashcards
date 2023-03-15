class Flashcards:
    def __init__(self):
        self.flashcard_dict = {}
        self.num_cards = 0

    def add_new_cards(self):
        new_cards = int(input('Input the number of cards:\n'))
        self.num_cards += new_cards

        for i in range(1, new_cards+1):

            term = input(f'The term for card #{i}:\n')
            while True:
                try:
                    if term not in self.flashcard_dict.keys():
                        break
                    else:
                        term = input(f'The term "{term}" already exists. Try again:\n')
                except ValueError:
                    print("Provide an valid term for card...")
                    continue

            definition = input(f'The definition for card #{i}:\n')
            while True:
                try:
                    if definition not in self.flashcard_dict.values():
                        break
                    else:
                        definition = input(f'The definition "{definition}" already exists. Try again:\n')
                except ValueError:
                    print("Provide an valid definition for card...")
                    continue

            self.flashcard_dict[term] = definition

    def test(self):
        for term in self.flashcard_dict:
            answer = input(f'Print the definition of "{term}":\n')

            if answer == self.flashcard_dict[term]:
                print('Correct!')
            elif answer in self.flashcard_dict.values():
                print(
                    f'Wrong. The right answer is "{self.flashcard_dict[term]}", but your definition is correct for "{list(self.flashcard_dict.keys())[list(self.flashcard_dict.values()).index(answer)]}".')
            else:
                print(f'Wrong. The right answer is "{self.flashcard_dict[term]}".')


def main():

    flashcards = Flashcards()

    flashcards.add_new_cards()
    flashcards.test()


if __name__ == '__main__':
    main()

