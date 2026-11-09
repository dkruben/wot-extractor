# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/help_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.help_view_model import HelpViewModel as HelpViewModel
from gui.impl.gen.view_models.views.lobby.crew.help_slide_view_model import HelpSlideViewModel as HelpSlideViewModel
from gui.impl.gen.view_models.views.lobby.crew.help_slide_section_view_model import HelpSlideSectionViewModel as HelpSlideSectionViewModel, SlideSectionSize as SlideSectionSize
from gui.impl.auxiliary.crew_help_config_reader import getHelpViewConfig as getHelpViewConfig
from gui.impl.pub import WindowImpl as WindowImpl
from .base_crew_view import BaseCrewSubView as BaseCrewSubView
SLIDE_SIZES: dict

class HelpView(BaseCrewSubView):
    __slots__: tuple
    __navigateFrom: Any
    def __init__(self, layoutID=..., navigateFrom=None):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillModel(self):
        ...
    def _onViewClose(self):
        ...

class HelpViewWindow(WindowImpl):
    def __init__(self, navigateFrom=None, parent=None):
        ...
