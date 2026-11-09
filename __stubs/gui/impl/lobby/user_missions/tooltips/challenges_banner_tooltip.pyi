# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/tooltips/challenges_banner_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.challenges.challenges_helpers import TIME_BEFORE_END_OF_EXPIRATION as TIME_BEFORE_END_OF_EXPIRATION
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.tooltips.challenges_banner_tooltip_model import ChallengesBannerTooltipModel as ChallengesBannerTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.missions.packers.events import ChallengeMissionUIDataPacker as ChallengeMissionUIDataPacker
from helpers import dependency as dependency
from skeletons.gui.challenges import IChallengesController as IChallengesController
from skeletons.gui.server_events import IEventsCache as IEventsCache

class ChallengesBannerTooltip(ViewImpl):
    __challenges: Any
    __eventsCache: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __fillInfo(self):
        ...
    def __getTimer(self, challenge):
        ...
