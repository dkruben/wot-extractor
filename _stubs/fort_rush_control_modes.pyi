# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush_control_modes.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
import CommandMapping as CommandMapping
from AvatarInputHandler.control_modes import PostMortemControlMode as PostMortemControlMode
_VEHICLE_SWITCH_CMDS: tuple

class FortRushPostMortemControlMode(PostMortemControlMode):
    def enable(self, **args):
        ...
    def selectPlayer(self, vehID):
        ...
    def onSwitchViewpoint(self, vehicleID, cameraPos):
        ...
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...
