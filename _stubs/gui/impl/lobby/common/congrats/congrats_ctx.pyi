# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/congrats/congrats_ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS as STORE_CONSTANTS
from gui.Scaleform.locale.RES_SHOP import RES_SHOP as RES_SHOP
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.gui_items.Vehicle import getShopVehicleIconPath as getShopVehicleIconPath
from skeletons.gui.shared.congrats import ICongratsCtx as ICongratsCtx

class CongratsCtx(ICongratsCtx):
    @property
    def background(self):
        ...
    @property
    def title(self):
        ...
    @property
    def description(self):
        ...
    @property
    def image(self):
        ...
    @property
    def imageAlt(self):
        ...
    @property
    def confirmLabel(self):
        ...
    @property
    def backLabel(self):
        ...
    def onConfirm(self):
        ...
    def onBack(self):
        ...

class GUIItemCongratsCtx(CongratsCtx):
    _item: Any
    def __init__(self, item):
        ...

class StyleCongratsCtx(GUIItemCongratsCtx):
    @property
    def description(self):
        ...
    @property
    def image(self):
        ...
