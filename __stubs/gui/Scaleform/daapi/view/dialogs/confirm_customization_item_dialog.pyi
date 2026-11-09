# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/dialogs/confirm_customization_item_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.utils import old_div as old_div
from debug_utils import LOG_ERROR as LOG_ERROR
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.meta.ConfirmItemWindowMeta import ConfirmItemWindowMeta as ConfirmItemWindowMeta
from gui.shared.formatters import getMoneyVO as getMoneyVO
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.Scaleform.locale.VEHICLE_CUSTOMIZATION import VEHICLE_CUSTOMIZATION as VEHICLE_CUSTOMIZATION

class CustomizationItemIconWidth(object):
    SMALL = 59
    MEDIUM = 118
    BIG = 161

class ConfirmCustomizationItemDialog(ConfirmItemWindowMeta):
    meta: Any
    handler: Any
    def __init__(self, meta, handler, **kwargs):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def onWindowClose(self):
        ...
    def submit(self, count, currency):
        ...
    def proceedSubmit(self, count, currency):
        ...
    def _callHandler(self, success, *kargs):
        ...
    def _prepareAndSendData(self):
        ...
    def __onUpdate(self, *_):
        ...
