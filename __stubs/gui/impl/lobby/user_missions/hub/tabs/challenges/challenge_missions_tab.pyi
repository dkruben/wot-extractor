# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hub/tabs/challenges/challenge_missions_tab.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers.AccountSettings import ChallengesMissions as ChallengesMissions
from challenges_common import ChallengeDifficulties as ChallengeDifficulties, ChallengeMainRewardTypes as ChallengeMainRewardTypes
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import getVehicleCDForStyle as getVehicleCDForStyle
from gui.challenges.challenges_decorators import createTooltipContentDecorator as createTooltipContentDecorator
from gui.challenges.challenges_helpers import getSettings as getSettings, setSettings as setSettings, setVisitedChallenge as setVisitedChallenge
from gui.customization.shared import getPurchaseGoldForCredits as getPurchaseGoldForCredits
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.customization.attachments_preview.attachments_preview_model import AttachmentsPreviewFeature as AttachmentsPreviewFeature
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.challenge_missions.challenge_missions import ChallengeMissions as ChallengeMissions
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.challenge_missions.challenges_pack import ChallengesPack as ChallengesPack
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.challenges.views_helpers import updateChallengeModel as updateChallengeModel, getSuitableVehicles as getSuitableVehicles
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.user_missions.hub.update_children_mixin import UpdateChildrenMixin as UpdateChildrenMixin
from gui.impl.lobby.user_missions.tooltips.challenges_restart_tooltip import ChallengesRestartTooltip as ChallengesRestartTooltip
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.event_dispatcher import showExchangeCurrencyWindowModal as showExchangeCurrencyWindowModal, showStylePreview as showStylePreview, showVehicleHubOverview as showVehicleHubOverview, selectVehicleInHangar as selectVehicleInHangar, showAttachmentsSetPreview as showAttachmentsSetPreview
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import Currency as Currency, Money as Money
from gui.shop import showBuyGoldForBundle as showBuyGoldForBundle
from helpers import dependency as dependency
from skeletons.gui.challenges import IChallengesController as IChallengesController
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache
from shared_utils import first as first, findFirst as findFirst
from typing import Optional as Optional
from gui.challenges.challenge_item import ChallengeItem as ChallengeItem

# base nao representavel no stub: ViewComponent[...]
class ChallengeMissionsTab(UpdateChildrenMixin):
    LAYOUT_ID: Any
    __challenges: Any
    __customizationService: Any
    __itemsCache: Any
    __challengeID: Any
    __enabled: Any
    __selectedChallenge: Any
    __isSuitableVehicles: Any
    __commands: Any
    __missionTooltipData: Any
    def __init__(self, challengeID):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def selectedChallenge(self):
        ...
    def update(self, challengeID=None):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    # decorador original: @createTooltipContentDecorator(...)
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def __onSettingsChanged(self, *_):
        ...
    def __onVehiclesSyncCompleted(self, _):
        ...
    def __onMoneyUpdated(self, _):
        ...
    # decorador original: @args2params(...)
    def __onSelectedChallengeChanged(self, selectedChallengeID):
        ...
    # decorador original: @args2params(...)
    def __onAction(self, action, isFree):
        ...
    def __getAvailableChallengesIDs(self):
        ...
    def __setVisitedChallenge(self):
        ...
    def __getAvailability(self):
        ...
    def __chooseSelectedChallenge(self):
        ...
    def __updateModel(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateChallenges(self, model=None):
        ...
    def __updateChallengePack(self, difficulty):
        ...
    # decorador original: @args2params(...)
    def __openPreview(self, bonusType, bonusId, styleID, attachmentsToken):
        ...
