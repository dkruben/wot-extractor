# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWBuffLaserSightComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Math as Math
import logging as logging
from gui.shared.utils.graphics import isRendererPipelineDeferred as isRendererPipelineDeferred
from dyn_components_groups import groupComponent as groupComponent
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from xml_config_specs import StrParam as StrParam, FloatParam as FloatParam
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from constants import CollisionFlags as CollisionFlags
_logger: Any

# decorador original: @groupComponent(...)
class HWBuffLaserSightComponent(DynamicScriptComponent):
    UPDATE_RATE = 0.1
    _beamModelPath: Any
    _beamModel: Any
    _beamMP: Any
    _bindNode: Any
    _taskID: Any
    _callbackDelayer: Any
    _modelLength: Any
    _sightMaxDistance: Any
    _appearanceReadySubscribed: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def _onAvatarReady(self):
        ...
    def _onLoaded(self, resourceRefs):
        ...
    def _onAppearanceReady(self):
        ...
    def _subscribeAppearanceReady(self):
        ...
    def _unsubscribeAppearanceReady(self):
        ...
    def _attachBeam(self):
        ...
    @property
    def _hasAppearance(self):
        ...
    def _updateLaserPoint(self):
        ...
