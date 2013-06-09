import numpy as np
from scipy.io.wavfile import write

"""
All sounds should be assumed to be periodic
Yeah, I could use FFTs and stuff. Possibly at the expense of clarity
and I don't need efficiency at this point.
"""

class Sound:
	"""
	Models a vocal sound. Input: source frequency spectrum
	(e.g. vocal fold raw output) and a filter object (Formant)
	"""
	def __init__(self, source, filt):
		pass


class Formant:
	pass


class Source:
	"""
	A raw vocal sound
	"""
	def __init__(self, fundamental,
				harmonics=np.array([1, 2, 3]),
				amplitudes=np.array([1., 0., 0.])):
		assert len(harmonics) == len(amplitudes)
		self.fundamental = fundamental
		self.harmonics = harmonics
		self.amplitudes = amplitudes

	def make_wave_file(self, filename='output.wav',
					seconds=2., bitrate=44100):
		"""
		Make a wave file of this sound
		"""
		t = np.linspace(0., 2., int(bitrate*seconds) + 1)
		data = np.zeros(t.shape)
		for i in xrange(0, len(self.harmonics)):
			f = self.harmonics[i]*self.fundamental
			data += self.amplitudes[i]*np.sin(2.*np.pi*f*t)
		scaled = np.int16(data*32767)
		write(filename, bitrate, scaled)
		return scaled

