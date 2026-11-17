# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/role_description.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import ROLE_TYPE_TO_LABEL as ROLE_TYPE_TO_LABEL, ACTION_TYPE_TO_LABEL as ACTION_TYPE_TO_LABEL, ARENA_PERIOD as ARENA_PERIOD
from items.vehicles import getActionsByRole as getActionsByRole
from helpers import dependency as dependency
from PlayerEvents import g_playerEvents as g_playerEvents
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui import makeHtmlString as makeHtmlString
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from gui.Scaleform.daapi.view.meta.RoleDescriptionMeta import RoleDescriptionMeta as RoleDescriptionMeta
from gui.Scaleform.daapi.view.battle.shared.hint_panel.plugins import RoleHelpPlugin as RoleHelpPlugin
from typing import Dict as Dict
from items.vehicles import VehicleDescriptor as VehicleDescriptor
_ROLE_HTML_TEMPLATE = 'html_templates:vehicleRoles/roleDescription'

class RoleDescription(RoleDescriptionMeta):
    __sessionProvider: Any
    __isActive: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onArenaPeriodChange(self, period, *_):
        ...
    def __setData(self, typeDescriptor):
        ...
    @staticmethod
    def __getRoleActionVO(action):
        ...
    def __hide(self):
        ...
    def __handleRoleHintToggled(self, event):
        ...
