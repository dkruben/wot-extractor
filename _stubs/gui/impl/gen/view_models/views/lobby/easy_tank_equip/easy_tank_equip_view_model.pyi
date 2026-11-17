# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/easy_tank_equip/easy_tank_equip_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.proposal_model import ProposalModel as ProposalModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.consumables_preset_model import ConsumablesPresetModel as ConsumablesPresetModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.crew_preset_model import CrewPresetModel as CrewPresetModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.opt_devices_preset_model import OptDevicesPresetModel as OptDevicesPresetModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.shells_preset_model import ShellsPresetModel as ShellsPresetModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.style_preset_model import StylePresetModel as StylePresetModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.deal_panel_model import DealPanelModel as DealPanelModel

class EasyTankEquipViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onSelectProposal: Any
    onSwitchPreset: Any
    onSwapSlots: Any
    def __init__(self, properties=6, commands=4):
        ...
    @property
    def dealPanel(self):
        ...
    @staticmethod
    def getDealPanelType():
        ...
    @property
    def crewProposal(self):
        ...
    @staticmethod
    def getCrewProposalType():
        ...
    @property
    def optDevicesProposal(self):
        ...
    @staticmethod
    def getOptDevicesProposalType():
        ...
    @property
    def shellsProposal(self):
        ...
    @staticmethod
    def getShellsProposalType():
        ...
    @property
    def consumablesProposal(self):
        ...
    @staticmethod
    def getConsumablesProposalType():
        ...
    @property
    def styleProposal(self):
        ...
    @staticmethod
    def getStyleProposalType():
        ...
    def _initialize(self):
        ...
