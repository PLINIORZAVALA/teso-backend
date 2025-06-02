from app import create_app

app = create_app('config/config_sede_a.py')

if __name__ == '__main__':
    app.run(port=5001, debug=True)
