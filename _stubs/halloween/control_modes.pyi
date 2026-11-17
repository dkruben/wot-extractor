# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/control_modes.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import CommandMapping as CommandMapping
from AvatarInputHandler import control_modes as control_modes

class HWArcadeControlMode(control_modes.ArcadeControlMode):
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...

class HWSniperControlMode(control_modes.SniperControlMode):
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...

class HWPostMortemControlMode(control_modes.PostMortemControlMode):
    def _isPostmortemDelayEnabled(self):
        ...
