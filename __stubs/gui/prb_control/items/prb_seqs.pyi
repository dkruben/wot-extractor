# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/items/prb_seqs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
from constants import PREBATTLE_CACHE_KEY as PREBATTLE_CACHE_KEY
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from gui.prb_control.prb_getters import getPrebattleAutoInvites as getPrebattleAutoInvites
from gui.prb_control.items.prb_items import PlayerPrbInfo as PlayerPrbInfo
from gui.prb_control.prb_helpers import BadgesHelper as BadgesHelper
from helpers.time_utils import makeLocalServerTime as makeLocalServerTime
from messenger.ext import passCensor as passCensor

class PrbListItem(object):
    __slots__: tuple
    prbID: Any
    time: Any
    arenaTypeID: Any
    creator: Any
    clanAbbrev: Any
    playersCount: Any
    isOpened: Any
    comment: Any
    creatorIgrType: Any
    creatorDbId: Any
    badges: Any
    prbClusterID: Any
    def __init__(self, t, prbID, info):
        ...
    def __repr__(self):
        ...
    def getCreatorFullName(self):
        ...
    def getCensoredComment(self):
        ...
    def getBadge(self):
        ...

class AutoInviteItem(object):
    __slots__: tuple
    prbID: Any
    peripheryID: Any
    prbType: Any
    addInfo: Any
    arenaTypeID: Any
    isValid: Any
    description: Any
    startTime: Any
    def __init__(self, prbID, type=..., peripheryID=0, description=None, startTime=0, arenaTypeID=0, isValid=True, addInfo=None):
        ...
    def __repr__(self):
        ...

def PrbListIterator(prebattles):
    ...
def RosterIterator(roster_data):
    ...
def AutoInvitesIterator():
    ...
