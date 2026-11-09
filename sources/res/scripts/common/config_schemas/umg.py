# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/config_schemas/umg.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/config_schemas/umg.py
from __future__ import absolute_import
from game_params_common.schema import GameParamsSchema
from dict2model import fields, models, schemas, validate
import typing

class WeightModel(models.Model):
    __slots__ = ('name', 'weight')

    def __init__(self, name, weight):
        super(WeightModel, self).__init__()
        self.name = name
        self.weight = weight

    def _reprArgs(self):
        return ('name={}, weight={}').format(self.name, self.weight)


class WeightsModel(models.Model):
    __slots__ = ('weights', '_weightByName')

    def __init__(self, weights):
        super(WeightsModel, self).__init__()
        self.weights = weights
        self._weightByName = {p.name: p for p in self.weights}

    def getWeightByName(self, name):
        return self._weightByName.get(name, None)

    def _reprArgs(self):
        return ('weights={}').format(self.weights)


_weightSchema = schemas.Schema[WeightModel](modelClass=WeightModel, fields={'name': (fields.String(deserializedValidators=validate.Length(minValue=2))), 
   'weight': (fields.Integer(deserializedValidators=validate.Range(0, 1000)))})
umgMissionsConfigSchema = GameParamsSchema[WeightsModel](gameParamsKey='umgMissions', modelClass=WeightsModel, fields={'weights': (fields.UniCapList(fieldOrSchema=_weightSchema, deserializedValidators=[
             validate.Length(minValue=1), validate.ValidateIterable([validate.IterableOfUnique('name')])]))})
umgEventsConfigSchema = GameParamsSchema[WeightsModel](gameParamsKey='umgEvents', modelClass=WeightsModel, fields={'weights': (fields.UniCapList(fieldOrSchema=_weightSchema, deserializedValidators=[
             validate.Length(minValue=1), validate.ValidateIterable([validate.IterableOfUnique('name')])]))})
