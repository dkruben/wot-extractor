# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/armor_inspector_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
import CGF as CGF
import armor_inspector as armor_inspector
from account_helpers.settings_core.settings_constants import GRAPHICS as GRAPHICS
from cgf_script.registration import registerComponent as registerComponent
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from shared_utils import nextTick as nextTick
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from constants import IS_EDITOR as IS_EDITOR, IS_CGF_DUMP as IS_CGF_DUMP
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.config.models import TierModel as TierModel
MatInfo: Any
_logger: Any
_PendingShow: Any

class HangarVehicle(object):
    ...

# decorador original: @registerComponent
class ArmorInspectorComponent(object):
    domain = CGF.Domain.Client
    editorTitle = 'Armor Inspector'
    vehicleID: Any
    fadeOnRemove: Any
    showProbability: Any
    def __init__(self):
        ...

class ArmorInspectorSystem(CGF.System):
    _settingsCore: Any
    InspectorActivated: Any
    InspectorDeactivated: Any
    HangarVehicleAccess: Any
    Reactions: Any
    _appearanceListeners: Any
    _pendingShow: Any
    def __init__(self, *args):
        ...
    def update(self):
        ...
    def onMappingLoaded(self):
        ...
    def onMappingUnloaded(self):
        ...
    def onAdded(self, gameObject, armorInspector, vehicleAccess):
        ...
    def _show(self, vehicle, gameObject, tierModel, showProbability, withFade):
        ...
    def _showImpl(self, vehicle, gameObject, tierModel, showProbability, withFade):
        ...
    # decorador original: @nextTick
    def _retryPending(self):
        ...
    def onRemoved(self, gameObject, component):
        ...
    def _setSettings(self):
        ...
    def _clientColorSettingsChanged(self, diff):
        ...
    def _registerAttachmentsUpdates(self, vehicle, armorInspector, gameObject, tierModel):
        ...
    def _unregisterAttachmentsUpdates(self, gameObject):
        ...
