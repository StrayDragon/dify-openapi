from typing import Literal, cast

FileInputTransferMethod = Literal["local_file", "remote_url"]

FILE_INPUT_TRANSFER_METHOD_VALUES: set[FileInputTransferMethod] = {
    "local_file",
    "remote_url",
}


def check_file_input_transfer_method(value: str) -> FileInputTransferMethod:
    if value in FILE_INPUT_TRANSFER_METHOD_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(FileInputTransferMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILE_INPUT_TRANSFER_METHOD_VALUES!r}")
