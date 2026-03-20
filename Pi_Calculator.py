"""
Protocolo de Benchmarking: Serie de Leibniz (Cálculo de Pi)
Autor: Fridsco 2026

Este módulo ejecuta la aproximación de Pi mediante la serie de Gregory-Leibniz, 
utilizando millones de operaciones aritméticas de punto flotante para medir la
potencia de procesamiento de la CPU.

ESPECIFICACIONES DE TELEMETRÍA:
- Objetivo: 10,000,000 de iteraciones.
- Métrica: Tiempo de ejecución mediante time.perf_counter.
- Propósito: Evaluar la estabilidad térmica y velocidad de cómputo en Hardware Legacy.
"""

import time

def calcular_pi_leibniz(iteraciones):
    print(f"--- Iniciando el cálculo de Pi ---")
    print(f"Objetivo: {iteraciones:,} operaciones de punto flotante")
    
    inicio = time.perf_counter()
    pi_aproximado = 0
    denominador = 1
    signo = 1
    
    for i in range(iteraciones):
        pi_aproximado += signo * (4 / denominador)
        denominador += 2
        signo *= -1
        
    fin = time.perf_counter()
    
    tiempo_total = fin - inicio
    print(f"\n¡Cálculo completado!")
    print(f"Valor obtenido: {pi_aproximado:.10f}")
    print(f"Tiempo total: {tiempo_total:.4f} segundos")
    return tiempo_total

if __name__ == "__main__":
    # 10 millones es un buen estándar para comparar
    calcular_pi_leibniz(10_000_000)
