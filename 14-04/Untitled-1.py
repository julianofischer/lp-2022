#sobrecarga (overload)
def metodo(inteiro=-1, string=None):
    if inteiro != -1:
        print('executa método para inteiro')
    elif string:
        print('executa método para string')

#metodo(1,2,3,5,6,'Juliano', (0,0), {1,2,3})

metodo('Juliano')

def novometodo(**xwargs):
    print(xwargs)

novometodo(a=1, b='Juliano', mouse='Microsoft', t=(1,2))

def mix(a, b, c=-1, *args, **kwargs):
    print(f'Posicionais {a} e {b}')
    print(f'Default {c}')
    print(f'args {args}')
    print(f'kwargs {kwargs}')


print('Execução 1:')
mix(10,20)

print('Execução 2:')
mix(10,20,30)

print('Execução 3:')
mix(10,20,30,40,50,60)

print('Execução 3:')
mix(10,20,30,40,50,60,kw1='a',kw2='b')

b = 2
b = 'dois'
mix(b)