# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/premacc/dashboard/parent_control_info_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.premacc.dashboard.parent_control_info_popover_model import ParentControlInfoPopoverModel as ParentControlInfoPopoverModel
from gui.impl.pub import PopOverViewImpl as PopOverViewImpl
from helpers import dependency as dependency
from skeletons.gui.game_control import IExternalLinksController as IExternalLinksController
_PARENT_CONTROL_HELP_URL = 'parentControlHelpURL'

class ParentControlInfoPopoverContent(PopOverViewImpl):
    __slots__: tuple
    __links: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    # decorador original: @adisp_process
    def __onLinkClicked(self):
        ...
