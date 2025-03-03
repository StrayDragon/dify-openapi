import os
from pathlib import Path

import pytest
from dify_sdk import DifyApi

OFFICIAL_DIFY_HOST = "https://api.dify.ai/v1"

TEST_DIFY_HOST = os.environ.get("TEST_DIFY_HOST") or OFFICIAL_DIFY_HOST


@pytest.fixture()
def ac():
    return DifyApi(token=os.environ["TEST_DIFY_APP_CHAT_API_KEY"], base_url=TEST_DIFY_HOST)


def test_audio_to_text(ac):
    response = ac.audio_to_text(
        file=(
            "audio.mp3",
            Path("tests/data/app/audio.mp3").read_bytes(),
            "audio/mp3",
        )
    )

    assert response is not None
    assert response.text is not None
    assert response.text != ""


def test_text_to_audio(ac):
    response = ac.text_to_audio(text="Hi")
    assert response is not None
