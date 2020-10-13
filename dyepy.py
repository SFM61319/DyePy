"""
Module with everything related to styles and colors in any way.

From rgb-hex converters to printing text in colors on a command-line,
this module allows you to deal with colors, also helpful when making
GUIs on Python (using tkinter, PyGame, etc.), by giving you the
colors you want in Hexadecimal to common colors to all types
of color representations supported by CSS4 too! Just name it!

Separate documentation for each function and class written with them.
To read the documentation, type `help(<function/class>)` into the CLI
"""


__author__: str = 'SFM61319'
__email__: str = 'svasssakavi@gmail.com'
__github__: str = 'https://github.com/SFM61319/DyePy'
__version__: str = '1.0.0'
__desc__: str = 'A Python module for all colors and related functions'


# Import `typing` for type-hinting
import typing

# Import `randint` from `random` as `_randint`
from random import randint as _randint


def clamp(
    value: typing.Union[int, float] = 0.5,
    minimum: typing.Union[int, float] = 0,
    maximum: typing.Union[int, float] = 1
) -> typing.Union[int, float]:
    """
    Returns the clamped value between *minimum* and *maximum*

    A clamped value is the value itself when it lies
    between the minimum and the maximum, and if the
    value crosses the extremes, then the extremity
    closer to the value becomes the clamped value.
    
    E.g.:
    clamp(0, 0.5, 1) -> 0.5;
    clamp(0, 2, 1) -> 1;
    clamp(0, -1, 1) -> 0;
    """

    if value < minimum:
        return minimum
    
    if value > maximum:
        return maximum
    
    return value


