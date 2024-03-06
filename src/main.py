# ----------------------------------------------------

try:
    from ctypes import windll # Only exists on Windows
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        'ZWX.WXord.WXord.1-0-0'
    )
except ImportError:
    pass

# ----------------------------------------------------

import sys, traceback, types, typing

import PyQt6.QtWidgets as wid
app = wid.QApplication(sys.argv)

import interface as i
import rsc

# ----------------------------------------------------

import logging
logging.basicConfig(
    filename    = rsc.Paths.LOG_FILE,
    filemode    = 'w',
    encoding    = 'utf-8',

    level       = logging.DEBUG,
    format      = '%(asctime)s [ %(levelname)s ] %(name)s : %(message)s',
    datefmt     = '%d/%m/%Y %H:%M:%S'
)
LOGGER = logging.getLogger('main')

# Redifinition of sys.excepthook in order to catch any exception raised
# and log it before exiting, instead of printing it on stdout and exit
def excepthook(
    exception: typing.Type[BaseException],
    value: BaseException,
    tback: types.TracebackType
):
    tb = ''.join(traceback.format_exception(exception, value, tback))
    LOGGER.critical('An unhandled exception occured\n%s', tb)
    LOGGER.info('Exiting %s', rsc.Strings.APPLICATION_NAME)
    wid.QApplication.exit(1)

# ----------------------------------------------------

def main():
    # Configuration
    rsc.Translator.load()

    window = i.MainWindow(1000, 600)
    window.show()
    sys.exit(app.exec())
    

if __name__ == '__main__':
    # Prelaunch config
    LOGGER.info('Started %s', rsc.Strings.APPLICATION_NAME)
    LOGGER.debug('Root directory is %s', rsc.Paths.ROOT)
    sys.excepthook = excepthook

    # Launch application
    main()
