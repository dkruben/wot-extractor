# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/battle_quest_awards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_quest_awards_model import BattleQuestAwardsModel as BattleQuestAwardsModel, BattleStatus as BattleStatus
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo as setEventInfo
from battle_royale.gui.impl.lobby.tooltips.proxy_currency_tooltip_view import ProxyCurrencyTooltipView as ProxyCurrencyTooltipView
from battle_royale.gui.impl.lobby.views.bonus_packer import getBonusPacker as getBonusPacker
from battle_royale.gui.sounds_constants import GENERAL_SOUND_SPACE as GENERAL_SOUND_SPACE
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.battle_pass.battle_pass_bonuses_packers import packBonusModelAndTooltipData as packBonusModelAndTooltipData, useBigAwardInjection as useBigAwardInjection
from gui.impl.gen import R as R
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses

class BattleQuestAwardsView(ViewImpl):
    _COMMON_SOUND_SPACE = GENERAL_SOUND_SPACE
    __slots__: tuple
    __tooltipData: Any
    _stage: Any
    def __init__(self, stage):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def updateModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onClose(self):
        ...
    def __onApprove(self):
        ...

class BattleQuestAwardsViewWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, stage, parent=None):
        ...

def awardsFactory(items, ctx=None):
    ...
