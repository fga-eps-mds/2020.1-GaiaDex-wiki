#!/bin/bash

python3 scripts/sort_by_epics.py
python3 scripts/add_acceptance_criteria_links.py
python3 scripts/reorder_acceptance_criteria.py