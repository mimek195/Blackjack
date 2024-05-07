class Card:
    def __init__(self, value, name, s_name):
        self.value = value
        self.name = name
        self.s_name = s_name


deck = [  # Hearts
    Card(2, "♥ Two", "♥2"), Card(3, "♥ Three", "♥3"), Card(4, "♥ Four", "♥4"),
    Card(5, "♥ Five", "♥5"), Card(6, "♥ Six", "♥6"), Card(7, "♥ Seven", "♥7"), Card(8, "♥ Eight", "♥8"),
    Card(9, "♥ Nine", "♥9"), Card(10, "♥ Ten", "♥10"), Card(10, "Valet of Hearts", "♥V"),
    Card(10, "Queen of Hearts", "♥Q"),
    Card(10, "King of Hearts", "♥K"), Card(11, "Ace of Hearts", "♥A"),
    # Spades
    Card(2, "♠ Two", "♠2"), Card(3, "♠ Three", "♠3"), Card(4, "♠ Four", "♠4"),
    Card(5, "♠ Five", "♠5"), Card(6, "♠ Six", "♠6"), Card(7, "♠ Seven", "♠7"), Card(8, "♠ Eight", "♠8"),
    Card(9, "♠ Nine", "♠9"), Card(10, "♠ Ten", "♠10"), Card(10, "Valet of Spades", "♠V"),
    Card(10, "Queen of Spades", "♠Q"),
    Card(10, "King of Spades", "♠K"), Card(11, "Ace of Spades", "♠A"),
    # Diamonds
    Card(2, "♦ Two", "♦2"), Card(3, "♦ Three", "♦3"), Card(4, "♦ Four", "♦4"),
    Card(5, "♦ Five", "♦5"), Card(6, "♦ Six", "♦6"), Card(7, "♦ Seven", "♦7"), Card(8, "♦ Eight", "♦8"),
    Card(9, "♦ Nine", "♦9"), Card(10, "♦ Ten", "♦10"), Card(10, "Valet of Diamonds", "♦V"),
    Card(10, "Queen of Diamonds", "♦Q"),
    Card(10, "King of Diamonds", "♦K"), Card(11, "Ace of Diamonds", "♦A"),
    # Clubs
    Card(2, "♣ Two", "♣2"), Card(3, "♣ Three", "♣3"), Card(4, "♣ Four", "♣4"),
    Card(5, "♣ Five", "♣5"), Card(6, "♣ Six", "♣6"), Card(7, "♣ Seven", "♣7"), Card(8, "♣ Eight", "♣8"),
    Card(9, "♣ Nine", "♣9"), Card(10, "♣ Ten", "♣10"), Card(10, "Valet of Clubs", "♣V"),
    Card(10, "Queen of Clubs", "♣Q"),
    Card(10, "King of Clubs", "♣K"), Card(11, "Ace of Clubs", "♣A"),
]
