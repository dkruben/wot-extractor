# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/shared/clip/extra_shot_clip_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from gui.battle_control.battle_constants import SHELL_QUANTITY_UNKNOWN as SHELL_QUANTITY_UNKNOWN, SHELL_SET_RESULT as SHELL_SET_RESULT
from gui.impl.gen.view_models.views.battle.shared.clip.extra_shot_clip_model import ClipState as ClipState, ExtraShotClipModel as ExtraShotClipModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.controllers.consumables.ammo_ctrl import _GunSettings as _GunSettings
_logger: Any

class ExtraShotClipPresenter(ViewComponent):
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
    def __onShellsUpdated(self, intCD, quantity, quantityInClip, result):
        ...
    def __onCurrentShellChanged(self, intCD):
        ...
    def __onCurrentShellReset(self):
        ...
    def __applyGunSettings(self, gunSettings):
        ...
    def __computeClipState(self, quantityInClip):
        ...
    def __applyAmmoStock(self, quantityInClip, clipState):
        ...
