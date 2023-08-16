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
