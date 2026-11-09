# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/dialogs/mono_dialog_template_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, Map as Map, ViewModel as ViewModel
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.mono_dialog_template_button_model import MonoDialogTemplateButtonModel as MonoDialogTemplateButtonModel

class MonoDialogTemplateViewModel(ViewModel):
    __slots__: tuple
    ACTION_ESCAPE = 'escape'
    ACTION_CLOSE = 'close'
    ACTION_SPACE = 'space'
    ACTION_CONFIRM = 'confirm'
    ACTION_CANCEL = 'cancel'
    ACTION_SECONDARY = 'secondary'
    onAction: Any
    def __init__(self, properties=5, commands=1):
        ...
    def getButtons(self):
        ...
    def setButtons(self, value):
        ...
    @staticmethod
    def getButtonsType():
        ...
    def getContent(self):
        ...
    def setContent(self, value):
        ...
    @staticmethod
    def getContentType():
        ...
    def getResources(self):
        ...
    def setResources(self, value):
        ...
    @staticmethod
    def getResourcesType():
        ...
    def getBackgroundImage(self):
        ...
    def setBackgroundImage(self, value):
        ...
    def getDimmerAlpha(self):
        ...
    def setDimmerAlpha(self, value):
        ...
    def _initialize(self):
        ...
