#! /usr/bin/env bash

set -o errexit
set -o nounset

readonly source_dir=$(cd $(dirname ${BASH_SOURCE[0]});pwd)

conan export ${source_dir} demo/testing