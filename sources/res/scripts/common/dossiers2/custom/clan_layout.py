# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/dossiers2/custom/clan_layout.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/dossiers2/custom/clan_layout.py
from __future__ import absolute_import
from dossiers2.common.DossierBlockBuilders import *
_rareAchievementsBlockBuilder = ListBlockBuilder('rareAchievements', 'I', {})
clanDossierLayout = (
 _rareAchievementsBlockBuilder,)
CLAN_DOSSIER_LIST_BLOCKS = [b.name for b in clanDossierLayout if isinstance(b, ListBlockBuilder)]
