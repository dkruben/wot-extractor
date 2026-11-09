# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/personal_progress/builders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import quest_progress as quest_progress
from gui.server_events.personal_progress import progress as progress
from gui.server_events.personal_progress import strategy as strategy
from personal_missions_constants import DISPLAY_TYPE as DISPLAY_TYPE, CONTAINER as CONTAINER, DESCRIPTIONS as DESCRIPTIONS

class ClientProgressBuilder(quest_progress.IProgressBuilder):
    @classmethod
    def build(cls, progressID, progressData):
        ...
    @classmethod
    def _createBodyProgress(cls, commonProgress, clientData):
        ...
    @classmethod
    def _createHeaderProgress(cls, commonProgress, clientData):
        ...
    @classmethod
    def _getCommonProgress(cls, progressID, progressData):
        ...
    @classmethod
    def _getValuesStrategy(cls, clientData):
        ...
    @classmethod
    def _getHeaderLabelsStrategy(cls, clientData):
        ...

class BinaryProgressBuilder(ClientProgressBuilder, quest_progress.BinaryProgressBuilder):
    @classmethod
    def _getValuesStrategy(cls, clientData):
        ...
    @classmethod
    def _getCommonProgress(cls, progressID, progressData):
        ...

class ValueProgressBuilder(ClientProgressBuilder, quest_progress.ValueProgressBuilder):
    @classmethod
    def _getValuesStrategy(cls, clientData):
        ...
    @classmethod
    def _createBodyProgress(cls, commonProgress, clientData):
        ...
    @classmethod
    def _getCommonProgress(cls, progressID, progressData):
        ...

class VehicleTypesProgressBuilder(ClientProgressBuilder, quest_progress.CounterProgressBuilder):
    @classmethod
    def _getValuesStrategy(cls, clientData):
        ...
    @classmethod
    def _createBodyProgress(cls, commonProgress, clientData):
        ...
    @classmethod
    def _getCommonProgress(cls, progressID, progressData):
        ...

class BiathlonProgressBuilder(ClientProgressBuilder, quest_progress.BattlesSeriesProgressBuilder):
    @classmethod
    def _getValuesStrategy(cls, clientData):
        ...
    @classmethod
    def _createHeaderProgress(cls, commonProgress, clientData):
        ...
    @classmethod
    def _getCommonProgress(cls, progressID, progressData):
        ...
