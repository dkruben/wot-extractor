# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/helpers/log/handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/log/handlers.py
from __future__ import absolute_import, print_function
import logging, sys, traceback
from contextlib import closing
from future.utils import viewitems
import BigWorld
from py2to3.moves.io import FastStringIO
_LOG_LEVEL_2_BW_FUNCTION = {(logging.NOTSET): (BigWorld.logTrace), 
   (logging.DEBUG): (BigWorld.logDebug), 
   (logging.INFO): (BigWorld.logInfo), 
   (logging.WARN): (BigWorld.logWarning), 
   (logging.WARNING): (BigWorld.logWarning), 
   (logging.ERROR): (BigWorld.logError), 
   (logging.CRITICAL): (BigWorld.logCritical), 
   (logging.FATAL): (BigWorld.logCritical)}

class WotFormatter(logging.Formatter):

    def formatException(self, ei):
        return ('').join(traceback.format_exception(*ei))


class WotExtendedFormatter(WotFormatter):

    def __init__(self, fmt=None, datefmt=None, frameSize=-1):
        super(WotExtendedFormatter, self).__init__(fmt, datefmt)
        self._frameSize = frameSize

    def formatException(self, ei):
        message = super(WotExtendedFormatter, self).formatException(ei)
        _, _, etb = ei
        frames = []
        while etb.tb_next:
            etb = etb.tb_next

        frame = etb.tb_frame
        while frame:
            frames.append(frame)
            frame = frame.f_back

        with closing(FastStringIO()) as sio:
            print(message, file=sio)
            for frame in reversed(frames):
                print('', file=sio)
                print(('Frame {} in {} at line {}').format(frame.f_code.co_name, frame.f_code.co_filename, frame.f_lineno), file=sio)
                size = self._frameSize
                for key, value in viewitems(frame.f_locals):
                    if not size:
                        break
                    size -= 1
                    try:
                        print(('\t{:>20} = {}').format(key, repr(value)), file=sio)
                    except Exception:
                        print(('\t{:>20} = <UNDEFINED>').format(key), file=sio)

            return sio.getvalue()


class WotLogHandler(logging.Handler):

    def emit(self, record):
        logCategory = record.name.encode(sys.getdefaultencoding())
        msg = self.format(record)
        finalMessage = msg.encode(sys.getdefaultencoding())
        logFunction = _LOG_LEVEL_2_BW_FUNCTION[record.levelno]
        logFunction(logCategory, finalMessage, None)
        return
