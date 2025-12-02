def calm_mentor(r: str) -> str:
    return (
        "Here’s a grounded perspective: " 
        f"{r}"
        "Take your time — you're making progress."
    )

def witty_friend(r: str) -> str:
    return (
        "Alright, here’s the tea ☕:"
        f"{r}"
        "Now keep shining, legend 😎"
    )

def therapist(r: str) -> str:
    return (
        "Let's talk through this slowly."
        f"{r}"
        "How does that make you feel?"
    )

def strict_coach(r: str) -> str:
    return (
        f"Focus. {r} Now get it done — no excuses."
    )

def formal_consultant(r: str) -> str:
    return (
        "Here is a structured observation:"
        f"{r}"
        "I can provide a detailed action plan if needed."
    )

PERSONALITIES = {
    "calm_mentor": calm_mentor,
    "witty_friend": witty_friend,
    "therapist": therapist,
    "strict_coach": strict_coach,
    "formal_consultant": formal_consultant,
    "neutral": lambda x: x
}

def apply_personality(response: str, personality: str) -> str:
    return PERSONALITIES.get(personality, lambda x: x)(response)
