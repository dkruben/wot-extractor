# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/gsw_cards/key_card_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import WindowStatus as WindowStatus, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from halloween.gui.impl.gen.view_models.views.lobby.widgets.keys_view_model import KeysViewModel as KeysViewModel
from halloween.gui.impl.lobby.tooltips.key_tooltip import KeyTooltipView as KeyTooltipView
from halloween.gui.impl.lobby.tooltips.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from halloween.gui.shared.event_dispatcher import showBundleWindow as showBundleWindow
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.skeletons.halloween_shop_controller import IHalloweenShopController as IHalloweenShopController
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader

# base nao representavel no stub: ViewComponent[...]
class KeyCardPresenter(TooltipPositionerMixin):
    _guiLoader: Any
    hwArtifactsCtrl: Any
    hwCtrl: Any
    hwShopCtrl: Any
    __slots__: tuple
    _source: Any
    def __init__(self, source):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __onSettingsUpdate(self):
        ...
    def __onArtefactKeyUpdated(self):
        ...
    def __onArtefactStatusUpdated(self, *args):
        ...
    def __hasOverlayWindow(self):
        ...
    def __fillViewModel(self):
        ...
    def __updateViewModel(self):
        ...
    def __isEnoughKeys(self):
        ...
    def __onClick(self):
        ...
    def __windowStatusChanged(self, uniqueID, newStatus):
        ...
