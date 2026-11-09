# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/readers/crewBooks_readers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import ResMgr as ResMgr
import nations as nations
import os as os
from past.builtins import intern as intern
from items import _xml as _xml
from items import vehicles as vehicles
from items.components import crew_books_constants as crew_books_constants
from items.components import tankmen_components as tankmen_components
import items.components.crew_books_components as cb
__xmlReaders: dict

def _readPriceForItem(pricesDest, xmlCtx, section, compactDescr):
    ...
def _copyPriceForItem(pricesDest, sourceCompactDescr, destCompactDescr, itemNotInShop):
    ...
def _readPriceGroups(pricesCache, cache, xmlCtx, section, sectionName):
    ...
def _readGroupTags(xmlCtx, section, subsectionName):
    ...
def _readBookItem(pricesCache, cache, xmlCtx, section, storage):
    ...
def _readBookTypeItem(pricesCache, cache, xmlCtx, section, storage):
    ...
def _readCrewBooksCacheFromXMLSection(pricesCache, cache, xmlCtx, section, sectionName, storage):
    ...
def readCrewBooksCacheFromXML(pricesCache, cache, folder):
    ...
