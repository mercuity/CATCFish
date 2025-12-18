from flask import Flask, request, jsonify, redirect
from .status import setStatus

def create_app(table):
    print("Сайт запущен")
    app = Flask(__name__)

    @app.route('/track')
    def track_click_query():
        id = request.args.get('id')
        if not id:
            return "ID не указан", 400 
        setStatus(id, table)
        return "Это была фишинговая ссылка"

    return app