# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mode_selector/mode_selector_data_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import defaultdict as defaultdict, OrderedDict as OrderedDict
import typing as typing
from Event import SafeEvent as SafeEvent
from gui.Scaleform.daapi.view.lobby.header import battle_selector_items as battle_selector_items
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_columns import ModeSelectorColumns as ModeSelectorColumns
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem as ModeSelectorLegacyItem
from gui.impl.lobby.mode_selector.items.epic_mode_selector_item import EpicModeSelectorItem as EpicModeSelectorItem
from gui.impl.lobby.mode_selector.items.mapbox_mode_selector_item import MapboxModeSelectorItem as MapboxModeSelectorItem
from gui.impl.lobby.mode_selector.items.random_mode_selector_item import RandomModeSelectorItem as RandomModeSelectorItem
from gui.impl.lobby.mode_selector.items.ranked_mode_selector_item import RankedModeSelectorItem as RankedModeSelectorItem
from gui.impl.lobby.mode_selector.items.spec_mode_selector_item import SpecModeSelectorItem as SpecModeSelectorItem
from gui.impl.lobby.mode_selector.items.strongholds_mode_selector_item import StrongholdsModeSelectorItem as StrongholdsModeSelectorItem
from gui.impl.lobby.mode_selector.items.trainings_mode_selector_item import TrainingsModeSelectorItem as TrainingsModeSelectorItem
from gui.impl.lobby.mode_selector.items.winback_mode_selector_item import WinbackModeSelectorItem as WinbackModeSelectorItem
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.shared.system_factory import registerModeSelectorItem as registerModeSelectorItem, collectModeSelectorItem as collectModeSelectorItem
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.Scaleform.daapi.view.lobby.header.battle_selector_items import SelectorItem as SelectorItem
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorItem as ModeSelectorItem
_logger: Any

class ModeSelectorDataProvider(IGlobalListener):
    __slots__: tuple
    __lobbyContext: Any
    MAX_COLUMN_SIZE = 6
    onListChanged: Any
    _items: Any
    def __init__(self):
        ...
    @property
    def itemList(self):
        ...
    @property
    def isDemonstrator(self):
        ...
    @property
    def hasNewIndicator(self):
        ...
    @property
    def isDemoButtonEnabled(self):
        ...
    @staticmethod
    def select(modeName):
        ...
    def dispose(self):
        ...
    def getItemByIndex(self, index):
        ...
    def forceRefresh(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def __onServerSettingsChange(self, _):
        ...
    def _onCardChangeHandler(self, *args, **kwargs):
        ...
    def _clearItems(self):
        ...
    def _clearItem(self, item):
        ...
    def _initializeModeSelectorItems(self):
        ...
    @staticmethod
    def _getModeSelectorLegacyItem(modeName, selectorItem):
        ...
    def _getSelectedItem(self):
        ...
    def _updateItems(self, selected=None):
        ...
    def _updateSelection(self, selected=None):
        ...
    def _updateItemsPosition(self):
        ...
    def __createItems(self, items):
        ...
    def __initializeItem(self, item):
        ...
    @staticmethod
    def __getItems():
        ...
