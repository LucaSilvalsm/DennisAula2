from LibPessoas import Pessoa
from LibDaos import PessoaDAO

class PessoaController:
    def __init__(self):
        self.dao = PessoaDAO()
    def incluir(self, pessoa):
        if(type(pessoa) is not Pessoa):
            raise "Não é uma pessoa!"
        if(type(pessoa.idade) is not int):
            raise "Idade deve ser inteira"
        return self.dao.incluir(pessoa)
    def alterar(self, pessoa):
        self.dao.alterar(pessoa)
    def excluir(self, chave):
        self.dao.excluir(chave)
    def obterTodos(self):
        return list(self.dao.obterTodos())
    def obter(self, chave):
        return self.dao.obter(chave)
    

