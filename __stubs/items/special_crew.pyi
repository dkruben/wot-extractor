# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/special_crew.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from future.utils import viewkeys as viewkeys
from debug_utils import LOG_WARNING as LOG_WARNING
from items.components.component_constants import EMPTY_STRING as EMPTY_STRING
from items.components.tankmen_components import SPECIAL_CREW_TAG as SPECIAL_CREW_TAG
from items.tankmen import hasTagInTankmenGroup as hasTagInTankmenGroup, unpackCrewParams as unpackCrewParams, getTankmenWithTag as getTankmenWithTag, getNationGroups as getNationGroups
from items.vehicles import VehicleType as VehicleType
from items.tankmen import TankmanDescr as TankmanDescr
from gui.shared.gui_items.Tankman import Tankman as Tankman

class CustomCrew(object):
    SABATON = 'sabaton'
    OFFSPRING = 'offspring'
    YHA = 'yha'
    WITCHES = 'witches'
    TAG_MAP: dict
    @staticmethod
    def hasTagInTankmen(tankmanDescr, tag):
        ...
    @staticmethod
    def getTankmanCrewName(tankmanDescr):
        ...
    @staticmethod
    def getCrewName(nationID, groupID, isPremium):
        ...

class CustomSkills(object):
    SABATON_BROTHERHOOD = 'sabaton_brotherhood'
    OFFSPRING_BROTHERHOOD = 'offspring_brotherhood'
    YHA_BROTHERHOOD = 'yha_brotherhood'
    WITCHES_BROTHERHOOD = 'witches_brotherhood'
    CUSTOM_CREW_MAP: dict
    @staticmethod
    def _getCustomSkill(skillName, customCrewName):
        ...
    @staticmethod
    def getCustomSkill(skillName, tankman=None, customCrewName=...):
        ...

def _isCrewCompleted(vehicleType, tankmenGroups, tag):
    ...
def isWitchesCrew(tankmanDescr):
    ...
def isMihoCrewCompleted(vehicleType, tankmenGroups):
    ...
def isMikaCrewCompleted(vehicleType, tankmenGroups):
    ...
def isDarjeelingCrewCompleted(vehicleType, tankmenGroups):
    ...
def isErwinCrewCompleted(vehicleType, tankmenGroups):
    ...
def isNakajimaCrewCompleted(vehicleType, tankmenGroups):
    ...
def isYhaCrewCompleted(vehicleType, tankmenGroups):
    ...
def isWitchesCrewCompleted(vehicleType, tankmenGroups):
    ...
def isHW25Crew(vehicleType, tankmenGroups, tag):
    ...
def isHW25CrewCompleted(vehicleType, tankmenGroups):
    ...
def isHW25CrewCNCompleted(vehicleType, tankmenGroups):
    ...
