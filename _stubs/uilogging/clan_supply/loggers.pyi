# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/clan_supply/loggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import json as json
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.clans.clan_cache import g_clanCache as g_clanCache
from uilogging.base.logger import MetricsLogger as MetricsLogger
from uilogging.clan_supply.constants import FEATURE as FEATURE, ClanSupplyLogAction as ClanSupplyLogAction
from uilogging.types import ItemType as ItemType, ParentScreenType as ParentScreenType, InfoType as InfoType

class ClanSupplyEventLogger(MetricsLogger):
    __slots__: tuple
    def __init__(self):
        ...
    def logCloseEvent(self, item, info):
        ...
    def logOpenEvent(self, item, parentScreen):
        ...
