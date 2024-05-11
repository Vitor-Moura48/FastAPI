from peewee import Model, CharField, DateTimeField
from database.database import db
import datetime

class Vaga(Model):
    titulo = CharField()
    descricao = CharField()
    local = CharField()
    tipo_contrato = CharField()
    salario = CharField()
    data_criacao = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db