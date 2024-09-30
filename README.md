# Aarno Labs' HACCS Operational Ontology

This repository includes the operational ontology created by Aarno
Labs and employed during DARPA's HACCS program to coordinate
operations among the performers.

The ontology is broken up into three parts (see subdirectories):

1. World model: devices, components, software, services, bots
1. Operational: bot detections, network intelligence, hosts, running
   processes, etc.
1. Communication messages: Hike communication messages

## Requirements

* virtualenv

## Configure

1. Create new virtualenv (`virtualenv -p <path to python3 binary> venv && source venv/bin/activate`)
1. `pip install -r requirements.txt`

## Testing

1. `pytest tests/*.py`