# A class to print in different colors (command-line only)
class Styles:
    """
    Styles class

    A class to help print both foreground and background in different
    styles and colors (both as variables) on a command-line.
    
    Print blue text with green background
    E.g.: print(Styles.Bg.GREEN, Styles.Fg.BLUE, 'Blue text', Styles.RESET)
    
    Or print the text in italics
    E.g.: print(Styles.ITALIC, 'Italic text', Styles.RESET)
    
    Here's what the constants are supposed to do:
    ---- Reset ----
    RESET: resets all the colors and styles used in the preceding text

    ---- Styles ----
    BOLD: bolds all the succeeding text
    DISABLE: reduces intensity (not widely supported)
    ITALIC: writes text in italics (not widely supported)
    UNDERLINE: underlines succeeding text
    SLOWBLINK: makes the text blink slowly (< 150 per minute)
    RAPIDBLINK: makes the text blink > 150/min (not widely supported)
    REVERSE: swaps default foreground and background colors and styles
    INVISIBLE: makes the foreground transparent
    STRIKETHROUGH: strikes through the text
    REVEAL: switches Conceal off (not widely supported)
    FRAME: frames the succeeding text
    ENCIRCLE: encircles the succeeding text
    OVERLINE: prints an overline on the succeeding text

    ---- Colors ----
        -- Foreground (Fg) --
        Fg.<COLOR_NAME>: sets the color to the succeeding fg
        Fg.n(<intensity>): sets the pre-selected color to fg
        Fg.rgb(<r>, <g>, <b>): sets the calculated color to fg

        -- Background (Bg) --
        Bg.<COLOR_NAME>: sets the color to the succeding bg
        Bg.n(<intensity>): sets the pre-selected color to bg
        Bg.rgb(<r>, <g>, <b>): sets the calculated color to bg

    For more info on `n`, refer to this table:
        https://i.stack.imgur.com/KTSQa.png
    
    Please do not attempt to change these constants in the module
    or the Python file this is being imported to, as it may affect
    the output of the colors and may even corrupt and work irregularly
    and not as expected when being ran in a Python environment
    
    For more information on command-line styling, refer to:
        http://ascii-table.com/ansi-escape-sequences-vt-100.php
    """

    # Reset
    RESET = reset = '\x1b[00m'

    # Styles
    BOLD = bold = '\x1b[01m'
    DISABLE = disable = '\x1b[02m'
    ITALIC = italic = '\x1b[03m'
    UNDERLINE = underline = '\x1b[04m'
    SLOWBLINK = slowblink = '\x1b[05m'
    RAPIDBLINK = rapidblink = '\x1b[06m'
    REVERSE = reverse = '\x1b[07m'
    INVISIBLE = invisible = '\x1b[08m'
    STRIKETHROUGH = strikethrough = '\x1b[09m'
    REVEAL = reveal = '\x1b[28m'
    FRAME = frame = '\x1b[51m'
    ENCIRCLE = encircle = '\x1b[52m'
    OVERLINE = overline = '\x1b[53m'

    # Foreground colors
    class Foreground:
        """
        Foreground (Fg) sub-class to set foreground
        colors of succeeding text occurences
        """

        BLACK = black = '\x1b[30m'
        RED = red = '\x1b[31m'
        GREEN = green = '\x1b[32m'
        ORANGE = orange = '\x1b[33m'
        BLUE = blue = '\x1b[34m'
        PURPLE = purple = '\x1b[35m'
        CYAN = cyan = '\x1b[36m'
        LIGHTGREY = lightgrey = '\x1b[37m'
        DARKGREY = darkgrey = '\x1b[90m'
        LIGHTRED = lightred = '\x1b[91m'
        LIGHTGREEN = lightgreen = '\x1b[92m'
        YELLOW = yellow = '\x1b[93m'
        LIGHTBLUE = lightblue = '\x1b[94m'
        PINK = pink = '\x1b[95m'
        LIGHTCYAN = lightcyan = '\x1b[96m'

        WHITE = white = '\x1b[38;2;255;255;255m'
        SPOTIFYGREEN = spotifygreen = '\x1b[38;2;29;185;84m'
        WINDOWSBLUE = '\x1b[38;2;0;120;215m'

        @staticmethod
        def n(intensity: typing.Union[int, float] = 0) -> str:
            """
            Returns calculated ANSI color code for unnamed bg colors

            Can be used as follow:
            print(Styles.Fg.n(255), 'Some random color', Styles.RESET)
            
            Refer to https://i.stack.imgur.com/KTSQa.png for more
            information on how to use the function to get a color
            """

            return f'\x1b[38;5;{clamp(round(intensity), 0, 255)}m'

        @staticmethod
        def rgb(
            red: typing.Union[int, float] = 0, 
            blue: typing.Union[int, float] = 0, 
            green: typing.Union[int, float] = 0
        ) -> str:
            """
            Returns calculated ANSI color code for unnamed fg colors

            Can be used as follows:
            print(Styles.Fg.rgb(0, 120, 215), 'Windows Default Blue', Styles.RESET)
            print(Styles.Fg.rgb(29, 185, 84), 'Spotify Green', Styles.RESET)
            
            NOTE: 0 ≤ r, g, b ≤ 255
            """

            return (
                f'\x1b[38;2;'
                f'{clamp(round(red), 0, 255)};'
                f'{clamp(round(blue), 0, 255)};'
                f'{clamp(round(green), 0, 255)}m'
            )

    Fg = Foreground

    # Background colors
    class Background:
        """
        Background (Bg) sub-class to set background
        colors of succeeding text occurences
        """

        BLACK = black = '\x1b[40m'
        RED = red = '\x1b[41m'
        GREEN = green = '\x1b[42m'
        ORANGE = orange = '\x1b[43m'
        BLUE = blue = '\x1b[44m'
        PURPLE = purple = '\x1b[45m'
        CYAN = cyan = '\x1b[46m'
        LIGHTGREY = lightgrey = '\x1b[47m'
        DARKGREY = darkgrey = '\x1b[100m'
        LIGHTRED = lightred = '\x1b[101m'
        LIGHTGREEN = lightgreen = '\x1b[102m'
        YELLOW = yellow = '\x1b[103m'
        LIGHTBLUE = lightblue = '\x1b[104m'
        PINK = pink = '\x1b[105m'
        LIGHTCYAN = lightcyan = '\x1b[106m'

        WHITE = white = '\x1b[48;2;255;255;255m'
        SPOTIFYGREEN = spotifygreen = '\x1b[48;2;29;185;84m'
        WINDOWSBLUE = '\x1b[48;2;0;120;215m'

        @staticmethod
        def n(intensity: typing.Union[int, float] = 255) -> str:
            """
            Returns calculated ANSI color code for unnamed bg colors

            Can be used as follow:
            print(Styles.Bg.n(255), 'Some random color', Styles.RESET)
            
            Refer to https://i.stack.imgur.com/KTSQa.png for more
            information on how to use the function to get a color
            """

            return f'\x1b[48;5;{clamp(round(intensity), 0, 255)}m'

        @staticmethod
        def rgb(
            red: typing.Union[int, float] = 255,
            blue: typing.Union[int, float] = 255,
            green: typing.Union[int, float] = 255
        ) -> str:
            """
            Returns calculated ANSI color code for unnamed bg colors

            Can be used as follows:
            print(Styles.Bg.rgb(0, 120, 215), 'Windows Default Blue', Styles.RESET)
            print(Styles.Bg.rgb(29, 185, 84), 'Spotify Green', Styles.RESET)
            
            NOTE: 0 ≤ red, green, blue ≤ 255
            """

            return (
                f'\x1b[48;2;'
                f'{clamp(round(red), 0, 255)};'
                f'{clamp(round(blue), 0, 255)};'
                f'{clamp(round(green), 0, 255)}m'
            )

    Bg = Background


