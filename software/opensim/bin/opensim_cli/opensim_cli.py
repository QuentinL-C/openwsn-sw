#!/usr/bin/python

import os
import sys

temp_path = sys.path[0]
if temp_path:
    sys.path.insert(0, os.path.join(temp_path, '..', '..'))

import logging
import logging.handlers
import binascii
from SimEngine import SimEngine

LOG_FORMAT  = "%(asctime)s [%(name)s:%(levelname)s] %(message)s"

#============================ logging =========================================

logFileName = 'logs/opensim.log'
loghandler  = logging.handlers.RotatingFileHandler(logFileName,
                                               maxBytes=2000000,
                                               backupCount=5,)
loghandler.setFormatter(logging.Formatter(LOG_FORMAT))

#============================ main ============================================

DEFAULT_NUM_MOTES = 1

def main():
    if len(sys.argv)>2:
        print 'usage: '+sys.argv[0]+' <nummotes>'
        sys.exit(0)
    
    # replace the prefix by the one passed as a variable
    if len(sys.argv)==2:
        try:
            nummotes = int(sys.argv[1])
        except ValueError:
            print 'invalid number of motes'
            sys.exit(0)
    else:
        nummotes = DEFAULT_NUM_MOTES

    # instantiate a SimEngine object
    simengine = SimEngine.SimEngine(loghandler,nummotes)
    simengine.start()
            
if __name__ == "__main__":
    main()
