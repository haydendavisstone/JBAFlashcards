class Flashcard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition


def add_new_card(flashcards):
    num_cards = input('Input the number of cards:\n')

    for i in range(1, int(num_cards)+1):

        term = input(f'The term for card #{i}:\n')
        while True:
            try:
                if term not in [i.term for i in flashcards]:
                    break
                else:
                    term = input(f'The term "{term}" already exists. Try again:\n')
            except ValueError:
                print("Provide an valid term for card...")
                continue

        definition = input(f'The definition for card #{i}:\n')
        while True:
            try:
                if definition not in [i.definition for i in flashcards]:
                    break
                else:
                    definition = input(f'The definition "{definition}" already exists. Try again:\n')
            except ValueError:
                print("Provide an valid definition for card...")
                continue

        flashcards.append(Flashcard(term, definition))


def main():

    flashcards = []
    add_new_card(flashcards)

    for flashcard in flashcards:
        answer = input(f'Print the definition of "{flashcard.term}":\n')

        if answer == flashcard.definition:
            print('Correct!')
        elif answer in [i.definition for i in flashcards]:
            correct_term = [i.term for i in flashcards if i.definition == answer]
            correct_term = correct_term[0]
            print(f'Wrong. The right answer is "{flashcard.definition}", but your definition is correct for "{correct_term}".')
        else:
            print(f'Wrong. The right answer is "{flashcard.definition}".')


if __name__ == '__main__':
    main()

