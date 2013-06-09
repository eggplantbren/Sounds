from Sound import *

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

bitrate = 44100
seconds = 2.

t = np.linspace(0., 2., int(bitrate*seconds) + 1)
frequency = 440.

data = np.sin(2.*np.pi*frequency*t)
scaled = np.int16(data*32767)
plt.plot(t, scaled)
plt.show()
write('test.wav', 44100, scaled)

