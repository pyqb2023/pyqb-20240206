# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Programming in Python
# ## Exam: February 6, 2024
#
# You can solve the exercises below by using standard Python 3.11 libraries, NumPy, Matplotlib, Pandas, PyMC.
# You can browse the documentation: [Python](https://docs.python.org/3.11/), [NumPy](https://numpy.org/doc/stable/user/index.html), [Matplotlib](https://matplotlib.org/stable/users/index.html), [Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html), [PyMC](https://docs.pymc.io).
# You can also look at the [slides of the course](https://homes.di.unimi.it/monga/lucidi2324/pyqb00.pdf) or your code on [GitHub](https://github.com).
#
# **It is forbidden to communicate with others or "ask questions" online (i.e., stackoverflow is ok if the answer is already there, but you cannot ask a new question)**
#
# To test examples in docstrings use
#
# ```python
# import doctest
# doctest.testmod()
# ```
#

import numpy as np
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pymc as pm   # type: ignore
import arviz as az   # type: ignore

# ### Exercise 1 (max 1 points)
#
# The file [trillium.csv](./trillium.csv) (Miller, Chelsea, Kwit, Charles, & Whitehead, Susan. (2021). Effects of seed morphology and elaiosome chemical composition on attractiveness of five Trillium species to seed-dispersing ants. https://doi.org/10.5061/dryad.hhmgqnkcz) contains a data matrix consisting of 125 columns and 31 rows. The first four columns are metadata columns, and contain information about the geographic distribution of each species (endemic v. widespread), the species specific epithet, the average probability of seed removal in the field, and two-letter abbreviation for the study site from which the sample was collected ("TB" = Tilton Bridge, "PB" = Pocket Branch, "OM" = Old Mine, "CA" = Cave, "WF" = WhiteWater Falls, "BR" = Boat Ramp, and "JG" = Jocassee Gorges). The remaining columns are the names of chemical compounds identified using Liquid-chromatography mass spectrometry. Each cell contains the raw area under the curve for each compound in each sample.
#
# Load the data in a Pandas dataframe.

pass

# ### Exercise 2 (max 2 points)
#
# Add a column `Location` with the complete name of the site where the sample was collected.
#

pass

# ### Exercise 3 (max 8 points)
#
# Define a function `averages` that takes a list of floats and returns a list of averages on the triplet of the ordered values of the input list. For example if the input values are `6.0, 1.0, 5.0, 2.0, 4.0, 3.0` the result is the list `[2.0, 5.0]` (the average of `1.0, 2.0, 3.0` and the average of `4.0 5.0 6.0`). If the number of values is not a multiple of three, the last average is computed on a smaller set.
#
#
# To get the full marks, you should declare correctly the type hints and add a test within a doctest string.

# +

pass

# +
# You can test your docstrings by executing this cell

import doctest
doctest.testmod()
# -

# ### Exercise 4 (max 4 points)
#
# Apply the function defined in Exercise 3 on the values of `Citrulline` collected at "Tilton Bridge".

pass

# ### Exercise 5 (max 4 points)
#
# Add a column to the data with, for each row, the highest value of all the chemical compounds identified using Liquid-chromatography mass spectrometry.

pass

# ### Exercise 6 (max 5 points)
#
# Plot together the histograms of `Citrulline` for each collection Location.

pass

# ### Exercise 7 (max 5 points)
#
# Make a scatter plot of `Citrulline` vs. `S-Adenosyl-L-methioninamine`. Color the points according to the `Status`.

pass

# ### Exercise 8 (max 4 points)
#
# Consider this statistical model:
#
# - a parameter $\alpha$ is normally distributed with $\mu = 0$ and $\sigma = 1$
# - a parameter $\beta$ is normally distributed with $\mu = 1$ and $\sigma = 1$
# - a parameter $\gamma$ is exponentially distributed with $\lambda = 1$
# - the observed `Citrulline` is normally distributed with standard deviation $\gamma$ and a mean given by $\alpha + \beta \cdot S$ (where $S$ is the correspondig value of `S-Adenosyl-L-methioninamine`).
#
# Code this model with pymc, sample the model, and plot the summary of the resulting estimation by using `az.plot_posterior`.
#
#
#

pass
