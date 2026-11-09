# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/user_missions/hangar_widget/presenters/event_shop_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getSteelHunterProductsUrl as getSteelHunterProductsUrl
from gui.impl.lobby.user_missions.hangar_widget.presenters.base_child_presenter import UserMissionChildPresenter as UserMissionChildPresenter
from gui.shared.event_dispatcher import showShop as showShop
from helpers import dependency as dependency
from gui.impl.gen import R as R
from battle_royale.gui.impl.lobby.views.user_missions.hangar_widget.overlap_ctrl import BattleRoyaleOverlapCtrlMixin as BattleRoyaleOverlapCtrlMixin
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from skeletons.gui.shared import IItemsCache as IItemsCache
from battle_royale.gui.impl.lobby.tooltips.shop_button_tooltip_view import ShopButtonTooltipView as ShopButtonTooltipView
from battle_royale.gui.impl.gen.view_models.views.lobby.views.widget.event_shop_model import EventShopModel as EventShopModel

# base nao representavel no stub: ViewComponent[...]
class BattleRoyaleEventShopPresenter(UserMissionChildPresenter, TooltipPositionerMixin, BattleRoyaleOverlapCtrlMixin):
    GROUP = 'shopEntryPoint'
    __battleRoyaleController: Any
    __itemsCache: Any
    def __init__(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def _onLoading(self):
        ...
    def __update(self, *_):
        ...
    @staticmethod
    def __onOpenShop():
        ...
