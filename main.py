from Sound import *

import numpy as np
import matplotlib.pyplot as plt

harmonics = np.arange(1, 50)
amplitudes = np.exp(-(harmonics-2)**2/2.**2)

# Supposedly the I vowel (en.wikipedia.org/wiki/Formant)
EH = Formant([240., 2400.], [1., 1.], [500., 500.])

# Make a middle C
s = Sound(220.*2.**(3./12), amplitudes)

plt.plot(harmonics, s.amplitudes, 'bo-', label='Input Source')
plt.xlabel('Harmonic')
plt.ylabel('Amplitude')

# Apply the EH
s.apply_formant(EH)
s.make_wave_file()

plt.plot(harmonics, s.amplitudes, 'ro-', label='With Formant')
plt.legend()
plt.show()

