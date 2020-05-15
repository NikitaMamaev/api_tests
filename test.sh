export PYTHONPATH=${PWD}

pytest -v -m "positive or negative" tests/*
