class Pessoa:
    def __init__(self, nome, idade, documentos):
        self.nome = nome
        self.idade = idade
        self.documentos = documentos

dados = print('nome: João', 'idade: 78', 'documentos: RG e CPF')

class Medico(Pessoa):
    def __init__(self, crm, nome, idade, documentos):
        super().__init__(nome, idade, documentos)
        self.crm = crm

dados = print(nome,)
crm = print('CRM 44056')


class Paciente(Pessoa):
    def __init__(self, doença, sintomas):
        self.doença = doença
        self.sintomas = sintomas

sintoma = print('Dor de cabeça, tontura, virose')