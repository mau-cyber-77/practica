from funciones.ejercicio_1 import ejercicio_1
from funciones.ejercicio_2 import fnejerecicio_2
from funciones.ejercicio_3 import fnejercicio_3
from funciones.ejercicio_4 import fnejercicio_4
from funciones.ejercicio_5 import fnejercicio_5
from funciones.ejercicio_6 import fnejercicio_6
from funciones.ejercicio_7 import fnejercicio_7
from funciones.integracion_numerica import integracion_numerica
from funciones.area_triangulo import leerdatos, calculoarea, mostrarresultado
from funciones.imc import leerdatos as leerdatos_imc, calculoimc, mostrarresultado as mostrarresultado_imc

def main():
    # Llamada a las funciones de los ejercicios
    ejercicio_1()
    fnejerecicio_2()
    fnejercicio_3()
    fnejercicio_4()
    fnejercicio_5()
    fnejercicio_6()
    fnejercicio_7()

    # Llamada a las funciones de integración numérica
    integracion_numerica()

    # Llamada a las funciones del área del triángulo
    leerdatos()
    calculoarea()
    mostrarresultado()
    
    # Llamada a las funciones del IMC
    leerdatos_imc()

    
if __name__ == "__main__":
    main()