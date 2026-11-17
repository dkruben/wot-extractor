# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/dialogs/builders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from collections import namedtuple as namedtuple
import logging as logging
from typing import Iterable as Iterable, Any as Any, Optional as Optional, TYPE_CHECKING as TYPE_CHECKING, Dict as Dict
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl.lobby.dialogs.contents.checkbox_content import CheckBoxDialogContent as CheckBoxDialogContent
from gui.impl.pub.simple_dialog_window import SimpleDialogWindow as SimpleDialogWindow
from gui.impl.pub.pure_dialog_window import PureDialogWindow as PureDialogWindow
from gui.impl.gen import R as R
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons, DialogFlags as DialogFlags
from gui.impl.lobby.dialogs.contents.common_balance_content import CommonBalanceContent as CommonBalanceContent
from gui.impl.gen.view_models.constants.dialog_presets import DialogPresets as DialogPresets
from gui.impl.gen.view_models.common.format_string_arg_model import FormatStringArgModel as FormatStringArgModel
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from frameworks.wulf import PyResAccessor as PyResAccessor
_logger: _Any
_MessageArgs: _Any
_DialogButton: _Any

class PureDialogBuilder(object):
    __appLoader: _Any
    __slots__: tuple
    _windowClass: _Any
    __title: _Any
    __formattedTitle: _Any
    __titleArgs: _Any
    __buttons: _Any
    __icon: _Any
    __backImg: _Any
    __preset: _Any
    __flags: _Any
    __showBalance: _Any
    __checkboxLabel: _Any
    __checkboxCheckedByDefault: _Any
    def __init__(self):
        ...
    def build(self, parent=None):
        ...
    def buildInLobby(self, parent=None):
        ...
    def setFormattedTitle(self, formattedTitle):
        ...
    def setTitle(self, title):
        ...
    def setCheckboxLabel(self, checkboxLabel):
        ...
    def setCheckboxDefaultValue(self, value):
        ...
    def setTitleArgs(self, args=None, fmtArgs=None, namedFmtArgs=True):
        ...
    def addButton(self, name, label, isFocused, soundDown=None, rawLabel=''):
        ...
    def setIcon(self, icon):
        ...
    def setBackImg(self, image):
        ...
    def setPreset(self, preset):
        ...
    def setFlags(self, flags):
        ...
    def setShowBalance(self, showBalance):
        ...

class SimpleDialogBuilder(PureDialogBuilder):
    __slots__: tuple
    _windowClass: _Any
    __message: _Any
    __formattedMessage: _Any
    __messageArgs: _Any
    def __init__(self):
        ...
    def build(self, parent=None):
        ...
    def setFormattedMessage(self, formattedMessage):
        ...
    def setMessage(self, message):
        ...
    def setMessageArgs(self, args=None, fmtArgs=None, namedFmtArgs=True):
        ...

class FormattedSimpleDialogBuilder(SimpleDialogBuilder):
    _DIALOG_PRESETS: tuple
    def setMessagesAndButtons(self, preset, title, message, buttons, focusedButton=None, btnDownSounds=None):
        ...

class ResSimpleDialogBuilder(SimpleDialogBuilder):
    def setMessagesAndButtons(self, message, buttons=..., focused=..., btnDownSounds=None):
        ...

class ResPureDialogBuilder(PureDialogBuilder):
    def setMessagesAndButtons(self, message, buttons=..., focused=..., btnDownSounds=None):
        ...

class InfoDialogBuilder(ResSimpleDialogBuilder):
    def __init__(self):
        ...

class WarningDialogBuilder(ResSimpleDialogBuilder):
    def __init__(self):
        ...

class ErrorDialogBuilder(ResSimpleDialogBuilder):
    def __init__(self):
        ...

def _makeMessageArgs(args=None, fmtArgs=None, namedFmtArgs=None):
    ...
def _setupButtonsBasedOnRes(obj, message, buttons=..., focused=..., btnDownSounds=None):
    ...
