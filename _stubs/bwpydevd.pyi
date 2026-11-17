# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/bwpydevd.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import os as os
import sys as sys
import ResMgr as ResMgr
import BigWorld as BigWorld
import threading as threading
import bwdebug as bwdebug
REPLACE_PATHS: list
HAS_BW_CONFIG = False
bwPyDevDStarted = False
bwActiveIde = None

class BWConfig:
    debugConfig = None
    @staticmethod
    def readString(key, default=''):
        ...
    @staticmethod
    def readBool(key, default=False):
        ...
    @staticmethod
    def readInt(key, default=0):
        ...
    @staticmethod
    def getSections(key):
        ...

def BWConfigWrapper(fn):
    ...
# decorador original: @BWConfigWrapper
def startDebug(isStartUp=False, host=None, port=None, ide=None):
    ...
def startPyDevD(ide, host='127.0.0.1', port=5678, suspend=False, traceOnlyCurrentThread=False, inspectDoubleUnderscore=False, pathMappings=None):
    ...
def stopPyDevD():
    ...
