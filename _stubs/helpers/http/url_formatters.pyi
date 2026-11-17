# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/http/url_formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from future.moves.urllib import parse as parse

class URL_PARTS_IDS(object):
    SCHEME = 0
    NETLOC = 1
    PATH = 2
    PARAMS = 3
    QUERY = 4
    FRAGMENT = 5

def addParamsToUrlQuery(url, params, keepBlankValues=False):
    ...
def separateQuery(url):
    ...
