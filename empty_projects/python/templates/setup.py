from setuptools import setup, find_packages

{% macro print_on_separate_lines(items, indent=3) -%}
{%- set base_tab = '\n' + ' '*4*(indent-1) -%}
{%- set tab = base_tab + ' '*4 -%}
{%- for item in items -%}
{{- "%s'%s'%s"|format(tab, item, base_tab if loop.last else ',') -}}
{%- endfor -%}
{%- endmacro %}

def readme():
    with open('README.md') as f:
        return f.read()


if __name__ == '__main__':
    setup(
        name='{{ project.name }}',
        version='{{ project.version }}',
        author='{{ project.author.name }}',
        author_email='{{ project.author.email }}',
        description='{{ project.description }}',
        long_description=readme(),
        classifiers=[{{- print_on_separate_lines(project.classifiers, indent=3) }}],
        keywords='{{ project.keywords | join(' ') }}',
        license='{{ project.license }}',
        packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
        scripts=['bin/*'],
        install_requires=[{{- print_on_separate_lines(project.dependencies, indent=3) }}],
        test_suite='tests',
        include_package_data=True
    )
