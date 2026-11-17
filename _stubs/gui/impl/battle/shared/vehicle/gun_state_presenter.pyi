# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/shared/vehicle/gun_state_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
from gui.battle_control.battle_constants import SHELL_SET_RESULT as SHELL_SET_RESULT
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.battle.shared.gun_state_model import GunStateModel as GunStateModel, GunType as GunType, ReloadStatus as ReloadStatus, ReloadType as ReloadType
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from helpers.time_utils import secondsToMS as secondsToMS
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.controllers.consumables.ammo_ctrl import IGunReloadingSnapshot as IGunReloadingSnapshot, _GunSettings as _GunSettings
_logger: Any
_RELOAD_ALIAS_BY_TYPE: dict

class GunStatePresenter(ViewComponent):
    __sessionProvider: Any
    __reloadingType: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    def __onGunSettingsSet(self, gunSettings):
        ...
    def __setUpPresenter(self, reloadingType):
        ...
    def __disablePresenter(self, reloadingType):
        ...
    def __onGunReloadTimeSet(self, _, state, __):
        ...
    def __onShellsUpdated(self, intCD, quantity, quantityInClip, result):
        ...
    def __onShellsCleared(self, state):
        ...
    def __onCurrentShellChanged(self, intCD):
        ...
    def __resetModel(self):
        ...
    def __applyGunSettings(self, gunSettings):
        ...
    def __applyReloadState(self, snapshot):
        ...
    def __onSwitchToPostmortem(self, _, __):
        ...
    @staticmethod
    def __resolveGunType(gunSettings):
        ...
    @staticmethod
    def __resolveReloadingType(gunSettings):
        ...
