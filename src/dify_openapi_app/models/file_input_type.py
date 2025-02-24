from typing import Literal, cast

FileInputType = Literal["audio", "custom", "document", "image", "video"]

FILE_INPUT_TYPE_VALUES: set[FileInputType] = {
    "audio",
    "custom",
    "document",
    "image",
    "video",
}


def check_file_input_type(value: str) -> FileInputType:
    if value in FILE_INPUT_TYPE_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(FileInputType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILE_INPUT_TYPE_VALUES!r}")
