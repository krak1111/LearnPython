def ask_user():
    while True:
        try:
            answer = input('How are you? ')
        except KeyboardInterrupt:
            print('By')
            break

        if answer == 'Well':
            break
        else:
            print('Please say "Well" !')


QA_dict = {
    'How are you?': 'Very Well!',
    'How old are you?': '27',
    'What are you doing?': 'Waiting for you!',
    'Who am I?': 'You are my master, Yoda!'
}

def user_interactive(QA_dictionary):
    print('Ask me a question. If you get tired type "stop"')
    question = input('Question: ')
    while question != 'stop':        
        try:
            print(QA_dictionary[question])

        except KeyError:
            print("I don't know")

        except KeyboardInterrupt:
            print('By')
            break

        question = input('Question: ')

    


if __name__ == '__main__':
    ask_user()
    user_interactive(QA_dict)