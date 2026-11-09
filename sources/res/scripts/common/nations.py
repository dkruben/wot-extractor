# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/nations.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/nations.py
NAMES = ('ussr', 'germany', 'usa', 'china', 'france', 'uk', 'japan', 'czech', 'sweden',
         'poland', 'italy')
INDICES = dict((n, i) for i, n in enumerate(NAMES))
MAP = dict(enumerate(NAMES))
AVAILABLE_NAMES = ('ussr', 'germany', 'usa', 'china', 'france', 'uk', 'japan', 'czech',
                   'sweden', 'poland', 'italy')
NONE_INDEX = 15
ALL_NATIONS_INDEX = -1

class Alliances(object):
    USSR = 'Alliance-USSR'
    GERMANY = 'Alliance-Germany'
    USA = 'Alliance-USA'
    FRANCE = 'Alliance-France'


ALLIANCES_TAGS_ORDER = (
 Alliances.USSR, Alliances.GERMANY, Alliances.USA, Alliances.FRANCE)
ALLIANCES_TAGS = frozenset(ALLIANCES_TAGS_ORDER)
ALLIANCE_IDS = dict((value, index) for index, value in enumerate(ALLIANCES_TAGS_ORDER))
ALLIANCE_TO_NATIONS = {(Alliances.USSR): (frozenset(('ussr', 'china'))), 
   (Alliances.GERMANY): (frozenset(('germany', 'japan'))), 
   (Alliances.USA): (frozenset(('usa', 'uk', 'poland'))), 
   (Alliances.FRANCE): (frozenset(('france', 'czech', 'sweden', 'italy')))}
ALLIANCE_IDS_MAP = {ai: set(INDICES[n] for n in ALLIANCE_TO_NATIONS[an]) for an, ai in ALLIANCE_IDS.items()}
NATION_TO_ALLIANCE_IDS_MAP = {ni: ai for ni in ALLIANCE_IDS_MAP.items()}
