""" "Convenient" function to provide llm imference

Will clean up this file later

"""

import os

from openai import OpenAI

from .llm_inference import get_response

# Automatically gets the
client = OpenAI(
    base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY")
)

client_args = {"temperature": 0.3, "model": "anthropic/claude-3.5-sonnet:beta"}

prompt_path = "/mnt/d/MyPath/Projects/summarize-media/summarize_media/summarize_transcription/prompts/default_prompt.txt"


with open(prompt_path, "r") as file:
    default_sys_prompt = file.read()


def get_summarization(input_text: str, sys_prompt: str = None) -> str:
    sys_prompt = sys_prompt if sys_prompt else default_sys_prompt
    sys_msg = {"role": "system", "content": sys_prompt}
    input_msg = {"role": "user", "content": input_text}
    messages = [sys_msg, input_msg]
    response = get_response(messages=messages, client=client, client_args=client_args)
    return response["content"]
