# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/consumables_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.Scaleform.daapi.view.battle.shared.consumables_panel import ConsumablesPanel as ConsumablesPanel
from gui.Scaleform.genConsts.CONSUMABLES_PANEL_SETTINGS import CONSUMABLES_PANEL_SETTINGS as CONSUMABLES_PANEL_SETTINGS
from story_mode.gui.battle_control.controllers.equipments_items import DistractionAbilityItem as DistractionAbilityItem, ReconAbilityItem as ReconAbilityItem
from story_mode_common.configs.story_mode_missions import missionsSchema as missionsSchema
from story_mode_common.story_mode_constants import EQUIPMENT_STAGES as STAGES, MissionsDifficulty as MissionsDifficulty
from gui.battle_control.controllers.consumables.equipment_ctrl import _EquipmentItem as _EquipmentItem

class SMConsumablesPanel(ConsumablesPanel):
    def _getActiveItemGlowType(self, item):
        ...
    def _isNormalDifficultyMission(self):
        ...
    def _updateEquipmentGlow(self, idx, item):
        ...
