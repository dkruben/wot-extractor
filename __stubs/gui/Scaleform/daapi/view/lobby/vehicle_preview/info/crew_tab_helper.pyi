# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/crew_tab_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import typing as typing
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.crew_constants import CrewConstants as CrewConstants
from gui.shared.gui_items.Tankman import Tankman as Tankman, getBigIconPath as getBigIconPath, NO_TANKMAN as NO_TANKMAN
from helpers.i18n import makeString as makeString
from items.tankmen import TankmanDescr as TankmanDescr, makeTmanDescrByTmanData as makeTmanDescrByTmanData
from shared_utils import first as first
from web.web_client_api.common import ItemPackType as ItemPackType
from items.tankmen import MAX_SKILL_LEVEL as MAX_SKILL_LEVEL
from gui.shared.gui_items.tankman_skill import TankmanSkill as TankmanSkill
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
GIRL_EMPTY = 'girl-empty'
NEW_SKILL_ICON = 'preview_new_skill_trained'
_SimpleSkill: Any
_SIMPLE_SKILL: Any

class PreviewTankman(Tankman):
    __slots__: tuple
    _previewData: Any
    def __init__(self, slotIdx, tmanData=None, tankman=None, vehicle=None):
        ...
    @property
    def fullUserName(self):
        ...
    @property
    def extensionLessIcon(self):
        ...
    @property
    def bigIconPath(self):
        ...
    @property
    def backportSkillList(self):
        ...
    @property
    def previewVehicleName(self):
        ...

def isValidCrewForVehicle(tankmenItems, roles):
    ...
def getCrewPreviewTitle(title, itemCrew):
    ...
def getCustomTitle(skill, role, forOne):
    ...
def getCustomHeader(customCrew):
    ...
def getPreviewCrewMemberArgs(isCustom, slotIdx, tankman):
    ...
