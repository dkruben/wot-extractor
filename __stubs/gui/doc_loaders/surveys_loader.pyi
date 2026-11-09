# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/doc_loaders/surveys_loader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple, defaultdict as defaultdict
import logging as logging
from gui.mapbox.mapbox_survey_helper import Condition as Condition, QuantifierTypes as QuantifierTypes, AlternativeOneManyQuestion as AlternativeOneManyQuestion, AlternativeQuestion as AlternativeQuestion, getQuestionClass as getQuestionClass, findQuestionById as findQuestionById
import resource_helper as resource_helper
from soft_exception import SoftException as SoftException
from shared_utils import findFirst as findFirst
_logger: Any
_SURVEYS_XML_PATH = 'gui/surveys.xml'
_SURVEYS = None
_Survey: Any
_GuiParams: Any
_AdditionalParam: Any
_TextParams: Any
_Responses: Any

def _readConditions(section, isRequired):
    ...
def _readCondition(section, isRequired):
    ...
def _readSourceSection(section):
    ...
def _readSomeSourceSection(section, sectionName):
    ...
def _readLinkedParameters(section):
    ...
def _readGuiParameters(section):
    ...
def _readOptions(section):
    ...
def _readResponses(section):
    ...
def _readQuestion(surveyGroup, questionSection, questionTypes):
    ...
def _readAlternativeQuestion(surveyGroup, questionSection, questionTypes, qId):
    ...
def _readSurveys():
    ...
def getSurvey(bonusType, surveyId):
    ...
