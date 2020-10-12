import dyepy


def test_clamp():
    assert dyepy.clamp() == 0.5
    assert dyepy.clamp(-1) == 0
    assert dyepy.clamp(2) == 1
    
    assert dyepy.clamp(10, 9, 11) == 10
    assert dyepy.clamp(8, 9, 11) == 9
    assert dyepy.clamp(12, 9, 11) == 11


def test_Styles():
    pass    # Nothing to test, Styles is a class of constant strings


def test_Colors():
    assert dyepy.Colors.WINDOWSBLUE == '#0078d7'
    assert dyepy.Colors.SPOTIFYGREEN == '#1db954'
    
    assert dyepy.Colors.rgb(0, 0, 0) == '#000000'
    assert dyepy.Colors.rgb(255, 255, 255) == '#ffffff'
    assert dyepy.Colors.rgb(0, 120, 215) == '#0078d7'
    assert dyepy.Colors.rgb(29, 185, 84) == '#1db954'
    
    assert dyepy.Colors.hsv(207, 1, 0.8431372549019608) == '#0078d7'
    assert dyepy.Colors.hsv(141, 0.8432432432432432, 0.7254901960784313) == '#1db954'
    
    assert dyepy.Colors.hsl(207, 1, 0.4215686274509804) == '#0078d7'
    assert dyepy.Colors.hsl(141, 0.7289719626168223, 0.4196078431372549) == '#1db954'
    
    assert dyepy.Colors.yiq(94, 0, 0) == '#0078d7'
    assert dyepy.Colors.yiq(127, 0, 0) == '#1db954'
    
    assert dyepy.Colors.cmyk(1, 0.4418604651162791, 0, 0.1568627450980392) == '#0078d7'
    assert dyepy.Colors.cmyk(0.8432432432432432, 0, 0.545945945945946, 0.27450980392156865) == '#1db954'


def test_Converters():
    # Conversions from HEX
    assert dyepy.Converters.hex2rgb('#000000') == (0, 0, 0)
    assert dyepy.Converters.hex2rgb('#fff') == (255, 255, 255)
    assert dyepy.Converters.hex2rgb('#0078d7') == (0, 120, 215)
    assert dyepy.Converters.hex2rgb(0x1db954) == (29, 185, 84)
    
    assert dyepy.Converters.hex2hsv('#0078d7') == (207, 1, 0.8431372549019608)
    assert dyepy.Converters.hex2hsv('#1db954') == (141, 0.8432432432432432, 0.7254901960784313)
    
    assert dyepy.Converters.hex2hsl('#0078d7') == (207, 1, 0.4215686274509804)
    assert dyepy.Converters.hex2hsl('#1db954') == (141, 0.7289719626168223, 0.4196078431372549)
    
    assert dyepy.Converters.hex2yiq('#0078d7') == (94, 0, 0)
    assert dyepy.Converters.hex2yiq('#1db954') == (127, 0, 0)
    
    assert dyepy.Converters.hex2cmyk('#0078d7') == (1, 0.4418604651162791, 0, 0.1568627450980392)
    assert dyepy.Converters.hex2cmyk('#1db954') == (0.8432432432432432, 0, 0.545945945945946, 0.27450980392156865)
    
    # Conversions from RGB
    assert dyepy.Converters.rgb2hsv(0, 120, 215) == (207, 1.0, 0.8431372549019608)
    assert dyepy.Converters.rgb2hsv(29, 185, 84) == (141, 0.8432432432432432, 0.7254901960784313)
    
    assert dyepy.Converters.rgb2hsl(0, 120, 215) == (207, 1, 0.4215686274509804)
    assert dyepy.Converters.rgb2hsl(29, 185, 84) == (141, 0.7289719626168223, 0.4196078431372549)
    
    assert dyepy.Converters.rgb2yiq(0, 120, 215) == (94, 0, 0)
    assert dyepy.Converters.rgb2yiq(29, 185, 84) == (127, 0, 0)
    
    assert dyepy.Converters.rgb2cmyk(0, 120, 215) == (1, 0.4418604651162791, 0, 0.1568627450980392)
    assert dyepy.Converters.rgb2cmyk(29, 185, 84) == (0.8432432432432432, 0, 0.545945945945946, 0.27450980392156865)


def test_getrandomcolor():
    pass    # Nothing to test, returns random hex color (random strings)
