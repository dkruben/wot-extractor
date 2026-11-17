# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/maps_training/markers2d.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from account_helpers.settings_core.settings_constants import BattleCommStorageKeys as BattleCommStorageKeys
from gui.battle_control import avatar_getter as avatar_getter
from gui.Scaleform.daapi.view.battle.shared.markers2d import plugins as plugins, vehicle_plugins as vehicle_plugins, MarkersManager as MarkersManager

class _MapsTrainingVehicleMarkerPlugin(vehicle_plugins.VehicleMarkerPlugin):
    __slots__: tuple
    __localGoals: Any
    def __init__(self, parentObj):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def _setMarkerInitialState(self, marker, vInfo):
        ...
    def __onLocalKillGoalsUpdated(self, localGoals):
        ...
    def __updateGoal(self, marker):
        ...

class MapsTrainingAreaStaticMarkerPlugin(plugins.AreaStaticMarkerPlugin):
    __slots__: tuple
    def start(self):
        ...
    def stop(self):
        ...
    def _onReplyFeedbackReceived(self, targetID, replierID, markerType, oldReplyCount, newReplyCount):
        ...
    def __onSettingsChange(self, diff):
        ...
    def __updateMarkerIsSticky(self, marker):
        ...

class MapsTrainingMarkersManager(MarkersManager):
    def _setupPlugins(self, arenaVisitor):
        ...
