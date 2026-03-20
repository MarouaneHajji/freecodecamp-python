# A class that represents a musical instrument
class MusicalInstrument:

    # Constructor — stores the instrument's name and family type
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

    # Prints a fun message about playing the instrument
    def play(self):
        print(f'The {self.name} is fun to play!')

    # Returns a fact about which instrument family it belongs to
    def get_fact(self):
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.'


instrument_1 = MusicalInstrument('Oboe', 'woodwind')
instrument_2 = MusicalInstrument('Trumpet', 'brass')

instrument_1.play()
print(instrument_1.get_fact())
instrument_2.play()
print(instrument_2.get_fact())