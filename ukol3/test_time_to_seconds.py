import pytest
from time_to_seconds import time_to_sec

def test_time_to_sec():
    assert time_to_sec('30') == 30
    assert time_to_sec('30.8') == 31
    assert time_to_sec('30s') == 30
    assert time_to_sec('60.5m') == 3630
    assert time_to_sec('3d5h2m10s') == 277330
    assert time_to_sec('s') == 1
    assert time_to_sec('m') == 60
    with pytest.raises(ValueError):
        assert time_to_sec('1y')
    with pytest.raises(ValueError):    
        assert time_to_sec('10seconds')
    with pytest.raises(ValueError):    
        assert time_to_sec('')
    with pytest.raises(ValueError):    
        assert time_to_sec('hms')