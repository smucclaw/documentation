:oprhan:

.. _links_returning:

#####################
L4 Language Reference
#####################

L4 is:

- A high level specification language
    - Its generic high level syntax is described in the section titled `L4 Language Specification`.

- Designed to be transpiled to various formats for different purposes.
    - These transpilation formats include document formats like Markdown, Word, and .pdf, 
      as well as (our specialized dialect of) Logical English <https://github.com/smucclaw/LogicalEnglish>
      programs, a logic programming based language, for execution.
    - For that reason, while there is one generic L4 syntax, 
      L4 really admits of different fragments, each with their own specialized semantics, 
      corresponding to the various transpilers. These transpilers 
      care about and operate on different fragments of L4, since some transpilers
      like those responsible for document outputs caring about formatting specific
      options, which are ignored by the Logical English one.
    - These transpilers and their corresponding semantic fragments of L4 are
      documented in the section titled `Export L4 Output`.

|
|

..
  We will discuss the syntax and semantics specific to these fragments and their various outputs later; 
  but before doing that, we will first outline the *generic* syntax of L4 that is common to the various fragments.

.. grid:: 2

    .. grid-item-card:: Export L4 Output
        :link: returning-transpilers
        :link-type: doc

        Export L4 output into other languages.

    .. grid-item-card:: List of Keywords in L4
        :link: returning-L4-keywords
        :link-type: doc

        A list of keywords found in L4.

.. grid:: 2

    .. grid-item-card:: L4 Language Specification
        :link: returning-specification
        :link-type: doc

        A semantic specification of L4 Syntax.

    .. grid-item-card:: Publications
        :link: https://cclaw.smu.edu.sg/projects-papers
        :link-type: url

        Read academic publications about L4.

..
    .. grid-item-card:: L4 Language Quickstart
        :link: returning-keywords
        :link-type: doc

        Get an overview of how L4 works.
        (Nemo: This page is too confusing and is not a good quickstart)

..
    .. grid-item-card:: Exporting L4
        :link: returning-exploring-L4
        :link-type: doc

        Learn how to export your L4 output into other formats.
        (Nemo: This page is not complete)

    .. grid-item-card:: Philosophy Behind L4's Design
        :link: links-law-and-computer-science
        :link-type: doc

        Get a deeper understanding of the philosophy behind L4's design.

======================================
Exploring L4 Futher: Intended Audience
======================================

This section is for users who want to learn more about using L4 and have already installed L4 on their computer.