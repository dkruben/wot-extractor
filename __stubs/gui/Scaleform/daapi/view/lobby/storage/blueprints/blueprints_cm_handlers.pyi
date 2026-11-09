# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/blueprints/blueprints_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from wg_async import wg_await as wg_await, wg_async as wg_async
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.impl.dialogs import dialogs as dialogs
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import ContextMenu as ContextMenu, option as option, CMLabel as CMLabel
from gui.shared.gui_items.items_actions import factory as factory
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from skeletons.gui.shared import IItemsCache as IItemsCache

class BlueprintsCMHandler(ContextMenu):
    __sqGen: Any
    __itemsCache: Any
    # decorador original: @option(...)
    # decorador original: @wg_async
    def convertBlueprintFragment(self):
        ...
    # decorador original: @option(...)
    # decorador original: @wg_async
    def convertMaxBlueprintFragments(self):
        ...
    # decorador original: @option(...)
    def showBlueprintView(self):
        ...
    def _getOptionCustomData(self, label):
        ...
    def __getMaxFragmentCount(self):
        ...
