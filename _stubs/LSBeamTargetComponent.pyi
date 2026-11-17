# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSBeamTargetComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import logging as logging
from future.utils import listvalues as listvalues
from typing import TYPE_CHECKING as TYPE_CHECKING
import CGF as CGF
import BigWorld as BigWorld
import GenericComponents as GenericComponents
import Math as Math
from CGF import HierarchyComponent as HierarchyComponent
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from BeamRibbonComponent import BeamRibbonComponent as BeamRibbonComponent
from gui.shared.utils.TimeInterval import TimeInterval as TimeInterval
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from ls_dyn_object_cache import LSPrefabs as LSPrefabs, getPrefabPath as getPrefabPath
from typing import Dict as Dict, List as List, Optional as Optional, Set as Set, Tuple as Tuple
_logger: Any
_BEAM_NAME_TO_PREFAB_KEY: dict

class BeamParam(object):
    beamName: Any
    targetVehId: Any
    sourcePosition: Any
    def __init__(self, beamName, targetVehId, sourcePosition):
        ...

class LSBeamTargetComponent(DynamicScriptComponent):
    _UPDATE_TICK_LENGTH = 0.5
    _DMG_BEAM_Y_OFFSET = 0.2
    _beams: Any
    _sourceVehId: Any
    _targetVehIds: Any
    _dmgBeams: Any
    _dmgTargets: Any
    _dmgBeamName: Any
    _dmgSourcePosition: Any
    _activeBeams: Any
    _updateTI: Any
    _callbackDelayer: Any
    _pendingBeams: Any
    _loadingBeams: Any
    _loadingDmgBeams: Any
    _step: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    @staticmethod
    def _safeRemove(queue, go):
        ...
    @staticmethod
    def _safeActivate(queue, go):
        ...
    @staticmethod
    def _safeDeactivate(queue, go):
        ...
    def applyEffects(self, beamName):
        ...
    def removeEffects(self, vehiclesIds):
        ...
    def showDamage(self, entityId):
        ...
    def _onGameObjectLoaded(self, entity, beamName, objects, queue):
        ...
    def _onDmgGameObjectLoaded(self, entityId, beamName, objects, queue):
        ...
    def _removeDMGEffect(self, entityId, beamName):
        ...
    def _beamVisibilityUpdate(self):
        ...
    def _setBeamActive(self, entityId, isActive, queue):
        ...
    def _onAvatarReady(self):
        ...
    def _applyEffect(self, entityId, beamParam, queue):
        ...
