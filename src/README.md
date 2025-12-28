"""
core-engine README
================

Core Engine is a high-performance, multi-threaded game engine written in Python.
It features a flexible architecture and is designed for both 2D and 3D game development.
"""

__version__ = "1.0.0"

import os
import sys

# Check if the environment variable 'CORE_ENGINE_HOME' is set
if 'CORE_ENGINE_HOME' not in os.environ:
    print("Error: CORE_ENGINE_HOME environment variable not set.")
    sys.exit(1)

# Set the core engine home directory
core_engine_home = os.environ['CORE_ENGINE_HOME']

# Import core engine modules
sys.path.insert(0, os.path.join(core_engine_home, 'rc'))

from core_engine.core import Engine
from core_engine.renderer import Renderer
from core_engine.model import Model
from core_engine.controller import Controller

# Example usage
if __name__ == "__main__":
    # Create a new engine instance
    engine = Engine()

    # Create a new renderer
    renderer = Renderer()

    # Create a new model
    model = Model()

    # Create a new controller
    controller = Controller()

    # Start the engine
    engine.start()