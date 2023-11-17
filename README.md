# How to make

To build docs locally:
* `make html` to build HTML docs in the build directory specified in the `Makefile`

Execute `make` without an argument to see which targets are available.

See https://www.sphinx-doc.org/en/master/usage/quickstart.html for more 


# Relese process

By default https://l4-documentation.readthedocs.io/ will point to stable tag in RTD
https://l4-documentation.readthedocs.io/en/stable/

Latest is still available at
https://l4-documentation.readthedocs.io/en/latest/

Hooks are configured at https://readthedocs.org/projects/l4-documentation/
in a way that when GH `main` is updated new `latest` RTD tag is created.
To update "default" stable url release tag need to be created in GH.
After that RTD will automatically build the `stable` tag
so new pages will be visible on default url.
