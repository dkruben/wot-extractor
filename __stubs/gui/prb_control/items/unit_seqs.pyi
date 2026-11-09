# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/items/unit_seqs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from messenger.ext import passCensor as passCensor
from gui.prb_control.items.unit_items import PlayerUnitInfo as PlayerUnitInfo, UnitFlags as UnitFlags
from gui.prb_control.settings import CREATOR_ROSTER_SLOT_INDEXES as CREATOR_ROSTER_SLOT_INDEXES

class UnitsListItem(object):
    __slots__: tuple
    cfdUnitID: Any
    unitMgrID: Any
    creator: Any
    rating: Any
    peripheryID: Any
    playersCount: Any
    commandSize: Any
    flags: Any
    isRosterSet: Any
    description: Any
    extra: Any
    def __init__(self, cfdUnitID, unitMgrID=0, cmdrRating=0, peripheryID=0, unit=None, **kwargs):
        ...
    def __repr__(self):
        ...
    def update(self, cmdrRating=0, unit=None, **kwargs):
        ...

def UnitsListIterator(requester, data):
    ...
def UnitsUpdateIterator(requester, data):
    ...
