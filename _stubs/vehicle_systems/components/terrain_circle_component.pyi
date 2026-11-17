# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/terrain_circle_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import math as math
import typing as typing
import BigWorld as BigWorld
import Math as Math
from Math import Vector2 as Vector2
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from BigWorld import PyTerrainSelectedArea as PyTerrainSelectedArea
g_logger: Any
MIN_OVER_TERRAIN_HEIGHT = 0
MIN_UPDATE_INTERVAL = 0

class TerrainCircleComponent(CallbackDelayer):
    CUT_OFF_ANGLE: Any
    __maxUpdateInterval: Any
    __areaVisual: Any
    __motor: Any
    __model: Any
    __vehicleID: Any
    __isVisible: Any
    def __init__(self):
        ...
    def configure(self, radius, terrainCircleSettings):
        ...
    def destroy(self):
        ...
    def isVisible(self):
        ...
    def isAttached(self):
        ...
    def setVisible(self, visible=True):
        ...
    def attach(self, vehicleID):
        ...
    def detach(self):
        ...
    def __attachAreaVisualToModel(self):
        ...
    def __detachAreaVisualFromModel(self):
        ...
    def __setMotor(self):
        ...
    def __removeMotor(self):
        ...
    def __create(self):
        ...
    def __update(self):
        ...
    def __getUpdateInterval(self):
        ...
