class Flashcard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition


    def output(self, answer):
        if answer == self.defintion:
            print('Your answer is right!')
        else:
            print('Your answer is wrong...')

def main():
    term = input()
    definition = input()
    flashcard = Flashcard(term, definition)
    answer = input()
    flashcard.output(answer)


if __name__ == '__main__':
    main()
    
