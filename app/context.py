def generate_neutral_response(user_last_message: str) -> str:
    return (
        "Here is a neutral response to your message: "
        f"'{user_last_message}'."
        "Let me know if you'd like more details"
    )