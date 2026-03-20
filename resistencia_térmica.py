"""
Protocolo de Benchmarking: Resistencia Térmica (Stress Test)
Autor: Fridsco 2026

Este módulo ejecuta un ráfaga ininterrumpida de hashes SHA-256 para evaluar 
la estabilidad térmica del sistema y detectar degradación por fatiga (Throttling).

ESPECIFICACIONES DE TELEMETRÍA:
- Objetivo: Mantener carga máxima de CPU durante 60s.
- Métrica: Hashes por segundo (H/s) con reportes de intervalo cada 5s.
- Diagnóstico: Cálculo porcentual de degradación entre el inicio y el final de la carga.
- Propósito: Validar la eficiencia de la pasta térmica y el sistema de disipación activa.
"""

import time
import hashlib

def test_resistencia(duracion_total_segundos=60, intervalo_reporte=5):
    print(f"--- Iniciando módulo de resistencia térmica ---")
    print(f"Objetivo: Monitorear degradación térmica por {duracion_total_segundos}s")
    print(f"Frecuencia de telemetría: Cada {intervalo_reporte}s\n")
    
    inicio_experimento = time.perf_counter()
    reportes = []
    
    try:
        while (time.perf_counter() - inicio_experimento) < duracion_total_segundos:
            inicio_intervalo = time.perf_counter()
            intentos_intervalo = 0
            
            # Ciclo para el intervalo actual
            while (time.perf_counter() - inicio_intervalo) < intervalo_reporte:
                test_pass = f"combate_{intentos_intervalo}".encode()
                hashlib.sha256(test_pass).hexdigest()
                intentos_intervalo += 1
            
            # Cálculo de rendimiento del intervalo
            fin_intervalo = time.perf_counter()
            duracion_intervalo = fin_intervalo - inicio_intervalo
            tasa_intervalo = intentos_intervalo / duracion_intervalo
            
            tiempo_transcurrido = int(fin_intervalo - inicio_experimento)
            reportes.append(tasa_intervalo)
            
            print(f"[{tiempo_transcurrido}s] Rendimiento: {tasa_intervalo:,.2f} hashes/seg")
            
        print("\n" + "="*55)
        print("RESUMEN DE ESTABILIDAD TÉRMICA")
        print("="*55)
        print(f"Rendimiento Inicial: {reportes[0]:,.2f} h/s")
        print(f"Rendimiento Final:   {reportes[-1]:,.2f} h/s")
        
        degradacion = (1 - (reportes[-1] / reportes[0])) * 100
        print(f"Degradación de Potencia: {degradacion:.2f}%")
        
        if degradacion > 5:
            print("Veredicto: Se detectó fatiga térmica (Thermal Throttling).")
        else:
            print("Veredicto: Sistema estable. Disipación de calor eficiente.")
        print("="*55)

    except KeyboardInterrupt:
        print("\nProtocolo abortado por el usuario.")

if __name__ == "__main__":
    # Vamos a estresarlo por 1 minuto completo
    test_resistencia(duracion_total_segundos=60, intervalo_reporte=5)
