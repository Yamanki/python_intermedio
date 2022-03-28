def fibonacci(n):
        if n == 0 or n == 1:
            return 1
        return fibonacci(n-1)+ fibonacci(n -2)

def run():
    n = int(input('Escribe un numero entero: '))
    print('El numero de fibonacci para', n , "es" ,fibonacci(n))



if __name__ =="__main__" :
    run()