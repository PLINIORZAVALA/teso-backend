from app import create_app

app = create_app('config/config_sede_b.py')

if __name__ == '__main__':
    app.run(port=5002, debug=True)
