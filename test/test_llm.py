from llm import ask_llm

# Test the ask_llm function
try:
    response = ask_llm(
        system_prompt="You are a helpful assistant.",
        user_message="What is the meaning of life?"
    )
    print("LLM Response:")
    print(response)
except Exception as e:
    print(f"Error: {e}")
