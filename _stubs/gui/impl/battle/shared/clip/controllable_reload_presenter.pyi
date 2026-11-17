# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/shared/clip/controllable_reload_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from constants import STATIONARY_RELOAD_STATE as STATIONARY_RELOAD_STATE
from gui.battle_control.battle_constants import SHELL_QUANTITY_UNKNOWN as SHELL_QUANTITY_UNKNOWN, SHELL_SET_RESULT as SHELL_SET_RESULT
from gui.impl.gen.view_models.views.battle.shared.clip.controllable_reload_model import ClipState as ClipState, ControllableReloadModel as ControllableReloadModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from helpers.time_utils import secondsToMS as secondsToMS
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.controllers.consumables.ammo_ctrl import IGunReloadingSnapshot as IGunReloadingSnapshot, _GunSettings as _GunSettings
_logger: Any

class ControllableReloadPresenter(ViewComponent):
    __sessionProvider: Any
    __clipCapacity: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __onGunSettingsSet(self, gunSettings):
        ...
    def __onShellsUpdated(self, _, __, quantityInClip, result):
        ...
    def __onCurrentShellChanged(self, _):
        ...
    def __onCurrentShellReset(self):
        ...
    def __onGunAutoReloadTimeSet(self, timeState, stationaryState, isSlowed):
        ...
    def __applyGunSettings(self, gunSettings):
        ...
    def __computeClipState(self, quantityInClip):
        ...
    def __applyQuantity(self, quantityInClip):
        ...
    def __applyControllableReloadFlag(self, stationaryState):
        ...
    def __applyAutoload(self, snapshot, stationaryState, isSlowed):
        ...
