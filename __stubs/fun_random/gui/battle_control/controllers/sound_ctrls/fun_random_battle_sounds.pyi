# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_control/controllers/sound_ctrls/fun_random_battle_sounds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from functools import partial as partial
import WWISE as WWISE
import BattleReplay as BattleReplay
from fun_random_common.fun_constants import UNKNOWN_WWISE_REMAPPING as UNKNOWN_WWISE_REMAPPING
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasBattleSubMode as hasBattleSubMode
from gui.battle_control.controllers.sound_ctrls.common import SoundPlayersBattleController as SoundPlayersBattleController
from shared_utils import nextTick as nextTick
from gui.battle_control.controllers import BattleSessionSetup as BattleSessionSetup
from gui.battle_control.controllers.sound_ctrls.common import SoundPlayer as SoundPlayer
from skeletons.gui.battle_session import IClientArenaVisitor as IClientArenaVisitor

class FunRandomBattleSoundController(SoundPlayersBattleController, FunSubModesWatcher):
    _remappingName: Any
    def __init__(self, setup):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def _initializeSoundPlayers(self):
        ...
    def _activateRemapping(self):
        ...
    def _deactivateRemapping(self):
        ...
    # decorador original: @hasBattleSubMode(...)
    def _getRemappingName(self, arenaVisitor=None):
        ...

class FunRandomBattleReplaySoundController(FunRandomBattleSoundController):
    _remappingName: Any
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def _activateRemapping(self):
        ...
    def _deactivateRemapping(self):
        ...
    def _startPlayers(self):
        ...
    def __onSubModesLoaded(self, *_):
        ...

def createFunRandomBattleSoundsController(setup):
    ...
