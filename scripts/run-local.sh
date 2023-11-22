#! /bin/bash

uvicorn azfn_fastapi_demo.main:app --host 0.0.0.0 --port 80 "$@"
