import requests

def get_a_deck():
    req1=requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=2")
    response=req1.json()
    return response['deck_id']

def draw_5_cards(deck_id):
    req2=requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5')
    response= req2.json().get('cards')
    for card in response:
        print(f'the card is {card['value']} of {card['suit']}')
def end():
    my_deck_id= get_a_deck()
    draw_5_cards(my_deck_id)
if __name__=='__main__':
    end()


