#  ACTIVIDAD FINAL: Calculadora básica mejorada en funcionamiento y usabilidad
def calculadora():
    """
    Calculadora básica con operaciones aritméticas
    """
    print("=== CALCULADORA MEJORADA ===")
    print("Operaciones disponibles: +, -, *, /, ** (potencia), % (módulo)")
    print("Escribe 'salir' para terminar\n")
    
    while True:
        try:
            entrada_1 = input("Primer número (o 'salir'): ").strip()
            if entrada_1.lower() == 'salir':
                print("¡Hasta luego!")
                break
            
            numero_1 = float(entrada_1)
            
            entrada_2 = input("Segundo número: ").strip()
            numero_2 = float(entrada_2)
            
            operacion = input("Operación (+, -, *, /, **, %): ").strip()
            
            resultado = realizar_operacion(numero_1, numero_2, operacion)
            
            if resultado is not None:
                print(f"El resultado es: {numero_1} {operacion} {numero_2} = {resultado}\n")
            
        except ValueError:
            print("Error: Por favor ingrese números válidos.\n")
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido. Hasta luego!")
            break

def realizar_operacion(a, b, operador):
    """
    Operación matemática especificada
    """
    operaciones = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '**': a ** b,
        '%': a % b if b != 0 else None
    }
    
    if operador == '/':
        if b != 0:
            return a / b
        else:
            print("Error: No se puede dividir por cero.")
            return None
    
    if operador in operaciones:
        resultado = operaciones[operador]
        if resultado is None:
            print("Error: No se puede calcular el módulo con divisor cero.")
            return None
        return resultado
    else:
        print(f"Error: Operación '{operador}' no válida.")
        print("Operaciones válidas: +, -, *, /, **, %")
        return None

def mostrar_estadisticas():
    """
    Estadísticas de uso de la calculadora
    """
    print("\n" + "="*40)
    print("Estadísticas de la calculadora:")
    print("- Operaciones disponibles: +, -, *, /, **, %")
    print("- Permite números decimales")
    print("- Errores de división por cero")
    print("="*40 + "\n")

if __name__ == "__main__":
    mostrar_estadisticas()
    calculadora()