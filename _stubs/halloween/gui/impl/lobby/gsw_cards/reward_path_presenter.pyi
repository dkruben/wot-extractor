# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/gsw_cards/reward_path_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from halloween.skeletons.halloween_twitch_con_controller import IHalloweenTwitchConController as IHalloweenTwitchConController
from helpers import dependency as dependency
from halloween.gui.impl.gen.view_models.views.lobby.widgets.reward_path_card_view_model import RewardPathCardViewModel as RewardPathCardViewModel
from halloween.gui.impl.lobby.tooltips.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from halloween.gui.shared.event_dispatcher import showRewardPathView as showRewardPathView, showStoryChoiceWindow as showStoryChoiceWindow
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween_common.halloween_constants import HWStoryChoiceSettings as HWStoryChoiceSettings
from skeletons.gui.shared import IItemsCache as IItemsCache

# base nao representavel no stub: ViewComponent[...]
class RewardPathCardPresenter(TooltipPositionerMixin):
    _hwArtefactsCtrl: Any
    _hwTwitchCtrl: Any
    __itemsCache: Any
    def __init__(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _isChoiceState(self):
        ...
    def __onClick(self):
        ...
    def __fillMetaWidget(self):
        ...
    def __onArtefactStatusUpdated(self, _):
        ...
    def __cerfCountUpdate(self):
        ...
    def __handleTokensUpdate(self, diff):
        ...
