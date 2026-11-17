# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/dialogs/dialog_template_button.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport.backport_tooltip import createBackportTooltipContent as createBackportTooltipContent
from gui.impl.dialogs.dialog_template_tooltip import DialogTemplateTooltip as DialogTemplateTooltip
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.dialog_template_button_view_model import ButtonType as ButtonType
from gui.impl.gen.view_models.views.dialogs.dialog_template_button_view_model import DialogTemplateButtonViewModel as DialogTemplateButtonViewModel
from gui.impl.gen.view_models.views.dialogs.custom_sound_button_model import CustomSoundButtonModel as CustomSoundButtonModel
from gui.impl.gen.view_models.views.dialogs.mono_dialog_template_button_model import MonoDialogTemplateButtonModel as MonoDialogTemplateButtonModel, ButtonType as MonoButtonType
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Callable as Callable, Optional as Optional
from frameworks.wulf import View as View
from gui.shared.money import Money as Money

class ButtonPresenter(object):
    __slots__: tuple
    _viewModel: Any
    __tooltip: Any
    def __init__(self, label, buttonID, buttonType=..., tooltipFactory=None, isBackportTooltip=False, isDisabled=False, *args, **kwargs):
        ...
    @property
    def buttonID(self):
        ...
    @property
    def label(self):
        ...
    @label.setter
    def label(self, value):
        ...
    @property
    def buttonType(self):
        ...
    @buttonType.setter
    def buttonType(self, value):
        ...
    @property
    def tooltipFactory(self):
        ...
    @tooltipFactory.setter
    def tooltipFactory(self, value):
        ...
    @property
    def isBackportTooltip(self):
        ...
    @isBackportTooltip.setter
    def isBackportTooltip(self, value):
        ...
    @property
    def isDisabled(self):
        ...
    @isDisabled.setter
    def isDisabled(self, value):
        ...
    @property
    def viewModel(self):
        ...
    def initialize(self):
        ...
    def dispose(self):
        ...
    def _getViewModel(self):
        ...

class CancelButton(ButtonPresenter):
    __slots__: tuple
    def __init__(self, label=..., buttonID=..., buttonType=..., tooltipFactory=None, isBackportTooltip=False, isDisabled=False):
        ...

class ConfirmButton(ButtonPresenter):
    __slots__: tuple
    def __init__(self, label=..., buttonID=..., buttonType=..., tooltipFactory=None, isBackportTooltip=False, isDisabled=False):
        ...

class CustomSoundButtonPresenter(ButtonPresenter):
    def __init__(self, label, buttonID, buttonType, tooltipFactory, isBackportTooltip, isDisabled, soundClick):
        ...
    @property
    def viewModel(self):
        ...
    def _getViewModel(self):
        ...

class CheckMoneyButton(ButtonPresenter):
    __slots__: tuple
    _itemsCache: Any
    __money: Any
    isDisabled: Any
    tooltipFactory: Any
    def __init__(self, money, label=..., buttonID=..., buttonType=..., isDisabled=False):
        ...
    @property
    def money(self):
        ...
    @money.setter
    def money(self, value):
        ...
    @property
    def shortage(self):
        ...
    def initialize(self):
        ...
    def dispose(self):
        ...
    def _moneyChangeHandler(self, *_):
        ...
    def _updateButton(self):
        ...
    def __notEnoughMoneyTooltipFactory(self):
        ...

class MonoButtonTemplate(object):
    __slots__: tuple
    _viewModel: Any
    def __init__(self, action, label, soundTarget='Button', buttonType=..., isDisabled=False):
        ...
    @property
    def viewModel(self):
        ...
    def _getViewModel(self):
        ...

def getConfirmButton(presenter=..., label=..., buttonID=..., buttonType=..., tooltipFactory=None, isBackportTooltip=False, isDisabled=False, *args, **kwargs):
    ...