# A class to use pre-defined colors from CSS4 and get HEX values
class Colors:
    """
    Colors class

    A class of named Hex color codes as constants
    that can be used simply by referencing them.
    
    These names and values have been inherited from CSS4,
    and there are some extra built-in colors like the
    Windows Default Blue color and the Spotify Green color.
    
    This class is completely different from the class
    `Styles` (which can be used for font-styling and coloring)
    """

    ALICEBLUE = '#f0f8ff'
    ANTIQUEWHITE = '#faebd7'
    AQUA = '#00ffff'
    AQUAMARINE = '#7fffd4'
    AZURE = '#f0ffff'
    BEIGE = '#f5f5dc'
    BISQUE = '#ffe4c4'
    BLACK = '#000000'
    BLANCHEDALMOND = '#ffebcd'
    BLUE = '#0000ff'
    BLUEVIOLET = '#8a2be2'
    BROWN = '#a52a2a'
    BURLYWOOD = '#deb887'
    CADETBLUE = '#5f9ea0'
    CHARTREUSE = '#7fff00'
    CHOCOLATE = '#d22551e'
    CORAL = '#ff7f50'
    CORNFLOWERBLUE = '#6495ed'
    CORNSILK = '#fff8dc'
    CRIMSON = '#dc143c'
    CYAN = '#00ffff'
    DARKBLUE = '#00008b'
    DARKCYAN = '#008b8b'
    DARKGOLDENROD = '#b8860b'
    DARKGRAY = '#a9a9a9'
    DARKGREEN = '#006400'
    DARKKHAKI = '#bdb76b'
    DARKMAGENTA = '#8b008b'
    DARKOLIVEGREEN = '#556b2f'
    DARKORANGE = '#ff8c00'
    DARKORCHID = '#9932cc'
    DARKRED = '#8b0000'
    DARKSALMON = '#e9967a'
    DARKSEAGREEN = '#8fbc8f'
    DARKSLATEBLUE = '#483d8b'
    DARKSLATEGRAY = '#2f4f4f'
    DARKTURQUOISE = '#00ced1'
    DARKVIOLET = '#9400d3'
    DEEPPINK = '#ff1493'
    DEEPSKYBLUE = '#00bfff'
    DIMGRAY = '#255255255'
    DODGERBLUE = '#1e90ff'
    FIREBRICK = '#b22222'
    FLORALWHITE = '#fffaf0'
    FORESTGREEN = '#228b22'
    FUCHSIA = '#ff00ff'
    GAINSBORO = '#dcdcdc'
    GHOSTWHITE = '#f8f8ff'
    GOLD = '#ffd700'
    GOLDENROD = '#daa520'
    GRAY = '#808080'
    GREEN = '#008000'
    GREENYELLOW = '#adff2f'
    HONEYDEW = '#f0fff0'
    HOTPINK = '#ff255b4'
    INDIANRED = '#cd5c5c'
    INDIGO = '#4b0082'
    IVORY = '#fffff0'
    KHAKI = '#f0e68c'
    LAVENDER = '#e6e6fa'
    LAVENDERBLUSH = '#fff0f5'
    LAWNGREEN = '#7cfc00'
    LEMONCHIFFON = '#fffacd'
    LIGHTBLUE = '#add8e6'
    LIGHTCORAL = '#f08080'
    LIGHTCYAN = '#e0ffff'
    LIGHTGOLDENRODYELLOW = '#fafad2'
    LIGHTGREEN = '#90ee90'
    LIGHTGREY = '#d3d3d3'
    LIGHTPINK = '#ffb6c1'
    LIGHTSALMON = '#ffa07a'
    LIGHTSEAGREEN = '#20b2aa'
    LIGHTSKYBLUE = '#87cefa'
    LIGHTSLATEGRAY = '#778899'
    LIGHTSTEELBLUE = '#b0c4de'
    LIGHTYELLOW = '#ffffe0'
    LIME = '#00ff00'
    LIMEGREEN = '#32cd32'
    LINEN = '#faf0e6'
    MAGENTA = '#ff00ff'
    MAROON = '#800000'
    MEDIUMAQUAMARINE = '#66cdaa'
    MEDIUMBLUE = '#0000cd'
    MEDIUMORCHID = '#ba55d3'
    MEDIUMPURPLE = '#9370d8'
    MEDIUMSEAGREEN = '#3cb371'
    MEDIUMSLATEBLUE = '#7b68ee'
    MEDIUMSPRINGGREEN = '#00fa9a'
    MEDIUMTURQUOISE = '#48d1cc'
    MEDIUMVIOLETRED = '#c71585'
    MIDNIGHTBLUE = '#191970'
    MINTCREAM = '#f5fffa'
    MISTYROSE = '#ffe4e1'
    MOCCASIN = '#ffe4b5'
    NAVAJOWHITE = '#ffdead'
    NAVY = '#000080'
    OLDLACE = '#fdf5e6'
    OLIVE = '#808000'
    OLIVEDRAB = '#6b8e23'
    ORANGE = '#ffa500'
    ORANGERED = '#ff4500'
    ORCHID = '#da70d6'
    PALEGOLDENROD = '#eee8aa'
    PALEGREEN = '#98fb98'
    PALETURQUOISE = '#afeeee'
    PALEVIOLETRED = '#d87093'
    PAPAYAWHIP = '#ffefd5'
    PEACHPUFF = '#ffdab9'
    PERU = '#cd853f'
    PINK = '#ffc0cb'
    PLUM = '#dda0dd'
    POWDERBLUE = '#b0e0e6'
    PURPLE = '#800080'
    REBECCAPURPLE = '#663399'
    RED = '#ff0000'
    ROSYBROWN = '#bc8f8f'
    ROYALBLUE = '#41255e1'
    SADDLEBROWN = '#8b4513'
    SALMON = '#fa8072'
    SANDYBROWN = '#f4a460'
    SEAGREEN = '#2e8b57'
    SEASHELL = '#fff5ee'
    SIENNA = '#a0522d'
    SILVER = '#c0c0c0'
    SKYBLUE = '#87ceeb'
    SLATEBLUE = '#6a5acd'
    SLATEGRAY = '#708090'
    SNOW = '#fffafa'
    SPOTIFYGREEN = '#1db954'
    SPRINGGREEN = '#00ff7f'
    STEELBLUE = '#4682b4'
    TAN = '#d2b48c'
    TEAL = '#008080'
    THISTLE = '#d8bfd8'
    TOMATO = '#ff6347'
    TURQUOISE = '#40e0d0'
    VIOLET = '#ee82ee'
    WHEAT = '#f5deb3'
    WHITE = '#ffffff'
    WHITESMOKE = '#f5f5f5'
    WINDOWSBLUE = '#0078d7'
    YELLOW = '#ffff00'
    YELLOWGREEN = '#9acd32'

    # A function to convert RGB values to Hex values
    @staticmethod
    def rgb(
        red: typing.Union[int, float] = 0,
        green: typing.Union[int, float] = 0,
        blue: typing.Union[int, float] = 0
    ) -> str:
        """
        Returns the Hex value from an RGB value for many modules use
        Hex values as their default or accepted color code values
        
        Can also be used as a RGB-to-Hex converter
        """

        return (
            f'#{clamp(round(red), 0, 255):02x}'
            f'{clamp(round(green), 0, 255):02x}'
            f'{clamp(round(blue), 0, 255):02x}'
        )

    # A function to convert HSV values to Hex values
    @staticmethod
    def hsv(
        hue: typing.Union[int, float] = 0,
        saturation: typing.Union[int, float] = 0,
        value: typing.Union[int, float] = 0
    ) -> str:
        """
        Returns the Hex value from an HSV value for many modules use
        Hex values as their default or accepted color code values
        
        0 ≤ hue ≤ 360; although other values is also acceptable
        0 ≤ saturation, value ≤ 1; any other value will be clamped
        
        NOTE: both HSB and HSV are the same colorspaces
        
        Can also be used as a HSV-to-Hex converter
        """

        return Colors.rgb(*Converters.hsv2rgb(hue, saturation, value))

    hsb = hsv  # Since both are the same

    # A function to convert HSL values to Hex values
    @staticmethod
    def hsl(
        hue: typing.Union[int, float] = 0,
        saturation: typing.Union[int, float] = 0,
        luminance: typing.Union[int, float] = 0
    ) -> str:
        """
        Returns the Hex value from an HSL value for many modules use
        Hex values as their default or accepted color code values
        
        0 ≤ hue ≤ 360; although a value > 360 is also acceptable
        0 ≤ saturation, luminance ≤ 1; any other value will be clamped
        
        NOTE: HSV and HSL are different colorspaces, for more information
        refer to:
            https://en.wikipedia.org/wiki/HSL_and_HSV
        
        Can also be used as a HSL-to-Hex converter
        """

        return Colors.rgb(*Converters.hsl2rgb(hue, saturation, luminance))

    # A function to convert a YIQ color to Hex values
    @staticmethod
    def yiq(
        y: typing.Union[int, float] = 0,
        i: typing.Union[int, float] = 0,
        q: typing.Union[int, float] = 0
    ) -> str:
        """
        Returns the Hex value from a YIQ color space for many modules
        use Hex values as their default or accepted color code values
        
        NOTE: The following are the acceptable values:
            0 ≤ y ≤ 1,
            -0.5959 ≤ i ≤ 0.5959,
            -0.5229 ≤ q ≤ 0.5229
        
        All other values will be clamped between these ranges
        
        Can also be used as a YIQ-to-Hex converter
        """

        return Colors.rgb(*Converters.yiq2rgb(y, i, q))

    # A function to convert a CMYK color to Hex values
    @staticmethod
    def cmyk(
        cyan: typing.Union[int, float] = 0,
        magenta: typing.Union[int, float] = 0,
        yellow: typing.Union[int, float] = 0,
        black_key: typing.Union[int, float] = 0
    ) -> str:
        """
        Returns the Hex value from a CMYK color space for many modules
        use Hex values as their default or accepted color code values
        
        0 ≤ cyan, magenta, yellow, black_key ≤ 1, other values will be clamped
        
        Can also be used as a CMYK-to-Hex converter
        """

        return Colors.rgb(*Converters.cmyk2rgb(cyan, magenta, yellow, black_key))
    
    @staticmethod
    def getrandomcolor() -> str:
        return Colors.rgb(_randint(0, 255), _randint(0, 255), _randint(0, 255))


