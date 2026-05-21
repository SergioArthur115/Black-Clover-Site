from flask import Flask, redirect, url_for, session, render_template  # importa flask
from database import init_db  # banco
from routes.auth_routes import bp as auth_bp  # rotas auth
from routes.user_routes import bp as user_bp  # rotas user
from routes.admin_routes import bp as admin_bp  # rotas admin
from models.user_model import get_user_by_id  # busca usuário
from config import SECRET_KEY  # config

app = Flask(__name__)  # cria app
app.secret_key = SECRET_KEY  # define chave

init_db()  # cria banco e admin

app.register_blueprint(auth_bp)  # registra auth
app.register_blueprint(user_bp)  # registra user
app.register_blueprint(admin_bp)  # registra admin


@app.route("/")  # rota inicial
def index():
    user = None
    if "user_id" in session:  # se logado
        user = get_user_by_id(session["user_id"])  # busca usuário

    return render_template("index.html", user=user)  # não logado


@app.route("/sobre")
def sobre():
    return render_template("pages/sobre.html")


@app.route("/personagens")
def personagens():
    return render_template("pages/personagens.html")


@app.route("/adaptacoes")
def adaptacoes():
    return render_template("pages/adaptacoes.html")


@app.route("/material_original")
def material_original():
    return render_template("pages/material_original.html")


@app.route("/universo")
def universo():
    return render_template("pages/universo.html")


@app.route("/fale_conosco")
def fale_conosco():
    return render_template("pages/fale_conosco.html")


if __name__ == "__main__":
    app.run(debug=True)  # roda sistema
