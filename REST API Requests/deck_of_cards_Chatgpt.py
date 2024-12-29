import requests
from deck_of_cards import get_a_deck

def draw_cards(deck_id, count):
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}"
    response = requests.get(url)
    if response.status_code == 200:
        cards = response.json().get("cards", [])
        return [card["code"] for card in cards]
    else:
        return []

def add_cards_to_pile(deck_id, pile_name, cards):
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/add/"
    payload = {"cards": ",".join(cards)}
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)
        print(response.text)

deck_id = get_a_deck()
cards_to_add = draw_cards(deck_id, count=21)
add_cards_to_pile(deck_id, "name", cards_to_add)
