#!/usr/bin/env bash
root=$(git rev-parse --show-toplevel)

flake8 "$root"
py.test --cov IPoFB "$root/tests"
exit $?
