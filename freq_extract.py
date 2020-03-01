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

        frq, X = self.freq_spec()

        plt.subplot(2, 1, 2)
        plt.plot(frq, X, 'b')
        plt.xlabel('Hz')
        plt.ylabel('Freq')
        plt.tight_layout()

        plt.show()


    def freq_spec(self):
        # taken almost directly from stack overflow
        x = self.noise
        x = x - np.average(x)  # zero-centering

        n = len(x)
        print(n)
        tarr = n / float(self.sampling_rate)
        frqarr = np.arange(n) / float(tarr)  # two sides frequency range

        frqarr = frqarr[range(n // 2)]  # one side frequency range

        x = fft(x) / n  # fft computing and normalization
        x = x[range(n // 2)]

        return frqarr, abs(x)

if __name__ == '__main__':
    wav_input = sys.argv[1]
    f = FreqExtract(wav_input)
    f.freq_show()
