# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/common/stat_column_settings_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel

class ColumnEnum(Enum):
    KILLS = 'kills'
    DAMAGE = 'damage'
    ASSIST = 'assist'
    BLOCKED = 'blocked'
    PLACE = 'place'
    ANOMALIES = 'anomalies'
    KEYS = 'keys'
    BOSSDAMAGE = 'bossDamage'

class StatColumnSettingsModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=1, commands=0):
        ...
    def getVisibleColumns(self):
        ...
    def setVisibleColumns(self, value):
        ...
    @staticmethod
    def getVisibleColumnsType():
        ...
    def _initialize(self):
        ...
