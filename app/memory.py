from typing import List, Dict

def extract_memory(user_messages: List[str]) -> Dict:
    preferences = []
    emotions = []
    facts = []

    for msg in user_messages:
        text = msg.strip()
        lower = text.lower()

        if any(kw in lower for kw in ["i like", "i love", "i prefer", "my favourite", "my favorite"]):
            preferences.append(text)

        if any(kw in lower for kw in ["i feel", "i am feeling", "i feel like", "i get stressed", "i get anxious", "i get angry", "i'm sad", "i am sad", "i'm happy", "i am happy"]):
            emotions.append(text)

        fact_keywords = [
            "i work as", "i work at", "i am working as",
            "i study", "i am studying",
            "my goal", "my goals",
            "i want to", "i plan to", "i am planning to",
            "i live in", "i am from",
            "i use", "i am learning", "i'm learning"
        ]
        if any(kw in lower for kw in fact_keywords):
            facts.append(text)

    preferences = list(set(preferences))
    emotions = list(set(emotions))
    facts = list(set(facts))

    return {
        "preferences": preferences,
        "emotional_patterns": emotions,
        "facts": facts
    }
