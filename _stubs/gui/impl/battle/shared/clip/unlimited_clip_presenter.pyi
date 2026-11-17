# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/shared/clip/unlimited_clip_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from gui.impl.gen.view_models.views.battle.shared.clip.unlimited_clip_model import UnlimitedClipModel as UnlimitedClipModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.controllers.consumables.ammo_ctrl import _GunSettings as _GunSettings
_logger: Any

class UnlimitedClipPresenter(ViewComponent):
    __sessionProvider: Any
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
    def __applyGunSettings(self, gunSettings):
        ...
