from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

# Cria uma instância do gerenciador do banco de dados.
db = SQLAlchemy()

class Entidade(db.Model):
    """ Model Entidade """

    # Nome da tabela no banco de dados.
    __tablename__ = 'entidades'

    # Colunas do banco de dados / Atributos da entidade.
    email = db.Column(db.String(255), primary_key=True)
    nome = db.Column(db.String(255))
    cnpj = db.Column(db.String(255))
    rua = db.Column(db.String(255))
    bairro = db.Column(db.String(255))
    cidade = db.Column(db.String(255))
    cep = db.Column(db.String(255))
    sobre = db.Column(db.Text, nullable=True)

    def to_dict(self) -> dict:
        """
        Retorna um dicionário contendo a entidade serializada.
        :return: dict
        """
        return dict(
            email=self.email,
            nome=self.nome,
            cnpj=self.cnpj,
            rua=self.rua,
            bairro=self.bairro,
            cidade=self.cidade,
            cep=self.cep,
            sobre=self.sobre,
        )
