# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/promo/hangar_teaser_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from functools import partial as partial
import BigWorld as BigWorld
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.promo.constants import PROMO_SOUNDS as PROMO_SOUNDS
from gui.promo.promo_logger import PromoLogActions as PromoLogActions
from gui.shared.formatters import icons as icons
from gui.shared.image_helper import ImageHelper as ImageHelper, getTextureLinkByID as getTextureLinkByID
from helpers import time_utils as time_utils, dependency as dependency
from items.components.shared_components import i18n as i18n
from skeletons.gui.shared.promo import IPromoLogger as IPromoLogger

class TeaserViewer(object):
    _TIMER_PERIOD = 0.1
    _SALE_PROMO_TYPE = 'hot_stock'
    __viewProxy: Any
    __teaserData: Any
    __promoCount: Any
    __prevTimerValue: Any
    __callbackID: Any
    __imagePath: Any
    __showCallback: Any
    __closeCallback: Any
    __timeIcon: Any
    def __init__(self, view, showCallback, closeCallback):
        ...
    def show(self, teaserData, promoCount):
        ...
    def stop(self, byUser=False):
        ...
    def __onImageLoaded(self, requestedTeaserID, image):
        ...
    def __startTimer(self):
        ...
    def __timerTick(self):
        ...
    def __stopTimer(self):
        ...
