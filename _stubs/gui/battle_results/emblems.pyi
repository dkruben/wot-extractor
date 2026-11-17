# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/emblems.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from gui.battle_results.settings import EMBLEM_TYPE as EMBLEM_TYPE
from gui.clans.clan_cache import g_clanCache as g_clanCache

class EmblemFetcher(object):
    __slots__: tuple
    _formationDBID: Any
    _url: Any
    def __init__(self, formationDBID):
        ...
    def fetch(self, callback):
        ...
    def getURL(self):
        ...

class ClanEmblemFetcher(EmblemFetcher):
    __slots__: tuple
    _url: Any
    def __init__(self, formationDBID, textureID):
        ...
    # decorador original: @adisp_process
    def fetch(self, callback):
        ...

def createFetcher(ctx):
    ...
