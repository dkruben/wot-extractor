# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/tooltips/event_mission_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from halloween.gui.game_control.halloween_artefacts_controller import getBonusPriority as getBonusPriority
from halloween.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel as BonusItemViewModel
from halloween.gui.impl.gen.view_models.views.lobby.tooltips.mission_tooltip_view_model import MissionTooltipViewModel as MissionTooltipViewModel
from halloween.gui.impl.lobby.hw_helpers import getArtefactState as getArtefactState
from halloween.gui.impl.lobby.hw_helpers.bonuses_formatters import HalloweenBonusesAwardsComposer as HalloweenBonusesAwardsComposer, getImgName as getImgName, getHWMetaAwardFormatter as getHWMetaAwardFormatter
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from helpers import dependency as dependency
from halloween.gui.game_control.halloween_artefacts_controller import Artefact as Artefact

class MissionsTooltip(ViewImpl):
    __slots__: tuple
    _hwArtefactsCtrl: Any
    _hwController: Any
    _MAX_BONUSES_IN_VIEW = 5
    __selectedArtefactID: Any
    __isHangar: Any
    def __init__(self, selectedArtefactID, isHangar):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self):
        ...
