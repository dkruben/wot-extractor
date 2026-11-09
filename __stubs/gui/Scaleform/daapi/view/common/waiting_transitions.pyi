# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/common/waiting_transitions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import SCALEFORM as SCALEFORM
from gui.Scaleform.daapi.view.external_components import ExternalFlashComponent as ExternalFlashComponent
from gui.Scaleform.daapi.view.external_components import ExternalFlashSettings as ExternalFlashSettings
from gui.Scaleform.daapi.view.meta.WaitingTransitionMeta import WaitingTransitionMeta as WaitingTransitionMeta
from gui.Scaleform.genConsts.ROOT_SWF_CONSTANTS import ROOT_SWF_CONSTANTS as ROOT_SWF_CONSTANTS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.app_loader import IWaitingWidget as IWaitingWidget
_logger: Any
_DEFAULT_MOVIE_BACKGROUND_ALPHA = 0.6

class TransitionMode(object):
    DISABLED = 0
    ENABLED = 1
    TRIGGER = 2
    SHOW_BACKGROUND = 4
    PERMANENT_MESSAGE = 8

class WaitingTransition(ExternalFlashComponent, WaitingTransitionMeta, IWaitingWidget):
    settingsCore: Any
    __textID: Any
    __mode: Any
    isEnabled: Any
    def __init__(self):
        ...
    def isInTransitionMode(self):
        ...
    def setTransitionMode(self, mode):
        ...
    def showWaiting(self, messageID, *args):
        ...
    def hideWaiting(self):
        ...
    def afterCreate(self):
        ...
    def beforeDelete(self):
        ...
    def __setupBackground(self):
        ...
    def __onAppResolutionChanged(self, event):
        ...
