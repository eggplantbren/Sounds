from Sound import *

import numpy as np
import matplotlib.pyplot as plt

# Make a middle C
fundamental = 110.*2.**(3./12)
harmonics = np.arange(1, 50)
amplitudes = np.exp(-(harmonics-2)**2/20.**2)

# Supposedly the I vowel (en.wikipedia.org/wiki/Formant)
formant = Formant([240., 2400.], [1., 1.], [100., 100.])

# Make the sound
s = Sound(fundamental, amplitudes)

plt.plot(fundamental*harmonics, s.amplitudes, 'bo-', label='Input Source')
plt.xlabel('Harmonic')
plt.ylabel('Amplitude')

f = fundamental*np.linspace(1., harmonics.max(), 10001)
plt.plot(f, formant.evaluate(f), 'r', label='Formant')

# Apply the formant
s.apply_formant(formant)
s.make_wave_file()

plt.plot(fundamental*harmonics, s.amplitudes, 'go-', label='With Formant')
plt.legend()
plt.show()

