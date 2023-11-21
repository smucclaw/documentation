====================
Expert system webapp
====================

One can turn an L4 specification into an expert system webapp using:

- The L4 to Logical English transpiler.
- The L4 to JSON Schema transpiler.
- The jsonforms-vue-seed project.

----------------------------------------------------------
Reasoning about classes/data types with constitutive rules
----------------------------------------------------------

Recall that:

- L4 constitutive rules can be transpiled to Logical English, which
  are in turn transpiled into Prolog and executed as such.
- L4 classes/data types can be transpiled to JSON schemas, and we can generate
  nested JSON instances conforming to these schemas.

Theoretical Overview
--------------------

In this sub-section, we describe the theoretical ideas behind the ideas in the
remaining sub-sections.
This part is *optional* and is primarily for more theoreticall inclined
readers who are interested to understand more about the underlying
motivation and ideas.

To facilitate reasoning about data defined via classes and objects using
constitutive rules,
we leverage well established techniques from the database and knowledge representation
worlds.
More precisely, we transform nested data representing instaces of L4 classes
into
`RDF subject-predicate-object <https://www.oxfordsemantic.tech/faqs/what-is-rdf>`_,
also known as `entity-attribute-value <https://en.wikipedia.org/wiki/Entity%E2%80%93attribute%E2%80%93value_model>`_
triples, which is a data model commonly used in commercial
`Datalog <https://en.wikipedia.org/wiki/Datalog>`_
(eg. `Datomic <https://www.datomic.com/>`_) and graph (eg. `Stardog <https://www.stardog.com/>`_)
databases.
Datalog is a declarative fragment of Prolog well suited for database applications,
and representing data in such a manner facilitates reasoning about them via
constitutive rules, which are interpreted as Prolog rules.
We refer the interested reader to the following resources for more details on
Datalog and graph database:

- https://blogit.michelin.io/an-introduction-to-datalog/
- https://aws.amazon.com/blogs/database/use-semantic-reasoning-to-infer-new-facts-from-your-rdf-graph-by-integrating-rdfox-with-amazon-neptune/

A more practical introduction
-----------------------------

To illustrate how this works in practice,
suppose we have L4 classes defined as follows.

.. csv-table::
    :widths: 15, 15, 10, 15, 15

    "DECLARE", "Address",,,
    "HAS", "city", "IS A",, "String"
    , "zipcode", "IS A",, "String"
    , "country", "IS A",, "String"
    ,,,,
    "DECLARE", "Person",,,
    "HAS", "name", "IS A",, "String"
    , "dob", "IS A",, "Date"
    , "hobbies", "IS", "LIST OF", "String"
    , "address", "IS A",, "Address"

One can visualise the corresponding JSON schema as an edge-labelled directed
graph via its corresponding
`UML class diagram <https://en.wikipedia.org/wiki/Class_diagram>`_.
In the graph below, classes and objects (ie instances of the classes)
are represented as nodes, with labelled, directed edges between them
representing fields / properties.

.. @startuml
    Address --> "1" String : city
    Address --> "1" String : zipcode
    Address --> "1" String : country
    Person --> "1" String : name
    Person --> "1" Date : date of birth
    Person --> "1" "List<String>" : hobbies
    Person --> "1" Address : address
  @enduml

.. raw:: html
    :file: ../images/expert-systems-webapp-uml-class-diagram.svg

Following the terminology used in Datalog and RDF databases, we call:

- the "source node" the "entity"
- the "edge label" the "attribute"
- the "destination node" the "value"

For instance, a ``Person`` is an entity which has a ``dob`` attribute
(representing his/her date of birth), with a ``Date`` object as a value.

With this, a corresponding instance of these classes can be viewed as a
collection of labelled, directed edges, each represented as
a triple of the form ``(entity, attribute, value)``.
(More technically, these triples are called EAV / RDF-triples.)
For instance, consider the following json instance conforming to the above
JSON schema:

.. code-block:: json

  {
    "name": "Alice",
    "dob": "1990-01-01",
    "hobbies": [
      "reading",
      "painting"
    ],
    "address": {
      "city": "London",
      "zipcode": "SW1A 1AA",
      "country": "United Kingdom"
    }
  }

This corresponds to a graph described by the following triples:

.. code-block:: text

  (node-0, name, "Alice")
  (node-0, dob, "1990-01-01")
  (node-0, hobbies, ["reading", "painting"])
  (node-0, address, node-2)
  (node-2, city, "London")
  (node-2, zipcode, "SW1A 1AA")
  (node-2, country, "United Kingdom")

L4 provides the following predicate to talk about such triples arising from
objects:

.. csv-table::
    :widths: 15, 15, 5, 15

    "entity's", "attribute", "IS", "value"

Such a triple can be viewed as accessing the ``attribute`` value of
``entity`` and then binding it to ``value``. 

We can use this to define the following rule for instance:

.. csv-table::
    :widths: 15, 15, 15, 15, 15

    "GIVEN", "Name", "IS A", "String",
    , "Hobbies", "IS", "LIST OF", "String"
    , "Hobby", "IS A", "String",
    , "Person", "IS A", "Person",
    "DECIDE", "Name", "likes", "Hobby",
    "IF", "Person's", "name", "IS", "Name"
    "AND", "Person's", "hobbies", "IS", "Hobbies"
    "AND", "Hobby", "IS", "IN", "Hobbies"

The above rule says that a ``Person`` named ``Name`` likes ``Hobby``
if it is found in the list of ``hobbies`` of the person named ``Name``.

Another example is the following, which says that ``Person`` lives in
``Country`` if his/her ``address`` has a ``Address`` whose ``country`` is
``Country``.

.. csv-table::
    :widths: 15, 15, 15, 15, 15

    "GIVEN", "Name", "IS A", "String",
    , "Country", "IS A", "Country",
    , "Address", "IS A", "Address",
    , "Person", "IS A", "Person",
    "DECIDE", "Name", "lives in", "Country",
    "IF", "Person's", "name", "IS", "Name"
    "AND", "Person's", "address", "IS", "Address"
    "AND", "Address's", "country", "IS", "Country"

Notice how we are essentially trying to access the value of the field
``country`` which is nested under the ``address`` field of ``Person``.
For those familiar with SQL, the ``Address`` variable is essentially used to
perform an implicit inner join on the value of the ``address`` attribute.

L4 also provides some syntactic sugar for these nested accessor predicates.
These have the form:

.. csv-table::
    :widths: 15, 15, 5, 15, 15, 15

    "entity's", "attribute_0's", "...", "attribute_n's", "IS", "value"

One can use this as such:

.. csv-table::
    :widths: 15, 15, 15, 15, 15, 15

    "GIVEN", "Name", "IS A", "String",,
    , "Country", "IS A", "Country",,
    , "Address", "IS A", "Address",,
    , "Person", "IS A", "Person",,
    "DECIDE", "Name", "lives in", "Country",,
    "IF", "Person's", "name", "IS", "Name",
    "AND", "Person's", "address's", "country", "IS", "Address"

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