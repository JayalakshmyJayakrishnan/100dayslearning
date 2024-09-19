card_vals = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']
card_signs= ['♥', '♠', '♦', '♣']

print("The deck of cards are:")
for val in range (len(card_vals)):
    for signval in range(len(card_signs)):
        print(card_vals[val], card_signs[signval])
        
