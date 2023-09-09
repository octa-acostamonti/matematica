import re
from sympy import divisors

# Input the polynomial as a string
polynomial = input("Enter the polynomial (e.g., '6*x**3 + 11*x**2 - 3*x - 4'): ")


# Split the polynomial string
y_split = re.split(r'[+-]', polynomial)

terminoIndependiente = y_split[-1]
coeficientePrincipal = y_split[0]

def encontrar_coeficientePrincipal(coeficientePrincipal):
    match = re.search(r'(\d+)\*', coeficientePrincipal)
    if match:
        return int(match.group(1))
    else:
        return 1

terminoIndependiente = int(terminoIndependiente)
coeficientePrincipal = encontrar_coeficientePrincipal(coeficientePrincipal)

divisoresterminoIndependiente = divisors(terminoIndependiente)
divisorescoeficientePrincipal = divisors(coeficientePrincipal)

terminoInd_coefPri = []

# Divide each divisor of Termino Independiente by each divisor of Coeficiente Principal
for divisor_tI in divisoresterminoIndependiente:
    for divisor_cP in divisorescoeficientePrincipal:
        result = divisor_tI / divisor_cP
        # Check if the result is not already in the list
        if result not in terminoInd_coefPri:
            # Add the positive and negative result to the list
            terminoInd_coefPri.append(result)
            terminoInd_coefPri.append(-result)

print("Roots of the polynomial:")
for x in terminoInd_coefPri:
    y = eval(polynomial)
    if abs(y) < 1e-6:
        print(f"Root found for x = {x}: y = {y}")
