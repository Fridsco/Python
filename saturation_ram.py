"""
Protocolo de Benchmarking: Saturación Crítica de RAM
Autor: Fridsco 2026

Este módulo ejecuta una prueba de estrés de memoria mediante la generación 
y ordenamiento masivo de 20,000,000 enteros criptográficamente seguros.

ESPECIFICACIONES DE TELEMETRÍA:
- Objetivo: Evaluar la gestión de memoria RAM y el uso de SWAP en Hardware Legacy.
- Métrica: Tiempo de generación vs. Tiempo de ordenamiento (Timsort).
- Diagnóstico: Monitoreo en tiempo real mediante psutil (RSS y Porcentaje de Memoria).
- Riesgo: Puede causar congelamiento temporal si el sistema carece de SWAP suficiente.
"""

import time
import secrets
import psutil
import os

def protocolo_mem_saturation(cantidad=20_000_000):
    process = psutil.Process(os.getpid())
    print(f"--- ALERTA: PROTOCOLO DE SATURACIÓN CRÍTICA ({cantidad:,} ELEMENTOS) ---")
    print("Estado actual de la RAM antes de iniciar:", f"{psutil.virtual_memory().percent}%")
    
    # Fase 1: Generación Masiva (Advertencia: Esto tardará)
    print(f"\nGenerando {cantidad:,} secretos... (Esto puede tomar tiempo)")
    inicio_gen = time.perf_counter()
    try:
        # Generamos los datos. Aquí es donde la RAM subirá rápidamente.
        datos = [secrets.randbelow(100_000_000) for _ in range(cantidad)]
    except MemoryError:
        print("\n¡ALERTA! Memoria RAM insuficiente. Sistema abortado para evitar un cierre forzado.")
        return
    
    fin_gen = time.perf_counter()
    
    # Fase 2: Ordenamiento de Gran Escala
    print(f"Generación completada en {(fin_gen - inicio_gen):.2f} s")
    print("Iniciando ordenamiento Timsort masivo...")
    inicio_sort = time.perf_counter()
    datos.sort()
    fin_sort = time.perf_counter()
    
    # Diagnóstico de Recursos Final
    mem_final = process.memory_info().rss / (1024 * 1024)
    print(f"\n--- DIAGNÓSTICO DE SATURACIÓN ---")
    print(f"Tiempo Ordenamiento: {(fin_sort - inicio_sort):.4f} s")
    print(f"Consumo de RAM por el script: {mem_final:.2f} MB")
    print(f"Carga total de RAM en el sistema: {psutil.virtual_memory().percent}%")
    
    if psutil.virtual_memory().percent > 90:
        print("Veredicto: SU PC ESTÁ USANDO SWAP.")

if __name__ == "__main__":
    protocolo_mem_saturation()
