# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/easy_tank_equip/loggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import json as json
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.proposal_model import ProposalType as ProposalType
from uilogging.base.logger import MetricsLogger as MetricsLogger
from uilogging.easy_tank_equip.constants import FEATURE as FEATURE, EasyTankEquipLogActions as EasyTankEquipLogActions, EasyTankEquipLogItems as EasyTankEquipLogItems, EasyTankEquipSwapInitiators as EasyTankEquipSwapInitiators
from typing import List as List
LOGGING_ITEMS_MAP: dict

class EasyTankEquipLogger(MetricsLogger):
    STATUS_KEY = 'status'
    PRESET_NUMBER_KEY = 'preset_number'
    IDS_KEY = 'ids'
    def __init__(self):
        ...
    def createCardInfo(self, status, presetNumber, ids):
        ...
    def onViewOpen(self, info):
        ...
    def onViewClose(self, isApplyBtnClicked, info):
        ...
    def onCancel(self):
        ...
    def onSwitchPreset(self, proposalType, fromPresetNumber, toPresetNumber):
        ...
    def onSwapSlots(self, proposalType, isDndUsed, firstSlotNumber, secondSlotNumber):
        ...
