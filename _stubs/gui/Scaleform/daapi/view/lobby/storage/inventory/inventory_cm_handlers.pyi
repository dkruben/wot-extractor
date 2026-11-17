# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inventory/inventory_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from gui import shop as shop
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import ContextMenu as ContextMenu, option as option, CMLabel as CMLabel
from gui.Scaleform.framework.managers.context_menu import CM_BUY_COLOR as CM_BUY_COLOR
from gui.shared import event_dispatcher as shared_events
from gui.shared.event_dispatcher import showBattleBoosterSellDialog as showBattleBoosterSellDialog
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from items import UNDEFINED_ITEM_CD as UNDEFINED_ITEM_CD
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.shared.event_dispatcher import showSellDialog as showSellDialog
_SOURCE = shop.Source.EXTERNAL
_ORIGIN = shop.Origin.STORAGE

class ModulesShellsCMHandler(ContextMenu):
    __sqGen: Any
    _itemsCache: Any
    # decorador original: @option(...)
    def showInfo(self):
        ...
    # decorador original: @option(...)
    def sell(self):
        ...
    def _getOptionCustomData(self, label):
        ...

class ModulesShellsNoSaleCMHandler(ContextMenu):
    _sqGen: Any
    _itemsCache: Any
    # decorador original: @option(...)
    def showInfo(self):
        ...
    def _getOptionCustomData(self, label):
        ...

class _ArmingCMHandler(ContextMenu):
    _sqGen: Any
    _itemsCache: Any
    # decorador original: @option(...)
    def showInfo(self):
        ...
    # decorador original: @option(...)
    def sell(self):
        ...
    def buy(self):
        ...
    def _getHighlightedLabels(self):
        ...
    def _generateOptions(self, ctx=None):
        ...
    def _getOptionCustomData(self, label):
        ...

class EquipmentCMHandler(_ArmingCMHandler):
    _enabled: Any
    # decorador original: @option(...)
    def buy(self):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _getHighlightedLabels(self):
        ...
    def _getOptionCustomData(self, label):
        ...

class OptionalDeviceCMHandler(_ArmingCMHandler):
    __lobbyContext: Any
    # decorador original: @option(...)
    def buy(self):
        ...
    # decorador original: @option(...)
    def upgrade(self):
        ...
    def _generateOptions(self, ctx=None):
        ...
    def _getHighlightedLabels(self):
        ...

class OptionalModernizedDeviceCMHandler(OptionalDeviceCMHandler):
    _itemsCache: Any
    # decorador original: @option(...)
    def sell(self):
        ...
    def _getOptionCustomData(self, label):
        ...

class BattleBoostersCMHandler(ContextMenu):
    __sqGen: Any
    _itemsCache: Any
    _enabled: Any
    def _initFlashValues(self, ctx):
        ...
    # decorador original: @option(...)
    def showInfo(self):
        ...
    # decorador original: @option(...)
    def sell(self):
        ...
    # decorador original: @option(...)
    def buy(self):
        ...
    def _getOptionCustomData(self, label):
        ...
    def _isVisible(self, label):
        ...

class DemountKitsCMHandler(ContextMenu):
    __sqGen: Any
    # decorador original: @option(...)
    def showInfo(self):
        ...
    # decorador original: @option(...)
    # decorador original: @adisp_process
    def sell(self):
        ...
    # decorador original: @option(...)
    def buy(self):
        ...
    def _getOptionCustomData(self, label):
        ...

class RecertificationFormsCMHandler(ContextMenu):
    __sqGen: Any
    # decorador original: @option(...)
    def showInfo(self):
        ...
    # decorador original: @option(...)
    # decorador original: @adisp_process
    def sell(self):
        ...
    # decorador original: @option(...)
    def buy(self):
        ...
    def _getOptionCustomData(self, label):
        ...

class MentoringLicensesCMHandler(ContextMenu):
    __sqGen: Any
    # decorador original: @option(...)
    def showInfo(self):
        ...
    # decorador original: @option(...)
    # decorador original: @adisp_process
    def sell(self):
        ...
    # decorador original: @option(...)
    def buy(self):
        ...
    def _getOptionCustomData(self, label):
        ...
