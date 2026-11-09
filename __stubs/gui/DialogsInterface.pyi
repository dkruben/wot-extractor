# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/DialogsInterface.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import ACCOUNT_KICK_REASONS as ACCOUNT_KICK_REASONS
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.view.dialogs import I18nInfoDialogMeta as I18nInfoDialogMeta, I18nConfirmDialogMeta as I18nConfirmDialogMeta, DisconnectMeta as DisconnectMeta, CheckBoxDialogMeta as CheckBoxDialogMeta
from gui.shared import events as events, g_eventBus as g_eventBus
from gui.shared.utils import decorators as decorators
__ifDisconnectDialogShown = False

class _DialogCallbackWrapper(object):
    __cb: Any
    def __init__(self, cb):
        ...
    def __call__(self, result):
        ...

# decorador original: @decorators.adisp_async
def showDialog(meta, callback, parent=None):
    ...
# decorador original: @decorators.adisp_async
def showI18nInfoDialog(i18nKey, callback, meta=None):
    ...
# decorador original: @decorators.adisp_async
def showI18nConfirmDialog(i18nKey, callback, ctx=None, meta=None, focusedID=None):
    ...
# decorador original: @decorators.adisp_async
def showI18nCheckBoxDialog(i18nKey, callback, meta=None, focusedID=None):
    ...
def showDisconnect(reason=None, kickReasonType=..., expiryTime=None):
    ...
