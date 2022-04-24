from utils import *

def test_whiten():
	fnjson = "../../BBH_events_v3.json"
	events = json.load(open(fnjson,"r"))

	event = events[eventname]
	fn_H1 = event['fn_H1']
	strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
	
	psd_H1 = None
	dt = None
    strain_H1_whiten = whiten(strain_H1,psd_H1,dt)
	assert type(strain_H1_whiten) == np.ndarray

def test_write_wavfile():
	# filename = "test"
	# fs = 1
	# data = None
	# write_wavfile(filename,fs,data)

    
def test_reqshift():
	# strain_H1_shifted = reqshift(strain_H1_whitenbp,fshift=fshift,sample_rate=fs)


def test_plot_PSD()
        # plot_PSD(time, timemax, SNR, pcolor, det, tevent, strain_whitenbp, template_match, eventname, plottype, template_fft, datafreq, d_eff, freqs, data_psd, fs)
