import re
from sympy import divisors

# Input del polinomio
polinomio = input("Enter the polinomio (e.g., '6*x**3 + 11*x**2 - 3*x - 4'): ")


# Separar el polinomio en terminos divididos por '+' y '-'
y_split = re.split(r'[+-]', polinomio)

# Conseguir el primer y ultimo termino del polinomio (Coeficiente principal y Termino independiente)
coeficientePrincipal = y_split[0]
terminoIndependiente = y_split[-1]


# Pasar a int al termino independiente y encontrar el coeficiente principal
terminoIndependiente = int(terminoIndependiente)
coeficientePrincipal = encontrar_coeficientePrincipal(coeficientePrincipal)

# Encontrar los divisores del terminoIndendiente y del coeficientePrincipal
divisoresterminoIndependiente = divisors(terminoIndependiente)
divisorescoeficientePrincipal = divisors(coeficientePrincipal)

# Iniciar una lista vacia de los divisibles de ambos terminos divididos entre sí ( +-(Termino independiente / Coeficiente principal)
terminoInd_coefPri = []

# Dividir cada divisor del Termino Independiente por cada divisor del Coeficiente Principal
for divisor_tI in divisoresterminoIndependiente:
    for divisor_cP in divisorescoeficientePrincipal:
        resultado = divisor_tI / divisor_cP
        # Chequear si el resultado ya esta en la lista
        if resultado not in terminoInd_coefPri:
            # Añadir el resultado positivo y negativo a la lista
            terminoInd_coefPri.append(resultado)
            terminoInd_coefPri.append(-resultado)

print("Raices of the polinomio:")
for x in terminoInd_coefPri:
    y = eval(polinomio)
    print(f"Root found for x = {x}: y = {y}")

    # Definir funcion para separar el coeficiente principal del 'x**n' ('a*x**n')

def separar_polinomio_terminos(polinomio):
    polinomio_separado = re.split(r'[+-]', polinomio)
    return polinomio_separado

def encontrar_coeficientePrincipal(coeficientePrincipal):
    
    match = re.search(r'(\d+)\*', coeficientePrincipal) # Encontrar en el coeficiente principal el digito seguido del asterisco (gracias a la libreria re)
    
    if match: # Si lo encuentra 
        return int(match.group(1)) # Devolver el primer digito ('a')
    
    else:
        return 1 # Si no encuentra 'a' devolver 1 
