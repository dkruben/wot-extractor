# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/teaser_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import SoundGroups as SoundGroups
from constants import GF_RES_PROTOCOL as GF_RES_PROTOCOL
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.teaser_model import TeaserModel as TeaserModel, Type as Type
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.promo.constants import PROMO_SOUNDS as PROMO_SOUNDS
from gui.promo.promo_logger import PromoLogActions as PromoLogActions
from gui.shared.image_helper import ImageHelper as ImageHelper, getTextureLinkByID as getTextureLinkByID
from helpers import dependency as dependency
from skeletons.gui.game_control import IPromoController as IPromoController
from skeletons.gui.shared.promo import IPromoLogger as IPromoLogger

# base nao representavel no stub: ViewComponent[...]
class TeaserPresenter:
    _SALE_PROMO_TYPE = 'hot_stock'
    _promoController: Any
    __imageId: Any
    __teaserData: Any
    __promoCount: Any
    __showCallback: Any
    __closeCallback: Any
    __shouldShow: Any
    def __init__(self):
        ...
    def prepare(self):
        ...
    @property
    def viewModel(self):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __clear(self):
        ...
    def __onTeaserReceived(self, teaserData, showCallback, closeCallback):
        ...
    def __prepareData(self, teaserData, promoCount):
        ...
    def __onImageLoaded(self, requestedTeaserID, image):
        ...
    def __onClose(self, byUser=True):
        ...
    def __onClick(self):
        ...
