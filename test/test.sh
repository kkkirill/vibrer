#!/bin/bash

source utils/bucket_create.sh

pytest -vv --ds=vibrer.settings apps/ test/upload/