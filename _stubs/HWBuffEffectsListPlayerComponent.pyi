# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWBuffEffectsListPlayerComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import random as random
import ResMgr as ResMgr
from functools import partial as partial
from dyn_components_groups import groupComponent as groupComponent
from helpers.EffectsList import effectsFromSection as effectsFromSection, EffectsListPlayer as EffectsListPlayer
from halloween.hw_buff_effect_component_common import HWBuffEffectComponentCommon as HWBuffEffectComponentCommon
from xml_config_specs import StrParam as StrParam, ListParam as ListParam, ObjParam as ObjParam
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
_START_EFFECTS_DELAY = 0.1

# decorador original: @groupComponent(...)
class HWBuffEffectsListPlayerComponent(HWBuffEffectComponentCommon):
    _callbackDelayer: Any
    __playerEffects: Any
    _effectsHideInSniperMode: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    @property
    def _componentConfigs(self):
        ...
    def _activateEffects(self):
        ...
    def _deactivateEffects(self):
        ...
    def _onSniperModeChanged(self, isEnabled):
        ...
    def __activateEffectsDelayed(self, effectsToStart):
        ...
