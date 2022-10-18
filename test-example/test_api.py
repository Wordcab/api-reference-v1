# coding=utf-8
"""Basic Python script to test the API."""
import json
import logging
import requests
from typing import Optional

import os
from dotenv import load_dotenv


load_dotenv()
logger = logging.getLogger(__name__)


def summarize_text_file(
    text_file_path: str,
    api_key: str,
    display_name: str,
    summary_type: Optional[str] = "narrative",
    summary_lens: Optional[str] = "3",
    split_long_utterances: Optional[bool] = False,
    tags: Optional[str] = None,
    ephemeral_data: Optional[bool] = False,
):
    """
    Test the summarize endpoint with a text file.

    Parameters
    ----------
    text_file_path : str
        Path to the text file to summarize.
    api_key : str
        API key to use.
    display_name : str
        A human-readable name for your job.
    summary_type : str, optional, default "narrative"
        The type of summary to generate. Can be "narrative" or "reason_conclusion".
    summary_lens : str, optional, default "3"
        The number of sentences to include in the summary. "1" to "5".
    split_long_utterances : bool, optional, default False
        Whether to split long utterances into multiple shorter utterances.
    tags : str, optional, default None
        A comma-separated list of tags to associate with the job.
    ephemeral_data : bool, optional, default False
        Whether to delete the job and its data after completion.
    """
    url = f"https://wordcab.com/api/v1/summarize?source=generic&display_name={display_name}t&summary_type={summary_type}&summary_lens={summary_lens}&tags={tags}&split_long_utterances={split_long_utterances}&pipeline=transcribe%252Csummarize&ephemeral_data={ephemeral_data}"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "authorization": f"Bearer {api_key}",
    }

    with open(f"{text_file_path}", "r") as f:
        payload = json.dumps({"transcript": [str(line).replace("\n", "") for line in f.readlines()]})

    logger.warning(f"Payload: {payload}")
    response = requests.post(url, data=payload, headers=headers)

    logger.warning(f"[{response.status_code}] {response.text}")


if __name__ == "__main__":
    summarize_text_file(
        text_file_path="tests/transcript_no_timestamps.txt",
        api_key=os.getenv("WORDCAB_API_KEY"),
        display_name="summarize_text_file",
    )
