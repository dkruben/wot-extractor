# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/items_parameters/xml_reader.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/items_parameters/xml_reader.py
from __future__ import absolute_import
import resource_helper
from future.utils import iteritems
_SIMPLIFIED_COEFFICIENTS_PATH = 'gui/params_coefficients.xml'

def _getBonusTypesGenerator(bonusTypes):
    for bonusType, items in iteritems(bonusTypes):
        for itemName in items:
            yield (itemName, bonusType)


def read():
    params = {}
    for item in resource_helper.root_iterator(_SIMPLIFIED_COEFFICIENTS_PATH):
        params[item.name] = item.value

    coefficients = params.pop('coefficients')
    bonuses = params.pop('bonuses')
    for paramName, bonusTypes in iteritems(bonuses):
        bonuses[paramName] = tuple(_getBonusTypesGenerator(bonusTypes))

    return (coefficients, bonuses)
