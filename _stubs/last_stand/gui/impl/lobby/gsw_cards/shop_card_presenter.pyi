# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/gsw_cards/shop_card_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.lobby.user_missions.hangar_widget.presenters.base_child_presenter import UserMissionChildPresenter as UserMissionChildPresenter
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.shop_card_view_model import ShopCardViewModel as ShopCardViewModel
from last_stand.gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import LastStandOverlapCtrlMixin as LastStandOverlapCtrlMixin
from last_stand.gui.shared.event_dispatcher import showLSShopAll as showLSShopAll

# base nao representavel no stub: ViewComponent[...]
class ShopCardPresenter(UserMissionChildPresenter, TooltipPositionerMixin, LastStandOverlapCtrlMixin):
    def __init__(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __onClick(self):
        ...
