#! /usr/bin/env bash

set -o errexit
set -o nounset

readonly source_dir=$(cd $(dirname ${BASH_SOURCE[0]});pwd)
readonly build_dir=${source_dir}/output/build
readonly package_dir=${source_dir}/output/package

conan install ${source_dir} -if ${build_dir}

# Build
    #Conan way for conanfile.py
    conan build ${source_dir} -bf ${build_dir} -sf ${source_dir}

    # Raw CMake
    #cmake -G Ninja -H${source_dir} -B${build_dir} #-DCONAN_LIBCXX=libstdc++11
    #cmake --build ${build_dir}

# Package
    conan package . --source-folder=${source_dir} --build-folder=${build_dir} --package-folder=${package_dir}

# Create a conan package  (user/channel)
    conan create ${source_dir} demo/testing

# Optionally, upload to a local repository
    #conan upload BoostExample/1.0.1 -r=local_server