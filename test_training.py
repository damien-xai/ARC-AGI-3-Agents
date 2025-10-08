#!/usr/bin/env python3
"""Test script to verify model training at step 50"""
import sys
import os

# Set max actions to 55 (just past training at step 50)
os.environ['MAX_ACTIONS'] = '55'
os.environ['PATTERN_DISCOVERY_INTERVAL'] = '50'

# Run main
from main import main
sys.exit(main())
