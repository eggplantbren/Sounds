import numpy as np
from scipy.io.wavfile import write

"""
All sounds should be assumed to be periodic
Yeah, I could use FFTs and stuff. Possibly at the expense of clarity
and I don't need efficiency at this point.
"""

class Formant:
	"""
	Mixture of Gaussians model for formant structure
	"""
	def __init__(self, frequencies, amplitudes, widths):
		assert len(frequencies) == len(amplitudes)
		assert len(frequencies) == len(widths)
		self.frequencies = frequencies
		self.amplitudes = amplitudes
		self.widths = widths

	def evaluate(self, f):
		"""
		Evaluate the formant function at some frequencies
		"""
		y = np.zeros(len(f))
		for i in xrange(0, len(self.frequencies)):
			y += self.amplitudes[i]*\
				np.exp(-0.5*((f - self.frequencies[i])/self.widths[i])**2)
		return y


class Sound:
	"""
	A sound
	"""
	def __init__(self, fundamental,	amplitudes=np.array([1., 0., 0.])):
		self.fundamental = fundamental
		self.amplitudes = amplitudes

	def make_wave_file(self, filename='output.wav',
					seconds=2., bitrate=44100):
		"""
		Make a wave file of this sound
		"""
		t = np.linspace(0., 2., int(bitrate*seconds) + 1)
		data = np.zeros(t.shape)
		for i in xrange(0, len(self.amplitudes)):
			f = (i+1)*self.fundamental
			data += self.amplitudes[i]*np.sin(2.*np.pi*f*t)
		scaled = np.int16(data/np.max(np.abs(data))*32767)
		write(filename, bitrate, scaled)
		return scaled

	def apply_formant(self, formant):
		"""
		Modify the amplitudes according to the formant given
		"""
		f = self.fundamental*np.arange(1, len(self.amplitudes) + 1)
		y = formant.evaluate(f)
		self.amplitudes *= y

