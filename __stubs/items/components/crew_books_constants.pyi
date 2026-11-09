# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/crew_books_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from builtins import range as range
CREW_BOOKS_XML_FILE = 'crewBooks.xml'
CREW_BOOKS_PRICE_GROUPS_XML_FILE = 'priceGroups.xml'
CREW_BOOK_TYPES_XML_FILE = 'crewBookTypes.xml'
CREW_BOOK_DISPLAYED_AWARDS_COUNT = 11

class CREW_BOOK_PROPERTIES_MASKS:
    FULL_CREW = 1
    ROLE_LEVEL = 2
    SPECIALIZATION = 4
    EMPTY_MASK = 0
    ALL: tuple

class CrewBookCacheType:
    CREW_BOOK = 1
    ITEM_GROUP = 2
    RANGE: set

class CREW_BOOK_RARITY:
    CREW_COMMON = 'brochure'
    CREW_RARE = 'guide'
    CREW_EPIC = 'crewBook'
    PERSONAL = 'personalBook'
    UNIVERSAL = 'universalBook'
    UNIVERSAL_GUIDE = 'universalGuide'
    UNIVERSAL_BROCHURE = 'universalBrochure'
    ALL_TYPES: tuple
    NO_NATION_TYPES: tuple
    ORDER: Any

class CREW_BOOK_SPREAD:
    CREW_BOOK = 'crewBook'
    PERSONAL_BOOK = 'personalBook'
    CREW_BOOK_NO_NATION = 'universalBook'
    ALL_SPREADS: tuple
