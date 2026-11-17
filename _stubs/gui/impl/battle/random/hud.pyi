# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/random/hud.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
from frameworks.wulf import WindowFlags as WindowFlags
from gui.app_loader import settings as app_settings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.battle.shared.hud_view_model import HudDisplay as HudDisplay, HudViewModel as HudViewModel
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.Scaleform.daapi.settings.views import BattleSharedLayoutType as BattleSharedLayoutType
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import Any as Any
_logger: _Any

class RandomHUDWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...

# base nao representavel no stub: ViewComponent[...]
class RandomHUDView:
    __sessionProvider: _Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getChildComponents(self):
        ...
    def _getListeners(self):
        ...
    def _getEvents(self):
        ...
    def __onBattleSessionStop(self):
        ...
    def __onGuiVisibility(self, event):
        ...
