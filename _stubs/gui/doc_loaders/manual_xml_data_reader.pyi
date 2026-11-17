# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/doc_loaders/manual_xml_data_reader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
import logging as logging
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers.html import translation as translation
import resource_helper as resource_helper
from gui.Scaleform.genConsts.MANUAL_TEMPLATES import MANUAL_TEMPLATES as MANUAL_TEMPLATES
from gui.shared.utils.functions import makeTooltip as makeTooltip
_logger: Any
_CHAPTERS_DATA_PATH = 'gui/manual/'
_CHAPTERS_LIST_XML = 'chapters_list.xml'
_MANUAL_LESSON_TEMPLATES: dict

class ManualPageTypes(object):
    HINTS_PAGE = 'hints_page'
    MAPS_TRAINING_PAGE = 'maps_training_page'
    VIDEO_PAGE = 'video_page'

def getChapters(filterFunction):
    ...
def getPagesIndexesList(filterFunction):
    ...
def getChaptersIndexesList(filterFunction):
    ...
def getChapterData(chapterFileName, filterFunction, chapterTitle=''):
    ...
def __isNew(lessonCtx, lessonSection):
    ...
def __readChapter(ctx, root, filterFunction, chapterTitle=''):
    ...
def __readChapters(ctx, root, filterFunction):
    ...
def __getChapterAttributes(chapterFileName, filterFunction):
    ...
def __getCustomSectionValue(ctx, section, name, safe=False):
    ...
def __getVideoRendererData(lessonCtx, lessonSection):
    ...
def __getHintsRendererData(lessonCtx, lessonSection):
    ...
