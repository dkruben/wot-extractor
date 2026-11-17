# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/MinimapLobby.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Union as Union
from past.utils import old_div as old_div
import ArenaType as ArenaType
from gui.Scaleform.daapi.view.meta.MinimapPresentationMeta import MinimapPresentationMeta as MinimapPresentationMeta
from gui.Scaleform.genConsts.MINIMAPENTRIES_CONSTANTS import MINIMAPENTRIES_CONSTANTS as MINIMAPENTRIES_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from points_of_interest_shared import PoiType as PoiType
_POI_TYPE_TO_STR: dict

class MinimapLobby(MinimapPresentationMeta):
    settingsCore: Any
    __playerTeam: Any
    __arenaTypeID: Any
    __cfg: Any
    __minimapSize: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def onSettingsChanging(self, diff):
        ...
    def setMap(self, arenaID):
        ...
    def setMinimapData(self, arenaID, playerTeam, size):
        ...
    def setPlayerTeam(self, playerTeam):
        ...
    def swapTeams(self, team):
        ...
    def setArena(self, arenaTypeID):
        ...
    def setEmpty(self):
        ...
    def setConfig(self, cfg):
        ...
    def build(self):
        ...
    def __getTeamColor(self, isPlayerTeam):
        ...

def _resilientMapIconPathGetter(gameplayName, geometryName):
    ...
