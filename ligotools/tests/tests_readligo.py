import readligo as rl

def test_loaddata1():
	fnjson = "BBH_events_v3.json"
	try:
		events = json.load(open(fnjson,"r"))
	except IOError:
		print("Cannot find resource file "+fnjson)
		print("You can download it from https://losc.ligo.org/s/events/"+fnjson)
		print("Quitting.")
		quit()
	
	event = events[eventname]
	fn_H1 = event['fn_H1']


    strain, time, chan_dict = rl.loaddata(fn_L1)
    assert type(time) == numpy.ndarray
    
def test_loaddata2():
    strain, time, chan_dict = rl.loaddata(fn_L1, 'H1')
    assert type(chan_dict) == dict
    
def test_dq_channel_to_seglist1():
    segment_list = rl.dq_channel_to_seglist(chan_dict[DQflag])
    assert type(segment_list) == list

def test_dq_channel_to_seglist2():
    ## TODO change
    assert len(segment_list) == 10
    