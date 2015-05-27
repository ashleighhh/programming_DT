#The beginning
reserve_price = int(input("What is the reserve price?"))
highest_bid = 0
name = ""
bid = 0
names = [""]
bids = [0]
#The auction
print ("Auction has started")
while name.upper() != 'F' :
    print ("Highest bid so far is $"+ str(max(bids))+ " \"F\" to finish)")
    name = input("What is your name?")
    name = name.title()
    print (name)
    if name.upper()!= "F":
        bid = int(input("What is your bid?"))
        print (bid)
        if bid > highest_bid:
            names.append(name)
            bids.append(bid)
            highest_bid = bid
        else:
            print ("Sorry ", name, " You'll need to make another, higher bid.")

#The end 
if highest_bid >= reserve_price:
    print ("Auction won by ", names[len(names)-1], " with a bid of $", highest_bid)
    for i in range (0, len(names)):
        print (names[i], " bid ", bids[i])
else:
    print ("Auction did not meet reserve price")
    for i in range (0, len(names)):
        print (names[i], " bid ", bids[i])
