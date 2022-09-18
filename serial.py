"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start=0):
        """ Make a new generator with user specified start val or 0 by default"""
        self.start = self.next = start
    
    def __repr__(self):
        """Show representation"""
        return f"{self.start}"

    def generate(self):
        """Return next serial by +1"""
        self.next += 1
        return self.next - 1
    
    def reset(self):
        """Reset number to original start"""

        self.next = self.start




