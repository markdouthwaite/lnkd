"""
A nice new Python package.
"""

try:
    from importlib import metadata
except ImportError:  # for Python<3.8
    import importlib_metadata as metadata

# this will load the latest _installed_ version.
__version__ = metadata.version("pkg")

print("Hello, world")
