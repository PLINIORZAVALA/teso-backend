from multiprocessing import Process
from app import create_app
from replicacion import sincronizar_db

def run_sede_a():
    app_a = create_app('config/config_sede_a.py')
    app_a.run(port=5001, debug=True, use_reloader=False) 

def run_sede_b():
    app_b = create_app('config/config_sede_b.py')
    app_b.run(port=5002, debug=True, use_reloader=False)

if __name__ == '__main__':

    # Proceso en sedes a y b
    p1 = Process(target=run_sede_a)
    p2 = Process(target=run_sede_b)

    # Proceso de replicación
    p3 = Process(target=sincronizar_db) 
    
    # Inicar ambos procesos
    p1.start()
    p2.start()
    # Iniciar el proceso de replicación
    p3.start()

    # Esperar a que ambos terminen
    p1.join()
    p2.join()
    # Esperar a que el proceso de replicación termine
    p3.join()
