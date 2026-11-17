# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/services/missions_container_service.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
from future.utils import viewvalues as viewvalues, viewitems as viewitems
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.impl.lobby.user_missions.hangar_widget.services import IMissionsContainerService as IMissionsContainerService
from gui.shared import g_eventBus as g_eventBus, events as events
from gui.shared.system_factory import collectUserMissionPlugins as collectUserMissionPlugins
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
import Event as Event
from typing import Any as Any, Dict as Dict, Optional as Optional
from gui.impl.lobby.user_missions.hangar_widget.plugins import IUserMissionPlugin as IUserMissionPlugin
_logger: _Any

class MissionsContainerService(IMissionsContainerService):
    settingsCore: _Any
    onShowPlugin: _Any
    onHidePlugin: _Any
    _plugins: _Any
    _visiblePlugins: _Any
    _selectedSlides: _Any
    def __init__(self):
        ...
    def isPluginVisible(self, viewAlias):
        ...
    def setPluginVisibility(self, viewAlias, visible):
        ...
    def getVisiblePlugins(self):
        ...
    def getSelectedSlide(self, sliderId):
        ...
    def onSlideChanged(self, selectedSlide):
        ...
    def finalize(self):
        ...
    def _showPlugin(self, viewAlias):
        ...
    def _hidePlugin(self, viewAlias):
        ...
    def _updateVisiblePlugins(self):
        ...
    def _collectPlugins(self, _):
        ...
