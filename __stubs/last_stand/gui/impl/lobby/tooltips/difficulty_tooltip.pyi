# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/difficulty_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from last_stand.gui.impl.gen.view_models.views.lobby.tooltips.difficulty_tooltip_view_model import DifficultyTooltipViewModel as DifficultyTooltipViewModel
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.difficulty_item_model import StateEnum as StateEnum
from last_stand.gui.impl.gen.view_models.views.lobby.tooltips.difficulty_wave_rewards_model import DifficultyWaveRewardsModel as DifficultyWaveRewardsModel
from last_stand.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel as BonusItemViewModel
from last_stand.gui.impl.lobby.ls_helpers.bonuses_formatters import LSBonusesAwardsComposer as LSBonusesAwardsComposer, getImgName as getImgName, getLSMetaAwardFormatter as getLSMetaAwardFormatter
from last_stand.gui.game_control.ls_artefacts_controller import getBonusPriority as getBonusPriority
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from helpers import dependency as dependency
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand.skeletons.ls_difficulty_missions_controller import ILSDifficultyMissionsController as ILSDifficultyMissionsController
from last_stand_common.last_stand_constants import DEFAULT_DIFFICULTY_MODIFIER as DEFAULT_DIFFICULTY_MODIFIER

class DifficultyTooltipView(ViewImpl):
    __slots__: tuple
    lsCtrl: Any
    lsMissionsCtrl: Any
    _MAX_BONUSES_IN_VIEW = 4
    __isHangar: Any
    __difficulty: Any
    __completedMissions: Any
    __state: Any
    __isLocked: Any
    def __init__(self, isHangar, difficulty, completedMissions, state=..., isLocked=True):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
