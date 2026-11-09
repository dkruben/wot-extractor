# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/soft_exception.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any

class SoftException(Exception):
    ...

class DisabledServiceSoftException(SoftException):
    message: Any
    def __init__(self, message='disabledService'):
        ...
