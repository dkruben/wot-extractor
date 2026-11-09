# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/development_features/vse_dev.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import fnmatch as fnmatch
import logging as logging
import os as os
from functools import wraps as wraps
import VSE as VSE
from visual_script.qa_blocks import Assert as Assert
logger: Any
base_executors: dict
planObj = None

def wrapBlock(block, beforeExecution=None, execute=None, afterExecution=None):
    ...
def unwrapBlock(block):
    ...
def collectPlans(vseDir, testDir, include, exclude=None):
    ...
def runTestPlan(planPath, aspect=None):
    ...
