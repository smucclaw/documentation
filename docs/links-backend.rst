:orphan:

############################################
L4 Backend Setup Instructions For Developers
############################################
|
|

.. grid:: 3

    .. grid-item-card:: Conceptual Explanation of the Backend
        :link: developers-explanations
        :link-type: doc

        In-depth conceptual explanation of how the L4 backend works.

    .. grid-item-card:: 1. Webtool Setup Instructions
        :link: developers-installation-webtool
        :link-type: doc

    .. grid-item-card:: 2. Google Sheets Setup Intructions
        :link: developers-installation-googlesheets
        :link-type: doc

.. grid:: 2

    .. grid-item-card:: 3. Compiling an Edited L4 Spreadsheet
        :link: developers-installation-L4spreadsheet
        :link-type: doc

    .. grid-item-card:: 4. Security Considerations
        :link: developers-security
        :link-type: doc

============================================
Installing the L4 Backend: Intended Audience
============================================

These instructions are tailored towards users who want to set up the entire L4 ecosystem on their own servers so that they do not have to rely on externally provided servers.

This section is aimed at a **full-stack developer, web application architect, or product manager** who wishes to install the Web Tool for their organisation. Users should be familiar with some of the following technologies commonly involved in web and mobile app development:

- Unix and Linux
- HTML, CSS, and Javascript
- Python for server-side programming
- RESTful APIs for web applications
- Git and Github for source-code distribution and version control
- Amazon Web Services EC2 (Elastic Compute Cloud)
- HTTP, HTTPS, and SSL certificates

A developer experienced with single-page apps should recognize the general architecture of the Web Tool. The Web Tool and the L4 backend which supports it are built using the following technologies:

- the Vue 3 framework for Javascript
- the Purescript language (used for web development)
- the Haskell language (used for the interpreter)
