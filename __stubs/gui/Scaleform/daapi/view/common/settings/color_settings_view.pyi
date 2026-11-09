# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/common/settings/color_settings_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from past.utils import old_div as old_div
import BigWorld as BigWorld
from debug_utils import LOG_DEBUG as LOG_DEBUG
import GUI as GUI
from account_helpers.AccountSettings import AccountSettings as AccountSettings, COLOR_SETTINGS_TAB_IDX as COLOR_SETTINGS_TAB_IDX, APPLIED_COLOR_SETTINGS as APPLIED_COLOR_SETTINGS
from account_helpers.settings_core import settings_constants as settings_constants
from account_helpers.settings_core.settings_constants import GRAPHICS as GRAPHICS, COLOR_GRADING_TECHNIQUE_DEFAULT as COLOR_GRADING_TECHNIQUE_DEFAULT
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.common.settings.mixins import LayerVisibilityMixin as LayerVisibilityMixin
from gui.Scaleform.daapi.view.meta.ColorSettingsViewMeta import ColorSettingsViewMeta as ColorSettingsViewMeta
from gui.Scaleform.genConsts.COLOR_SETTINGS import COLOR_SETTINGS as COLOR_SETTINGS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.SETTINGS import SETTINGS as SETTINGS
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.shared.events import GameEvent as GameEvent
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils import flashObject2Dict as flashObject2Dict, graphics as graphics
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import dependency as dependency, i18n as i18n
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore

class TABS(object):
    DEFAULT = 0
    FILTERS = 1
    CUSTOM = 2

class ColorSettingsView(LayerVisibilityMixin, ColorSettingsViewMeta):
    settingsCore: Any
    __selectedTabIdx: Any
    __componentWidth: Any
    __isColorPreviewFilterActive: Any
    __initSettings: Any
    __tabsPreviewSettings: Any
    __wasGraphicsOptimizationEnabled: Any
    __blur: Any
    _savedBackgroundAlpha: Any
    def __init__(self, ctx=None):
        ...
    def setViewWidth(self, value):
        ...
    def moveSpace(self, dx, dy, dz):
        ...
    def onSettingsChange(self, settingName, settingValue):
        ...
    def onApply(self, diff):
        ...
    def onTabSelected(self, selectedTab):
        ...
    def onReset(self):
        ...
    def onClose(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __getLastAppliedTabsSettings(self):
        ...
    def __getTabSettings(self, lastAppliedSettings, tabIdx, settingKeys):
        ...
    def __getTypes(self):
        ...
    def __getFiltersTypes(self):
        ...
    def __getSettings(self):
        ...
    def __showColorPreviewFilter(self):
        ...
    def __hideColorPreviewFilter(self):
        ...
    def __hasChangesInSettings(self, settingsNames, diff):
        ...
    def __getCurrentTabSettings(self):
        ...
    def __previewSettings(self, settings):
        ...
    def __onExternalBackgroundAlphaChange(self, event):
        ...
