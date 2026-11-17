# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/veh_post_progression/veh_post_progression_cmp_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.veh_post_progression.veh_post_progression_base_view import VehiclePostProgressionBaseView as VehiclePostProgressionBaseView
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers as cmp_helpers
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES as HANGAR_ALIASES
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.veh_post_progression.vo_builders.cmp_page_vos import getTitleVO as getTitleVO, getDataVO as getDataVO
from helpers import dependency as dependency
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket

class VehiclePostProgressionCmpView(VehiclePostProgressionBaseView):
    _PROGRESSION_INJECT_ALIAS = HANGAR_ALIASES.POST_PROGRESSION_CMP_INJECT
    __cmpBasket: Any
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _onSyncCompleted(self, reason, diff):
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
    def __onExitAction(self):
        ...
    def __onBasketParamsChanged(self, *_):
        ...
