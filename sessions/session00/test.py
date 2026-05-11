from anthropic import Anthropic

client = Anthropic()

with client.messages.stream(
    model="claude-sonnet-4-20250514",
    max_tokens=300,
    system="You are a helpful assistant, and also a duck. You like to quack!",
    messages=[
        {
            "role": "user",
            "content": "Tell me a fun story about Hult International Business School."
        }
    ]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)