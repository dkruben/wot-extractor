# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/comp7_helpers/comp7_bonus_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import copy as copy
import enum as enum
import typing as typing
from future.utils import viewitems as viewitems
from constants import PREMIUM_ENTITLEMENTS as PREMIUM_ENTITLEMENTS
from dog_tags_common.components_config import componentConfigAdapter as componentConfigAdapter
from dog_tags_common.config.common import ComponentViewType as ComponentViewType
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as ACHIEVEMENT_BLOCK, BADGES_BLOCK as BADGES_BLOCK
from gui.server_events.bonuses import C11nProgressTokenBonus as C11nProgressTokenBonus, DossierBonus as DossierBonus
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import Currency as Currency
from shared_utils import first as first
from gui.selectable_reward.constants import SELECTABLE_BONUS_NAME as SELECTABLE_BONUS_NAME
from typing import Any as Any
from gui.server_events.bonuses import SimpleBonus as SimpleBonus, ItemsBonus as ItemsBonus, CustomizationsBonus as CustomizationsBonus, GoodiesBonus as GoodiesBonus, CrewBooksBonus as CrewBooksBonus, PlusPremiumDaysBonus as PlusPremiumDaysBonus, CreditsBonus as CreditsBonus, CrystalBonus as CrystalBonus, DogTagComponentBonus as DogTagComponentBonus, VehiclesBonus as VehiclesBonus, TokensBonus as TokensBonus
_BONUS_HELPERS_MAP: dict

class BonusTypes(enum.IntEnum):
    NONE = 0
    ACHIEVEMENT = 1
    DELUXE_DEVICE = 2
    CREWBOOK = 3
    PREMIUM = 4
    CRYSTAL = 5
    CREDITS = 6
    OPTIONAL_DEVICE = 7
    BOOSTER = 8
    EQUIPMENT = 9
    BATTLE_BOOSTER = 10
    RENT_VEHICLE = 11
    STYLE = 12
    STYLE_PROGRESS = 13
    BADGE = 14
    BADGE_SUFFIX = 15
    DOGTAG_ENGRAVING = 16
    DOGTAG_BACKGROUND = 17
    OFFER = 18
    STYLE_3D_PROGRESS = 19
    CREW = 20
    TOKEN = 21
    EQUIP_COIN = 22
    STYLE_3D = 23

class _BaseBonusHelper(object):
    @staticmethod
    def getBonusType(bonus):
        ...

class _ItemsBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...

class CustomizationsBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...
    @staticmethod
    def getBonusC11Item(bonus):
        ...

class _GoodiesBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...

class _CrewBooksBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...

class _VehiclesBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...

class _DogTagBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...

class _DossierBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...

class _PremiumBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...

class _CreditsBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...

class _CrystalBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...

class _StyleProgressBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...

class _OfferBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...

class _Style3DProgressBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...

class _TankmenBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...

class _TokensBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...

class _EquipCoinBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...

class _TokenBonusHelper(_BaseBonusHelper):
    @staticmethod
    def getBonusType(bonus):
        ...

def getBonusType(bonus):
    ...
def splitDossierBonuses(bonuses):
    ...
def _splitDossierBonus(dossier):
    ...
