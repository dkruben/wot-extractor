# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/battle_hints/battle_hints_schemas.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from dict2model import fields as fields
from dict2model import schemas as schemas
from dict2model import validate as validate
from gui import makeHtmlString as makeHtmlString
from gui.impl import backport as backport
from gui.impl.gen import R as R
from hints.battle.schemas.const import HTML_TEMPLATE_PATH as HTML_TEMPLATE_PATH
from hints_common.battle.schemas.base import CommonHintContextModel as CommonHintContextModel
from hints.battle.schemas.base import validateHintTextTemplate as validateHintTextTemplate, ClientHintModel as ClientHintModel, ClientHintSchema as ClientHintSchema, ClientHintTextModel as ClientHintTextModel, ClientHintTextSchema as ClientHintTextSchema, CHMVisualType as CHMVisualType, CHMLifecycleType as CHMLifecycleType, HMCPropsType as HMCPropsType, CHMSoundType as CHMSoundType, CHMHistoryType as CHMHistoryType
hintContextSchema: Any
hintTextSchema: Any
hintSchema: Any

class LSHintContextModel(CommonHintContextModel):
    __slots__: tuple
    extraPadding: Any
    offsetY: Any
    isAdaptive: Any
    def __init__(self, extraPadding, offsetY, isAdaptive):
        ...

class LSHintTextModel(ClientHintTextModel):
    __slots__: tuple
    templatePinnable: Any
    _templateSmall: Any
    _messagePinnable: Any
    def __init__(self, raw, key, template, highlight, templatePinnable, templateSmall):
        ...
    @property
    def messagePinnable(self):
        ...
    @property
    def templateSmall(self):
        ...
    def _reprArgs(self):
        ...

# base nao representavel no stub: ClientHintTextSchema[...]
class LSHintTextSchema:
    __slots__: tuple
    def __init__(self):
        ...

# base nao representavel no stub: ClientHintModel[...]
class LSHintModel:
    __slots__: tuple
    def _createVO(self, data):
        ...
