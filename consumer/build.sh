#! /usr/bin/env bash

set -o errexit
set -o nounset

readonly source_dir=$(cd $(dirname ${BASH_SOURCE[0]});pwd)
readonly build_dir=${source_dir}/output/build
readonly package_dir=${source_dir}/output/package

# Get all dependencies and build BoostExample from source
    conan install ${source_dir} -if ${build_dir} --build=BoostExample

# Build
    conan build ${source_dir} -bf ${build_dir} -sf ${source_dir}

conan create ${source_dir} demo/testing