import threading
from app import create_app

def run_sede_a():
    app_a = create_app('config/config_sede_a.py')
    app_a.run(port=5001, debug=True, use_reloader=False)  # importante desactivar use_reloader

def run_sede_b():
    app_b = create_app('config/config_sede_b.py')
    app_b.run(port=5002, debug=True, use_reloader=False)

if __name__ == '__main__':
    # Crear los hilos
    t1 = threading.Thread(target=run_sede_a)
    t2 = threading.Thread(target=run_sede_b)

    # Iniciar los hilos
    t1.start()
    t2.start()

    # Esperar a que ambos terminen
    t1.join()
    t2.join()
