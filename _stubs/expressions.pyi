# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/expressions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import tokenize as tokenize
import token as token
from py2to3.moves.io import FastStringIO as FastStringIO
from soft_exception import SoftException as SoftException

class ParserException(SoftException):
    ...

class _Tokenizer:
    tokenizer: Any
    __currentToken: Any
    def __init__(self, s):
        ...
    def __next(self):
        ...
    def peek(self):
        ...
    def match(self, toknum, tokval=None):
        ...

class ExpressionParser(object):
    _CMP_OPERATORS: dict
    _SUM_OPERATORS: dict
    tokens: Any
    def __init__(self):
        ...
    def parseExpression(self, s):
        ...
    def _parseOperator(self, tokenizer, operators):
        ...
    def _parseExpression(self, tokenizer):
        ...
    def _parseOrExpression(self, tokenizer):
        ...
    def _parseAndExpression(self, tokenizer):
        ...
    def _parseCondition(self, tokenizer):
        ...
    def _parseSum(self, tokenizer):
        ...
    def _parseTerm(self, tokenizer):
        ...

def parseExpression(condition):
    ...
