import re
from sympy import divisors

def main():
    polinomio = "0"
    while True:
        print("Polinomio:", polinomio)

        accion = input("""
                    1. Ingresar un polinomio (ej:'6*x**3 + 11*x**2 - 3*x - 4')
                    2. Encontrar raices
                    3. Salir
                   """)

        if accion == "1":
            polinomio = input("Enter the polinomio (e.g., '6*x**3 + 11*x**2 - 3*x - 4'): ")
        elif accion == "2":
            # Separar el polinomio en terminos
            polinomio_separado = separar_polinomio_terminos(polinomio)
            
            # Conseguir el termino independiente y el coeficiente principal
            terminoIndependiente, coeficientePrincipal = conseguir_termIndependiente_coefPrincipal(polinomio_separado)
            
            # Encontrar los divisores de ambos terminos
            divisoresterminoIndependiente, divisorescoeficientePrincipal = encontrar_divisores_terminos(terminoIndependiente, coeficientePrincipal)
            
            # Evaluar los divisores y encontrar raices
            encontrar_raices(divisoresterminoIndependiente, divisorescoeficientePrincipal, polinomio)

            seguir = input(""" Desea continuar?
                           
                           1. Sí
                           2. No

                           """)
            if seguir == "1":
                continue
            elif seguir == "2":
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida")

            
        elif accion == "3":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def separar_polinomio_terminos(polinomio):
    # Separar el polinomio en términos divididos por '+' y '-'
    polinomio_separado = re.split(r'[+-]', polinomio)
    return polinomio_separado

def conseguir_termIndependiente_coefPrincipal(polinomio_separado):
    # Obtener el primer y último término del polinomio (Coeficiente principal y Término independiente)
    coeficientePrincipal = polinomio_separado[0]
    terminoIndependiente = polinomio_separado[-1]
    return terminoIndependiente, coeficientePrincipal

def encontrar_coeficientePrincipal(coeficientePrincipal):
    # Definir función para separar el coeficiente principal del 'x**n' ('a*x**n')
    match = re.search(r'(\d+)\*', coeficientePrincipal) 
    
    if match: 
        return int(match.group(1)) 
    else:
        return 1 

def encontrar_divisores_terminos(terminoIndependiente, coeficientePrincipal):
    # Convertir el término independiente a int y encontrar el coeficiente principal
    terminoIndependiente = int(terminoIndependiente)
    coeficientePrincipal = encontrar_coeficientePrincipal(coeficientePrincipal)
    
    # Encontrar los divisores del término independiente y del coeficiente principal
    divisoresterminoIndependiente = divisors(terminoIndependiente)
    divisorescoeficientePrincipal = divisors(coeficientePrincipal)
    return divisoresterminoIndependiente, divisorescoeficientePrincipal

def encontrar_raices(divisoresterminoIndependiente, divisorescoeficientePrincipal, polinomio):
    # Iniciar una lista vacía de las raíces encontradas
    raices = []

    # Dividir cada divisor del Término Independiente por cada divisor del Coeficiente Principal
    for divisor_tI in divisoresterminoIndependiente:
        for divisor_cP in divisorescoeficientePrincipal:
            resultado = divisor_tI / divisor_cP
            
            # Evaluar el polinomio en el resultado para ver si es una raíz
            y = eval(polinomio.replace('x', str(resultado)))
            
            # Si la evaluación es cercana a cero, considerar el resultado como una raíz
            if abs(y) < 1e-6:
                raices.append(resultado)
    
    if len(raices) == 0:
        print("No se encontraron raíces.")
    else:
        print("Raíces encontradas:", raices)

if __name__ == "__main__":
    main()
