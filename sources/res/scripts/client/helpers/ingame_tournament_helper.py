# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/helpers/ingame_tournament_helper.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/ingame_tournament_helper.py
from __future__ import absolute_import
from enum import Enum

class IngameTournamentType(Enum):
    WCI = 'wci'
    OLS = 'ols'


class IngameTournamentState(Enum):
    INTRO = 'tournament_intro'
    IN_PROGRESS = 'tournament_in_live'
    BETWEEN_SHOWMATCHES = 'tournament_between_showmatch_days'
    FINISHED = 'tournament_finished'


class IngameTournamentBracketType(Enum):
    RR = 'RR'
    DE = 'DE'


class IngameTournamentMatchState(Enum):
    UPCOMING = 'upcoming'
    IN_LIVE = 'in_live'
    COMPLETED = 'completed'


class IngameTournamentUrlType(Enum):
    YOUTUBE = 'youtube'
    TWITCH = 'twitch'
    DOUYIN = 'douyin'
    HUYA = 'huya'


class IngameTournamentLogoSize(Enum):
    SMALL = '48x48'
    MEDIUM = '86x86'
    LARGE = '260x260'
    EXTRA_LARGE = '522x522'
