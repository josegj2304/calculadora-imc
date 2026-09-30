"""Calculadora de Índice de Masa Corporal (IMC)."""


def calcular_imc(peso_kg: float, estatura_m: float) -> float:
    """Devuelve el IMC: peso (kg) / estatura (m)^2."""
    if peso_kg <= 0 or estatura_m <= 0:
        raise ValueError("El peso y la estatura deben ser mayores que cero.")
    return peso_kg / (estatura_m ** 2)


def clasificar_imc(imc: float) -> str:
    """Clasificación según la Organización Mundial de la Salud (OMS)."""
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad grado I"
    elif imc < 40:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III"


def pedir_numero(mensaje: str) -> float:
    """Pide un número positivo al usuario hasta que ingrese uno válido."""
    while True:
        try:
            valor = float(input(mensaje).replace(",", "."))
            if valor > 0:
                return valor
            print("  El valor debe ser mayor que cero.")
        except ValueError:
            print("  Ingresa un número válido.")


def main():
    print("=== Calculadora de IMC ===")
    peso = pedir_numero("Peso en kilogramos (ej. 70): ")
    estatura = pedir_numero("Estatura en metros (ej. 1.75): ")

    # Si el usuario escribió la estatura en centímetros, convertirla a metros
    if estatura > 3:
        estatura /= 100

    imc = calcular_imc(peso, estatura)
    print(f"\nTu IMC es: {imc:.2f}")
    print(f"Clasificación: {clasificar_imc(imc)}")


if __name__ == "__main__":
    main()
