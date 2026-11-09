# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/easy_tank_equip_deal_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.proposal_model import ProposalType as ProposalType
from gui.impl.lobby.easy_tank_equip.easy_tank_equip_buy_price_builder import EasyTankEquipBuyPriceModelBuilder as EasyTankEquipBuyPriceModelBuilder
from gui.impl.lobby.tank_setup.configurations.base import BaseDealPanel as BaseDealPanel
from gui.shared.gui_items.fitting_item import canBuyWithGoldExchange as canBuyWithGoldExchange
from gui.shared.money import ZERO_MONEY as ZERO_MONEY, Currency as Currency
from typing import Dict as Dict, Optional as Optional
from collections import OrderedDict as OrderedDict
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.money import Money as Money
from gui.impl.gen.view_models.views.lobby.tank_setup.common.deal_panel_model import DealPanelModel as DealPanelModel
from gui.impl.lobby.easy_tank_equip.data_providers.base_data_provider import BaseDataProvider as BaseDataProvider, PresetInfo as PresetInfo

class EasyTankEquipDealPanel(BaseDealPanel):
    _IN_TANK = 'inTank'
    _KITS = 'demountKits'
    _DEF_PRICE = 'defPrice'
    _DISCOUNT = 'discount'
    _DEFAULT_PRICES: dict
    _prices: Any
    @classmethod
    def updateDealPanelPrice(cls, vehicle, presets, dealPanelModel):
        ...
    @classmethod
    def addItem(cls, vehicle, item, prices):
        ...
    @classmethod
    def updatePrices(cls, dealPanelModel):
        ...
    @classmethod
    def getTotalPrice(cls):
        ...
    @classmethod
    def _fillDealPanelPrice(cls, model):
        ...
    @classmethod
    def _updateDisabled(cls, prices, dealPanelModel):
        ...

class EasyTankEquipBottomContent(SubModelPresenter):
    __providers: Any
    def __init__(self, viewModel, parentView, providers):
        ...
    @staticmethod
    def getTotalPrice():
        ...
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def update(self):
        ...
    def updatePrices(self):
        ...
    def __getSelectedPresets(self):
        ...
