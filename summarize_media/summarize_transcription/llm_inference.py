# "Normal" text response
from typing import Any, Dict, List, Union

from groq import Groq
from openai import OpenAI
from ratelimit import limits, sleep_and_retry


@sleep_and_retry
@limits(calls=1, period=0.5)
def get_response(
    messages: List[dict],
    client: Union[Groq, OpenAI],
    client_args: Dict[str, Any],
    kept_keys: List[str] = None,
    discard_keys: List[str] = None,
    **kwargs,
):
    """Gets a text response from llm client

    Desinged for dependency injection use case, example:
    ```python
    messages = [{"role": "system", "content": "<some message>"}, <more messages>]
    response_func = partial(get_response, client = OpenAI_client, client_args = client_args)

    new_message = response_func(messages)
    messages.append(new_messages)
    ```

    Args:
        messages (List[dict]): The conversation history, each message (dictionary) in the list must have fields "role" and "content"
        client (Union[Groq, OpenAI]): llm client to be used
        client_args (dict): arguments to supply to the llm client
        kept_keys (List[str], optional): A list of keys to keep. If not provided, keeps the "role" and "content" keys only, if argument `discard_keys` is also provided, the behavior of this argument will be over-ridden and not take effect
        discard_keys (List[str], optional): A List of keys to discard. Overrides behavior of `keep_keys`

    Returns:
        dict: A dictionary containing the response
    """
    response = client.chat.completions.create(messages=messages, **client_args)
    response_dict = dict(response.choices[0].message)

    kept_keys = kept_keys if kept_keys else ["role", "content"]
    if discard_keys is not None:
        for key in discard_keys:
            response_dict.pop(key, None)
    else:
        kept_keys_dict = {
            key: response_dict[key] for key in kept_keys if key in response_dict
        }
        response_dict = kept_keys_dict

    return response_dict
