class Time:
    """Egyszeru osztaly eltelt ido modellezesere
    """

    def __init__(self, seconds:int=0):
        """Inicializalja az idot a megadott masodpercekkel

        Args:
            seconds (int): a masodpercek szama
        """
        self.seconds = seconds
        
    def to_seconds(self) -> int:
        """Adja vissza egy `int`-ben, hogy masodpercben kifejezve mennyi az ido

        Returns:
            int: a tarolt ido masodpercekben

        >>> Time(12).to_seconds()
        12
        >>> Time(345).to_seconds()
        345
        """
        return self.seconds

    def _ss(self)->int:
        """Visszaadja, hogy mennyit mutat a "masodpercmutato"

        Returns:
            int: egesz perceket leszamitva a masodpercek szama

        >>> Time(12)._ss()
        12
        >>> Time(72)._ss()
        12
        >>> Time(1234)._ss()
        34
        """
        while self.seconds > 60:
            self.seconds -= 60
        return self.seconds
    
    def _mm(self) -> int:
        """Visszaadja, hogy mennyit mutat a "percmutato"

        Returns:
            int: egesz orakat leszamitva az egesz percek szma

        >>> Time(12)._mm()
        0
        >>> Time(72)._mm()
        1
        >>> Time(1234)._mm()
        20
        """
        return int(self.seconds / 60)
    
    def _hh(self) -> int:
        """Visszaadja, hogy mennyit mutat az "oramutato", amely sosem nullazodik.

        Returns:
            int: az egesz letelt orak szama, 24 fole is mehet
        
        >>> Time(12)._hh()
        0
        >>> Time(72)._hh()
        0
        >>> Time(1234)._hh()
        0
        >>> Time(3600)._hh()
        1
        >>> Time(12345)._hh()
        3
        """
        return int(self.seconds / 3600)
    
    def pretty_format(self) -> str:
        """Visszaadja az idot szep modon
         - `s` vagy `ss` egy perc alatt
         - `m:ss` vagy `mm:ss` egy perc felett es egy ora alatt
         - `h:mm:ss` egy ora felett. (Az orak szama tetszolegesen nagy lehet)

        Returns:
            str: a szepen formazott ido

        >>> Time(12).pretty_format()
        '12'
        >>> Time(72).pretty_format()
        '1:12'
        >>> Time(3600).pretty_format()
        '1:00:00'
        >>> Time(12345).pretty_format()
        '3:25:45'
        >>> Time(123456).pretty_format()
        '34:17:36'
        """
        secs = self.seconds
        hour, minutes, seconds = None, None, None

        hour = Time(secs)._hh()
        secs -= 3600*hour

        minutes = Time(secs)._mm()
        secs -= minutes * 60

        seconds = Time(secs)._ss()

        if hour > 0:
            return f'{hour:d}:{minutes:02d}:{seconds:02d}'
        elif hour == 0 and minutes == 0:
            return f'{seconds:02d}'
        else: 
            return f'{minutes}:{seconds:02d}'

    def set_from_string(self, time:str) -> int:
        """Beallitja az idot egy string alapjan, melynek a formatuma olyan mint a `pretty_format` eseteben.

        Returns:
            int: a beallitott ido masodpercekben

        Args:
            time (str): az ido szoveg formaban
        
        >>> Time().set_from_string('12')
        12
        >>> Time().set_from_string('1:12')
        72
        >>> Time().set_from_string('1:00:00')
        3600
        >>> Time().set_from_string('3:25:45')
        12345
        >>> Time().set_from_string('111:01:23')
        399683
        """
        hms = time.split(':')
        if len(hms) == 1:
            return int(hms[0])
        if len(hms) == 2:
            return int(hms[0])*60 + int(hms[1])
        if len(hms) == 3:
            return int(hms[0])*3600 + int(hms[1]) * 60 + int(hms[2])