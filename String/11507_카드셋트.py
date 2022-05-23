num_cards={'P':13,'K':13,'H':13,'T':13}
s=input()
card_set=set()

check=0
for idx in range(0,len(s),3):
    if s[idx:idx+3] in card_set :
        print("GRESKA")
        check=1
        break
    card_set.add(s[idx:idx+3])
    num_cards[s[idx]]-=1

if check==0:
    print(*num_cards.values())
