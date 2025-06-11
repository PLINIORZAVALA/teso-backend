from multiprocessing import Process
from app import create_app

def run_sede_a():
    app_a = create_app('config/config_sede_a.py')
    app_a.run(port=5001, debug=True, use_reloader=False) 

def run_sede_b():
    app_b = create_app('config/config_sede_b.py')
    app_b.run(port=5002, debug=True, use_reloader=False)

if __name__ == '__main__':
    
    """
    # PROCESO HACIENDO USO DE PROCESOS HACIENDO USO DE LOS HILOS
    import threading
    t1 = threading.Thread(target=run_sede_a)
    t2 = threading.Thread(target=run_sede_b)

    # PROCESO HACIENDO USO DE PROCESOS HACIEDO USO DEL PARALELISMO DE PROCESOS
    from multiprocessing import Process
    p1 = Process(target=run_sede_a)
    p2 = Process(target=run_sede_b)
    """

    # Proceso en sedes a y b
    p1 = Process(target=run_sede_a)
    p2 = Process(target=run_sede_b)
    
    # Iniciar los hilos
    p1.start()
    p2.start()

    # Esperar a que ambos terminen
    p1.join()
    p2.join()
