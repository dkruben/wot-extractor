# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mode_selector/items/mapbox_mode_selector_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.mode_performance_model import PerformanceRiskEnum as PerformanceRiskEnum
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_card_types import ModeSelectorCardTypes as ModeSelectorCardTypes
from gui.impl.lobby.mode_selector.items import setBattlePassState as setBattlePassState
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem as ModeSelectorLegacyItem, formatSeasonLeftTime as formatSeasonLeftTime
from gui.impl.lobby.mode_selector.items.items_constants import ModeSelectorRewardID as ModeSelectorRewardID
from gui.shared.event_dispatcher import showMapboxIntro as showMapboxIntro
from gui.shared.utils.graphics import isLowPreset as isLowPreset
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IMapboxController as IMapboxController
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import ModeSelectorNormalCardModel as ModeSelectorNormalCardModel

class MapboxModeSelectorItem(ModeSelectorLegacyItem):
    __slots__: tuple
    _CARD_VISUAL_TYPE = ModeSelectorCardTypes.MAPBOX
    __mapboxCtrl: Any
    def handleClick(self):
        ...
    def handleInfoPageClick(self):
        ...
    @property
    def calendarTooltipText(self):
        ...
    @property
    def isSelectable(self):
        ...
    def _isInfoIconVisible(self):
        ...
    def _isNeedToHideCard(self):
        ...
    def _getIsDisabled(self):
        ...
    def _onInitializing(self):
        ...
    def _onDisposing(self):
        ...
    def __onPrimeTimeStatusUpdate(self, *_):
        ...
    def __fillViewModel(self):
        ...
    def __getNotActiveStatus(self):
        ...
    def __getCurrentSeasonDate(self):
        ...
    def __getDate(self, date):
        ...
