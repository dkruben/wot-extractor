# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/view/splash_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
import typing as typing
import BigWorld as BigWorld
import ScaleformFileLoader as ScaleformFileLoader
import Settings as Settings
import account_shared as account_shared
import game_loading_bindings as game_loading_bindings
import gui as gui
from SoundGroups import MASTER_VOLUME_DEFAULT as MASTER_VOLUME_DEFAULT
from gui.Scaleform import SCALEFORM_SWF_PATH_V3 as SCALEFORM_SWF_PATH_V3
from gui.Scaleform.daapi.view.external_components import ExternalFlashComponent as ExternalFlashComponent
from gui.Scaleform.daapi.view.external_components import ExternalFlashSettings as ExternalFlashSettings
from gui.Scaleform.daapi.view.meta.SplashScreenMeta import SplashScreenMeta as SplashScreenMeta
from gui.Scaleform.genConsts.SPLASHSCREENCONSTANTS import SPLASHSCREENCONSTANTS as SPLASHSCREENCONSTANTS
from gui.doc_loaders.GuiDirReader import GuiDirReader as GuiDirReader
from helpers import uniprof as uniprof
from ResMgr import DataSection as DataSection
_logger: Any
_VideoSettings: Any
VIDEO_FADE_OUT_TIME = 250
DEFAULT_VIDEO_BUFFERING_TIME = 2.0
ALWAYS_SHOW_SPLASH_SCREEN = 'development/alwaysShowIntroVideo'

class SplashScreen(ExternalFlashComponent, SplashScreenMeta):
    __slots__: tuple
    _userPrefs: Any
    _movieFiles: Any
    _writeSetting: Any
    _bufferTime: Any
    _soundValue: Any
    _canSkip: Any
    _currentMovie: Any
    _width: Any
    _height: Any
    def __init__(self, preferences):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def onLoad(self):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def onDelete(self):
        ...
    def onComplete(self):
        ...
    def onError(self):
        ...
    def fadeOutComplete(self):
        ...
    def setStageSize(self, width, height):
        ...
    def turnDAAPIon(self, setScript, movieClip):
        ...
    def tryToSkip(self):
        ...
    def applicationVisibilityChanged(self):
        ...
    def _populate(self):
        ...
    def _destroy(self):
        ...
    def _nextMovie(self):
        ...
    def _sendDataToFlash(self):
        ...
    def _allVideosComplete(self):
        ...
    def _getVideoVolume(self):
        ...

def getCompulsoryVideoSettings(path):
    ...
def versionChanged(userPrefs):
    ...
def mustShowSplashScreen(userPrefs):
    ...
def createSplashScreen(preferences):
    ...
