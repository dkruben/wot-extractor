# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/reusable/extension_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum

class ReusableInfoFactory(object):
    __default: dict
    __infoForBonusType: dict
    class Keys(Enum):
        COMMON = 'common'
        AVATARS = 'avatars'
        AVATAR = 'avatar'
        PERSONAL = 'personal'
        PLAYERS = 'players'
        PLAYER = 'player'
        TEAM_BASES = 'teamBases'
        VEHICLE_DETAILED = 'vehicleDetailed'
        VEHICLE_SUMMARIZED = 'vehicleSummarized'
        VEHICLES = 'vehicles'
        FAIRPLAY_VIOLATIONS = 'fairplayViolations'
        SQUAD_BONUS = 'squadBonus'
    @classmethod
    def setDefaults(cls, defaults):
        ...
    @classmethod
    def addForBonusType(cls, bonusType, key, infoCls):
        ...
    @classmethod
    def commonInfoForBonusType(cls, bonusType):
        ...
    @classmethod
    def avatarsInfoForBonusType(cls, bonusType):
        ...
    @classmethod
    def avatarInfoForBonusType(cls, bonusType):
        ...
    @classmethod
    def personalInfoForBonusType(cls, bonusType):
        ...
    @classmethod
    def playerInfoForBonusType(cls, bonusType):
        ...
    @classmethod
    def playersInfoForBonusType(cls, bonusType):
        ...
    @classmethod
    def teamBasesInfoForBonusType(cls, bonusType):
        ...
    @classmethod
    def vehicleDetailedInfoForBonusType(cls, bonusType):
        ...
    @classmethod
    def vehicleSummarizeInfoForBonusType(cls, bonusType):
        ...
    @classmethod
    def vehiclesInfoForBonusType(cls, bonusType):
        ...
    @classmethod
    def fairplayViolationForBonusType(cls, bonusType):
        ...
    @classmethod
    def squadBonusInfoForBonusType(cls, bonusType):
        ...
    @classmethod
    def __getForBonusType(cls, bonusType, key):
        ...
