# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/customization_inscription_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
from account_helpers.AccountSettings import AccountSettings as AccountSettings, CUSTOMIZATION_SECTION as CUSTOMIZATION_SECTION
from gui import SystemMessages as SystemMessages
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.daapi.view.lobby.customization.shared import SEASON_TYPE_TO_INFOTYPE_MAP as SEASON_TYPE_TO_INFOTYPE_MAP, formatPersonalNumber as formatPersonalNumber, fitPersonalNumber as fitPersonalNumber, EMPTY_PERSONAL_NUMBER as EMPTY_PERSONAL_NUMBER
from gui.Scaleform.daapi.view.lobby.customization.sound_constants import SOUNDS as SOUNDS
from gui.Scaleform.daapi.view.meta.CustomizationInscriptionControllerMeta import CustomizationInscriptionControllerMeta as CustomizationInscriptionControllerMeta
from gui.Scaleform.locale.READABLE_KEY_NAMES import READABLE_KEY_NAMES as READABLE_KEY_NAMES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.Scaleform.locale.VEHICLE_CUSTOMIZATION import VEHICLE_CUSTOMIZATION as VEHICLE_CUSTOMIZATION
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.shared import g_eventBus as g_eventBus
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from helpers.i18n import makeString as _ms
from items.components.c11n_components import isPersonalNumberAllowed as isPersonalNumberAllowed
from items.customizations import PersonalNumberComponent as PersonalNumberComponent
from skeletons.gui.customization import ICustomizationService as ICustomizationService
_ERROR_ICON_DESC: dict
_ENTER_ICON_DESC: dict
_BACKSPACE_ICON_DESC: dict
_DEL_ICON_DESC: dict
_PRESS_ENTER_HINT_SHOWN_FIELD = 'isPressEnterHintShown'
_ENTER_NUMBER_HINT_SHOWN_FIELD = 'isEnterNumberHintShown'
_DEFAULT_HINT_DURATION = 3000
_DEFAULT_HINT_DELAY = 3000

class CustomizationInscriptionController(CustomizationInscriptionControllerMeta, CallbackDelayer):
    service: Any
    __currentNumber: Any
    __ctx: Any
    __isProhibitedHintShown: Any
    __visible: Any
    __digitsCount: Any
    __slotId: Any
    __storedNumber: Any
    __clearedNumber: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    @property
    def visible(self):
        ...
    @property
    def _component(self):
        ...
    @property
    def _digitsCount(self):
        ...
    @_digitsCount.setter
    def _digitsCount(self, digitsCount):
        ...
    @property
    def _currentNumber(self):
        ...
    @_currentNumber.setter
    def _currentNumber(self, number):
        ...
    def handleLobbyClick(self):
        ...
    def handleEscBtn(self):
        ...
    def handleDelBtn(self):
        ...
    def start(self, slotId):
        ...
    def finish(self, cancelIfEmpty=False):
        ...
    def cancel(self):
        ...
    def stop(self):
        ...
    def show(self):
        ...
    def hide(self):
        ...
    def update(self, slotId):
        ...
    def sendChar(self, char):
        ...
    def removeChar(self):
        ...
    def deleteAll(self):
        ...
    def __handleLobbyViewMouseEvent(self, event):
        ...
    def __manageCamera(self):
        ...
    def __prohibitedHintShown(self, value):
        ...
    def __showProhibitedNumberSystemMsg(self, item, number):
        ...
    def __showProhibitedHint(self, number):
        ...
    def __showEditHint(self):
        ...
    def __showConfirmitionHint(self):
        ...
    def __showPromptHint(self, showImmediately=False):
        ...
    def __getHintVO(self, hintMessage, icons=None, duration=0, delay=0):
        ...
    def __onPersonalNumberCleared(self, number):
        ...
    @staticmethod
    def __calcHintTimings(accountSettingName):
        ...
