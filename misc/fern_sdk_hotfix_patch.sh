#!/bin/bash

# FIXME: @l8ng fern 4.3.14 has a bug where the process_rule is not serialized correctly
TARGET_FILE="src/dify_sdk/documents/client.py"
rg --passthru -N '"process_rule": process_rule' -r '"process_rule": process_rule.model_dump_json() if process_rule else None' $TARGET_FILE  > tmp.txt && mv tmp.txt $TARGET_FILE





