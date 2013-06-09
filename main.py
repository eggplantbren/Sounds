from Sound import *

import numpy as np
import matplotlib.pyplot as plt

harmonics = np.arange(1, 50)
amplitudes = np.exp(-harmonics/5.)

s = Sound(440., amplitudes)
s.apply_formant(Formant([2000.], [1.], [500.]))
s.make_wave_file()

plt.plot(harmonics, s.amplitudes, 'bo-')
plt.xlabel('Harmonic')
plt.ylabel('Amplitude')
plt.title('Input Source')
plt.show()

