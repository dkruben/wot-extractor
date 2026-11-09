# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mode_selector/items/epic_mode_selector_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_card_types import ModeSelectorCardTypes as ModeSelectorCardTypes
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_epic_model import ModeSelectorEpicModel as ModeSelectorEpicModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import BattlePassState as BattlePassState
from gui.impl.lobby.mode_selector.items import setBattlePassState as setBattlePassState
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem as ModeSelectorLegacyItem
from gui.impl.lobby.mode_selector.items.items_constants import ModeSelectorRewardID as ModeSelectorRewardID
from gui.shared.event_dispatcher import showFrontlineInfoWindow as showFrontlineInfoWindow, showHangar as showHangar
from gui.shared.formatters import time_formatters as time_formatters
from gui.shared.formatters.ranges import toRomanRangeString as toRomanRangeString, toRangeString as toRangeString
from gui.shared.utils import isRomanNumberForbidden as isRomanNumberForbidden
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController

class EpicModeSelectorItem(ModeSelectorLegacyItem):
    _VIEW_MODEL = ModeSelectorEpicModel
    _CARD_VISUAL_TYPE = ModeSelectorCardTypes.EPIC_BATTLE
    __epicController: Any
    @property
    def isVisible(self):
        ...
    @property
    def isSelectable(self):
        ...
    def handleInfoPageClick(self):
        ...
    def handleClick(self):
        ...
    def _getIsDisabled(self):
        ...
    def _onInitializing(self):
        ...
    def _onDisposing(self):
        ...
    def __onEpicUpdate(self, *_):
        ...
    def __onEventEnded(self):
        ...
    def _isInfoIconVisible(self):
        ...
    def __fillViewModel(self):
        ...
    @staticmethod
    def __resetViewModel(vm):
        ...
