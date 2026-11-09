# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/realm_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import ResMgr as rmgr
from constants import CURRENT_REALM as CURRENT_REALM, IS_CLIENT as IS_CLIENT, IS_EDITOR as IS_EDITOR, REALMS as REALMS
from py2to3.patched_future import with_metaclass as with_metaclass

class _ResMgrMeta(type):
    def __getattr__(cls, item):
        ...

# base nao representavel no stub: with_metaclass(...)
class ResMgr:
    @staticmethod
    def openSection(filepath, createIfMissing=False):
        ...
    @staticmethod
    def purge(filepath, recursive=False):
        ...

def getRealmFilePath(filepath):
    ...
def isFileWithRealm(fileName):
    ...
def isFileWithCurrentRealm(fileName):
    ...
