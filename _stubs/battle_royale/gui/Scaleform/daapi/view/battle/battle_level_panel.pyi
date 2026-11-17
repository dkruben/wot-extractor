# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/battle_level_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import BattleReplay as BattleReplay
from helpers import int2roman as int2roman
import WWISE as WWISE
from gui.Scaleform.daapi.view.meta.BattleLevelPanelMeta import BattleLevelPanelMeta as BattleLevelPanelMeta
from battle_royale.gui.battle_control.controllers.progression_ctrl import IProgressionListener as IProgressionListener

class BattleLevelPanel(BattleLevelPanelMeta, IProgressionListener):
    __SOUND_XP_DIFF = 1
    __XP_UPDATE_TIME_DIFF = 1.0
    __firstShow: Any
    __maxLevelAchieved: Any
    __isInitialized: Any
    __lastXPUpdateTime: Any
    def __init__(self):
        ...
    def updateData(self, arenaLevelData):
        ...
    def __update(self, arenaLevel, animationState):
        ...
    def onPlaySound(self, soundType):
        ...
