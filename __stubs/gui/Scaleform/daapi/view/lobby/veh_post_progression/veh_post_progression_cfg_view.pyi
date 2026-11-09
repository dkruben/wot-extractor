# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/veh_post_progression/veh_post_progression_cfg_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.Scaleform.daapi.view.lobby.veh_post_progression.veh_post_progression_vehicle import g_postProgressionVehicle as g_postProgressionVehicle
from gui.Scaleform.daapi.view.meta.VehiclePostProgressionViewMeta import VehiclePostProgressionViewMeta as VehiclePostProgressionViewMeta
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES as HANGAR_ALIASES
from gui.shared.event_dispatcher import showVehicleHubModules as showVehicleHubModules, showVehicleHubOverview as showVehicleHubOverview, selectVehicleInHangar as selectVehicleInHangar
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from gui.veh_post_progression.sounds import PP_VIEW_SOUND_SPACE as PP_VIEW_SOUND_SPACE
from gui.veh_post_progression.vo_builders.cfg_page_vos import getDataVO as getDataVO, getTitleVO as getTitleVO
from helpers import dependency as dependency
from nation_change.nation_change_helpers import iterVehTypeCDsInNationGroup as iterVehTypeCDsInNationGroup
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket, IHeroTankController as IHeroTankController
from skeletons.gui.shared import IItemsCache as IItemsCache

class VehiclePostProgressionCfgView(VehiclePostProgressionViewMeta):
    _COMMON_SOUND_SPACE = PP_VIEW_SOUND_SPACE
    _PROGRESSION_INJECT_ALIAS = HANGAR_ALIASES.POST_PROGRESSION_INJECT
    __cmpBasket: Any
    __itemsCache: Any
    __heroTanks: Any
    _intCD: Any
    _goToVehicleAllowed: Any
    _overrideVehiclePreviewEvent: Any
    def __init__(self, ctx=None):
        ...
    def compareVehicle(self):
        ...
    # decorador original: @adisp_process
    def demountAllPairs(self):
        ...
    def goToVehicleView(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _getDiffVehicle(self):
        ...
    def _getModVehicle(self):
        ...
    def _getVehicle(self):
        ...
    def _checkNationChange(self):
        ...
    def _updateData(self, *_):
        ...
    def _updateTitle(self):
        ...
    def __onCmpBasketChange(self, changedData):
        ...
    def __onGoBackAction(self):
        ...
    def __onResearchAction(self):
        ...
