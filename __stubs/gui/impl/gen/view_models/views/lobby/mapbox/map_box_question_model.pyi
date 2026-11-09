# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/mapbox/map_box_question_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.wrappers.user_list_model import UserListModel as UserListModel
from gui.impl.gen.view_models.views.lobby.mapbox.map_box_answers_model import MapBoxAnswersModel as MapBoxAnswersModel
from gui.impl.gen.view_models.views.lobby.mapbox.map_box_option_model import MapBoxOptionModel as MapBoxOptionModel

class QuestionType(Enum):
    VEHICLE = 'vehicle'
    IMAGE = 'image'
    TABLE = 'table'
    INTERACTIVE_MAP = 'interactiveMap'
    TEXT = 'text'
    UNDEFINED = 'undefined'
    ALTERNATIVE = 'alternative'
    MULTIPLE_CHOICE = 'multipleChoice'

class MapBoxQuestionModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=8, commands=0):
        ...
    @property
    def answers(self):
        ...
    @staticmethod
    def getAnswersType():
        ...
    @property
    def options(self):
        ...
    @staticmethod
    def getOptionsType():
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def getImagePath(self):
        ...
    def setImagePath(self, value):
        ...
    def getPathPrefix(self):
        ...
    def setPathPrefix(self, value):
        ...
    def getShowIcons(self):
        ...
    def setShowIcons(self, value):
        ...
    def getQuestionId(self):
        ...
    def setQuestionId(self, value):
        ...
    def getTitleParams(self):
        ...
    def setTitleParams(self, value):
        ...
    @staticmethod
    def getTitleParamsType():
        ...
    def _initialize(self):
        ...
