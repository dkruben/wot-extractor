# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/BWLogging.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/BWLogging.py
from __future__ import absolute_import
import json, logging, sys, BigWorld

class BWLogger(logging.Logger):
    TRACE = logging.DEBUG - 1
    NOTICE = logging.INFO + 1
    HACK = logging.CRITICAL + 1

    def __init__(self, name, level=logging.NOTSET):
        logging.Logger.__init__(self, name, level)

    def trace(self, msg, *args, **kw):
        if self.isEnabledFor(BWLogger.TRACE):
            self._log(BWLogger.TRACE, msg, args, **kw)

    def notice(self, msg, *args, **kw):
        if self.isEnabledFor(BWLogger.NOTICE):
            self._log(BWLogger.NOTICE, msg, args, **kw)

    def hack(self, msg, *args, **kw):
        if self.isEnabledFor(BWLogger.HACK):
            self._log(BWLogger.HACK, msg, args, **kw)


logLevelToBigWorldFunction = {(logging.NOTSET): (BigWorld.logTrace), 
   (BWLogger.TRACE): (BigWorld.logTrace), 
   (logging.DEBUG): (BigWorld.logDebug), 
   (logging.INFO): (BigWorld.logInfo), 
   (BWLogger.NOTICE): (BigWorld.logNotice), 
   (logging.WARN): (BigWorld.logWarning), 
   (logging.WARNING): (BigWorld.logWarning), 
   (logging.ERROR): (BigWorld.logError), 
   (logging.CRITICAL): (BigWorld.logCritical), 
   (logging.FATAL): (BigWorld.logCritical), 
   (BWLogger.HACK): (BigWorld.logHack)}

class BWLogRedirectionHandler(logging.Handler):

    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):
        logCategory = record.name.encode(sys.getdefaultencoding())
        msg = record.getMessage()
        finalMessage = msg.encode(sys.getdefaultencoding())
        if hasattr(record, 'metadata'):
            logMetaData = json.dumps(record.metadata)
        else:
            logMetaData = None
        bwInternalLogFunction = logLevelToBigWorldFunction[record.levelno]
        bwInternalLogFunction(logCategory, finalMessage, logMetaData)
        return


_bwRedirectionHandler = None

def getBwHandler():
    global _bwRedirectionHandler
    return _bwRedirectionHandler


def init():
    global _bwRedirectionHandler
    _bwRedirectionHandler = BWLogRedirectionHandler()
    logging.setLoggerClass(BWLogger)
    logging.addLevelName(BWLogger.TRACE, 'TRACE')
    logging.addLevelName(BWLogger.NOTICE, 'NOTICE')
    logging.addLevelName(BWLogger.HACK, 'HACK')
    rootLogger = logging.getLogger()
    rootLogger.addHandler(_bwRedirectionHandler)
    rootLogger.setLevel(BWLogger.TRACE)
    logging.captureWarnings(True)
