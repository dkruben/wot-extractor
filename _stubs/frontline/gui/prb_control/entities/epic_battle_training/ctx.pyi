# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/prb_control/entities/epic_battle_training/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from gui.prb_control import settings as prb_settings
from gui.prb_control.entities.base.legacy.ctx import TeamSettingsCtx as TeamSettingsCtx, JoinLegacyCtx as JoinLegacyCtx
from gui.shared.utils.decorators import ReprInjector as ReprInjector
_REQUEST_TYPE = prb_settings.REQUEST_TYPE
_FUNCTIONAL_FLAG = prb_settings.FUNCTIONAL_FLAG

# decorador original: @ReprInjector.withParent(...)
class EpicTrainingSettingsCtx(TeamSettingsCtx):
    __slots__: tuple
    __arenaTypeID: Any
    __roundLen: Any
    def __init__(self, waitingID='', isOpened=True, comment='', isRequestToCreate=True, arenaTypeID=0, roundLen=900, flags=...):
        ...
    @classmethod
    def fetch(cls, settings):
        ...
    def getArenaTypeID(self):
        ...
    def setArenaTypeID(self, arenaTypeID):
        ...
    def getRoundLen(self):
        ...
    def setRoundLen(self, roundLen):
        ...
    def isArenaTypeIDChanged(self, settings):
        ...
    def isRoundLenChanged(self, settings):
        ...
    def areSettingsChanged(self, settings):
        ...

class JoinEpicBattleTrainingCtx(JoinLegacyCtx):
    __slots__: tuple
    def __init__(self, prbID, prbClusterID, waitingID='', flags=...):
        ...
