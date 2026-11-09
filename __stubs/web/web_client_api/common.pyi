# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import long as long
import itertools as itertools
from collections import namedtuple as namedtuple
from enum import Enum as Enum, unique as unique
from gui.shared.money import MONEY_UNDEFINED as MONEY_UNDEFINED
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
SPA_ID_TYPES: tuple
VehicleOfferEntry: Any
ItemPackEntry: Any
CompensationSpec: Any

class _Enum(Enum):
    @classmethod
    def hasValue(cls, value):
        ...

# decorador original: @unique
class TManLocation(_Enum):
    NEWBIES = 'newbies'
    BARRACKS = 'barracks'
    TANKS = 'tanks'
    DEMOBILIZED = 'demobilized'

# decorador original: @unique
class TManGender(_Enum):
    MALE = 'male'
    FEMALE = 'female'

class ShopItemType(CONST_CONTAINER):
    VEHICLE = 'vehicle'
    CREW = 'crew'
    EQUIPMENT = 'equipment'
    DEVICE = 'device'
    BOOSTER = 'booster'
    BATTLE_BOOSTER = 'battleBooster'
    MODULE = 'module'
    SHELL = 'shell'
    PREMIUM = 'premium'
    PAINT = 'paint'
    CAMOUFLAGE = 'camouflage'
    MODIFICATION = 'modification'
    STYLE = 'style'
    DECAL = 'decal'
    EMBLEM = 'emblem'
    INSCRIPTION = 'inscription'
    PROJECTION_DECAL = 'projectionDecal'
    ATTACHMENT = 'attachment'
    ENHANCEMENT = 'enhancements'
    CREW_BOOKS = 'crew_books'

