import readligo as rl

def test_loaddata1():
	fnjson = "../../BBH_events_v3.json"
	events = json.load(open(fnjson,"r"))

	event = events[eventname]
	fn_H1 = event['fn_H1']

    strain, time, chan_dict = rl.loaddata(fn_L1)
    assert type(time) == numpy.ndarray
    
def test_loaddata2():
	fnjson = "../../BBH_events_v3.json"
	events = json.load(open(fnjson,"r"))

	event = events[eventname]
	fn_H1 = event['fn_H1']
	
    strain, time, chan_dict = rl.loaddata(fn_L1)
    assert type(chan_dict) == dict
    
def test_dq_channel_to_seglist1():
	fnjson = "../../BBH_events_v3.json"
	events = json.load(open(fnjson,"r"))

	event = events[eventname]
	fn_H1 = event['fn_H1']
	
	
	DQflag = 'CBC_CAT3'
	strain, time, chan_dict = rl.loaddata(fn_L1, 'H1')
	
	
	chan_dict[DQflag] 
	
    segment_list = rl.dq_channel_to_seglist(chan_dict[DQflag])
    assert type(segment_list) == list

def test_dq_channel_to_seglist2():
    ## TODO change
	fnjson = "../../BBH_events_v3.json"
	events = json.load(open(fnjson,"r"))

	event = events[eventname]
	fn_H1 = event['fn_H1']
	
	
	DQflag = 'CBC_CAT3'
	strain, time, chan_dict = rl.loaddata(fn_L1, 'H1')
	
	
	chan_dict[DQflag] 
	
    segment_list = rl.dq_channel_to_seglist(chan_dict[DQflag])
	
    assert len(segment_list) == 10
    