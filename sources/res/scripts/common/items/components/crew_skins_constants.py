# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/items/components/crew_skins_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/items/components/crew_skins_constants.py
CREW_SKINS_XML_FILE = 'crewSkins.xml'
CREW_SKINS_PRICE_GROUPS_XML_FILE = 'priceGroups.xml'
NO_CREW_SKIN_ID = 0
NO_CREW_SKIN_SOUND_SET = '-'

class CREW_SKIN_PROPERTIES_MASKS:
    SEX = 2
    NATION = 4
    EMPTY_MASK = 0


class CrewSkinType:
    CREW_SKIN = 1
    ITEM_GROUP = 2
    RANGE = {
     CREW_SKIN, ITEM_GROUP}


class TANKMAN_SEX:
    NONE = ''
    MALE = 'male'
    FEMALE = 'female'
    ALL = (
     MALE, FEMALE)
    AVAILABLE = (NONE, MALE, FEMALE)

    @staticmethod
    def getTankmanSex(tmanDescr):
        if tmanDescr.isFemale:
            return TANKMAN_SEX.FEMALE
        return TANKMAN_SEX.MALE


class CREW_SKIN_RARITY:
    COMMON = 1
    RARE = 2
    EPIC = 3
    ALL = (
     COMMON, RARE, EPIC)
