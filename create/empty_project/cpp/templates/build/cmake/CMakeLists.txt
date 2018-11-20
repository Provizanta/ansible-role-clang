cmake_minimum_required(VERSION 3.1...3.12)

if(${CMAKE_VERSION} VERSION_LESS 3.12)
    cmake_policy(VERSION ${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION})
{% if ansible_os_family == 'Windows' %}
else()
    # a bug in MSVC server mode - this line should be implicit, 2018-11-20
    cmake_policy(VERSION 3.12)
{% endif %}
endif()

project({{ project['name'] }}
        VERSION {{ project['version'] | default('0.1') }}
        DESCRIPTION "{{ project['description'] }}"
        LANGUAGES "{{ project['languages'] | join(' ') }}")

set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake" ${CMAKE_MODULE_PATH})

target_compile_features({{ project['name'] }} PUBLIC cxx_std_17)

# Require out-of-source builds
file(TO_CMAKE_PATH "${PROJECT_BINARY_DIR}/CMakeLists.txt" LOC_PATH)
if(EXISTS "${LOC_PATH}")
    message(FATAL_ERROR "You cannot build in a source directory (or containing CMakeLists.txt file). Please make a build subdirectory. Feel free to remove CMakeCache.txt and CMakeFiles.")
endif()
