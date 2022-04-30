from typing import Tuple

from flask import Blueprint, request, jsonify, Response

from src.constants.http_status_codes import (HTTP_409_CONFLICT, HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND,
                                             HTTP_204_NO_CONTENT)
from src.database import Entidade, db

# Criação do Blueprint das rotas de gerenciamento de entidades.
entidades_bp = Blueprint('entidades', __name__, url_prefix='/api/entidades')


@entidades_bp.post('')
def create() -> Tuple[Response, int]:
    """
    Cria uma nova entidade.
    Método da Requisição: POST.
    Variáveis Obrigatórias (JSON): 'email', 'nome', 'cnpj', 'rua', 'bairro', 'cidade', 'cep' e 'sobre'.
    :return: Tuple[Response, int]
    """

    # Busca as variáveis obrigatórias no corpo da requisição.
    email = request.json.get('email', None)
    nome = request.json.get('nome', None)
    cnpj = request.json.get('cnpj', None)
    rua = request.json.get('rua', None)
    bairro = request.json.get('bairro', None)
    cidade = request.json.get('cidade', None)
    cep = request.json.get('cep', None)
    sobre = request.json.get('sobre', None)

    # Busca uma entidade no banco de dados com o email informado e, caso ela já exista, retorna uma resposta JSON
    # com status 409 (Conflito) contendo a mensagem do erro.
    if Entidade.query.filter_by(email=email).first():
        return jsonify({
            'error': 'Entidade já cadastrado.',
        }), HTTP_409_CONFLICT

    # Cria o modelo da nova entidade.
    entidade = Entidade(
            email=email,
            nome=nome,
            cnpj=cnpj,
            rua=rua,
            bairro=bairro,
            cidade=cidade,
            cep=cep,
            sobre=sobre,
    )

    # Adiciona a nova entidade à transação atual.
    db.session.add(entidade)

    # Efetua o commit da transação atual.
    db.session.commit()

    # Caso a criação seja bem sucedida, retorna uma resposta JSON com status 201 (Criado), contendo a nova entidade.
    return jsonify({
        'entidade': entidade.to_dict(),
    }), HTTP_201_CREATED


@entidades_bp.get('')
def read_all() -> Tuple[Response, int]:
    """
    Busca todas as entidades contidas no banco de dados.
    É possível filtrar as entidades informando os atributos e valores.
    Método da Requisição: GET.
    Variáveis Opcionais (Params): 'email', 'nome', 'cnpj', 'rua', 'bairro', 'cidade', 'cep' e 'sobre'.
    :return: Tuple[Response, int]
    """

    # Busca as variáveis opcionais nos parâmetros da requisição, e a transforma em um dicionário.
    query: dict = request.args.to_dict()

    # Busca todas as entidades contidas no banco de dados, utilizando como filtro os parâmetros informados (dicionário 'query').
    entidades = Entidade.query.filter_by(**query).all()

    # Cria uma lista que conterá os pedidos encontrados, serializados.
    data = []

    # Faz um loop nas entidades encontradas no banco de dados, e para cada uma delas, as insere serializadas na lista
    # criada anteriormente.
    for entidade in entidades:
        data.append(entidade.to_dict())

    # Caso a busca seja bem sucedida, retorna uma resposta JSON com status 200 (OK), contendo as entidades encontradas e
    # os filtros utilizados na busca.
    return jsonify({
        'query': query,
        'entidades': data,
    }), HTTP_200_OK


@entidades_bp.get('/<string:email>')
def read_one(email: str) -> Tuple[Response, int]:
    """
    Busca uma entidade existente no banco de dados, com o respectivo 'email' informado.
    Método da Requisição: GET.
    Variáveis Obrigatórias (URI): 'email'.
    :param email: str
    :return: Tuple[Response, int]
    """

    # Busca uma entidade no banco de dados com o email informado na URI.
    entidade = Entidade.query.filter_by(email=email).first()

    # Caso a entidade não exista, retorna uma resposta JSON com status 404 (Não Encontrado), contendo a mensagem de erro.
    if not entidade:
        return jsonify({
            'error': 'Entidade não cadastrada.',
        }), HTTP_404_NOT_FOUND

    # Caso a entidade exista, retorna uma resposta JSON com status 200 (OK), contendo a entidade encontrada.
    return jsonify({
        'entidade': entidade.to_dict(),
    }), HTTP_200_OK


@entidades_bp.put('/<string:email>')
@entidades_bp.patch('/<string:email>')
def update(email: str) -> Tuple[Response, int]:
    """
    Atualiza uma entidade existente no banco de dados, cujo 'email' é o informado na URI.
    Método da Requisição: PUT, PATCH.
    Variáveis Obrigatórias (URI): 'email'.
    Variáveis Opcionais (Params): 'nome', 'cnpj', 'rua', 'bairro', 'cidade', 'cep' e 'sobre'.
    :param email: str
    :return: Tuple[Response, int]
    """

    # Busca uma entidade no banco de dados com o email informado na URI.
    entidade = Entidade.query.filter_by(email=email).first()

    # Caso a entidade não exista, retorna uma resposta JSON com status 404 (Não Encontrado), contendo a mensagem de erro.
    if not entidade:
        return jsonify({
            'error': 'Entidade não cadastrada.',
        }), HTTP_404_NOT_FOUND

    # Atualiza os atributos da entidade na transação atual.
    entidade.nome = request.json.get('nome', entidade.nome)
    entidade.cnpj = request.json.get('cnpj', entidade.cnpj)
    entidade.rua = request.json.get('rua', entidade.rua)
    entidade.bairro = request.json.get('bairro', entidade.bairro)
    entidade.cidade = request.json.get('cidade', entidade.cidade)
    entidade.cep = request.json.get('cep', entidade.cep)
    entidade.sobre = request.json.get('sobre', entidade.sobre)

    # Efetua o commit da transação atual.
    db.session.commit()

    # Caso a atualização seja bem sucedida, retorna uma resposta JSON com status 200 (OK), contendo a entidade encontrada.
    return jsonify({
        'entidade': entidade.to_dict(),
    }), HTTP_200_OK


@entidades_bp.delete('/<string:email>')
def delete(email: str) -> Tuple[Response, int]:
    """
    Exclui uma entidade existente no banco de dados, cujo 'email' é o informado na URI.
    Método da Requisição: DELETE.
    Variáveis Obrigatórias (URI): 'email'.
    :param email: str
    :return: Tuple[Response, int]
    """

    # Busca uma entidade no banco de dados com o email informado na URI.
    entidade = Entidade.query.filter_by(email=email).first()

    # Caso a entidade não exista, retorna uma resposta JSON com status 404 (Não Encontrado), contendo a mensagem de erro.
    if not entidade:
        return jsonify({
            'error': 'Entidade não cadastrada.',
        }), HTTP_404_NOT_FOUND

    # Exclui a entidade na transação atual.
    db.session.delete(entidade)

    # Efetua o commit da transação atual.
    db.session.commit()

    # Caso a exclusão seja bem sucedida, retorna uma resposta JSON com status 204 (Sem Conteúdo).
    return jsonify({}), HTTP_204_NO_CONTENT
