# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/dialogs/dialog_template_focus.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.gen.view_models.views.dialogs.dialog_base_focus_view_model import DialogBaseFocusViewModel as DialogBaseFocusViewModel
from gui.impl.gen.view_models.views.dialogs.dialog_focus_view_model import DialogFocusViewModel as DialogFocusViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from typing import List as List, Optional as Optional, Union as Union, Dict as Dict
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel as DialogTemplateViewModel

class BaseFocusPresenter(ViewImpl):
    __slots__: tuple
    focusElementCount = 0
    def __init__(self, settings, *args, **kwargs):
        ...
    def updateFocusIndex(self, value):
        ...

class ButtonFocusingHandler(object):
    __slots__: tuple
    __dialogTemplateViewModel: Any
    def __init__(self, dialogTemplateViewModel):
        ...
    def updateFocusIndex(self, value):
        ...
    def dispose(self):
        ...
    @property
    def focusElementCount(self):
        ...

class DialogTemplateFocusingSystem(object):
    __slots__: tuple
    __dialogTemplateViewModel: Any
    __presenters: Any
    __currentFocusIndex: Any
    __buttonFocusing: Any
    __indexShifting: Any
    __maxIndex: Any
    __isStarted: Any
    def __init__(self, dialogTemplateViewModel):
        ...
    def start(self):
        ...
    def dispose(self):
        ...
    def addFocusPresenter(self, presenter):
        ...
    def setFocusingIndex(self, value):
        ...
    def __setFocus(self, presenter, globalIndex):
        ...
    def __tabPressHandler(self, args):
        ...
    def __next(self, backwards):
        ...

def clampFocusIndex(value, topLimit):
    ...
