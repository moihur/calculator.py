# Esta calculadora realiza las operaciones de:
# -Suma 
# -Resa 
# -Division 
# -Multiplicacion 

# Realiza validaciones: sobre el signo a operar, división entre cero, etc

class variables:
    num1 = ''
    sym1 = ''
    num2 = ''

def validarApagado():
    valAlagado = input('¿Quiere apagar la calculadora?(S/N): ')
    if valAlagado in ['S', 's', 'N', 'n']:
        if valAlagado in ['S', 's']:
            pass
        else:
            calculadora()

def calculadora():
    inputs = variables()
    resultado = ''
    inputs.num1 = float(input('1er factor: '))
    inputs.sym1 = input('Signo (puede ser +, -, * y /): ') # Input del signo''
    inputs.num2 = float(input('2nd factor: ')) # Input del segundo dígito

    sym1Limpio = inputs.sym1.strip() # Quitamos los espacios del signo
    symValido = ['+', '-', '*', '/' ] # Declaramos la lista de posibilidades que tenemos de validar el signo

    if sym1Limpio not in symValido: # Validamos que el signo sea un signo dentro de nuestra lista
            print('El signo no es valido, ha usado el carácter: "' + sym1Limpio + '"')
            validarApagado()

    else:
        if (inputs.num1 and inputs.num2 == 0) and sym1Limpio == '/': # Validamos que no se esté dividiendo por cero
            print('No se permite la división entre ceros')
            validarApagado()

        else:
            print('Quieres calcular la siguiente operación ¿es correcto?')
            print(inputs.num1, sym1Limpio, inputs.num2)

            validacion = input('¿S/N?') # Confirmación de si queremos realizar la operación
            validacionLimpio = validacion.strip() # Quitamos los espacios de la confirmación
            if validacionLimpio in ['S', 's']:
                if sym1Limpio == '+': # Suma
                    resultado = inputs.num1 + inputs.num2

                elif sym1Limpio == '-': # Resta
                    resultado = inputs.num1 - inputs.num2

                elif sym1Limpio == '*': # Multiplicar
                    resultado = inputs.num1 * inputs.num2

                elif sym1Limpio == '/': # Dividir
                    resultado = inputs.num1 / inputs.num2

                print(inputs.num1, sym1Limpio, inputs.num2, ' = ', resultado) # Mostramos el resultado
                validarApagado()

            elif validacion not in ['N', 'n']:
                validarApagado()

            elif validacion not in ['N', 'n', 'S', 's']:
                print('Carácter no contemplado')
                validarApagado()

calculadora()