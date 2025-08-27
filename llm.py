import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def ask_llm(system_prompt="", user_message="", model="openai/gpt-5"):
    """
    Ask an LLM a question using the OpenRouter API.

    Args:
        system_prompt (str): The system prompt to guide the LLM's behavior
        user_message (str): The user's message/question
        model (str): The model to use. Defaults to "moonshotai/kimi-k2"

    Returns:
        str: The LLM's response content
    """
    # Get API key from environment variables
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables")

    # Initialize the OpenAI client
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    # Prepare messages
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})

    if user_message:
        messages.append({"role": "user", "content": user_message})

    # Make the API call
    completion = client.chat.completions.create(
        model=model,
        messages=messages
    )

    # Return the response content
    return completion.choices[0].message.content

# Example usage:
# response = ask_llm(
#     system_prompt="You are a helpful assistant.",
#     user_message="What is the meaning of life?"
# )
# print(response)
