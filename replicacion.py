import shutil
import os
import time

def sincronizar_db(maestro='instance/data_sede_a.db', esclavo='instance/data_sede_b.db', intervalo=10):
    print("[REPLICACIÓN] Iniciando proceso de sincronización...")

    last_mod = 0

    while True:
        try:
            if os.path.exists(maestro):
                mod_time = os.path.getmtime(maestro)
                if mod_time != last_mod:
                    shutil.copy2(maestro, esclavo)
                    last_mod = mod_time
                    print("[REPLICACIÓN] Base de datos replicada de A → B")
                else:
                    print("[REPLICACIÓN] Sin cambios detectados.")
            else:
                print("[REPLICACIÓN] Archivo maestro no encontrado.")
        except Exception as e:
            print(f"[REPLICACIÓN] Error durante la sincronización: {e}")
        
        time.sleep(intervalo)
