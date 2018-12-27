#!/usr/bin/env python

import subprocess
import re
import json
from datetime import datetime
from argparse import ArgumentParser

VERSION = '0.1'

def parseargs():
    p = ArgumentParser()
    p.add_argument('--log', required=False, help='Log file')
    p.add_argument('--report', required=False, action='store_true', help='Generate report')
    p.add_argument('--version', required=False, action='store_true', help='Show version')
    p.add_argument('-d','--debug', required=False, action='store_true', help='Enable debug')
    return vars(p.parse_args())


def run_command(command, first_strings=0):
    res = subprocess.check_output(command)
    res = res.split('\n')
    if first_strings:
        return res[:first_strings]
    else:
        return res


def main():
    args = parseargs()

    if args.get('version'):
        print 'Version:', VERSION
        exit(0)

    if args.get('report'):
        raise Exception('Not implemented')

    else:
        if not args.get('log') and not args.get('debug'):
            print 'Either --log or --debug argument is required, exiting...'
            exit(1)

        stats = {'ts': datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}

        top_raw = run_command(['top', '-l', '1'], 10)

        load_avg_raw = top_raw[2]
        stats['load_avg'] = float(re.search(r'Load Avg:\s(\d+\.\d+)', load_avg_raw).groups()[0])

        processes_raw = top_raw[0]
        processes = re.search(r'Processes: (\d+) total, (\d+) running, (\d+) sleeping', processes_raw).groups()
        stats['processes'] = {'total': processes[0], 'running': processes[1], 'sleeping': processes[2]}

        cpu_usage_raw = top_raw[3]
        cpu_usage = re.search(
            r'CPU usage: (\d+\.\d+)% user, (\d+\.\d+)% sys, (\d+\.\d+)% idle', cpu_usage_raw).groups()
        stats['cpu'] = {'usr': float(cpu_usage[0]), 'sys': float(cpu_usage[1]), 'idle': float(cpu_usage[2])}

        battery_raw = run_command(['pmset', '-g', 'batt'])
        battery_level, battery_state = re.search(r'\s+\S+\s(\d+)%; (\w+);', battery_raw[1]).groups()
        stats['power'] = {
            'source': 'ac' if 'AC' in battery_raw[0] else 'battery',
            'battery_level': int(battery_level),
            'battery_state': battery_state
        }

        if args.get('debug'):
            print stats
        else:
            with open(args['log'], 'a') as f:
                f.write(json.dumps(stats)+'\n')

main()
