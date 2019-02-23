from pymorphy import inflect

class Предложение():
    def __init__(self, word_list):
        self.word_list = word_list

    def __str__(self):
        out = ' '.join(self.word_list) + '.'
        n = 0
        for self.word_list in Word_list:
            out.inflect({'gent'})
            n += 1
        return out.capitalize()


def main():
    a = Предложение(["мама", "мыть", "рама"])
    print (a)

if __name__ == '__main__':
    main()
