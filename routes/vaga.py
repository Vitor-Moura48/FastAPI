from fastapi import APIRouter
from database.models.vaga import Vaga

router = APIRouter()

@router.get("/")
def obter_vagas():

    vagas = list(Vaga.select())
    return vagas

@router.get("/{vaga_id}")
def obter_vaga(vaga_id: int):

    try:
        vaga = Vaga.get_by_id(vaga_id)
        return vaga
    except:
        return 'Não encontrado'

@router.post("/adicionar")
def adicionar_vaga(titulo: str, descricao: str, local: str, tipo_contrato: str, salario: float):

    try:
        Vaga.create(titulo = titulo, descricao = descricao, local = local, tipo_contrato = tipo_contrato, salario = salario)
        return 'Vaga Cadastrada!'
    except:
        return 'Não foi possível adicionar...'



