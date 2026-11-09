# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWBuffSequencesComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CGF as CGF
import GenericComponents as GenericComponents
import Math as Math
from dyn_components_groups import groupComponent as groupComponent
from halloween.hw_buff_effect_component_common import HWBuffEffectComponentCommon as HWBuffEffectComponentCommon
from xml_config_specs import StrParam as StrParam, Vector3Param as Vector3Param, ListParam as ListParam, ObjParam as ObjParam, IntParam as IntParam, BoolParam as BoolParam
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from helpers import dependency as dependency
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID

# decorador original: @groupComponent(...)
class HWBuffSequencesComponent(HWBuffEffectComponentCommon):
    guiSessionProvider: Any
    _gameObjects: Any
    _gameObjectsHideInSniperMode: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def _onAvatarReady(self):
        ...
    @property
    def _componentConfigs(self):
        ...
    @property
    def _animators(self):
        ...
    @property
    def _hasAppearance(self):
        ...
    @property
    def _hwBattleGuiCtrl(self):
        ...
    def _activateEffects(self):
        ...
    def _startEffects(self, startTime=0.0):
        ...
    def _stopEffects(self):
        ...
    def _triggerEffects(self, triggerName):
        ...
    def _deactivateEffects(self):
        ...
    def _createGameObject(self, queue, bindNode='', transform=...):
        ...
    def _onSniperModeChanged(self, isEnabled):
        ...
    def _onAppearanceReady(self):
        ...
    def _checkNode(self, config):
        ...
    def _onVehicleModelHidden(self, vehicleID, isHidden):
        ...
