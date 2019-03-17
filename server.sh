$ port
export FLASK_APP=Controller/router.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port="$1"