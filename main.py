from Sound import *

import numpy as np
import matplotlib.pyplot as plt

harmonics = np.arange(1, 50)
amplitudes = np.exp(-harmonics/5.)

s = Source(440., amplitudes)
s.make_wave_file()

plt.plot(harmonics, amplitudes, 'bo-')
plt.xlabel('Harmonic')
plt.ylabel('Amplitude')
plt.title('Input Source')
plt.show()

