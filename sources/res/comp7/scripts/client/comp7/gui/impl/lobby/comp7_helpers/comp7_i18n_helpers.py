# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/comp7_helpers/comp7_i18n_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/comp7_helpers/comp7_i18n_helpers.py
from __future__ import absolute_import
from gui.impl import backport
from gui.impl.gen import R
from comp7.gui.impl.gen.view_models.views.lobby.enums import Rank, Division
RANK_MAP = {(Rank.FIRST): 'first', 
   (Rank.SECOND): 'second', 
   (Rank.THIRD): 'third', 
   (Rank.FOURTH): 'fourth', 
   (Rank.FIFTH): 'fifth', 
   (Rank.SIXTH): 'sixth'}
DIVISION_MAP = {(Division.A): 'A', 
   (Division.B): 'B', 
   (Division.C): 'C', 
   (Division.D): 'D', 
   (Division.E): 'E'}

def getRankLocale(rank):
    rankString = RANK_MAP[Rank(rank)]
    return backport.text(R.strings.comp7_ext.rank.dyn(rankString)())


def getDivisionLocale(division):
    divisionString = DIVISION_MAP[Division(division)]
    return backport.text(R.strings.comp7_ext.division.dyn(divisionString)())
