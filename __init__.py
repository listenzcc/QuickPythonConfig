# File: __init__.py
# Aim: Package initial

# %%
from .config import Config

CONFIG = Config()

CONFIG.load_logger(name='develop')
CONFIG.reload_cfg()
# %%
