# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/bwobsolete_weather.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import ResMgr as ResMgr
import FX as FX
import random as random
from functools import partial as partial
import traceback as traceback
import Bloom as Bloom
from Listener import Listenable as Listenable
import Math as Math
import game as Personality
import Personality as Personality
weatherXML: Any
s_weather = None

class WeatherSystem:
    name: Any
    skyBoxes: Any
    skyBoxModels: Any
    rain: Any
    sun: Any
    ambient: Any
    fog: Any
    windSpeed: Any
    windGustiness: Any
    skyBoxFogFactor: Any
    bloom: Any
    bloomPreset: Any
    fader: Any
    fx: Any
    fxName: Any
    loaded: Any
    tempCopy: Any
    def __init__(self, ds):
        ...
    def _loadSkyBoxes(self, callback=None, immediate=False):
        ...
    def _onLoadSkyBoxes(self, callback, resourceRef):
        ...
    def _unload(self):
        ...
    def _loadFX(self, callback=None):
        ...
    def _onLoadFX(self, callback, resourceRef):
        ...
    def _fadeOutFX(self):
        ...
    def fadeIn(self, fadingIn, fadeSpeed, immediate=False):
        ...
    def _fogAmount(self, amount):
        ...
    def prepareResources(self, callback=None, immediate=False):
        ...
    def setFadeSpeed(self, duration):
        ...
    def edUnloadSkyBoxes(self):
        ...
    def edReloadSkyBoxes(self):
        ...

class Weather(Listenable):
    fadeSpeed: Any
    system: Any
    randomWeatherCallback: Any
    summoning: Any
    pendingWeatherChange: Any
    localOverride: Any
    overridenWeather: Any
    currentSpaceID: Any
    weatherController: Any
    sunlightController: Any
    ambientController: Any
    fogController: Any
    skyBoxFogFactor: Any
    def __init__(self):
        ...
    def toggleRandomWeather(self, force=None):
        ...
    def isWeatherRandom(self):
        ...
    def nextWeatherSystem(self, direction, immediate=False):
        ...
    def _randomWeather(self, initial=False):
        ...
    def _setFadeSpeed(self, duration):
        ...
    def _weatherSystemsForCurrentSpace(self):
        ...
    def onChangeSpace(self, spaceID=-1, spaceSettings=None):
        ...
    def summon(self, systemName, immediate=False, serverSync=False, resummon=False):
        ...
    def override(self, systemName, immediate=False):
        ...
    def _systemReadySummon(self, system, immediate, resummon):
        ...
    def _onSystemSummoned(self):
        ...
    def newSystemByName(self, systemName):
        ...
    def _animateValue(self, value, v4a, index):
        ...
    def _animateVector4(self, v4a, value):
        ...
    def rain(self, amount):
        ...
    def fog(self, value, applyToSystem=True):
        ...
    def sun(self, value):
        ...
    def ambient(self, value):
        ...

def weather():
    ...
def fini():
    ...
