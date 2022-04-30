from flask import Blueprint, render_template

# Criação do Blueprint das rotas da SPA (Single Page Application).
spa_bp = Blueprint('spa', __name__)


@spa_bp.route('/', defaults={'path': ''})
@spa_bp.route('/<path:path>')
def spa(path) -> str:
    """
    Renderiza a SPA.
    :param path:
    :return: str
    """

    # Efetua o log no console, das rotas acessadas
    print("Path: {}".format(path))

    # Renderiza a página da SPA.
    return render_template("vue/index.html")
