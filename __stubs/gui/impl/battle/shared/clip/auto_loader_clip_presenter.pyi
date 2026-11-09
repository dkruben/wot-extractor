# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/shared/clip/auto_loader_clip_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from gui.battle_control.battle_constants import SHELL_QUANTITY_UNKNOWN as SHELL_QUANTITY_UNKNOWN, SHELL_SET_RESULT as SHELL_SET_RESULT
from gui.battle_control.controllers.consumables.ammo_ctrl import AutoReloadingBoostStates as AutoReloadingBoostStates
from gui.impl.gen.view_models.views.battle.shared.clip.auto_loader_clip_model import AutoLoaderClipModel as AutoLoaderClipModel, BoostState as BoostState
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from helpers.time_utils import secondsToMS as secondsToMS
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import Optional as Optional
from gui.battle_control.controllers.consumables.ammo_ctrl import IGunReloadingSnapshot as IGunReloadingSnapshot, _GunSettings as _GunSettings
_logger: Any
_BOOST_STATE_MAP: dict

class AutoLoaderClipPresenter(ViewComponent):
    __sessionProvider: Any
    __clipCapacity: Any
    __shellsInClip: Any
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
    def __onShellsUpdated(self, intCD, quantity, quantityInClip, result):
        ...
    def __onCurrentShellChanged(self, intCD):
        ...
    def __onCurrentShellReset(self):
        ...
    def __onGunReloadTimeSet(self, _, state, skipAutoLoader):
        ...
    def __onShellsCleared(self, state):
        ...
    def __onGunAutoReloadTimeSet(self, timeState, _, stunned):
        ...
    def __onBoostUpdated(self, state, stateDuration, stateTotalTime, _):
        ...
    def __applyGunSettings(self, gunSettings):
        ...
    def __applyQuantity(self, quantityInClip):
        ...
    def __applyShellLoading(self, snapshot):
        ...
    def __applyAutoload(self, snapshot, stunned):
        ...
    def __applyBoost(self, state, stateDuration, stateTotalTime):
        ...
