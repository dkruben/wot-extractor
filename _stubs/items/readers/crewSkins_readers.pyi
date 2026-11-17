# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/readers/crewSkins_readers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import os as os
from past.builtins import intern as intern
import ResMgr as ResMgr
import nations as nations
import items.components.crew_skins_components as cc
from constants import REGIONAL_REALMS as REGIONAL_REALMS
from items import _xml as _xml
from items import vehicles as vehicles
from items.components import crew_skins_constants as crew_skins_constants
from items.components import tankmen_components as tankmen_components

def _readPriceForItem(pricesDest, xmlCtx, section, compactDescr):
    ...
def _copyPriceForItem(pricesDest, sourceCompactDescr, destCompactDescr, itemNotInShop):
    ...
def _readPriceGroups(pricesCache, cache, xmlCtx, section, sectionName):
    ...
def _readGroupTags(xmlCtx, section, subsectionName):
    ...
def _readSkinItem(pricesCache, cache, xmlCtx, section, storage):
    ...
def _readCrewSkinsCacheFromXMLSection(pricesCache, cache, xmlCtx, section, sectionName, storage):
    ...
def readCrewSkinsCacheFromXML(pricesCache, cache, folder):
    ...
