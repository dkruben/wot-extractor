# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ContactInfo.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Settings as Settings

class ContactInfo(object):
    KEY_USER = 'user'
    KEY_HOST = 'host'
    KEY_EMAIL = 'email'
    KEY_PASSWORD = 'password'
    KEY_REMEMBER = 'remember'
    host: Any
    user: Any
    email: Any
    password: Any
    rememberPassword: Any
    def __init__(self):
        ...
    def readLocalLoginData(self):
        ...
    def writeLocalLoginData(self):
        ...
    def getLoginDataSection(self):
        ...
    def __checkLoginDataSection(self):
        ...
