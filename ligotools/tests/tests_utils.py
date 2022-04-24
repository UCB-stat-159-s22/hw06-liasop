from utils import *

def test_whiten():
    strain_H1_whiten = whiten(strain_H1,psd_H1,dt)

def test_write_wavfile():
    filename = "test"
    write_wavfile(filename,fs,data)

    
def test_reqshift():
    strain_H1_whiten = whiten(strain_H1,psd_H1,dt)

def test_plot_PSD()
    