# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/notifications/punishment_notification_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from past.builtins import basestring as basestring
from frameworks.wulf import WindowFlags as WindowFlags, ViewSettings as ViewSettings
from gui.impl import backport as backport
from gui.impl.dialogs.dialog_template_button import ConfirmButton as ConfirmButton
from gui.impl.dialogs.dialog_template_utils import toString as toString
from gui.impl.dialogs.widgets.icon_set import IconSet as IconSet
from gui.impl.dialogs.widgets.warning_text import WarningText as WarningText
from gui.impl.gen.resources import R as R
from gui.impl.gen.view_models.views.lobby.hangar.dialogs.punishment_dialog_model import PunishmentDialogModel as PunishmentDialogModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared.utils.functions import getArenaShortName as getArenaShortName, getArenaSubTypeName as getArenaSubTypeName
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import i18n as i18n, dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.impl import IGuiLoader as IGuiLoader
_LOC = R.strings.dialogs.punishmentWindow
_DEFAULT_ICON_RES = R.images.gui.maps.icons.lobby.dialog_warning
_BAN_ICON_RES = R.images.gui.maps.icons.lobby.dialog_ban
_DEFAULT_DIMMER_ALPHA = 0.6
_DEFAULT_INFO_TEXT = R.strings.dialogs.punishmentWindow.info
_BAN_REASON_TEXT = R.strings.dialogs.punishmentWindow.reason.mixed

class PunishmentDialogLocaleKeys(Enum):
    WARNING = 'warning'
    PENALTY = 'penalty'
    BAN = 'ban'

class PunishmentView(ViewImpl):
    __slots__: tuple
    LAYOUT_ID: Any
    VIEW_MODEL = PunishmentDialogModel
    _guiLoader: Any
    __iconResID: Any
    __title: Any
    __text: Any
    __infoText: Any
    __reason: Any
    __dimmerAlpha: Any
    def __init__(self, title, text, reason, infoText=None, layoutID=None, iconResID=..., dimmerAlpha=...):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _updateViewModel(self):
        ...
    def _fillViewModel(self, vm):
        ...
    def _setComponents(self):
        ...
    def _closeClickHandler(self, _=None):
        ...
    def _buttonClickHandler(self, _=None):
        ...

class WarningView(PunishmentView):
    def __init__(self, arenaTypeID, time, reason, isAFKViolation, layoutID=None):
        ...

class PenaltyView(PunishmentView):
    def __init__(self, arenaTypeID, time, reason, isAFKViolation, layoutID=None):
        ...

class BanView(PunishmentView):
    def __init__(self, arenaTypeID, time, duration, layoutID=None):
        ...

class AfkLeaverNotification(LobbyNotificationWindow):
    __slots__: tuple
    __appLoader: Any
    _blur: Any
    def __init__(self, content, parent=None):
        ...
    def _initialize(self):
        ...
    def __onViewLoaded(self, _, *args):
        ...
    def _finalize(self):
        ...

class WarningNotificationWindow(AfkLeaverNotification):
    __slots__: tuple
    arenaTypeID: Any
    time: Any
    reason: Any
    isAFKViolation: Any
    def __init__(self, arenaTypeID, time, reason, isAFKViolation, parent=None):
        ...
    def __eq__(self, other):
        ...

class PenaltyNotificationWindow(AfkLeaverNotification):
    __slots__: tuple
    arenaTypeID: Any
    time: Any
    reason: Any
    isAFKViolation: Any
    def __init__(self, arenaTypeID, time, reason, isAFKViolation, parent=None):
        ...
    def __eq__(self, other):
        ...

class BanNotificationWindow(AfkLeaverNotification):
    __slots__: tuple
    arenaTypeID: Any
    time: Any
    duration: Any
    def __init__(self, arenaTypeID, time, duration, parent=None):
        ...
    def __eq__(self, other):
        ...

def __getLocaleByGameplayName(path, gameplayName):
    ...
def getPunishmentDialogLocale(localeKey, gameplayName):
    ...
