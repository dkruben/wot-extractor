# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/offers/offer_reward_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import shared_utils as shared_utils
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.impl.auxiliary.rewards_helper import getRewardsBonuses as getRewardsBonuses
from gui.impl.backport import TooltipData as TooltipData, BackportTooltipWindow as BackportTooltipWindow
from gui.impl.lobby.offers import getGfImagePath as getGfImagePath
from gui.shared.event_dispatcher import showOfferGiftsWindow as showOfferGiftsWindow
from gui.shared.utils.functions import stripAllTags as stripAllTags
from helpers import dependency as dependency
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.offers.offer_reward_model import OfferRewardModel as OfferRewardModel
from gui.impl.pub import ViewImpl as ViewImpl
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
_logger: Any

class OfferRewardWindow(ViewImpl):
    _lobbyContext: Any
    _offersProvider: Any
    _COMMON_SOUND_SPACE: Any
    _offer: Any
    _gift: Any
    _cdnTitle: Any
    _cdnDescription: Any
    _cdnIcon: Any
    _tooltipData: Any
    def __init__(self, layoutID, offerID, giftID, cdnTitle='', cdnDescription='', cdnIcon=''):
        ...
    def createToolTip(self, event):
        ...
    @property
    def _viewModel(self):
        ...
    @property
    def _serverSettings(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onClose(self):
        ...
