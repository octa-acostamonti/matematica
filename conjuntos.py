def main():
    A = set()
    B = set()

    while True:
        print("Conjunto A:", A)
        print("Conjunto B:", B)
        
        action = input("""Que operacion desea hacer?
                    1. Cambiar Conjunto A
                    2. Cambiar Conjunto B
                    3. Producto Cartesiano
                    4. Union
                    5. Interseccion
                    6. Resta de Conjuntos
                    7. Salir
                   """)

        if action == "1":
            A = input_conjunto("A")
        elif action == "2":
            B = input_conjunto("B")
        elif action == "3":
            print(prod_cartesiano(A, B))
        elif action == "4":
            print(union(A, B))
        elif action == "5":
            print(interseccion(A, B))
        elif action == "6":
            print(resta_conjuntos(A, B))
        elif action == "7":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def input_conjunto(name):
    conjunto = input(f"Inserte el conjunto {name}: ")
    elements = set(map(int, conjunto.replace("{", "").replace("}", "").split(",")))
    return elements

def prod_cartesiano(A, B):
    return [(a, b) for a in A for b in B]

def union(A, B):
    return A.union(B)

def interseccion(A, B):
    return A.intersection(B)

def resta_conjuntos(A, B):
    return A - B

if __name__ == "__main__":
    main()
