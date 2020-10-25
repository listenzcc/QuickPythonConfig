# %%
from Package import CONFIG
from module1 import main as m1
from module2 import main as m2

# %%

CONFIG.reload_logger(name='release')
CONFIG.reload_cfg('examples/example_config.ini')
CONFIG.display()

# %%
m1()
CONFIG.reload_logger(name='develop')
m2()
