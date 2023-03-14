class Flashcard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def output(self, answer):
        if answer == self.definition:
            print('Correct!')
        else:
            print(f'Wrong. The right answer is "{self.definition}".')

def add_new_card(flashcards):
    num_cards = input('Input the number of cards:\n')

    for i in range(1, int(num_cards)+1):
        term = input(f'The term for card #{i}:\n')
        definition = input(f'The definition for card #{i}:\n')
        flashcards.append(Flashcard(term, definition))


def main():

    flashcards = []
    add_new_card(flashcards)

    for flashcard in flashcards:
        answer = input(f'Print the definition of "{flashcard.term}":\n')
        flashcard.output(answer)


if __name__ == '__main__':
    main()

