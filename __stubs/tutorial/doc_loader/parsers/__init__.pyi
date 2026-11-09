# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/doc_loader/parsers/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import ResMgr as ResMgr
from items import _xml as _xml
from tutorial.data.chapter import Chapter as Chapter, Scene as Scene
from tutorial.data.descriptor import DescriptorData as DescriptorData
from tutorial.data.hints import HintsData as HintsData
from tutorial.doc_loader import sub_parsers as sub_parsers
from tutorial.settings import BONUSES_REFS_FILE_PATH as BONUSES_REFS_FILE_PATH

class DescriptorParser(object):
    def parse(self, filePath):
        ...
    def __parseChapterSummaries(self, xmlCtx, section, descriptor):
        ...
    def _parseChapter(self, bonuses, descriptor, subSection, xmlCtx):
        ...
    def _getCommonChapterValues(self, bonuses, subSection, xmlCtx):
        ...
    def _parseBonus(self, xmlCtx, section, bonuses):
        ...

class ChapterParser(object):
    def _parseScene(self, xmlCtx, section, scene, flags, itemFlags, frontEffects=False):
        ...
    def _parseSharedScene(self, chapter, scene, flags, itemFlags):
        ...
    def parse(self, chapter, initial=False):
        ...
    def _parseVars(self, xmlCtx, section, flags, chapter):
        ...
    def _parseScenes(self, xmlCtx, section, chapter, flags, itemFlags, initial):
        ...
    def _parseTriggers(self, xmlCtx, section, flags, chapter):
        ...
    def _parseEntities(self, xmlCtx, section, flags, chapter):
        ...
    def _parseGlobalRuntimeEffects(self, xmlCtx, section, flags, chapter):
        ...

class BonusRefParser(object):
    def parse(self):
        ...

class HintsParser(object):
    @staticmethod
    def parse(filePath, excludedHints):
        ...
