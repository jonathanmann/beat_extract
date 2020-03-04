#!/usr/bin/env python
import numpy as np
from scipy import fft
from scipy.io import wavfile
import matplotlib.pyplot as plt
import sys

class FreqExtract:
    def __init__(self,wav_input):

        self.sampling_rate, signal = wavfile.read(wav_input)
        self.noise = signal[:, 0]  # use first channel
        self.time = np.arange(len(self.noise)) / float(self.sampling_rate)

    def freq_show(self):
        # taken almost directly from stack overflow
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.plot(self.time, self.noise)
        plt.xlabel('time (seconds)')
        plt.ylabel('noise')

        freq, X = self.freq_spec()

        short_freq = [x for x in freq if x < 1.0]
        short_X = X[:len(short_freq)]

        plt.subplot(2, 2, 4)
        plt.plot(short_freq, short_X, 'b')
        plt.xlabel('Hz-Zoom')
        plt.ylabel('Freq-Zoom')

        plt.subplot(2, 2, 3)
        plt.plot(freq, X, 'b')
        plt.xlabel('Hz')
        plt.ylabel('Freq')
        plt.tight_layout()

        plt.show()

    def freq_spec(self):
        # taken almost directly from stack overflow
        x = self.noise
        x = x - np.average(x)  # zero-centering

        n = len(x)
        tarr = n / float(self.sampling_rate)
        frqarr = np.arange(n) / float(tarr)  # two sides frequency range

        frqarr = frqarr[range(n // 2)]  # one side frequency range

        x = fft(x) / n  # fft computing and normalization
        x = x[range(n // 2)]

        return frqarr, abs(x)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please try again using the following syntax:")
        print("$ ./freq_extract.py <input wave file>")
    else:
        wav_input = sys.argv[1]
        f = FreqExtract(wav_input)
        f.freq_show()
