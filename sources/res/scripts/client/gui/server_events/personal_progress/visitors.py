# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/server_events/personal_progress/visitors.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/server_events/personal_progress/visitors.py
import typing
from collections import namedtuple
from personal_missions_constants import PROGRESS_TEMPLATE
from gui.server_events.personal_progress import metrics_wrappers
WrapperInfo = namedtuple('WrapperInfo', ('wrapper', 'isTopMetric'))

class WrappersVisitor(object):

    @classmethod
    def isSuitableForProgress(cls, progress):
        raise NotImplementedError

    @classmethod
    def getWrappers(cls):
        raise NotImplementedError


class BinaryProgressVisitor(WrappersVisitor):

    @classmethod
    def isSuitableForProgress(cls, progress):
        return progress.getTemplateID() == PROGRESS_TEMPLATE.BINARY

    @classmethod
    def getWrappers(cls):
        return [
         WrapperInfo(metrics_wrappers.wrapSimple, True)]


class ValueLikeBinaryProgressVisitor(WrappersVisitor):

    @classmethod
    def isSuitableForProgress(cls, progress):
        return progress.getTemplateID() == PROGRESS_TEMPLATE.VALUE and progress.getGoal() == 1

    @classmethod
    def getWrappers(cls):
        return [
         WrapperInfo(metrics_wrappers.wrapSimple, True)]


class ValueProgressVisitor(WrappersVisitor):

    @classmethod
    def isSuitableForProgress(cls, progress):
        return progress.getTemplateID() == PROGRESS_TEMPLATE.VALUE and progress.getGoal() != 1

    @classmethod
    def getWrappers(cls):
        return [
         WrapperInfo(metrics_wrappers.wrapRangeValue, False),
         WrapperInfo(metrics_wrappers.wrapCurrentValue, True)]


class LobbyValueProgressVisitor(ValueProgressVisitor):

    @classmethod
    def isSuitableForProgress(cls, progress):
        return progress.getTemplateID() == PROGRESS_TEMPLATE.VALUE and progress.isCumulative()


class CounterProgressVisitor(WrappersVisitor):

    @classmethod
    def isSuitableForProgress(cls, progress):
        return progress.getTemplateID() == PROGRESS_TEMPLATE.COUNTER

    @classmethod
    def getWrappers(cls):
        return [
         WrapperInfo(metrics_wrappers.wrapRangeValue, False),
         WrapperInfo(metrics_wrappers.wrapCurrentValue, False),
         WrapperInfo(metrics_wrappers.wrapVehiclesValue, True)]


class LimiterProgressVisitor(WrappersVisitor):

    @classmethod
    def isSuitableForProgress(cls, progress):
        return progress.getLimiter() is not None

    @classmethod
    def getWrappers(cls):
        return [
         WrapperInfo(metrics_wrappers.wrapLimiterValue, False)]


class TimerProgressVisitor(WrappersVisitor):

    @classmethod
    def isSuitableForProgress(cls, progress):
        return progress.getCountDown() is not None

    @classmethod
    def getWrappers(cls):
        return [
         WrapperInfo(metrics_wrappers.wrapTimerValue, False)]
