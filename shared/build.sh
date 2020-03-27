#! /usr/bin/env bash

set -o errexit
set -o nounset

readonly source_dir=$(cd $(dirname ${BASH_SOURCE[0]});pwd)

conan export ${source_dir} conan-shared/0.1@demo/testing