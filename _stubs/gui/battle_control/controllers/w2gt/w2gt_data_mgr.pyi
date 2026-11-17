# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/w2gt/w2gt_data_mgr.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import typing as typing
from typing import Optional as Optional, Dict as Dict, List as List, Tuple as Tuple
from helpers.server_settings import _W2GTConfig as _W2GTConfig
from gui.game_control.w2gt_controller import _W2gtResponseData as _W2gtResponseData
_ZONE_TYPE_MAP: dict

class _ZoneTags(object):
    BRAWLING = 'brawling'
    AMBUSH = 'ambush'
    UNIVERSAL = 'universal'
    RECON = 'recon'
    ARTILLERY = 'artillery'
    UNKNOWN = 'unknown'
    ALL: tuple

# base nao representavel no stub: namedtuple(...)
class W2gtProgress:
    def __new__(cls, **kwargs):
        ...
    @property
    def isCapable(self):
        ...
    def asDict(self):
        ...
    def replace(self, **kwargs):
        ...

class W2GTDataMgr(object):
    __progress: Any
    __w2gtConfig: Any
    __zones: Any
    def __init__(self):
        ...
    def init(self, data, progress, w2gtConfig):
        ...
    def __readData(self, data):
        ...
    @property
    def progress(self):
        ...
    @property
    def zones(self):
        ...
    @property
    def config(self):
        ...
    def destroy(self):
        ...
    def __readZones(self, data):
        ...

class _BattleZone(object):
    __id: Any
    __tags: Any
    __zoneType: Any
    __area2D: Any
    __center2D: Any
    def __init__(self, zoneID, ctx):
        ...
    @property
    def zoneID(self):
        ...
    @property
    def zoneType(self):
        ...
    @property
    def area2D(self):
        ...
    @property
    def center2D(self):
        ...
    @staticmethod
    def _readTags(ctx):
        ...
