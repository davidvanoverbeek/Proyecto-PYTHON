import csv
import os


# Datos: Banco de preguntas

def cargar_preguntas():
    return [
        {
            "pregunta": "¿Cuál es la capital de Francia?",
            "opciones": ["A. Madrid", "B. Roma", "C. París", "D. Berlín"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué planeta está más cerca del Sol?",
            "opciones": ["A. Tierra", "B. Mercurio", "C. Venus", "D. Marte"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuál es el río más largo del mundo?",
            "opciones": ["A. Amazonas", "B. Nilo", "C. Yangtsé", "D. Misisipi"],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "¿Cuál es el edificio mas alto del mundo?",
            "opciones": ["A. Torre de Shanghái, Shanghái", "B. Merdeka 118, Kuala Lumpur", "C. Burj Khalifa, Dubái", "D. Abraj Al-Bait, La Meca"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Cuál es el animal mas pesado del plantes?",
            "opciones": ["A. Elefante africano de sabana", "B. Cachalote:", "C. Hipopótamo", "D. Ballena Azul "],
            "respuesta_correcta": "D"
        },
        {
            "pregunta": "¿Cual es el continente mas grande del planeta?",
            "opciones": ["A. América", "B. Asia", "C. África", "D. Europa"],
            "respuesta_correcta": "B"
        }
    ]

ARCHIVO_RANKING = "ranking.csv"


# Funciones del cuestionario

def mostrar_pregunta(pregunta, num, total):
    print(f"\nPregunta {num}/{total}")
    print(pregunta["pregunta"])
    for opcion in pregunta["opciones"]:
        print(opcion)


def obtener_respuesta():
    while True:
        r = input("Tu respuesta: ").strip().upper()
        if r in ["A", "B", "C", "D"]:
            return r
        print("Entrada no válida. Intenta de nuevo.")


def corregir_respuesta(respuesta, correcta):
    return respuesta == correcta


def mostrar_resultados(aciertos, total):
    porcentaje = aciertos / total * 100
    print("\n=== RESULTADOS ===")
    print(f"Preguntas: {total}")
    print(f"Aciertos: {aciertos}")
    print(f"Porcentaje: {porcentaje:.2f}%")
    print(valoracion(porcentaje))


def valoracion(porcentaje):
    if porcentaje >= 80:
        return "¡Muy bien!"
    elif porcentaje >= 50:
        return "Puedes mejorar."
    else:
        return "Necesitas practicar."


# Ranking

def guardar_resultado(nombre, aciertos, total):
    porcentaje = round(aciertos / total * 100, 2)
    existe = os.path.exists(ARCHIVO_RANKING)
    with open(ARCHIVO_RANKING, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(["Nombre", "Aciertos", "Total", "Porcentaje"])
        writer.writerow([nombre, aciertos, total, porcentaje])


def mostrar_ranking():
    if not os.path.exists(ARCHIVO_RANKING):
        print("\nTodavía no hay resultados guardados.\n")
        return
    print("\n=== Ranking ===")
    with open(ARCHIVO_RANKING, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for fila in reader:
            print("\t".join(fila))
    print()


# Flujo principal

def empezar_cuestionario():
    nombre = input("Ingresa tu nombre: ").strip() or "Anónimo"
    preguntas = cargar_preguntas()
    total = len(preguntas)
    aciertos = 0

    for i, p in enumerate(preguntas, start=1):
        mostrar_pregunta(p, i, total)
        r = obtener_respuesta()
        if corregir_respuesta(r, p["respuesta_correcta"]):
            print("✅ Correcto")
            aciertos += 1
        else:
            print(f"❌ Incorrecto. Respuesta correcta: {p['respuesta_correcta']}")

    mostrar_resultados(aciertos, total)
    guardar_resultado(nombre, aciertos, total)


def menu():
    while True:
        print("\n=== MENÚ ===")
        print("1. Empezar cuestionario")
        print("2. Ranking")
        print("3. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            empezar_cuestionario()
        elif opcion == "2":
            mostrar_ranking()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()