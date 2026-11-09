# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/callout_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CommandMapping as CommandMapping
import Event as Event
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES
from gui.Scaleform.daapi.view.meta.CalloutPanelMeta import CalloutPanelMeta as CalloutPanelMeta
from gui.Scaleform.genConsts.BATTLEDAMAGELOG_IMAGES import BATTLEDAMAGELOG_IMAGES as _IMAGES
from gui.Scaleform.locale.READABLE_KEY_NAMES import READABLE_KEY_NAMES as READABLE_KEY_NAMES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.shared.utils.key_mapping import getReadableKey as getReadableKey
from helpers import dependency as dependency
from helpers.i18n import makeString as makeString
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_VEHICLE_CLASS_TAGS_ICONS: dict
_CALLOUT_COMMMAND_TO_UI_VISUAL_STATE: dict
_HINT_TEXT_MAP: dict
_HINT_TEXT_DEFAULT: Any

class CalloutPanel(CalloutPanelMeta):
    sessionProvider: Any
    settingsCore: Any
    __hidingInProgress: Any
    onHidingFinished: Any
    def __init__(self):
        ...
    def onHideStart(self):
        ...
    def onHideCompleted(self):
        ...
    def setShowData(self, senderVehicleID, cmdName):
        ...
    def setHideData(self, wasAnswered=False, commandReceived=None):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __reset(self):
        ...
    def __onCrosshairViewChanged(self, viewID):
        ...
    def __onPrebattleHighlightsStart(self, _=None):
        ...
