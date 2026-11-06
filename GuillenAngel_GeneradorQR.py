# ---------------------------------------------------------
# Asignatura: Introducción a la Ingeniería en Dev. de Software
# Nombre del Alumno: Guillen Angel de Jesus
# Actividad: Generador Dinámico de Códigos QR
# ---------------------------------------------------------

import qrcode


def generar_codigo_qr():

    print("==========================================")
    print("   GENERADOR DINÁMICO DE CÓDIGOS QR   ")
    print("==========================================")

    # 1. Agregar el contenido del QR (puede ser texto o página web)
    contenido_qr = input("\nIngrese el enlace para generar su QR: ")

    # Validación por si el usuario deja el contenido vacío
    if not contenido_qr.strip():
        print(
            "\n Error: No se ha ingresado información. El QR no puede estar vacío. Intente de nuevo."
        )
        return

    # 2. Agregar el nombre para tu imagen
    nombre_archivo = input(
        "Ingrese el nombre con el que desea guardar el archivo (sin extensión): "
    )

    # Validación por si no ingresa un nombre de archivo
    if not nombre_archivo.strip():
        print(
            "\n Error: Debe especificar un nombre para guardar el archivo."
        )
        return

    # 3. Agregar la extensión .png al nombre proporcionado por el usuario
    archivo_final = nombre_archivo + ".png"

    print("\nGenerando imagen de código QR...")

    # 4. Generar la imagen del código QR a partir de lo ingresado
    img = qrcode.make(contenido_qr)

    # 5. Guardar el archivo .png en la carpeta actual de trabajo
    img.save(archivo_final)

    # 6. Confirmación de finalización exitosa
    print("------------------------------------------")
    print(f" ¡Su QR fue generado exitosamente!")
    print(f" El nombre de su archivo guardado: {archivo_final}")
    print("------------------------------------------")


# Punto de entrada para ejecutar la función
if __name__ == "__main__":
    generar_codigo_qr()