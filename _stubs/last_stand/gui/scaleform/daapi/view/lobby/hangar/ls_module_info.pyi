# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/lobby/hangar/ls_module_info.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.framework.entities.View import View as View
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.shared.tooltips import contexts as contexts
from last_stand.gui.scaleform.daapi.view.tooltips.event import EventModuleBlockTooltipData as EventModuleBlockTooltipData
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.Scaleform.daapi.view.lobby.ModuleInfoWindow import ModuleInfoWindow as ModuleInfoWindow
from gui.impl import backport as backport
from gui.impl.gen import R as R

class LSModuleInfoWindow(ModuleInfoWindow):
    itemsCache: Any
    __vehicleDescr: Any
    def __init__(self, ctx=None):
        ...
    def _populate(self):
        ...
