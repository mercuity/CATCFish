from flask import Flask, request, jsonify, redirect, render_template
from .status import setStatus

def create_app(table):
    print("Сайт запущен")
    app = Flask(__name__)

    @app.route('/login', methods=['GET'])
    def login_form():
        id = request.args.get('id')
        if not id:
            return "ID не указан", 400 
        setStatus(id, 1, table)
        return render_template('index.html',id=id)
    @app.route('/login', methods=['POST'])
    def login_submit():
        id = request.form.get('id')
        if not id:
            return "ID не указан", 400 
        setStatus(id, 2, table)
        return ""
    return app