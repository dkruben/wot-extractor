# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/shared/clip/cassette_clip_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import math as math
import typing as typing
from gui.battle_control.battle_constants import SHELL_SET_RESULT as SHELL_SET_RESULT, SHELL_QUANTITY_UNKNOWN as SHELL_QUANTITY_UNKNOWN
from gui.impl.gen.view_models.views.battle.shared.clip.cassette_clip_model import CassetteClipModel as CassetteClipModel, ClipState as ClipState
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.controllers.consumables.ammo_ctrl import AmmoController as AmmoController, _GunSettings as _GunSettings
_logger: Any

class CassetteClipPresenter(ViewComponent):
    __sessionProvider: Any
    __clipCapacity: Any
    __burstSize: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self):
        ...
    def _getEvents(self):
        ...
    def __onGunSettingsSet(self, gunSettings):
        ...
    def __onShellsUpdated(self, intCD, quantity, quantityInClip, result):
        ...
    def __onCurrentShellChanged(self, _):
        ...
    def __onCurrentShellReset(self):
        ...
    def __applyGunSettings(self, gunSettings):
        ...
    def __computeClipState(self, quantityInClip):
        ...
    def __applyAmmoStock(self, quantityInClip, clipState, clipReloaded):
        ...