# A class to convert colors to-fro different colorspaces
class Converters:
    """
    A class of color space converters (static)
    
    Usage:
        dyepy.Converters.hex2rgb(0xffffff)
    """
    
    # A function to convert Hex values to RGB colors
    @staticmethod
    def hex2rgb(hexcode: typing.Union[str, int] = '#000000')\
        -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent RGB values of a hex color *hexcode*
        """
        
        if isinstance(hexcode, int):
            hexcode = hex(hexcode)
        
        hexcode = hexcode.replace('0x', '#')

        if len(hexcode) == 4:  # Repetative shortcut
            hexcode = f'#{hexcode[1]*2}{hexcode[2]*2}{hexcode[3]*2}'

        return (
            int(hexcode[1:3], 16),
            int(hexcode[3:5], 16),
            int(hexcode[5:7], 16)
        )

    # A function to convert Hex values to HSV colors
    @staticmethod
    def hex2hsv(hexcode: typing.Union[str, int] = '#000000')\
        -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent HSV/HSB values of a hex color *hexcode*
        """

        return Converters.rgb2hsv(*Converters.hex2rgb(hexcode))

    # A function to convert Hex values to HSL colors
    @staticmethod
    def hex2hsl(hexcode: typing.Union[str, int] = '#000000')\
        -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent HSL values of a hex color *hexcode*
        """

        return Converters.rgb2hsl(*Converters.hex2rgb(hexcode))

    # A function to convert Hex values to YIQ colors
    @staticmethod
    def hex2yiq(hexcode: typing.Union[str, int] = '#000000')\
        -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent YIQ values of a hex color *hexcode*
        """

        return Converters.rgb2yiq(*Converters.hex2rgb(hexcode))

    # A function to convert Hex values to CMYK colors
    @staticmethod
    def hex2cmyk(hexcode: typing.Union[str, int] = '#000000')\
        -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent CMYK values of a hex color *hexcode*
        """

        return Converters.rgb2cmyk(*Converters.hex2rgb(hexcode))

    # A function to convert RGB colors to HSV colors
    @staticmethod
    def rgb2hsv(
        red: typing.Union[int, float] = 0,
        green: typing.Union[int, float] = 0,
        blue: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent HSV values of an RGB color value
        """
        
        red = clamp(round(red), 0, 255) / 255
        green = clamp(round(green), 0, 255) / 255
        blue = clamp(round(blue), 0, 255) / 255

        cmax = max(red, green, blue)
        cmin = min(red, green, blue)

        diff = cmax - cmin

        # Hue calculation
        if diff == 0:
            hue = 0

        elif cmax == red:
            hue = round(60 * (((green - blue) / diff) % 6))

        elif cmax == green:
            hue = round(60 * (((blue - red) / diff) + 2))

        elif cmax == blue:
            hue = round(60 * (((red - green) / diff) + 4))

        # Saturation calculation
        saturation = 0 if cmax == 0 else diff / cmax

        # Value calculation
        value = cmax

        return (hue, saturation, value)

    # A function to convert an RGB color to an HSL color
    @staticmethod
    def rgb2hsl(
        red: typing.Union[int, float] = 0,
        green: typing.Union[int, float] = 0,
        blue: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent HSL values of an RGB color value
        """

        red = clamp(round(red), 0, 255) / 255
        green = clamp(round(green), 0, 255) / 255
        blue = clamp(round(blue), 0, 255) / 255

        cmax = max(red, green, blue)
        cmin = min(red, green, blue)

        diff = cmax - cmin

        # Luminance calculation
        luminance = (cmax + cmin) / 2

        # Hue calculation
        if diff == 0:
            hue = 0

        elif cmax == red:
            hue = round(60 * (((green - blue) / diff) % 6))

        elif cmax == green:
            hue = round(60 * (((blue - red) / diff) + 2))

        elif cmax == blue:
            hue = round(60 * (((red - green) / diff) + 4))

        # Saturation calculation
        saturation = 0 if diff == 0 else diff / (1 - abs(2 * luminance - 1))

        return (hue, saturation, luminance)

    # A function to convert an RGB color to YIQ color
    @staticmethod
    def rgb2yiq(
        red: typing.Union[int, float] = 0,
        green: typing.Union[int, float] = 0,
        blue: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent YIQ values of an RGB color value
        """

        red = clamp(round(red), 0, 255) / 255
        green = clamp(round(green), 0, 255) / 255
        blue = clamp(round(blue), 0, 255) / 255

        y = clamp(0.299*red+0.587*green+0.114*blue)
        i = clamp(0.596*red-0.274*green-0.322*blue, -0.5959, 0.5959)
        q = clamp(0.211*red-0.523*green+0.312*blue, -0.5229, 0.5229)

        return (y, i, q)

    # A function to convert an RGB color to CMYK color
    @staticmethod
    def rgb2cmyk(
        red: typing.Union[int, float] = 0,
        green: typing.Union[int, float] = 0,
        blue: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent CMYK values of an RGB color value
        """

        red = clamp(round(red), 0, 255) / 255
        green = clamp(round(green), 0, 255) / 255
        blue = clamp(round(blue), 0, 255) / 255

        black_key = 1 - max(red, green, blue)
        
        if black_key == 1:
            return (0, 0, 0, 1)

        cyan = (1 - black_key - red) / (1 - black_key)
        magenta = (1 - black_key - green) / (1 - black_key)
        yellow = (1 - black_key - blue) / (1 - black_key)

        return (cyan, magenta, yellow, black_key)

    # A function to convert an HSV color to an RGB color
    @staticmethod
    def hsv2rgb(
        hue: typing.Union[int, float] = 0,
        saturation: typing.Union[int, float] = 0,
        value: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent RGB values of an HSV color value
        """

        hue -= 360 * (hue // 360)   # Cycle clamping *hue* in [0, 360]
        hue /= 360

        saturation = clamp(saturation)
        value = clamp(value)

        if saturation == 0:
            red = green = blue = value * 255

            return (red, green, blue)

        i = int(hue * 6)
        f = hue * 6 - i
        p = 255 * (value * (1 - saturation))
        q = 255 * (value * (1 - saturation * f))
        t = 255 * (value * (1 - saturation * (1 - f)))

        value *= 255
        i %= 6

        if i == 0:
            return (value, t, p)

        if i == 1:
            return (q, value, p)

        if i == 2:
            return (p, value, t)

        if i == 3:
            return (p, q, value)

        if i == 4:
            return (t, p, value)

        if i == 5:
            return (value, p, q)

    # A function to convert an HSV color to an HSL color
    @staticmethod
    def hsv2hsl(
        hue: typing.Union[int, float] = 0,
        saturation: typing.Union[int, float] = 0,
        value: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent HSL values of an HSV color value
        """

        return Converters.rgb2hsl(*Converters.hsv2rgb(hue, saturation, value))

    # A function to convert an HSV color to a YIQ color
    @staticmethod
    def hsv2yiq(
        hue: typing.Union[int, float] = 0,
        saturation: typing.Union[int, float] = 0,
        value: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent YIQ values of an HSV color value
        """

        return Converters.rgb2yiq(*Converters.hsv2rgb(hue, saturation, value))

    # A function to convert an HSV color to a CMYK color
    @staticmethod
    def hsv2cmyk(
        hue: typing.Union[int, float] = 0,
        saturation: typing.Union[int, float] = 0,
        value: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent CMYK values of an HSV color value
        """

        return Converters.rgb2cmyk(*Converters.hsv2rgb(hue, saturation, value))

    # A function to convert HSL color to an RGB color
    @staticmethod
    def hsl2rgb(
        hue: typing.Union[int, float] = 0,
        saturation: typing.Union[int, float] = 0,
        luminance: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent RGB values of an HSL color value
        """

        hue -= 360 * (hue // 360)

        saturation = clamp(saturation)
        luminance = clamp(luminance)

        c = (1 - abs(2 * luminance - 1)) * saturation
        x = c * (1 - abs((hue / 60) % 2 - 1))
        m = luminance - c / 2

        if 0 <= hue < 60:
            return (round((c + m) * 255), round((x + m) * 255), 0)

        if 60 <= hue < 120:
            return (round((x + m) * 255), round((c + m) * 255), 0)

        if 120 <= hue < 180:
            return (0, round((c + m) * 255), round((x + m) * 255))

        if 180 <= hue < 240:
            return (0, round((x + m) * 255), round((c + m) * 255))

        if 240 <= hue < 300:
            return (round((x + m) * 255), 0, round((c + m) * 255))

        if 300 <= hue < 360:
            return (round((c + m) * 255), 0, round((x + m) * 255))

    # A function to convert an HSL color to an HSV color
    @staticmethod
    def hsl2hsv(
        hue: typing.Union[int, float] = 0,
        saturation: typing.Union[int, float] = 0,
        luminance: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent HSV values of an HSL color value
        """

        return Converters.rgb2hsv(*Converters.hsl2rgb(hue, saturation, luminance))

    # A function to convert an HSL color to a YIQ color
    @staticmethod
    def hsl2yiq(
        hue: typing.Union[int, float] = 0,
        saturation: typing.Union[int, float] = 0,
        luminance: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent YIQ values of an HSL color value
        """

        return Converters.rgb2yiq(*Converters.hsl2rgb(hue, saturation, luminance))

    # A function to convert an HSL color to a CMYK color
    @staticmethod
    def hsl2cmyk(
        hue: typing.Union[int, float] = 0,
        saturation: typing.Union[int, float] = 0,
        luminance: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent CMYK values of an HSL color value
        """

        return Converters.rgb2cmyk(*Converters.hsl2rgb(hue, saturation, luminance))

    # A function to convert a YIQ color to an RGB color
    @staticmethod
    def yiq2rgb(
        y: typing.Union[int, float] = 0,
        i: typing.Union[int, float] = 0,
        q: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent RGB values of a YIQ color value
        
        NOTE: The following are the acceptable values:
            0 ≤ y ≤ 1
            -0.5959 ≤ i ≤ 0.5959
            -0.5229 ≤ q ≤ 0.5229
        
        The values will be clamped between these ranges
        """

        y = clamp(y)
        i = clamp(i, -0.5959, 0.5959)
        q = clamp(q, -0.5229, 0.5229)

        red = y + 0.956 * i + 0.621 * q
        green = y - 0.272 * i - 0.647 * q
        blue = y - 1.11 * i + 1.7 * q

        return (
            round(clamp(red) * 255),
            round(clamp(green) * 255),
            round(clamp(blue) * 255)
        )

    # A function to convert a YIQ color to an HSV color
    @staticmethod
    def yiq2hsv(
        y: typing.Union[int, float] = 0,
        i: typing.Union[int, float] = 0,
        q: typing.Union[int, float] = 0,
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent HSV values of a YIQ color value
        """

        return Converters.rgb2hsv(*Converters.yiq2rgb(y, i, q))

    # A function to convert a YIQ color to an HSL color
    @staticmethod
    def yiq2hsl(
        y: typing.Union[int, float] = 0,
        i: typing.Union[int, float] = 0,
        q: typing.Union[int, float] = 0,
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent HSL values of a YIQ color value
        """

        return Converters.rgb2hsl(*Converters.yiq2rgb(y, i, q))

    # A function to convert a YIQ color to a CMYK color
    @staticmethod
    def yiq2cmyk(
        y: typing.Union[int, float] = 0,
        i: typing.Union[int, float] = 0,
        q: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent CMYK values of a YIQ color value
        """

        return Converters.rgb2cmyk(*Converters.yiq2rgb(y, i, q))

    # A function to convert a CMYK color to an RGB color
    @staticmethod
    def cmyk2rgb(
        cyan: typing.Union[int, float] = 0,
        magenta: typing.Union[int, float] = 0,
        yellow: typing.Union[int, float] = 0,
        black_key: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent RGB values of an CMYK color value
        """

        cyan = clamp(cyan)
        magenta = clamp(magenta)
        yellow = clamp(yellow)
        black_key = clamp(black_key)

        return (
            round(255 * (1 - cyan) * (1 - black_key)),
            round(255 * (1 - magenta) * (1 - black_key)),
            round(255 * (1 - yellow) * (1 - black_key))
        )

    # A function to convert a CMYK color to an HSV color
    @staticmethod
    def cmyk2hsv(
        cyan: typing.Union[int, float] = 0,
        magenta: typing.Union[int, float] = 0,
        yellow: typing.Union[int, float] = 0,
        black_key: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent HSV values of an CMYK color value
        """

        return Converters.rgb2hsv(*Converters.cmyk2rgb(cyan, magenta, yellow, black_key))

    # A function to convert a CMYK color to an HSL color
    @staticmethod
    def cmyk2hsl(
        cyan: typing.Union[int, float] = 0,
        magenta: typing.Union[int, float] = 0,
        yellow: typing.Union[int, float] = 0,
        black_key: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent HSL values of an CMYK color value
        """

        return Converters.rgb2hsl(*Converters.cmyk2rgb(cyan, magenta, yellow, black_key))

    # A function to convert a CMYK color to a YIQ color
    @staticmethod
    def cmyk2yiq(
        cyan: typing.Union[int, float] = 0,
        magenta: typing.Union[int, float] = 0,
        yellow: typing.Union[int, float] = 0,
        black_key: typing.Union[int, float] = 0
    ) -> typing.Tuple[typing.Union[int, float]]:
        """
        Returns the equivalent YIQ values of an CMYK color value
        """

        return Converters.rgb2yiq(*Converters.cmyk2rgb(cyan, magenta, yellow, black_key))


def main(clear: bool = False) -> None:
    """
    The main function of the program (direct entry point)
    
    Auto-runs when module is run directly, or can be run by calling
    
    clear (bool) = False - clears screen before starting if True
    """
    
    if clear:
        __import__('os').system('cls')  # Clears screen in Windows
        __import__('os').system('clear')    # Clears screen in Unix OSs
    
    print("Welcome to DyePy's mini command-line interpreter.")
    print("Enter '!exit' to exit.\n")

    while True:
        # Acts like a command-line REPL for python
        func = input('python> ')

        if func == '!exit':
            break

        try:
            func = eval(func)

        except (SyntaxError, BaseException):
                if func != '' and not func.isspace():   # Not empty line
                    func = ''.join((
                        Styles.Background.RED,
                        Styles.Foreground.WHITE,
                        'Invalid statement/function call!',
                        Styles.RESET
                    ))

        if func is not None:
            print(func)


if __name__ == '__main__':
    import sys
    
    main('--cls' in sys.argv or '--clear' in sys.argv)
