import random
class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
    def show(self):
        print("{} of {}".format(self.val, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
    def build(self):
        for c in ["clubs", "spades", "diamonds", "hearts"]:
            for i in range(1, 11):
                self.cards.append(Card(c, i))
        for c in ["clubs", "spades", "diamonds", "hearts"]:
            for i in ["J", "Q", "K"]:
                self.cards.append(Card(c, i))
    
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

    def show(self):
        for i in self.cards:
            i.show()

class Player:
    def __init__(self):
        self.hand = [] # list of Card
    def draw(self, deck):
        drawn_card = deck.drawCard()
        self.hand.append(drawn_card)
        return drawn_card
    def show(self):
        print("Your cards:")
        for i in self.hand:
            i.show() # call Card.show() method
    
    def getTotalPoints(self, sum):
        for i in range(len(self.hand)):
            cur = self.getPoints(self.hand[i])
            sum = sum + cur
        return int(sum)
    
    def getCumulativePoints(self, card, sum):
        sum = sum + self.getPoints(card)
        return int(sum)

    def getPoints(self, card):
        val = str(card.val)
        if val == 'J' or val == 'Q' or val == 'K':
            return 10
        elif val == '1':
            print("{} of {} is drawn. What you choose? ".format(card.val, card.suit))
            print("Enter 1 for 1")
            print("Enter 2 for 11")
            choice = int(input())
            if choice == 1:
                return 1
            elif choice == 2:
                return 11
        else: 
            return int(val)

class Dealer:
    def __init__(self):
        self.hand = []
    def draw(self, deck):
        drawn_card = deck.drawCard()
        self.hand.append(drawn_card)
        return drawn_card
    def show(self):
        print("Dealer cards:")
        for i in self.hand:
            i.show() # call Card.show() method

    def getTotalPoints(self, sum):
        for i in range(len(self.hand)):
            cur = self.getPoints(self.hand[i])
            sum = sum + cur
        return int(sum)
    
    def getCumulativePoints(self, card, sum):
        sum = sum + self.getPoints(card)
        return int(sum)

    def getPoints(self, card):
        val = str(card.val)
        if val == 'J' or val == 'Q' or val == 'K':
            return 10
        elif val == '1':
            print("{} of {} is drawn. What you choose? ".format(card.val, card.suit))
            print("Enter 1 for 1")
            print("Enter 2 for 11")
            choice = int(input())
            if choice == 1:
                return 1
            elif choice == 2:
                return 11
        else: 
            return int(val)

def printPoints(d, p):
    print("\nDealer score : {}".format(d))
    print("Your score : {}".format(p))

# main() method 
def main():
    deck = Deck()
    deck.build()
    deck.shuffle()
    #deck.show()

    print("Game begins...")
    print("Drawing cards for player...")
    # initialize player
    player = Player()
    player.draw(deck)
    player.draw(deck)

    player.show()
    player_total_points = player.getTotalPoints(0)
    print("Your points till now : {}".format(player_total_points))
    if player_total_points == 21:
        print("BlackJack! You win!")
        return

     #initialize dealer
    print("Drawing cards for Dealer...")
    dealer = Dealer()
    dealer.draw(deck)
    dealer.show()
    dealer_total_points = dealer.getTotalPoints(0)
    print("Dealer points till now : {}".format(dealer_total_points))

    while True:
        print("\nWhat do you want to do ?")
        print("1 for get another card")
        print("2 for quit")
        choice = int(input())
        if choice == 1:
            drawn_card = player.draw(deck)
            player.show()
            player_total_points = player.getCumulativePoints(drawn_card, player_total_points)
            print("\nYour points till now : {}".format(player_total_points))
            if player_total_points == 21:
                printPoints(dealer_total_points, player_total_points)
                print("BlackJack! You win!")
                break
            elif player_total_points > 21:
                printPoints(dealer_total_points, player_total_points)
                print("Your score busted....Dealer wins!")
                break
            #elif player_total_points < 21:
             #   continue
        if choice == 2:
            while dealer_total_points < player_total_points and dealer_total_points <= 17:
                drawn_card = dealer.draw(deck)
                dealer_total_points = dealer.getCumulativePoints(drawn_card, dealer_total_points)
                
                if dealer_total_points < player_total_points:
                    continue
                elif dealer_total_points > 17:
                    print("Dealer reached limit..Score calculating...")
                    break
        if dealer_total_points > 21:
                    printPoints(dealer_total_points, player_total_points)
                    print("Dealer score busted...You win!")
                    break
        elif dealer_total_points == 21:
                    printPoints(dealer_total_points, player_total_points)
                    print("BlackJack! Dealer wins!")
                    break
        elif dealer_total_points > player_total_points:
            printPoints(dealer_total_points, player_total_points)
            print("Dealer wins!")
            break
        elif dealer_total_points == player_total_points:  
            printPoints(dealer_total_points, player_total_points)
            print("Draw!")
            break
        
if __name__ == "__main__":
    main()

