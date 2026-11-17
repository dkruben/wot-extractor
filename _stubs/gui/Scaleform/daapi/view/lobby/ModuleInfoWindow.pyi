# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/ModuleInfoWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.meta.ModuleInfoMeta import ModuleInfoMeta as ModuleInfoMeta
from gui.Scaleform.framework.entities.View import View as View
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.tooltips import contexts as contexts
from gui.shared.tooltips.crew_book import CrewBookTooltipDataBlock as CrewBookTooltipDataBlock
from gui.shared.tooltips.module import ModuleBlockTooltipData as ModuleBlockTooltipData
from gui.shared.tooltips.shell import ShellBlockToolTipData as ShellBlockToolTipData
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache

class ModuleInfoWindow(ModuleInfoMeta):
    itemsCache: Any
    lobbyContext: Any
    _settingsCore: Any
    moduleCompactDescr: Any
    __vehicleDescr: Any
    def __init__(self, ctx=None):
        ...
    def onCancelClick(self):
        ...
    def onWindowClose(self):
        ...
    def _populate(self):
        ...
    def _updateModuleInfo(self, data):
        ...
