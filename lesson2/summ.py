def get_summ(x , y):
    summ = x + y
    print (f'Sum is : {summ}')
    return summ

def int_input(id):
    while True:
        try:
            x = int(input(f'Num {id}: '))
            return x
        except ValueError:
            print('Must be an int')
            

if __name__ == '__main__':
    
    x = int_input(1)
    y = int_input(2)

    get_summ(x, y)