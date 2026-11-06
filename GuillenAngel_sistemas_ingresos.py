### TAREA: TIPOS DE DATOS Y ESTRUCTURAS EN PYTHON
###  Guillen Vazquez Angel de Jesus

###  Estructuras de Conrol
# Descripción: Sistema de evaluación de ingreso a carreras de Ingeniería
# ==============================================================================

# 1. Mensaje de bienvenida
print("Bienvenido al sistema de evaluación de ingenierías")

# 2. Presentación de claves válidas
print("\nClaves Válidas:\n")
print(" 1. Ingeniería Civil")
print(" 2. Ingeniería Mecánica")
print(" 3. Ingeniería Eléctrica")
print(" 4. Ingeniería en Sistemas\n")

try:
    # 3. Solicitar clave
    clave = int(input("Por favor seleccione la clave de la carrera (1-4): "))

    # Validar si la clave ingresada está dentro del rango permitido (1-4)
    if clave < 1 or clave > 4:
        print("\n[ERROR]: La clave ingresada no es válida. Debe elegir un número entre 1 y 4.")
    else:
        # Solicitar edad y promedio
        edad = int(input("Ingrese su edad: "))
        
        # OJO: Recuerda usar PUNTO (.) para los decimales (ej. 8.5) y no coma (,)
        promedio = float(input("Ingrese su promedio académico (ej. 8.5): "))

        # Definir el promedio mínimo requerido según la carrera
        if clave == 1:
            carrera = "Ingeniería Civil"
            promedio_requerido = 7.5
        elif clave == 2:
            carrera = "Ingeniería Mecánica"
            promedio_requerido = 8.0
        elif clave == 3:
            carrera = "Ingeniería Eléctrica"
            promedio_requerido = 8.5
        elif clave == 4:
            carrera = "Ingeniería en Sistemas"
            promedio_requerido = 7.0

        print(f"\n--- EVALUANDO SOLICITUD PARA {carrera.upper()} ---")

        # Condiciones anidadas para evaluar Edad y Promedio
        if edad >= 17:
            if promedio >= promedio_requerido:
                print(f"✅ ¡FELICIDADES! Has sido ACEPTADO en {carrera}.")
                print(f"   Tu promedio de {promedio} cumple con el mínimo requerido ({promedio_requerido}).")
            else:
                print(f"❌ RECHAZADO: Tu promedio ({promedio}) es menor al mínimo requerido para {carrera} ({promedio_requerido}).")
        else:
            print(f"❌ RECHAZADO: Tienes {edad} años. La edad mínima requerida para ingresar es 17 años.")

except ValueError:
    print("\n[ERROR]: Entrada inválida. Por favor, ingrese únicamente valores numéricos.")

#  PAUSA FINAL: Evita que la ventana se cierre de golpe al terminar
print("\n" + "="*50)
input("Presiona ENTER para salir del sistema educativo Cesun...")