# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/goodies/goodies_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import time as time
import calendar as calendar
import datetime as datetime
from future.utils import viewitems as viewitems
import helpers_common as helpers_common
import XmlConfigReader as XmlConfigReader
from debug_utils import LOG_WARNING as LOG_WARNING
from goodies import goodie_helpers as goodie_helpers
from goodies.goodie_constants import GOODIE_VARIETY as GOODIE_VARIETY
from items.vehicles import makeVehicleTypeCompDescrByName as makeVehicleTypeCompDescrByName
from soft_exception import SoftException as SoftException
_CONFIG_FILE = 'scripts/server_xml/goodies.xml'
g_cache = None

def readConfig(verbose):
    ...
def _readGoodieResource(section):
    ...
def _readGoodieTarget(reader, subsectionName):
    ...
def _readGoodieCondition(section):
    ...
def _readPrice(reader, subsectionName):
    ...
def _validator(uid, variety, resource, price):
    ...
def _readGoodies(reader, subsectionName):
    ...
def init(gameParams=None):
    ...
