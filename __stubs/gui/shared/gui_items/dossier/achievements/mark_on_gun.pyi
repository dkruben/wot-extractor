# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/mark_on_gun.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from helpers import i18n as i18n
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB, MARK_ON_GUN as MARK_ON_GUN
from gui import makeHtmlString as makeHtmlString
from gui.shared.gui_items.dossier.achievements.abstract import RegularAchievement as RegularAchievement
from items import vehicles as vehicles
from nations import NAMES as NATION_NAMES

class MarkOnGunAchievement(RegularAchievement):
    __slots__: tuple
    IT_95X85 = '95x85'
    __nationId: Any
    __damageRating: Any
    def __init__(self, dossier, value=None):
        ...
    def setVehicleNationID(self, nationID):
        ...
    def getVehicleNationID(self):
        ...
    def getUserCondition(self):
        ...
    def setDamageRating(self, val):
        ...
    def getDamageRating(self):
        ...
    def getIcons(self):
        ...
    def getI18nValue(self):
        ...
    def _getActualName(self):
        ...
    @classmethod
    def _readDamageRating(cls, dossier):
        ...
    @classmethod
    def _readVehicleNationID(cls, dossier):
        ...
    def __getIconPath(self, dir_):
        ...
    def __repr__(self):
        ...
