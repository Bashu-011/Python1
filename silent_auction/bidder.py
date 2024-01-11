from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
bidding = True

def highest_bidder(new_dict):
  highest_bid = 0
  for bidder in new_dict:
    bid_amount = new_dict[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The highest bidder is {winner} with a bid of ${highest_bid}")

new_dict = {}

while bidding:
  name = input("Enter you name: ")
  bid = int(input("Enter your bid price: $"))
  new_dict[name] = bid
  more_bidders = input("Are there other bidders: ")
  if more_bidders == "yes":
    clear()
  elif more_bidders == "no":
    highest_bidder(new_dict)
    bidding = False