# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/challenges/awards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.challenges.challenges_decorators import createTooltipContentDecorator as createTooltipContentDecorator
from gui.challenges.challenges_award_manager import AwardsManager as AwardsManager
from gui.challenges.challenges_bonuses_packers import getChallengesBonusPacker as getChallengesBonusPacker
from gui.challenges.sounds import CHALLENGE_AWARDS_SOUND_SPACE as CHALLENGE_AWARDS_SOUND_SPACE
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.challenges.awards_view_model import AwardsViewModel as AwardsViewModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared.event_dispatcher import selectVehicleInHangar as selectVehicleInHangar
from gui.server_events.events_dispatcher import showChallenges as showChallenges
from helpers import dependency as dependency
from skeletons.gui.challenges import IChallengesController as IChallengesController
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData

class ChallengesAwardsView(ViewImpl):
    _COMMON_SOUND_SPACE = CHALLENGE_AWARDS_SOUND_SPACE
    __challenges: Any
    __tooltipItems: Any
    __challenge: Any
    __isCompleted: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    # decorador original: @createTooltipContentDecorator(...)
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def _onLoading(self, challenge, rewardsData, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onClose(self):
        ...
    # decorador original: @args2params(...)
    def __onHangar(self, vehicleCD):
        ...
    def __onChallenges(self):
        ...
    def __setRewards(self, rewardsData, model):
        ...

class ChallengesAwardsScreen(LobbyNotificationWindow):
    def __init__(self, challenge, rewards):
        ...
