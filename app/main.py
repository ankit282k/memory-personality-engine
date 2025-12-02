from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from .memory import extract_memory
from .personality import apply_personality
from .context import generate_neutral_response

app = FastAPI(title="Memory + Personality Engine")

class Request(BaseModel):
    messages: List[str]
    personality: str = "calm_mentor"

class Response(BaseModel):
    memory: dict
    personality_response: dict

@app.post("/process", response_model=Response)
def process(req: Request):

    # Step 1: Extract memory
    memory = extract_memory(req.messages)

    # Step 2: Generate a neutral response
    last_message = req.messages[-1]
    original_response = generate_neutral_response(last_message)

    # Step 3: Transform using personality engine
    transformed_response = apply_personality(last_message, req.personality)

    return Response(
        memory=memory,
        personality_response={
            "original": last_message,
            "transformed": transformed_response
        }
    )
