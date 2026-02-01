#!/usr/bin/env python3
"""
Vietnamese Stock Monitor - DEMO MODE
Uses mock data to demonstrate functionality when API is not accessible
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

# Enable demo mode BEFORE importing monitor
from src.demo_data import use_demo_data
use_demo_data()

# Now import and run the monitor
from monitor import main

if __name__ == "__main__":
    print("=" * 70)
    print("🎮 DEMO MODE - Using Mock Stock Data")
    print("=" * 70)
    print("This uses realistic demo data to show how the tool works.")
    print("For real data, run this from Vietnam network or use VPN.")
    print("=" * 70)
    print()

    main()
