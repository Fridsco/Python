"""
Protocolo de Benchmarking: Torres de Hanói (Recursividad Pura)
Autor: Fridsco 2026

Este módulo ejecuta una prueba de estrés sobre el Stack de la CPU, midiendo la 
velocidad de conmutación de contextos en llamadas recursivas profundas.

ESPECIFICACIONES DE TELEMETRÍA:
- Objetivo: < 10.0s para 25 discos en Hardware Legacy.
- Métrica: Tiempo de ejecución mediante time.perf_counter (precisión de nanosegundos).
- Propósito: Validar la eficiencia en la gestión de ciclos de arquitecturas x86/x64.
"""

import time

def torres_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        return
    torres_hanoi(n - 1, origen, auxiliar, destino)
    torres_hanoi(n - 1, auxiliar, destino, origen)

def test_hanoi_stark(discos=25):
    print(f"--- Hanói ---")
    print(f"Objetivo: Resolver {discos} discos ({2**discos - 1:,} movimientos)")
    
    inicio = time.perf_counter()
    torres_hanoi(discos, 'A', 'C', 'B')
    fin = time.perf_counter()

    tiempo_total = fin - inicio
    print(f"\nPrueba completada")
    print(f"Tiempo total: {tiempo_total:.4f} segundos")
    
if __name__ == "__main__":
    test_hanoi_stark(25)
