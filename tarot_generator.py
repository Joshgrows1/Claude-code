import random

TAROT_CARDS = [
    # Major Arcana
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World",
    # Minor Arcana - Wands
    "Ace of Wands", "Two of Wands", "Three of Wands", "Four of Wands",
    "Five of Wands", "Six of Wands", "Seven of Wands", "Eight of Wands",
    "Nine of Wands", "Ten of Wands", "Page of Wands", "Knight of Wands",
    "Queen of Wands", "King of Wands",
    # Minor Arcana - Cups
    "Ace of Cups", "Two of Cups", "Three of Cups", "Four of Cups",
    "Five of Cups", "Six of Cups", "Seven of Cups", "Eight of Cups",
    "Nine of Cups", "Ten of Cups", "Page of Cups", "Knight of Cups",
    "Queen of Cups", "King of Cups",
    # Minor Arcana - Swords
    "Ace of Swords", "Two of Swords", "Three of Swords", "Four of Swords",
    "Five of Swords", "Six of Swords", "Seven of Swords", "Eight of Swords",
    "Nine of Swords", "Ten of Swords", "Page of Swords", "Knight of Swords",
    "Queen of Swords", "King of Swords",
    # Minor Arcana - Pentacles
    "Ace of Pentacles", "Two of Pentacles", "Three of Pentacles", "Four of Pentacles",
    "Five of Pentacles", "Six of Pentacles", "Seven of Pentacles", "Eight of Pentacles",
    "Nine of Pentacles", "Ten of Pentacles", "Page of Pentacles", "Knight of Pentacles",
    "Queen of Pentacles", "King of Pentacles",
]

CARD_MEANINGS = {
    "The Fool": "New beginnings, spontaneity, a free spirit",
    "The Magician": "Manifestation, resourcefulness, power",
    "The High Priestess": "Intuition, sacred knowledge, divine feminine",
    "The Empress": "Femininity, beauty, nature, abundance",
    "The Emperor": "Authority, structure, control, fatherhood",
    "The Hierophant": "Spiritual wisdom, tradition, conformity",
    "The Lovers": "Love, harmony, relationships, choices",
    "The Chariot": "Control, willpower, success, determination",
    "Strength": "Courage, persuasion, influence, compassion",
    "The Hermit": "Soul-searching, introspection, inner guidance",
    "Wheel of Fortune": "Good luck, karma, life cycles, destiny",
    "Justice": "Justice, fairness, truth, cause and effect",
    "The Hanged Man": "Pause, surrender, letting go, new perspectives",
    "Death": "Endings, change, transformation, transition",
    "Temperance": "Balance, moderation, patience, purpose",
    "The Devil": "Shadow self, attachment, addiction, restriction",
    "The Tower": "Sudden change, upheaval, chaos, revelation",
    "The Star": "Hope, faith, purpose, renewal, spirituality",
    "The Moon": "Illusion, fear, the unconscious, intuition",
    "The Sun": "Positivity, fun, warmth, success, vitality",
    "Judgement": "Reflection, reckoning, awakening, absolution",
    "The World": "Completion, integration, accomplishment, travel",
}

ORIENTATIONS = ["Upright", "Reversed"]


def draw_cards(count=5):
    """Draw `count` unique random tarot cards."""
    return random.sample(TAROT_CARDS, count)


def display_reading(cards):
    positions = ["Past", "Present", "Future", "Advice", "Outcome"]
    print("\n" + "=" * 50)
    print("        YOUR TAROT READING")
    print("=" * 50)
    for i, card in enumerate(cards):
        orientation = random.choice(ORIENTATIONS)
        position = positions[i] if i < len(positions) else f"Card {i + 1}"
        meaning = CARD_MEANINGS.get(card, "Reflect on this card's symbolism")
        print(f"\n[{position}]")
        print(f"  Card:        {card} ({orientation})")
        print(f"  Meaning:     {meaning}")
    print("\n" + "=" * 50 + "\n")


def main():
    print("Welcome to the Tarot Card Generator!")
    while True:
        input("Press Enter to draw 5 cards (or Ctrl+C to quit)...")
        cards = draw_cards(5)
        display_reading(cards)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nFarewell! May the cards guide your path.")
