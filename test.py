import numpy, scipy, pylab, random

xs = []
rawsignal = []
with open("test.dat", 'r') as f:
      for line in f:
            if line[0] != '#' and len(line) > 0:
                xs.append( int( line.split()[0] ) )
                rawsignal.append( int( line.split()[1] ) )

h, w = 3, 1
pylab.figure(figsize=(12,9))
pylab.subplots_adjust(hspace=.7)

pylab.subplot(h,w,1)
pylab.title("Signal")
pylab.plot(xs,rawsignal)

pylab.subplot(h,w,2)
pylab.title("FFT")
fft = scipy.fft(rawsignal)
#~ pylab.axis([None,None,0,1000])
pylab.ylim([0,1000])
pylab.plot(abs(fft))


pylab.show()