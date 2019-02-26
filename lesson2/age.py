def occupation(age):
    if age < 7:
        return 'You are preschooler'
    elif age < 17:
        return 'You are schoolchild'
    elif age < 24:
        return 'You are student'
    else:
        return 'You are worker'


def age_validator():
    while True:
        try:
            age = int(input('Enter your age: '))
            break
        except ValueError:
            print('Retry! Enter an integer!')
        except KeyboardInterrupt:
            print('By')
            break
        
        
if __name__ == '__main__':
              
    age_validator()

    print(f'Your age is {age}')

    answer = occupation(age)

    print(answer)