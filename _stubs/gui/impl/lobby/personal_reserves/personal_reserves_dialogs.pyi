# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_reserves/personal_reserves_dialogs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from wg_async import wg_async as wg_async
from adisp import adisp_async as adisp_async
from goodies.goodie_constants import GOODIE_RESOURCE_TYPE as GOODIE_RESOURCE_TYPE
from gui.goodies.goodie_items import Booster as Booster
from gui.impl import backport as backport
from gui.impl.dialogs.dialog_template_button import ConfirmButton as ConfirmButton, CancelButton as CancelButton
from gui.impl.dialogs.gf_builders import ResDialogBuilder as ResDialogBuilder
from gui.impl.dialogs.sub_views.common.simple_text import ImageSubstitution as ImageSubstitution
from gui.impl.dialogs.sub_views.content.simple_text_content import SimpleTextContent as SimpleTextContent
from gui.impl.dialogs.sub_views.footer.single_price_footer import SinglePriceFooter as SinglePriceFooter
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as DefaultDialogPlaceHolders
from gui.impl.gen.view_models.views.dialogs.dialog_template_button_view_model import ButtonType as ButtonType
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencySize as CurrencySize
from gui.impl.gen.view_models.views.dialogs.sub_views.multiple_icons_set_view_model import IconPositionLogicEnum as IconPositionLogicEnum
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogWindowWrapper as FullScreenDialogWindowWrapper
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from typing import Union as Union
from gui.impl.dialogs.dialog_template import DialogTemplateView as DialogTemplateView
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from frameworks.wulf import PyResAccessor as PyResAccessor
__all__: tuple
BOOSTER_IMAGE_LOOKUP: dict
UPGRADE_IMAGE_LOOKUP: dict

class BuyAndActivateBoosterDialogBuilder(ResDialogBuilder):
    __slots__: tuple
    boosterPrice: Any
    needsToBuy: Any
    warning: Any
    def __init__(self, boosterPrice, needsToBuy=True, uniqueID=None):
        ...
    def setWarning(self, warning):
        ...
    def _extendTemplate(self, template):
        ...
    def _getConfirmLabel(self, needsToBuy):
        ...

class BuyGoldDialogBuilder(ResDialogBuilder):
    __slots__: tuple
    boosterPrice: Any
    warning: Any
    def __init__(self, boosterPrice, uniqueID=None):
        ...
    def setWarning(self, warning):
        ...
    def _extendTemplate(self, template):
        ...

# decorador original: @adisp_async
# decorador original: @wg_async
def showDialogAndLogInteraction(dialog, callback):
    ...
def getUpgradeBoosterDialog(booster, previousBooster):
    ...
def getBuyAndActivateBoosterDialog(booster):
    ...
def getBuyGoldDialog(booster):
    ...
