{{- set cmake_version = 3.10 -}}
{{- set cmake_highest_version = 3.12 -}}
cmake_minimum_required(VERSION {{ cmake_version if cmake_version < 3.12 else cmake_version }} FATAL_ERROR)

if(${CMAKE_VERSION} VERSION_LESS {{ CMAKE_VERSION }})
    cmake_policy(VERSION ${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION})
else()
    # a bug in MSVC server mode - this line should be implicit, 2018-11-20
    cmake_policy(VERSION 3.12)
endif()

project({{ project['name'] }}
        VERSION {{ project['version'] | default('0.1') }}
        DESCRIPTION "{{ project['description'] | default('Project description should go here') }}"
        LANGUAGES "{{ project['languages'] | join(' ') }}")

set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake" ${CMAKE_MODULE_PATH})

target_compile_features({{ project['name'] }} PUBLIC cxx_std_17)

# Require out-of-source builds
file(TO_CMAKE_PATH "${PROJECT_BINARY_DIR}/CMakeLists.txt" LOC_PATH)
if(EXISTS "${LOC_PATH}")
    message(FATAL_ERROR "You cannot build in a source directory (or containing CMakeLists.txt file). Please make a build subdirectory. Feel free to remove CMakeCache.txt and CMakeFiles.")
endif()