class ItemPackType(CONST_CONTAINER):
    VEHICLE = 'vehicle'
    VEHICLE_LIGHT = 'vehicle/lightTank'
    VEHICLE_MEDIUM = 'vehicle/mediumTank'
    VEHICLE_HEAVY = 'vehicle/heavyTank'
    VEHICLE_AT_SPG = 'vehicle/AT-SPG'
    VEHICLE_SPG = 'vehicle/SPG'
    ITEM_EQUIPMENT = 'item/equipment'
    ITEM_DEVICE = 'item/optionalDevice'
    ITEM_SHELL = 'item/shell'
    ITEM_CREW_SKIN = 'item/crewSkin'
    GOODIE_GOLD = 'goodie/gold'
    GOODIE_CREDITS = 'goodie/credits'
    GOODIE_EXPERIENCE = 'goodie/experience'
    GOODIE_FREE_EXPERIENCE = 'goodie/free_experience'
    GOODIE_CREW_EXPERIENCE = 'goodie/crew_experience'
    GOODIE_FREE_AND_CREW_EXPERIENCE = 'goodie/free_xp_and_crew_xp'
    GOODIE_FRONTLINE_EXPERIENCE = 'goodie/fl_experience'
    GOODIE_RECERTIFICATIONFORM = 'goodie/recertificationForm'
    CREW_50 = 'crew/50'
    CREW_75 = 'crew/75'
    CREW_100 = 'crew/100'
    CUSTOM_CREW_100 = 'custom_crew/100'
    CREW_BUNDLE = 'crew/bundle'
    CREW_CUSTOM = 'crew/custom'
    CUSTOM_PREMIUM = 'custom/premium'
    CUSTOM_PREMIUM_PLUS = 'custom/premium_plus'
    CUSTOM_CRYSTAL = 'custom/crystal'
    CUSTOM_GOLD = 'custom/gold'
    CUSTOM_CREDITS = 'custom/credits'
    CUSTOM_EVENT_COIN = 'custom/eventCoin'
    CUSTOM_EVENT_COIN_EXTERNAL = 'custom/event_coin'
    CUSTOM_BPCOIN = 'custom/bpcoin'
    CUSTOM_EQUIP_COIN = 'custom/equipCoin'
    CUSTOM_EQUIP_COIN_EXTERNAL = 'custom/equip_coin'
    CUSTOM_SLOT = 'custom/slot'
    CUSTOM_SEVERAL_SLOTS = 'custom/slots'
    CUSTOM_REFERRAL_CREW = 'custom/crew'
    CUSTOM_SUPPLY_POINT = 'custom/supply_point'
    CUSTOM_BATTLE_PASS_POINTS = 'custom/battlePassPoints'
    CUSTOM_X5_BATTLE_BONUS = 'custom/X5_battle'
    CUSTOM_X3_CREW_BONUS = 'custom/X3_crew'
    CUSTOM_FREE_XP = 'custom/freeXP'
    TOKEN = 'token'
    PAINT_ALL = 'paint/all'
    PAINT_SUMMER = 'paint/summer'
    PAINT_WINTER = 'paint/winter'
    PAINT_DESERT = 'paint/desert'
    CAMOUFLAGE_ALL = 'camouflage/all'
    CAMOUFLAGE_SUMMER = 'camouflage/summer'
    CAMOUFLAGE_WINTER = 'camouflage/winter'
    CAMOUFLAGE_DESERT = 'camouflage/desert'
    DECAL_1 = 'decal/1'
    DECAL_2 = 'decal/2'
    PROJECTION_DECAL = 'projection_decal/all'
    PERSONAL_NUMBER = 'personal_number/all'
    MODIFICATION = 'modification/all'
    STYLE = 'style/all'
    ATTACHMENT = 'attachment'
    ACHIEVEMENT = 'achievement'
    BADGE = 'badge'
    REFERRAL_BADGE = 'referralBadge'
    PLAYER_BADGE = 'playerBadges'
    SINGLE_ACHIEVEMENTS = 'singleAchievements'
    FRONTLINE_TOKEN = 'frontline_token'
    TRADE_IN_INFO = 'tradeInInfo'
    CREW_BOOK = 'crewBook'
    CREW_BOOK_BROCHURE = 'crew_book/brochure'
    CREW_BOOK_GUIDE = 'crew_book/guide'
    CREW_BOOK_CREW_BOOK = 'crew_book/crewBook'
    CREW_BOOK_PERSONAL_BOOK = 'crew_book/personalBook'
    CREW_BOOK_UNIVERSAL_BOOK = 'crew_book/universalBook'
    CREW_BOOK_UNIVERSAL_GUIDE = 'crew_book/universalGuide'
    CREW_BOOK_UNIVERSAL_BROCHURE = 'crew_book/universalBrochure'
    CREW_BOOK_RANDOM = 'crew_book/random'
    CREW_BOOK_BROCHURE_RANDOM = 'crew_book/brochure_random'
    CREW_BOOK_GUIDE_RANDOM = 'crew_book/guide_random'
    CREW_BOOK_MANUAL_RANDOM = 'crew_book/crewBook_random'
    BLUEPRINT = 'blueprint'
    BLUEPRINT_NATIONAL = 'blueprint/national'
    BLUEPRINT_INTELEGENCE_DATA = 'blueprint/intelligence_data'
    BLUEPRINT_ANY = 'blueprint/any'
    BLUEPRINT_NATIONAL_ANY = 'blueprint/nationalAny'
    BLUEPRINT_NATIONAL_RANDOM = 'blueprint/national_random'
    DEMOUNT_KIT = 'demountKit'
    REFERRAL_AWARDS = 'referral_awards'
    DEMOUNT_KITS = 'demountKit/common'
    OFFER = 'offer'
    OFFER_BROCHURE = 'offer/crew_book/brochure'
    OFFER_BATTLE_BOOSTER = 'offer/item/equipment'
    TMAN_TOKEN = 'tmanToken'

class ItemPackTypeGroup(CONST_CONTAINER):
    ITEM: tuple
    VEHICLE: tuple
    GOODIE: tuple
    CAMOUFLAGE: tuple
    PAINT: tuple
    STYLE: tuple
    MODIFICATION: tuple
    ATTACHMENT: tuple
    DECAL: tuple
    PROJECTION_DECAL: tuple
    PERSONAL_NUMBER: tuple
    CUSTOMIZATION: Any
    CUSTOM: tuple
    CREW: tuple
    TOKEN: tuple
    DISCOUNT: tuple
    TRADE_IN: tuple
    CREW_BOOKS: tuple
    OFFER: tuple
    TMAN_TOKEN: set

class CompensationType(CONST_CONTAINER):
    MONEY = 'money'

def getItemPackByGroupAndName(group, name, default=None):
    ...
def sanitizeResPath(relPath):
    ...
