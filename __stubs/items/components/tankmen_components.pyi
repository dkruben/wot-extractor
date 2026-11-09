# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/tankmen_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from debug_utils import LOG_ERROR as LOG_ERROR
from items.components import component_constants as component_constants
from items.components import legacy_stuff as legacy_stuff
from items.components import skills_constants as skills_constants
from soft_exception import SoftException as SoftException
from past.builtins import unicode as unicode
from items.components import shared_components as shared_components

class SPECIAL_VOICE_TAG(object):
    BUFFON = 'buffonSpecialVoice'
    SABATON = 'sabatonSpecialVoice'
    OFFSPRING = 'offspringSpecialVoice'
    RACER = 'racerSpecialVoice'
    RACER_EN = 'racerSpecialVoiceEn'
    CELEBRITY_2021 = 'celebrity21SpecialVoice'
    CELEBRITY_2022 = 'celebrity22SpecialVoice'
    CELEBRITY_2023 = 'celebrity23SpecialVoice'
    CELEBRITY_2024 = 'celebrity24SpecialVoice'
    CELEBRITY_2025 = 'celebrity25SpecialVoice'
    CELEBRITY_2026 = 'celebrity26SpecialVoice'
    DAY_OF_COSMONAUTICS_21 = 'gagarin21_specialVoice'
    MIHO = 'mihoSpecialVoice'
    YHA = 'yhaSpecialVoice'
    QUICKY_BABY = 'quickyBabySpecialVoice'
    WITCHES_CREW = 'witchesSpecialVoice'
    HAND_OF_BLOOD = 'handOfBloodSpecialVoice'
    NAMELESS = 'japan:J29_Nameless'
    EDELWEISS = 'japan:J30_Edelweiss'
    TALKTOME_GOOSE = 'talktomeGooseSpecialVoice'
    SKILL_4_LTU = 'skill4ltuSpecialVoice'
    ALICE = 'aliceSpecialVoice'
    DARJEELING = 'darjeelingSpecialVoice'
    KEI = 'keiSpecialVoice'
    HW25_QUICKYBABY = 'hw25_Quickybaby_SpecialVoice'
    HW25_MAILAND = 'hw25_Mailand_SpecialVoice'
    HW25_MOUZ_AKROBAT = 'hw25_MouzAkrobat_SpecialVoice'
    HW25_SKILL4LTU = 'hw25_Skill4ltu_SpecialVoice'
    HW25_LU_JUN_CN = 'hw25_LuJun_CN_SpecialVoice'
    HW25_TITI_CN = 'hw25_Titi_CN_SpecialVoice'
    HW25_DA_KUN_CN = 'hw25_DaKun_CN_SpecialVoice'
    HW25_PANCHEZHANG_CN = 'hw25_Panchezhang_CN_SpecialVoice'
    ERWIN = 'erwinSpecialVoice'
    JAGER_MAILAND = 'jager_mailand_SpecialVoice'
    JAGER_MOUZAKROBAT = 'jager_mouzAkrobat_SpecialVoice'
    FR_SPARK = 'fr_spark_SpecialVoice'
    NAKAJIMA = 'nakajima_SpecialVoice'
    BATTLE_OF_BLOGGERS: tuple
    BATTLE_OF_BLOGGERS_2021: tuple
    G_I_JOE_TWITCH_2021: tuple
    WHITE_TIGER_EVENT_2021: tuple
    WHITE_TIGER_EVENT_2022: tuple
    WHITE_TIGER_EVENT_2023: tuple
    WHITE_TIGER_EVENT_2024: tuple
    SABATON_2021 = 'sabaton21_specialVoice'
    G_I_JOE_2022: tuple
    BPH_2022: tuple
    BP_12_M: tuple
    BP_H2: tuple
    BP_13: tuple
    CYGAN = 'cygan_SpecialVoice'
    MARTY_VOLE = 'martyVole_SpecialVoice'
    CTM_24: tuple
    ERIKA = 'erikaSpecialVoice'
    MIKA = 'mikaSpecialVoice'
    BP_14_M: tuple
    MT_LB_1 = 'tankmen_mtlb1_1'
    BP_15_M: tuple
    BP_H4: tuple
    BP_16_M: tuple
    BP_17_DC_M: tuple
    BP_18_M: tuple
    BP_18_NM: tuple
    BP_H5: tuple
    BP_H6: tuple
    BP_19_M: tuple
    BP_20_M: tuple
    BP_21_M: tuple
    MT_LB_4 = 'tankmen_mtlb4_1'
    ALL: Any

class SPECIAL_CREW_TAG(object):
    SABATON = 'sabatonCrew'
    OFFSPRING = 'offspringCrew'
    MIHO = 'mihoCrew'
    YHA = 'yhaCrew'
    WITCHES_CREW = 'witchesCrew'
    MIKA_CREW = 'mikaCrew'
    DARJEELING_CREW = 'darjeelingCrew'
    HW25_CREW = 'hw25_Crew'
    HW25_CREW_CN = 'hw25_Crew_CN'
    HIPPO_CREW = 'hippoCrew'
    LEOPON_CREW = 'leoponCrew'
    ALL: tuple

