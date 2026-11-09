# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/hints/battle/schemas/maps_training.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
import typing as typing
from dict2model import fields as fields
from dict2model import validate as validate
from hints_common.battle.schemas.base import HMCContextType as HMCContextType, CommonHintPropsModel as CommonHintPropsModel, CommonHintPropsSchema as CommonHintPropsSchema
from hints.battle.schemas.base import ClientHintSchema as ClientHintSchema, ClientHintTextModel as ClientHintTextModel, ClientHintSoundModel as ClientHintSoundModel, ClientHintTextSchema as ClientHintTextSchema, ClientHintSoundSchema as ClientHintSoundSchema, ClientHintModel as ClientHintModel, validateHintTextKey as validateHintTextKey, CHMVisualType as CHMVisualType, CHMLifecycleType as CHMLifecycleType, CHMHistoryType as CHMHistoryType
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from account_helpers.settings_core.settings_constants import OnceOnlyHints as OnceOnlyHints
from dict2model.extensions.battle_type import BattleTypeModel as BattleTypeModel
mtHintPropsSchema: Any
mtHintTextSchema: Any
mtHintSoundSchema: Any
hintSchema: Any

# decorador original: @enum.unique
class HintType(str, enum.Enum):
    HINT = 'hint'
    GOAL = 'goal'
    TIMER_GREEN = 'timerGreen'
    TIMER_RED = 'timerRed'

class MTClientHintPropsModel(CommonHintPropsModel):
    __slots__: tuple
    hintType: Any
    def __init__(self, name, scope, component, unique, priority, battleTypes, skipOverlay, hintType):
        ...
    def _reprArgs(self):
        ...

class MTClientHintTextModel(ClientHintTextModel):
    __slots__: tuple
    key2: Any
    _message2: Any
    def __init__(self, raw, key, template, highlight, key2):
        ...
    @property
    def message2(self):
        ...
    def _reprArgs(self):
        ...

class MTClientHintSoundModel(ClientHintSoundModel):
    __slots__: tuple
    notifyNewbie: Any
    def __init__(self, fx, notify, aliveOnly, notifyNewbie):
        ...
    def _createNotify(self):
        ...
    def _reprArgs(self):
        ...

# base nao representavel no stub: CommonHintPropsSchema[...]
class MTClientHintPropsSchema:
    __slots__: tuple
    def __init__(self):
        ...

# base nao representavel no stub: ClientHintTextSchema[...]
class MTClientHintTextSchema:
    __slots__: tuple
    def __init__(self):
        ...

# base nao representavel no stub: ClientHintSoundSchema[...]
class MTClientHintSoundSchema:
    __slots__: tuple
    def __init__(self):
        ...

# base nao representavel no stub: ClientHintModel[...]
class MTClientHintModel:
    __slots__: tuple
    def _createVO(self, data):
        ...
