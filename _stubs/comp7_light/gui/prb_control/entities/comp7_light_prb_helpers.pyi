# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/prb_control/entities/comp7_light_prb_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import adisp as adisp
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import GUI_START_BEHAVIOR as GUI_START_BEHAVIOR
from comp7_light.gui.comp7_light_constants import COMP7_HANGAR_ALIAS as COMP7_HANGAR_ALIAS, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from comp7_light.gui.impl.lobby.comp7_light_helpers.comp7_light_gui_helper import isComp7LightIntroShouldBeShown as isComp7LightIntroShouldBeShown
from comp7_light.gui.prb_control.entities.base.ctx import Comp7LightPrbAction as Comp7LightPrbAction
from comp7_light.gui.shared import event_dispatcher as comp7_light_events
from frameworks.wulf import WindowLayer as WindowLayer
from gui.app_loader import sf_lobby as sf_lobby
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IComp7LightController as IComp7LightController

class Comp7LightViewPresenter(object):
    __settingsCore: Any
    __comp7LightCtrl: Any
    # decorador original: @sf_lobby
    def __app(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def __subscribe(self):
        ...
    def __unsubscribe(self):
        ...
    def __onViewLoaded(self, view, *_, **__):
        ...
    def __showView(self):
        ...
    @classmethod
    def __isHangarViewLoaded(cls):
        ...
    @classmethod
    def __isViewShown(cls, key):
        ...

# decorador original: @adisp.adisp_process
# decorador original: @dependency.replace_none_kwargs(...)
def selectComp7Light(comp7LightController=None):
    ...
# decorador original: @adisp.adisp_process
def createComp7LightSquad(squadSize):
    ...