class GROUP_TAG(object):
    PASSPORT_REPLACEMENT_FORBIDDEN = 'passportReplacementForbidden'
    RESTRICTIONS: tuple
    RANGE: Any

class Rank(legacy_stuff.LegacyStuff):
    __slots__: tuple
    __name: Any
    __i18n: Any
    __icon: Any
    def __init__(self, name, i18n=None, icon=None):
        ...
    def __repr__(self):
        ...
    @property
    def name(self):
        ...
    @property
    def userString(self):
        ...
    @property
    def icon(self):
        ...

class RanksSet(object):
    __slots__: tuple
    __ranks: Any
    __rankIDsByNames: Any
    def __init__(self):
        ...
    def __repr__(self):
        ...
    def add(self, rank):
        ...
    def getRankByID(self, rankID):
        ...
    def getRankByName(self, name):
        ...
    def getIDByName(self, name):
        ...
    def generator(self):
        ...

class RoleRanks(legacy_stuff.LegacyStuff):
    __slots__: tuple
    __ranks: Any
    def __init__(self):
        ...
    def __repr__(self):
        ...
    @property
    def commander(self):
        ...
    @property
    def radioman(self):
        ...
    @property
    def driver(self):
        ...
    @property
    def gunner(self):
        ...
    @property
    def loader(self):
        ...
    def getRanksIDs(self, roleName):
        ...
    def getRankID(self, roleName, rankIdx):
        ...
    def setRanksIDs(self, roleName, roleIDs):
        ...

class NationGroup(legacy_stuff.LegacyStuff):
    __slots__: tuple
    __groupID: Any
    __name: Any
    __isFemales: Any
    __notInShop: Any
    __firstNamesIDs: Any
    __lastNamesIDs: Any
    __iconsIDs: Any
    __weight: Any
    __tags: Any
    __roles: Any
    def __init__(self, groupID, name, isFemales, notInShop, firstNamesIDs, lastNamesIDs, iconsIDs, weight, tags, roles):
        ...
    def __repr__(self):
        ...
    @property
    def groupID(self):
        ...
    @property
    def name(self):
        ...
    @property
    def isFemales(self):
        ...
    @property
    def notInShop(self):
        ...
    @property
    def firstNames(self):
        ...
    @property
    def firstNamesList(self):
        ...
    @property
    def lastNames(self):
        ...
    @property
    def lastNamesList(self):
        ...
    @property
    def icons(self):
        ...
    @property
    def iconsList(self):
        ...
    @property
    def weight(self):
        ...
    @weight.setter
    def weight(self, value):
        ...
    @property
    def tags(self):
        ...
    @property
    def roles(self):
        ...
    @property
    def rolesList(self):
        ...
    @property
    def isUnique(self):
        ...

class NationConfig(legacy_stuff.LegacyStuff):
    __slots__: tuple
    __name: Any
    __normalGroups: Any
    __premiumGroups: Any
    __roleRanks: Any
    __firstNames: Any
    __lastNames: Any
    __icons: Any
    __ranks: Any
    def __init__(self, name, normalGroups=None, premiumGroups=None, roleRanks=None, firstNames=None, lastNames=None, icons=None, ranks=None):
        ...
    def __repr__(self):
        ...
    @property
    def normalGroups(self):
        ...
    @property
    def premiumGroups(self):
        ...
    @property
    def roleRanks(self):
        ...
    @property
    def firstNames(self):
        ...
    @property
    def lastNames(self):
        ...
    @property
    def icons(self):
        ...
    @property
    def ranks(self):
        ...
    def hasFirstName(self, nameID):
        ...
    def hasLastName(self, nameID):
        ...
    def hasIcon(self, iconID):
        ...
    def getGroups(self, isPremium):
        ...
    def getRoleRanks(self, roleName):
        ...
    def getFirstName(self, nameID):
        ...
    def getLastName(self, nameID):
        ...
    def getIcon(self, iconID):
        ...
    def getExtensionLessIcon(self, iconID):
        ...
    def getRank(self, rankID):
        ...

class LoreGroupComponent(object):
    __slots__: tuple
    DEFAULT = 'default'
    descr_by_nation: Any
    def __init__(self, descr):
        ...
    def addDescrForNation(self, nation, descr):
        ...
    def getDescrForNation(self, nation):
        ...

class LoreComponent(object):
    __slots__: tuple
    SECTION = 'descr_by_group'
    NATION_SECTION = 'nations'
    __DEFAULT = 'default'
    descr_by_group: Any
    def __init__(self):
        ...
    def addDescrForGroup(self, group, descr):
        ...
    def addNationDescrForGroup(self, group, naiton, descr):
        ...
    def getLoreDescrForGroup(self, group, nation=..., isDefault=False):
        ...
    def __repr__(self):
        ...
