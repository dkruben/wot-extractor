# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/style_buying.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from adisp import adisp_process as adisp_process
from gui import DialogsInterface as DialogsInterface
from gui.shared.formatters import formatPrice as formatPrice
from gui.shared.money import Money as Money, Currency as Currency
from gui.shop import showBuyGoldForBundle as showBuyGoldForBundle, showBuyProductOverlay as showBuyProductOverlay
from gui.Scaleform.daapi.view.dialogs import DIALOG_BUTTON_ID as DIALOG_BUTTON_ID, I18nConfirmDialogMeta as I18nConfirmDialogMeta
from gui.Scaleform.daapi.view.dialogs.ExchangeDialogMeta import ExchangeCreditsWebProductMeta as ExchangeCreditsWebProductMeta
from gui.Scaleform.daapi.view.lobby.vehicle_preview.info import dyn_currencies_utils as dyn_utils
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from typing import Optional as Optional, Dict as Dict, Union as Union

class StyleBuyingProcessor(object):
    __itemsCache: Any
    __buyParams: Any
    __confirmationKey: Any
    __style: Any
    def __init__(self, confirmationKey='buyConfirmation'):
        ...
    def setConfiramtionKey(self, confirmationKey):
        ...
    def setStyle(self, style):
        ...
    def setBuyParams(self, buyParams):
        ...
    def mayObtain(self, price):
        ...
    # decorador original: @adisp_process
    def buy(self, price):
        ...
    # decorador original: @adisp_process
    def __buy(self, money):
        ...
    def __obtainByOrdinaryCurrency(self, money):
        ...
    def __obtainByDynamicCurrency(self, money):
        ...

def _buyRequestConfirmation(productName, priceStr, key):
    ...
