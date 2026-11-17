# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/fort_rush_progression_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from fort_rush.gui.impl.lobby.presenters.fort_rush_progression_presenter import FortRushProgressionPresenter as FortRushProgressionPresenter
from fort_rush.gui.sounds.sound_constants import FORT_RUSH_PROGRESSION_SOUND_SPACE as FORT_RUSH_PROGRESSION_SOUND_SPACE
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from fort_rush.gui.impl.gen.view_models.views.progression.progression_view_model import ProgressionViewModel as ProgressionViewModel

class FortRushProgressionView(ViewImpl):
    _COMMON_SOUND_SPACE = FORT_RUSH_PROGRESSION_SOUND_SPACE
    __presenter: Any
    def __init__(self, layoutId):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
