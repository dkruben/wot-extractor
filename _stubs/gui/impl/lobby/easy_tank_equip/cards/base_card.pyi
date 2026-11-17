# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/cards/base_card.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.preset_model import PresetModel as PresetModel
from gui.impl.lobby.easy_tank_equip.easy_tank_equip_buy_price_builder import EasyTankEquipBuyPriceModelBuilder as EasyTankEquipBuyPriceModelBuilder
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.impl.wrappers.user_compound_price_model import PriceModelBuilder as PriceModelBuilder
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.proposal_model import ProposalModel as ProposalModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.slot_info_model import SlotInfoModel as SlotInfoModel
from gui.impl.lobby.easy_tank_equip.data_providers.base_data_provider import BaseDataProvider as BaseDataProvider, PresetInfo as PresetInfo, SlotInfo as SlotInfo
from gui.shared.money import Money as Money
from typing import Optional as Optional

class BaseCard(SubModelPresenter):
    provider: Any
    def __init__(self, viewModel, parentView, provider):
        ...
    @property
    def viewModel(self):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def updateModel(self):
        ...
    def _getEvents(self):
        ...
    def _getPreset(self):
        ...
    def _onSelect(self):
        ...
    def _onSwitchPreset(self):
        ...
    def _onPricesUpdated(self, balance):
        ...
    def _onPresetsUpdated(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillProposalModel(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillPresetsModels(self, proposalPresets, model=None):
        ...

class BasePreset(object):
    @classmethod
    def fillPresetModel(cls, model, presetInfo, balance=None):
        ...
    @classmethod
    def fillSlotInfoModel(cls, model, slotInfo):
        ...
    @classmethod
    def getPresetModel(cls):
        ...
    @classmethod
    def updatePresetModelPrice(cls, model, presetInfo, balance=None):
        ...
