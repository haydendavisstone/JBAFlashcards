class Flashcard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition


    def output(self):
        print('Card:')
        print(f'{self.term}')
        print('Definition:')
        print(f'{self.definition}')


def main():
    flashcard = Flashcard('front', 'back')
    flashcard.output()


if __name__ == '__main__':
    main()
    
