import random

class BlackJack():

    '''
        The BlackJack class has a few methods:

        - startGame:
            - deals player 2 cards and self 2 cards
            - shows what the player has, but not the dealer
            - adds players cards together
                - if cards = 21, show "Blackjack! You win"
            - adds dealers cards together
            - deals player 1 additional card
            - adds players cards together:
                - if number is > 21, show "Bust"
                - else add players cards together
            
        - stand:
            - compare dealers hand to players hand
                - if players hand > dealers hand, "Player wins!"
                - else, "Player loses!"



        Expected Attributes:
        - deck: list []
        - player_hand: list []
        - dealer_hand: list []
    '''

    def __init__(self, deck, player_hand, dealer_hand):
        self.deck = deck
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand


    def startGame(self):
        self.player_hand.append(random.choice(self.deck))
        self.player_hand.append(random.choice(self.deck))

        self.dealer_hand.append(random.choice(self.deck))
        self.dealer_hand.append(random.choice(self.deck))

        print(f"Your hand is {self.player_hand} which equals {sum(self.player_hand)}.\n")

        if sum(self.player_hand) == 21:
            print("Blackjack! You win!")

        if sum(self.player_hand) > 21:
            print("You busted!")

        
        while True:
            response = input("\nWould you like to hit or stand?\n").lower()
            if response == 'hit':
                self.player_hand.append(random.choice(self.deck))
                if sum(self.player_hand) > 21:
                    print(f"Your hand is {self.player_hand} which equals {sum(self.player_hand)}.\n")
                    print("You busted!")
                    self.player_hand = []
                    self.dealer_hand = []
                    break
                else:
                    print(f"Your hand is {self.player_hand} which equals {sum(self.player_hand)}.\n")
                    continue
            
            elif response == 'stand':
                    self.stand()
                    break
            
            


    def stand(self):
        print(f"Your total is {sum(self.player_hand)}")
        print(f"The dealer's hand is {self.dealer_hand} which totals {sum(self.dealer_hand)}")
        

        if sum(self.player_hand) > sum(self.dealer_hand):
            print("You win!")
            self.player_hand = []
            self.dealer_hand = []

        elif sum(self.player_hand) == sum(self.dealer_hand):
            print("Tie!")
            self.player_hand = []
            self.dealer_hand = []
            
        else:
            print("You lose!")
            self.player_hand = []
            self.dealer_hand = []
            


game_1 = BlackJack((([i for i in range(1, 14)]) * 4), [], [])

def run():
    while True:
        response = input("Welcome to the table! The goal is to get 21. If you go over, you bust and automatically lose.\nPlease select an option: start / leave: ").lower()

        if response == 'start':
            game_1.startGame()

        elif response == 'leave':
            print("Thank you for playing!")
            break
    
        else:
            print("Please try a different input!")

run()