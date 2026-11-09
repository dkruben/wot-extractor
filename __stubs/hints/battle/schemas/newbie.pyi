# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/hints/battle/schemas/newbie.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from dict2model import fields as fields, validate as validate
from helpers import dependency as dependency
from hints_common.battle.schemas.base import HMCContextType as HMCContextType, HMCPropsType as HMCPropsType
from hints.battle.newbie import getLogger as getLogger
from hints.battle.schemas.base import ClientHintHistoryModel as ClientHintHistoryModel, ClientHintHistorySchema as ClientHintHistorySchema, ClientHintModel as ClientHintModel, ClientHintSchema as ClientHintSchema, CHMTextType as CHMTextType, CHMVisualType as CHMVisualType, CHMSoundType as CHMSoundType, CHMLifecycleType as CHMLifecycleType
from skeletons.gui.battle_hints.newbie_battle_hints_controller import INewbieBattleHintsController as INewbieBattleHintsController
from gui.battle_control.controllers.battle_hints.history import BattleHintsHistory as BattleHintsHistory
from typing import Optional as Optional
_logger: Any
_DEFAULT_DISPLAY_COUNT = 5
hintSchema: Any

class NewbieClientHintHistoryModel(ClientHintHistoryModel):
    __slots__: tuple
    displayCount: Any
    def __init__(self, modifyPriority, cooldown, totalDisplayCount, perBattleCount, displayCount):
        ...
    def _reprArgs(self):
        ...

# base nao representavel no stub: ClientHintHistorySchema[...]
class NewbieClientHintHistorySchema:
    __slots__: tuple
    def __init__(self):
        ...

# base nao representavel no stub: ClientHintModel[...]
class NewbieClientHintModel:
    __slots__: tuple
    _newbieHintsCtrl: Any
    def validate(self, *args, **kwargs):
        ...
    def canBeShown(self, historyStorage=None):
        ...
