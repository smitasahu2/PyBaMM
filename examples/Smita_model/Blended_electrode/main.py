import pybamm
import os # interact with the operating system
import matplotlib.pyplot as plt
import numpy as np
import pandas as p                    # last data manupulation
import timeit                         # tic-toc
os.chdir(pybamm.__path__[0]+'/..')
pybamm.set_logging_level("INFO")     # debug mode



start = timeit.default_timer()
model = pybamm.lithium_ion.DFN({
    "working electrode": "positive",
    "particle phases": ("1", "2"),
    "open-circuit potential": ( "single", ("single", "current sigmoid"))
})