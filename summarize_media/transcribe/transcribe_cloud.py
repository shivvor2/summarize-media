"""Transcribe input media (e.g. podcasts) via cloud service e.g. replicate"""

from typing import Literal, Any
import replicate

models = {
    "medium": "carnifexer/whisperx:1e0315854645f245d04ff09f5442778e97b8588243c7fe40c644806bde297e04",
    "large-v2": "daanelson/whisperx:9aa6ecadd30610b81119fc1b6807302fd18ca6cbb39b3216f430dcf23618cedd",
    "large-v3": "victor-upmeet/whisperx:84d2ad2d6194fe98a17d2b60bef1c7f910c46b2f6fd38996ca457afd9c8abfcb",
}


# Input must be a .wav file
def get_transcribe_cloud(
    file_path: str,
    model_name: Literal["medium", "large-v2", "large-v3"] = "large-v2",
    **kwargs: Any,
) -> Any:
    """Transcribes an audio file via replicate (cloud service)

    Has multilingual support but not always guarenteed
    For other arguments, please check the available arguments for whisperX [medium](https://replicate.com/carnifexer/whisperx/api/schema), [large-v2](https://replicate.com/daanelson/whisperx/api/schema) and [large-v3](https://replicate.com/victor-upmeet/whisperx/api)
    Providing an invalid argument will likely result in an error

    Args:
        file_path (str): relative path to the locally stored .wav file
        model (str): Choose which model to use, must be one of "medium", "large-v2" and "large-v3", defaults to "large-v2"
        kwargs: Refer to each model's schema page

    returns:
        A dictionary containing transcribed audio and sentence level timestamps
    """
    audio_key = "audio_path" if model_name == "large-v3" else "audio"
    audio = open(file_path, "rb")
    inputs = {audio_key: audio} | kwargs

    output = replicate.run(models[model_name], inputs=inputs)

    return output
