# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/cgf_components/vehicle_highlight.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
import GenericComponents as GenericComponents
from aih_constants import CTRL_MODES as CTRL_MODES, CTRL_MODE_NAME as CTRL_MODE_NAME
from constants import IS_CLIENT as IS_CLIENT

class PlayerAvatar(object):
    ...

class VehicleHighlightSystem(CGF.System):
    AvatarActivated: Any
    AvatarDeactivated: Any
    Reactions: Any
    def update(self):
        ...
    def onAdded(self, controlModeStatus):
        ...
    def onRemoved(self, controlModeStatus):
        ...
