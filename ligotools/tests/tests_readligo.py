import readligo as rl

def test_loaddata1():
    strain, time, chan_dict = rl.loaddata(fn_L1, 'H1')
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
    