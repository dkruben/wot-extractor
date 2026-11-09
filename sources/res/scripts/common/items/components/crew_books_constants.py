# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/items/components/crew_books_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/items/components/crew_books_constants.py
from __future__ import absolute_import
from builtins import range
CREW_BOOKS_XML_FILE = 'crewBooks.xml'
CREW_BOOKS_PRICE_GROUPS_XML_FILE = 'priceGroups.xml'
CREW_BOOK_TYPES_XML_FILE = 'crewBookTypes.xml'
CREW_BOOK_DISPLAYED_AWARDS_COUNT = 11

class CREW_BOOK_PROPERTIES_MASKS:
    FULL_CREW = 1
    ROLE_LEVEL = 2
    SPECIALIZATION = 4
    EMPTY_MASK = 0
    ALL = (
     FULL_CREW, ROLE_LEVEL, SPECIALIZATION)


class CrewBookCacheType:
    CREW_BOOK = 1
    ITEM_GROUP = 2
    RANGE = {
     CREW_BOOK, ITEM_GROUP}


class CREW_BOOK_RARITY:
    CREW_COMMON = 'brochure'
    CREW_RARE = 'guide'
    CREW_EPIC = 'crewBook'
    PERSONAL = 'personalBook'
    UNIVERSAL = 'universalBook'
    UNIVERSAL_GUIDE = 'universalGuide'
    UNIVERSAL_BROCHURE = 'universalBrochure'
    ALL_TYPES = (
     CREW_COMMON, CREW_RARE, CREW_EPIC, PERSONAL, UNIVERSAL_BROCHURE, UNIVERSAL_GUIDE, UNIVERSAL)
    NO_NATION_TYPES = (PERSONAL, UNIVERSAL, UNIVERSAL_GUIDE, UNIVERSAL_BROCHURE)
    ORDER = dict(zip(ALL_TYPES, range(len(ALL_TYPES))))


class CREW_BOOK_SPREAD:
    CREW_BOOK = 'crewBook'
    PERSONAL_BOOK = 'personalBook'
    CREW_BOOK_NO_NATION = 'universalBook'
    ALL_SPREADS = (
     CREW_BOOK, PERSONAL_BOOK, CREW_BOOK_NO_NATION)
