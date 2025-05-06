#pip install matplotlib
import matplotlib.pyplot as plt

import numpy as np

plt.style.use('_mpl-gallery')

# quantità barre e punto inizio:
x = 0.5 + np.arange(5)
#altezza coordinate y
y = [2, 4, 6, 8, 10]

# plot
fig, ax = plt.subplots()

#linewidth=spessore linea

ax.bar(x, y, width=1, edgecolor="black", linewidth=0.5)

ax.set(xlim=(0, 8), xticks=np.arange(1, 10),
       ylim=(0, 8), yticks=np.arange(1, 10))

plt.show()