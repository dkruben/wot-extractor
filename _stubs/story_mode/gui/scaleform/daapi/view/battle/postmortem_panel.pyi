# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/postmortem_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
from gui.Scaleform.daapi.view.battle.pve_base.postmortem_panel import PvePostmortemPanel as PvePostmortemPanel, LivesState as LivesState
from story_mode.gui.sound_constants import RESPAWN_TIMER_SOUND_EVENT as RESPAWN_TIMER_SOUND_EVENT, RESPAWN_TIMER_STATE_GROUP as RESPAWN_TIMER_STATE_GROUP, RESPAWN_TIMER_STATE_OFF as RESPAWN_TIMER_STATE_OFF, RESPAWN_TIMER_STATE_ON as RESPAWN_TIMER_STATE_ON
from story_mode_common.story_mode_constants import VEHICLE_BUNKER_TURRET_TAG as VEHICLE_BUNKER_TURRET_TAG
BUNKER_CODE = 'DEATH_FROM_BUNKER'
SHOT_CODES: tuple
BOT_CODE = 'DEATH_FROM_BOT'

class StoryModePostmortemPanel(PvePostmortemPanel):
    __slots__: tuple
    _RESPAWN_TIMER_SOUND_EVENT = RESPAWN_TIMER_SOUND_EVENT
    _deathInfo: Any
    def resetDeathInfo(self):
        ...
    def _dispose(self):
        ...
    def _showOwnDeathInfo(self):
        ...
    def _prepareMessage(self, code, killerVehID, device=None):
        ...
    def _applyLivesState(self, livesState):
        ...
    def __isBunkerTurret(self, vehicleID):
        ...
    def __isBot(self, vehicleID):
        ...
    def __showCustomMessage(self, code, killerVehID, device=None):
        ...
