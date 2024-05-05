from fastapi import APIRouter
from database.models.cliente import Cliente

router = APIRouter()

@router.post("/adicionar")
def adicionar_clientes(nome: str, email: str):

    Cliente.create(nome = nome, email = email)
    return 'Cliente Cadastrado!'

@router.get("/")
def obter_clientes():

    clientes = list(Cliente.select())
    return clientes

@router.put("/atualizar/")
def atualizar_cliente(cliente_id: int, nome: str, email: str):

    cliente = Cliente.get_by_id(cliente_id)
    cliente.nome = nome
    cliente.email = email
    cliente.save()
    return "Cliente Atualizado!"

@router.delete("/deletar/{cliente_id}")
def deletar_cliente(cliente_id: int):

    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
   
    return 'Cliente Deletado!'
