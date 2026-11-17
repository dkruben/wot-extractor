# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/battle_hints/battle_hints_schema.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from dict2model import fields as fields
from hints.battle.schemas.base import ClientHintTextModel as ClientHintTextModel, ClientHintModel as ClientHintModel, CHMLifecycleType as CHMLifecycleType, CHMVisualType as CHMVisualType, CHMSoundType as CHMSoundType, ClientHintSchema as ClientHintSchema, ClientHintTextSchema as ClientHintTextSchema, CHMHistoryType as CHMHistoryType
from hints_common.battle.schemas.base import CommonHintContextModel as CommonHintContextModel, CommonHintPropsSchema as CommonHintPropsSchema, CommonHintPropsModel as CommonHintPropsModel
from dict2model.extensions.battle_type import BattleTypeModel as BattleTypeModel
hintPropsSchema: Any
hintTextSchema: Any
hintSchema: Any

class FortRushHintTextModel(ClientHintTextModel):
    __slots__: tuple
    descriptionKey: Any
    _description: Any
    def __init__(self, raw, key, template, highlight, descriptionKey):
        ...
    @property
    def description(self):
        ...

class FortRushHintPropsModel(CommonHintPropsModel):
    __slots__: tuple
    showCountdown: Any
    def __init__(self, name, scope, component, unique, priority, skipOverlay, battleTypes, showCountdown):
        ...

# base nao representavel no stub: CommonHintPropsSchema[...]
class FortRushHintPropsSchema:
    def __init__(self):
        ...

# base nao representavel no stub: ClientHintTextSchema[...]
class FortRushHintTextSchema:
    def __init__(self):
        ...

# base nao representavel no stub: ClientHintModel[...]
class FortRushHintModel:
    ...
