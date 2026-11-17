# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/battle_page/ammunition_panel/prebattle_ammunition_panel_inject.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.meta.PrebattleAmmunitionPanelViewMeta import PrebattleAmmunitionPanelViewMeta as PrebattleAmmunitionPanelViewMeta
from gui.Scaleform.framework.entities.inject_component_adaptor import hasAliveInject as hasAliveInject
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.battle_control.battle_constants import COUNTDOWN_STATE as COUNTDOWN_STATE
from gui.battle_control.controllers.consumables.ammo_ctrl import IAmmoListener as IAmmoListener
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView as IAbstractPeriodView
from gui.battle_control.controllers.prebattle_setups_ctrl import IPrebattleSetupsListener as IPrebattleSetupsListener
from gui.impl.battle.battle_page.ammunition_panel.prebattle_ammunition_panel_view import PrebattleAmmunitionPanelView as PrebattleAmmunitionPanelView
from gui.impl.gen.view_models.views.battle.battle_page.prebattle_ammunition_panel_view_model import State as State
from gui.shared.utils.MethodsRules import MethodsRules as MethodsRules
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class PrebattleAmmunitionPanelInject(MethodsRules, PrebattleAmmunitionPanelViewMeta, IPrebattleSetupsListener, IAmmoListener, IAbstractPeriodView):
    __sessionProvider: Any
    __slots__: tuple
    _state: Any
    __currShellCD: Any
    __nextShellCD: Any
    __timeLeft: Any
    __isViewLoaded: Any
    __isViewActive: Any
    def __init__(self):
        ...
    @property
    def isActive(self):
        ...
    def onViewIsHidden(self):
        ...
    # decorador original: @hasAliveInject(...)
    def onArenaLoaded(self):
        ...
    # decorador original: @MethodsRules.delayable(...)
    # decorador original: @hasAliveInject(...)
    def setCurrentShellCD(self, shellCD):
        ...
    # decorador original: @MethodsRules.delayable(...)
    # decorador original: @hasAliveInject(...)
    def setNextShellCD(self, shellCD):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def showSetupsView(self, vehicle, isArenaLoaded=False):
        ...
    # decorador original: @hasAliveInject(...)
    def updateVehicleSetups(self, vehicle):
        ...
    # decorador original: @hasAliveInject(...)
    def stopSetupsSelection(self):
        ...
    # decorador original: @hasAliveInject(...)
    def hideSetupsView(self):
        ...
    def setCountdown(self, state, timeLeft):
        ...
    def hideCountdown(self, state, _):
        ...
    def _dispose(self):
        ...
    def _onPopulate(self):
        ...
    def _hideSetupsView(self, useAnim=True):
        ...
    def _makeInjectView(self, vehicle, *args):
        ...
    def _addInjectContentListeners(self):
        ...
    def _removeInjectContentListeners(self):
        ...
    def _getShowShadows(self):
        ...
    def _switchLayout(self, groupID, layoutIdx):
        ...
    def _updateCurrentState(self, isArenaLoaded):
        ...
    def __onViewLoaded(self):
        ...
    def __onSwitchLayout(self, groupID, layoutIdx):
        ...
