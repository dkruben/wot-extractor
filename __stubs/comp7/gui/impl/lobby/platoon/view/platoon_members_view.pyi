# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/platoon/view/platoon_members_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import lrange as lrange
from shared_utils import findFirst as findFirst
from comp7.gui.comp7_constants import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from comp7.gui.impl.gen.view_models.views.lobby.enums import Division as Division, Rank as Rank
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7.gui.impl.gen.view_models.views.lobby.platoon.comp7_slot_model import Comp7SlotModel as Comp7SlotModel
from comp7.gui.impl.gen.view_models.views.lobby.platoon.comp7_window_model import Comp7WindowModel as Comp7WindowModel
from comp7.gui.impl.gen.view_models.views.lobby.progression_item_base_model import ProgressionItemBaseModel as ProgressionItemBaseModel
from comp7.gui.impl.lobby.comp7_helpers import comp7_shared as comp7_shared
from comp7.gui.impl.lobby.meta_view.meta_view_helper import setRankItemData as setRankItemData
from comp7.gui.impl.lobby.tooltips.division_tooltip import DivisionTooltip as DivisionTooltip
from comp7.gui.impl.lobby.tooltips.fifth_rank_tooltip import FifthRankTooltip as FifthRankTooltip
from comp7.gui.impl.lobby.tooltips.general_rank_tooltip import GeneralRankTooltip as GeneralRankTooltip
from comp7.gui.impl.lobby.tooltips.rank_compatibility_tooltip import RankCompatibilityTooltip as RankCompatibilityTooltip
from comp7.gui.impl.lobby.tooltips.sixth_rank_tooltip import SixthRankTooltip as SixthRankTooltip
from comp7_common.comp7_constants import CLIENT_UNIT_CMD as CLIENT_UNIT_CMD
from comp7_core.gui.impl.lobby.comp7_core_helpers.comp7_core_model_helpers import getSeasonNameEnum as getSeasonNameEnum
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
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from comp7.helpers.comp7_server_settings import Comp7RanksConfig as Comp7RanksConfig
from comp7_ranks_common import Comp7Division as Comp7Division
_logger: Any

class Comp7MembersView(SquadMembersView):
    _comp7Controller: Any
    _prebattleType = PrebattleTypes.COMP7
    __lobbyCtx: Any
    _layoutID: Any
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
    def _onLoading(self, *args, **kwargs):
        ...
    def _addSubviews(self):
        ...
    def _setModeSlotSpecificData(self, slotData, slotModel):
        ...
    def _initWindowModeSpecificData(self, model):
        ...
    def __updateRankTips(self, model):
        ...
    def _updateHeader(self):
        ...
    def _getLayoutStyle(self):
        ...
    def _hasFreeSlot(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    # decorador original: @args2params(...)
    def __onMemberCountDropdown(self, selectedIds):
        ...
    def __updateDropDown(self, model):
        ...
    def __updateMemberCountDropdown(self, model):
        ...
    def __updateDropdownItem(self, item, playersCount):
        ...
    def __updateEntityState(self):
        ...
    def __getDropDownTooltipText(self):
        ...
    def __getDropDownItemTooltipText(self):
        ...
    @classmethod
    def __getDivision(cls, rank, rating):
        ...
