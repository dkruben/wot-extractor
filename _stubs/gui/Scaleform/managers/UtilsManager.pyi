# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/managers/UtilsManager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import calendar as calendar
import Keys as Keys
from Keys import KEY_NONE as KEY_NONE
from gui.Scaleform.framework.managers.TextManager import TextManager as TextManager
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.shared.utils.functions import getAbsoluteUrl as getAbsoluteUrl
import nations as nations
import BigWorld as BigWorld
from gui import GUI_NATIONS as GUI_NATIONS
from gui.shared import utils as utils
from gui.Scaleform.framework.entities.abstract.UtilsManagerMeta import UtilsManagerMeta as UtilsManagerMeta
from gui.shared.utils.key_mapping import SCALEFORM_TO_BW as SCALEFORM_TO_BW, canGetVirtualKey as canGetVirtualKey, BW_TO_SCALEFORM as BW_TO_SCALEFORM, MappingType as MappingType
from helpers import i18n as i18n, getClientLanguage as getClientLanguage
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
ONE_SECOND = 1

class UtilsManager(UtilsManagerMeta):
    _textMgr: Any
    def __init__(self):
        ...
    def registerTextManager(self, flashObject):
        ...
    def destroy(self):
        ...
    def __unregisterMrgs(self):
        ...
    def __isKeyboardKey(self, inKey):
        ...
    @property
    def textManager(self):
        ...
    def getGUINations(self):
        ...
    def getNationNames(self):
        ...
    def mapScaleformToVirtualKey(self, inKey):
        ...
    def getCharFromVirtualKey(self, key):
        ...
    def getNationIndices(self):
        ...
    def changeStringCasing(self, string, isUpper, _):
        ...
    @classmethod
    def getAbsoluteUrl(cls, relativeUrl):
        ...
    @classmethod
    def getHtmlIconText(cls, properties):
        ...
    def getFirstDayOfWeek(self):
        ...
    def getWeekDayNames(self, full, isUpper, isLower, useRegionSettings=True):
        ...
    def getMonthsNames(self, full, isUpper, isLower):
        ...
    def _dispose(self):
        ...
    def intToStringWithPrefixPatern(self, value, count, fill):
        ...
    def isTwelveHoursFormat(self):
        ...

class ImageUrlProperties(object):
    imageAlias: Any
    width: Any
    height: Any
    vSpace: Any
    hSpace: Any
    def __init__(self, imageAlias, width=16, height=16, vSpace=-4, hSpace=0):
        ...
