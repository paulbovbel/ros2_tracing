#!/usr/bin/env python3
# Entrypoint/script to convert CTF trace data to a pickle file
# TODO

import sys
from pickle import Pickler
from tracetools_analysis.conversion.ctf import *

def main(argv=sys.argv):
    if len(argv) != 3:
        print("usage: /trace/directory pickle_target_file")
        exit(1)

    trace_directory = sys.argv[1]
    pickle_target_file = sys.argv[2]

    with open(pickle_target_file, 'wb') as f:
        p = Pickler(f, protocol=4)
        ctf_to_pickle(trace_directory, p)