# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/dialogs/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from constants import ACCOUNT_KICK_REASONS as ACCOUNT_KICK_REASONS, IS_CHINA as IS_CHINA
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.locale.DIALOGS import DIALOGS as DIALOGS
from gui.impl import backport as backport
from gui.shared import events as events
from helpers import i18n as i18n, time_utils as time_utils
I18N_PRICE_KEY = '{0:>s}/messagePrice'
I18N_TITLE_KEY = '{0:>s}/title'
I18N_MESSAGE_KEY = '{0:>s}/message'
I18N_CANCEL_KEY = '{0:>s}/cancel'
I18N_SUBMIT_KEY = '{0:>s}/submit'

class DIALOG_BUTTON_ID(object):
    SUBMIT = 'submit'
    CLOSE = 'close'
    HYPERLINK = 'hyperLink'

class IDialogMeta(object):
    def getEventType(self):
        ...
    def getViewScopeType(self):
        ...

class ISimpleDialogButtonsMeta(object):
    def getLabels(self):
        ...

class ISimpleDialogMeta(IDialogMeta):
    def getTitle(self):
        ...
    def getMessage(self):
        ...
    def getButtonLabels(self):
        ...
    def getTimer(self):
        ...

class InfoDialogButtons(ISimpleDialogButtonsMeta):
    _close: Any
    def __init__(self, close):
        ...
    def getLabels(self):
        ...

class ConfirmDialogButtons(InfoDialogButtons):
    _submit: Any
    def __init__(self, submit, close):
        ...
    def getLabels(self):
        ...

class I18nInfoDialogButtons(ISimpleDialogButtonsMeta):
    _i18nKey: Any
    _buttonID: Any
    def __init__(self, i18nKey='common', buttonID=...):
        ...
    def getLabels(self):
        ...

class I18nConfirmDialogButtons(I18nInfoDialogButtons):
    _i18nKey: Any
    _focusedIndex: Any
    def __init__(self, i18nKey='common', focusedIndex=None):
        ...
    def getLabels(self):
        ...
    def __getButtonInfoObject(self, buttonID, label, focused):
        ...

class SimpleDialogMeta(ISimpleDialogMeta):
    _title: Any
    _message: Any
    _buttons: Any
    _timer: Any
    _scope: Any
    def __init__(self, title=None, message=None, buttons=None, timer=0, scope=...):
        ...
    def getTitle(self):
        ...
    def getMessage(self):
        ...
    def getButtonLabels(self):
        ...
    def getTimer(self):
        ...
    def getEventType(self):
        ...
    def getCallbackWrapper(self, callback):
        ...
    def getViewScopeType(self):
        ...

class I18nDialogMeta(SimpleDialogMeta):
    _key: Any
    _titleCtx: Any
    _messageCtx: Any
    _buttons: Any
    _meta: Any
    def __init__(self, key, buttons, titleCtx=None, messageCtx=None, meta=None, scope=...):
        ...
    def getTitle(self):
        ...
    def getMessage(self):
        ...
    def getButtonLabels(self):
        ...
    def getTimer(self):
        ...
    def getKey(self):
        ...
    def _makeString(self, key, ctx):
        ...
    def getViewScopeType(self):
        ...

class I18nInfoDialogMeta(I18nDialogMeta):
    def __init__(self, key, titleCtx=None, messageCtx=None, meta=None, scope=...):
        ...

class I18nConfirmDialogMeta(I18nDialogMeta):
    def __init__(self, key, titleCtx=None, messageCtx=None, meta=None, focusedID=None, scope=...):
        ...

class IconDialogMeta(I18nConfirmDialogMeta):
    def getEventType(self):
        ...
    def getIcon(self):
        ...

class IconPriceDialogMeta(IconDialogMeta):
    _operationPrice: Any
    _action: Any
    _item: Any
    def __init__(self, key, titleCtx=None, messageCtx=None, meta=None, focusedID=None):
        ...
    def __calcMessagePrice(self):
        ...
    def __calcAction(self):
        ...
    def getEventType(self):
        ...
    def getMessagePrice(self):
        ...
    def getAction(self):
        ...

class PMConfirmationDialogMeta(IconDialogMeta):
    def getEventType(self):
        ...

class HtmlMessageDialogMeta(SimpleDialogMeta):
    _path: Any
    _key: Any
    _ctx: Any
    _sourceKey: Any
    def __init__(self, path, key, ctx=None, scope=..., sourceKey='text'):
        ...
    def getTitle(self):
        ...
    def getMessage(self):
        ...

class HtmlMessageLocalDialogMeta(HtmlMessageDialogMeta):
    def __init__(self, path, key, ctx=None):
        ...

class DisconnectMeta(I18nInfoDialogMeta):
    reason: Any
    kickReasonType: Any
    expiryTime: Any
    def __init__(self, reason=None, kickReasonType=..., expiryTime=None):
        ...
    def getCallbackWrapper(self, callback):
        ...
    def getMessage(self):
        ...

class TimerConfirmDialogMeta(I18nConfirmDialogMeta):
    _timer: Any
    def __init__(self, key, titleCtx=None, messageCtx=None, meta=None, focusedID=None, timer=0):
        ...

class CheckBoxDialogMeta(I18nConfirmDialogMeta):
    __checkBoxSelected: Any
    def __init__(self, key, titleCtx=None, messageCtx=None, meta=None, focusedID=None, scope=..., selected=False):
        ...
    def getEventType(self):
        ...
    def getButtonsSubmitCancel(self):
        ...
    def getCheckBoxButtonLabel(self):
        ...
    def getCheckBoxSelected(self):
        ...
    def getViewScopeType(self):
        ...

def _getDialogStr(i18nKey):
    ...
