# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/shared/cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import inspect as inspect
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler as AbstractContextMenuHandler
from gui.impl import backport as backport
from gui.impl.gen import R as R

class CMLabel(object):
    INFORMATION = 'information'
    STATS = 'showVehicleStatistics'
    SELL = 'sell'
    REMOVE = 'remove'
    SALE_OPTION = 'saleOption'
    BUY = 'buy'
    BUY_MORE = 'buyMore'
    EXCHANGE = 'exchange'
    ADD_TO_COMPARE = 'addToCompare'
    SHOW_IN_HANGAR = 'showInHangar'
    PREVIEW = 'preview'
    RESTORE = 'restore'
    ACTIVATE = 'activate'
    PREVIEW_CUSTOMIZATION = 'previewCustomization'
    CONVERT_BLUEPRINT = 'convertBlueprint'
    CONVERT_BLUEPRINT_MAX = 'convertBlueprintMax'
    SHOW_BLUEPRINT = 'showBlueprint'
    NATION_CHANGE = 'nationChange'
    UPGRADE = 'upgrade'
    GO_TO_COLLECTION = 'goToCollection'
    DECONSTRUCT = 'deconstruct'

class StorageOptionCustomData(object):
    label: Any
    enabled: Any
    visible: Any
    isNew: Any
    textColor: Any
    labelCtx: Any
    def __init__(self, label, enabled=True, visible=True, isNew=False, textColor=None, labelCtx=None):
        ...
    def asDict(self):
        ...

class ContextMenu(AbstractContextMenuHandler):
    __handlerMethods: Any
    _id: Any
    def __init__(self, cmProxy=None, ctx=None):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _generateOptions(self, ctx=None):
        ...
    def _makeOption(self, label, data):
        ...
    def _getOptionCustomData(self, label):
        ...
    def _isVisible(self, label):
        ...

def _makeMenuLabel(label, data):
    ...
def option(order, label):
    ...
