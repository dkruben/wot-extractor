# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mode_selector/items/winback_mode_selector_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from account_helpers.AccountSettings import Winback as Winback, AccountSettings as AccountSettings
from gui.Scaleform.daapi.view.lobby.header import battle_selector_items as battle_selector_items
from gui.impl.gen import R as R
from gui.impl.lobby.mode_selector.items.random_mode_selector_item import RandomModeSelectorItem as RandomModeSelectorItem
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.shared import g_eventBus as g_eventBus
from gui.shared.events import ModeSelectorPopoverEvent as ModeSelectorPopoverEvent
from gui.winback.winback_helpers import getWinbackSetting as getWinbackSetting

class WinbackModeSelectorItem(RandomModeSelectorItem):
    @property
    def modeName(self):
        ...
    def isSelected(self):
        ...
    def getViewModel(self):
        ...
    def _onInitializing(self):
        ...
    def _onDisposing(self):
        ...
    def _isInfoIconVisible(self):
        ...
    def __onAccountSettingsChanging(self, key, _):
        ...
    def __onModeSelectorPopoverEvent(self, event):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillCardModel(self, model=None):
        ...
