# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/dialogs/dialog_template_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.gen.view_models.views.dialogs.dialog_template_generic_tooltip_view_model import TooltipType as TooltipType
from typing import Callable as Callable, Optional as Optional
from frameworks.wulf import View as View
from gui.impl.gen.view_models.views.dialogs.dialog_template_generic_tooltip_view_model import DialogTemplateGenericTooltipViewModel as DialogTemplateGenericTooltipViewModel

class DialogTemplateTooltip(object):
    __slots__: tuple
    __viewModel: Any
    __tooltipFactory: Any
    __isBackportTooltip: Any
    def __init__(self, tooltipFactory=None, isBackportTooltip=False, viewModel=None):
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
    def initialize(self, viewModel):
        ...
    def dispose(self):
        ...
    def __updateTooltipType(self):
        ...
