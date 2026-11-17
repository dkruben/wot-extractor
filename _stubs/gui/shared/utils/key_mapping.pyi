# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/key_mapping.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from builtins import chr as chr
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
import CommandMapping as CommandMapping
import Keys as Keys
from helpers.i18n import makeString as makeString
from gui.Scaleform.locale.READABLE_KEY_NAMES import READABLE_KEY_NAMES as READABLE_KEY_NAMES
BW_TO_SCALEFORM: dict
SCALEFORM_TO_BW: dict
BW_TO_SCALEFORM_OVERRIDE: dict
SCALEFORM_TO_BW_OVERRIDE: dict
voidSymbol = 0

class MappingType(object):
    MAPVK_VK_TO_VSC = 0
    MAPVK_VSC_TO_VK = 1
    MAPVK_VK_TO_CHAR = 2
    MAPVK_VSC_TO_VK_EX = 3

def getBigworldNameFromKey(bigworldKey):
    ...
def getBigworldKeyFromName(bigworldName):
    ...
def getBigworldKey(scaleformKey):
    ...
def getScaleformKey(bigworldKey):
    ...
def getKey(command):
    ...
def canGetVirtualKey(key):
    ...
def getVirtualKey(command):
    ...
def getReadableKey(command):
    ...
def __getVK(command):
    ...
