import dyepy


def test_clamp():
    assert dyepy.clamp() == 0.5
    assert dyepy.clamp(-1) == 0
    assert dyepy.clamp(2) == 1
    
    assert dyepy.clamp(10, 9, 11) == 10
    assert dyepy.clamp(8, 9, 11) == 9
    assert dyepy.clamp(12, 9, 11) == 11
