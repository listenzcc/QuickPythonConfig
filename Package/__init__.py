# File: __init__.py
# Aim: Package initial

# %%
from .defines import Config

CONFIG = Config()
CONFIG.reload_logger(name='develop')

# %%
