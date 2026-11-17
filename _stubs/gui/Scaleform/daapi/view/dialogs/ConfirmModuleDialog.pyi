# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/dialogs/ConfirmModuleDialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from PlayerEvents import g_playerEvents as g_playerEvents
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.daapi.view.meta.ConfirmItemWindowMeta import ConfirmItemWindowMeta as ConfirmItemWindowMeta
from gui.Scaleform.genConsts.CONFIRM_DIALOG_ALIASES import CONFIRM_DIALOG_ALIASES as CONFIRM_DIALOG_ALIASES
from gui.shared.formatters import getMoneyVO as getMoneyVO
from gui.shared.utils import EXTRA_MODULE_INFO as EXTRA_MODULE_INFO, FIELD_HIGHLIGHT_TYPE as FIELD_HIGHLIGHT_TYPE
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class ConfirmModuleDialog(ConfirmItemWindowMeta):
    itemsCache: Any
    meta: Any
    handler: Any
    _data: Any
    def __init__(self, meta, handler, **kwargs):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _callHandler(self, success, *kargs):
        ...
    def _onShopResync(self):
        ...
    def _prepareAndSendData(self):
        ...
    @staticmethod
    def __getIcon(item):
        ...
    def onWindowClose(self):
        ...
    def submit(self, count, currency):
        ...
