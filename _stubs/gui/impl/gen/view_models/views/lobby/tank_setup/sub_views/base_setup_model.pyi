# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/base_setup_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.deal_panel_model import DealPanelModel as DealPanelModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.filters_model import FiltersModel as FiltersModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.setup_tabs_model import SetupTabsModel as SetupTabsModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_slot_model import BaseSlotModel as BaseSlotModel

class BaseSetupModel(ViewModel):
    __slots__: tuple
    SELECT_SLOT_ACTION = 'select'
    REVERT_SLOT_ACTION = 'undo'
    RETURN_TO_STORAGE_ACTION = 'cancel'
    SWAP_SLOTS_ACTION = 'swap'
    DEMOUNT_SLOT_ACTION = 'demount'
    DEMOUNT_SLOT_FROM_SETUP_ACTION = 'demount_from_setup'
    DEMOUNT_SLOT_FROM_SETUPS_ACTION = 'demount_from_setups'
    DESTROY_SLOT_ACTION = 'destroy'
    SHOW_INFO_SLOT_ACTION = 'show_info'
    UPGRADE_SLOT_ACTION = 'upgrade'
    ADD_ONE_SLOT_ACTION = 'add_one'
    DRAG_AND_DROP_SLOT_ACTION = 'drag_drop'
    DECONSTRUCT_SLOT_ACTION = 'deconstruct'
    onSlotAction: Any
    onDealConfirmed: Any
    onDealCancelled: Any
    onAutoRenewalChanged: Any
    onTabChanged: Any
    onFilterChanged: Any
    onFilterReset: Any
    def __init__(self, properties=5, commands=7):
        ...
    @property
    def filter(self):
        ...
    @staticmethod
    def getFilterType():
        ...
    @property
    def dealPanel(self):
        ...
    @staticmethod
    def getDealPanelType():
        ...
    @property
    def tabs(self):
        ...
    @staticmethod
    def getTabsType():
        ...
    def getSlots(self):
        ...
    def setSlots(self, value):
        ...
    @staticmethod
    def getSlotsType():
        ...
    def getSyncInitiator(self):
        ...
    def setSyncInitiator(self, value):
        ...
    def _initialize(self):
        ...
