# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/readers/perks_readers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import os as os
from collections import OrderedDict as OrderedDict
import typing as typing
from future.utils import lmap as lmap
import ResMgr as ResMgr
from items import _xml as _xml
from items.components import perks_constants as perks_constants
from items.components.perks_components import Perk as Perk, PerkArgument as PerkArgument
from items.components.perks_constants import PerkTags as PerkTags
PERKS_READERS: dict

def _readPerkArguments(xmlCtx, section):
    ...
def _readPerkItem(xmlCtx, section, storage):
    ...
def _readPerksCacheFromXMLSection(xmlCtx, section, sectionName, storage):
    ...
def readPerksCacheFromXML(cache, folder):
    ...
