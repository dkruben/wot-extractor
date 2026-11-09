# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_loading/preferences.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/preferences.py
import typing
if typing.TYPE_CHECKING:
    from ResMgr import DataSection
SECTION_NAME = 'gameLoading'

class GameLoadingPreferences(object):
    __slots__ = ('_gameLoadingPrefs', )

    def __init__(self, preferences):
        super(GameLoadingPreferences, self).__init__()
        if not preferences.has_key(SECTION_NAME):
            preferences.write(SECTION_NAME, '')
        self._gameLoadingPrefs = preferences[SECTION_NAME]

    def getLoadingMax(self, slideID):
        loadingMax = self._gameLoadingPrefs[slideID]
        if loadingMax is None:
            return loadingMax
        else:
            return loadingMax.asInt

    def setLoadingMax(self, slideID, value):
        self._gameLoadingPrefs.write(slideID, value)
