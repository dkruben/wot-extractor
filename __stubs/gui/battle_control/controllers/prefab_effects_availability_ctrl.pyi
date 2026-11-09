# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/prefab_effects_availability_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from config_schemas.prefab_effects_availability import prefabEffectsAvailabilitySchema as prefabEffectsAvailabilitySchema
from gui.battle_control.arena_info.interfaces import IArenaLoadController as IArenaLoadController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from helpers.prefab_effects import setCachePrefabEffectsEnabledForBattle as setCachePrefabEffectsEnabledForBattle, resetCachePrefabEffectsEnabledForBattle as resetCachePrefabEffectsEnabledForBattle

class PrefabEffectsAvailabilityController(IArenaLoadController):
    __slots__: tuple
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def getControllerID(self):
        ...
    def spaceLoadStarted(self):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
    def _pushValue(self):
        ...
