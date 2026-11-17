# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/reward_path_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from frameworks.wulf import ViewSettings as ViewSettings
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from last_stand.gui.impl.gen.view_models.views.lobby.tooltips.reward_path_tooltip_view_model import RewardPathTooltipViewModel as RewardPathTooltipViewModel
from last_stand.gui.impl.lobby.ls_helpers import fillRewardPathWidgetViewModel as fillRewardPathWidgetViewModel, fillRewards as fillRewards
from last_stand.skeletons.ls_artefacts_controller import ILSArtefactsController as ILSArtefactsController
from last_stand.gui.game_control.ls_artefacts_controller import Artefact as Artefact

class RewardPathTooltip(ViewImpl):
    lsArtefactsCtrl: Any
    _MAX_BONUSES_IN_VIEW = 6
    __idGen: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
