# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/integrated_auction/tooltips/event_banner_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.gen.view_models.views.lobby.integrated_auction.tooltips.auction_event_banner_tooltip_model import AuctionEventBannerTooltipModel as AuctionEventBannerTooltipModel
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService as IEventsService
from gui.integrated_auction.constants import AUCTION_ENTRY_POINT_NAME as AUCTION_ENTRY_POINT_NAME
from helpers import dependency as dependency
from helpers.time_utils import getServerUTCTime as getServerUTCTime, getTimestampByStrDate as getTimestampByStrDate

class EventBannerTooltip(ViewImpl):
    __eventService: Any
    __entry: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __getTimerValue(self):
        ...
    def __getAuctionStart(self):
        ...
    def __getIsAvailable(self):
        ...
