# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/platoon/view/platoon_members_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_light.gui.impl.gen.view_models.views.lobby.platoon.comp7_light_slot_model import Comp7LightSlotModel as Comp7LightSlotModel
from comp7_light.gui.impl.gen.view_models.views.lobby.platoon.comp7_light_window_model import Comp7LightWindowModel as Comp7LightWindowModel
from comp7_light_constants import CLIENT_UNIT_CMD as CLIENT_UNIT_CMD
from comp7_light.gui.comp7_light_constants import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.platoon.dropdown_item import DropdownItem as DropdownItem
from gui.impl.gen.view_models.views.lobby.platoon.members_window_model import PrebattleTypes as PrebattleTypes
from gui.impl.gen.view_models.views.lobby.platoon.slot_model import ErrorType as ErrorType
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.platoon.platoon_helpers import getPlatoonBonusState as getPlatoonBonusState
from gui.impl.lobby.platoon.view.platoon_members_view import SquadMembersView as SquadMembersView, _LayoutStyle as _LayoutStyle
from gui.impl.lobby.platoon.view.subview.platoon_chat_subview import ChatSubview as ChatSubview
from gui.impl.lobby.premacc.squad_bonus_tooltip_content import SquadBonusTooltipContent as SquadBonusTooltipContent
from gui.prb_control import prb_getters as prb_getters, prbEntityProperty as prbEntityProperty
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class Comp7LightMembersView(SquadMembersView):
    _layoutID: Any
    _prebattleType = PrebattleTypes.COMP7LIGHT
    __comp7LightController: Any
    __lobbyCtx: Any
    __unitMgr: Any
    def __init__(self, prbType):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def _viewModelClass(self):
        ...
    @property
    def _slotModelClass(self):
        ...
    def _addSubviews(self):
        ...
    def _getLayoutStyle(self):
        ...
    def _setModeSlotSpecificData(self, slotData, slotModel):
        ...
    def _initWindowModeSpecificData(self, model):
        ...
    def _updateHeader(self):
        ...
    def _getWindowInfoTooltipHeaderAndBody(self):
        ...
    def _hasFreeSlot(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def __updateDropDown(self, model):
        ...
    def __updateMemberCountDropdown(self, model):
        ...
    def __updateDropdownItem(self, item, playersCount):
        ...
    def __updateEntityState(self):
        ...
    # decorador original: @args2params(...)
    def __onMemberCountDropdown(self, selectedIds):
        ...
    @staticmethod
    def __getDropDownTooltipText():
        ...
    @staticmethod
    def __getDropDownItemTooltipText():
        ...
