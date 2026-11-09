# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/prb_control/entities/comp7_prb_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import adisp as adisp
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import GUI_START_BEHAVIOR as GUI_START_BEHAVIOR
from comp7.gui.comp7_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, COMP7_HANGAR_ALIAS as COMP7_HANGAR_ALIAS
from comp7.gui.impl.lobby.comp7_helpers.comp7_gui_helpers import isComp7OnboardingShouldBeShown as isComp7OnboardingShouldBeShown, isComp7WhatsNewShouldBeShown as isComp7WhatsNewShouldBeShown
from comp7.gui.prb_control.entities.base.ctx import Comp7PrbAction as Comp7PrbAction
from comp7.gui.shared import event_dispatcher as comp7_events
from frameworks.wulf import WindowLayer as WindowLayer
from gui.app_loader import sf_lobby as sf_lobby
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
_logger: Any

class Comp7ViewPresenter(object):
    __settingsCore: Any
    __comp7Ctrl: Any
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
    @staticmethod
    def __showOnboarding():
        ...
    @staticmethod
    def __showWhatsNew():
        ...

# decorador original: @adisp.adisp_process
# decorador original: @dependency.replace_none_kwargs(...)
def selectComp7(comp7Controller=None):
    ...
# decorador original: @adisp.adisp_process
def createComp7Squad(squadSize):
    ...
