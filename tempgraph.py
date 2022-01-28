import argparse
import sys
import time
import webbrowser
import os

import graph
import db

parser = argparse.ArgumentParser()
parser.add_argument("--value", "-v", action="append")
parser.add_argument("--temperature", "-t", type=float)
parser.add_argument("--web", "-w", action="store_true")
parser.add_argument("--graph", "-g", action="store_true", help ="render a graph")
parser.add_argument("--list", "-l", action="store_true")

if len(sys.argv) < 2:
    parser.print_help()

options = vars(parser.parse_args())
options['output_filename'] = "output.html"

if options['temperature']:
    db.add_temperature(int(time.time()), float(options['temperature']), options)

if options['value']:
    for value in options['value']:
        timestamp, temperature = value.split("=")
        db.add_temperature(int(timestamp), float(temperature), options)

if options['graph']:
    graph.render_graph(db.get_temperatures(), options)

if options['web']:
    webbrowser.open("file://"+os.path.abspath(options['output_filename']))

if options['list']:
    print(db.get_temperatures())
