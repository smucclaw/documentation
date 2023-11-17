====================
Expert system webapp
====================

One can turn an L4 specification into an expert system webapp using:
- The L4 to Logical English transpiler.
- The L4 to JSON Schema transpiler.
- The jsonforms-vue-seed project.

Reasoning about classes/data types with constitutive rules
----------------------------------------------------------
Recall that L4 constitutive rules can be translated to Logical English, which
To facilitate reasoning about data defined in classes via constitutive rules,
we use well established techniques from the database world.
More specifically, we model `Datalog <https://en.wikipedia.org/wiki/Datalog>`_ is a syntactic subset of

In the database world, data models based on
`RDF subject-predicate-object <https://www.oxfordsemantic.tech/faqs/what-is-rdf>`_,
also known as `entity-attribute-value <https://en.wikipedia.org/wiki/Entity%E2%80%93attribute%E2%80%93value_model>`_
triples, are common

Suppose we have L4 classes defined as follows.

.. csv-table::
    :widths: 15, 15, 10, 15, 15

    "DECLARE", "Address",,,
    "HAS", "city", "IS A",, "String" 
    , "zipcode", "IS A",, "String"
    , "country", "IS A",, "String"
    ,,,,
    "DECLARE", "Person",,,
    "HAS", "name", "IS A",, "String"
    , "age", "IS A",, "Integer"
    , "hobbies", "IS", "LIST OF", "String"
    , "address", "IS A",, "Address"

.. [Joe todo]

.. Talk about the interaction betweeen the various components here,
.. namely the webapp json and the transpiled LE.

.. MAYBE: Give some context: Explain that in an insurance usecase, we had the L4 -> LE, json schema transpiler, json -> asami db, etc

.. Explain how the web form data types are coupled with the encoding 'field accessors' in an important way

.. Form json -> Asami db [1 - 2 paras]
.. 1. high level idea / intuition [no more than 1 para, probably]
..    1. what is the transformation from our json to the graph db
..    2. how we use this in our context
.. 2. how to run the thing / call the thing
..    1. at the least: a link to readme for how to run the thing