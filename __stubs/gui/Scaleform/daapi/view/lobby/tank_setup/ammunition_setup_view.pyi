# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/ammunition_setup_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.tank_setup.ammunition_setup_vehicle import g_tankSetupVehicle as g_tankSetupVehicle
from gui.Scaleform.daapi.view.meta.AmmunitionSetupViewMeta import AmmunitionSetupViewMeta as AmmunitionSetupViewMeta
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES as HANGAR_ALIASES
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import AmmunitionSetupViewEvent as AmmunitionSetupViewEvent
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader

class AmmunitionSetupView(AmmunitionSetupViewMeta):
    _appLoader: Any
    __ctx: Any
    __injectedView: Any
    __parametersView: Any
    def __init__(self, ctx):
        ...
    @property
    def injectedView(self):
        ...
    def registerFlashComponent(self, component, alias, *args):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _onUnregisterFlashComponent(self, viewPy, alias):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def destroy(self):
        ...
    def onClose(self):
        ...
    def onEscapePress(self):
        ...
    def __onAmmunitionSetupViewResized(self, event):
        ...
    def __onUpdateTTC(self, event):
        ...
    def __onCloseInjectView(self):
        ...
    def __onAnimationEnd(self):
        ...
    def __onChangeView(self, _):
        ...
