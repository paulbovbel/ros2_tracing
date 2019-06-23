#!/usr/bin/env python3
# Entrypoint/script to setup and start an LTTng tracing session

import os

from tracetools_trace.tools import args
from tracetools_trace.tools import lttng
from tracetools_trace.tools import names


def main():
    params = args.parse_args()

    session_name = params.session_name
    base_path = params.path
    full_path = os.path.join(base_path, session_name)
    ros_events = params.events_ust
    kernel_events = params.events_kernel

    ust_enabled = len(ros_events) > 0
    kernel_enabled = len(kernel_events) > 0
    if ust_enabled:
        print(f'UST tracing enabled ({len(ros_events)} events)')
        if params.list:
            print(f'\tevents: {ros_events}')
    else:
        print('UST tracing disabled')
    if kernel_enabled:
        print(f'kernel tracing enabled ({len(kernel_events)} events)')
        if params.list:
            print(f'\tevents: {kernel_events}')
    else:
        print('kernel tracing disabled')

    print(f'writting tracing session to: {full_path}')
    input('press enter to start...')
    lttng.lttng_init(session_name, full_path, ros_events=ros_events, kernel_events=kernel_events)
    input('press enter to stop...')

    print('stopping & destroying tracing session')
    lttng.lttng_fini(session_name)
