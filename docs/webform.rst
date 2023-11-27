========
Web form
========

Recall that:

- L4 constitutive rules can be transpiled to Logical English, which
  are in turn transpiled into Prolog and executed as such.

- L4 classes / data types can be transpiled to JSON schema.

One can turn an L4 specification into a web form using:

- The `Example form app <https://github.com/smucclaw/example-l3-form-app>`_.

  - This utilises `JSON Forms <https://jsonforms.io/>`_
    to render the output of the L4 to JSON Schema transpiler
    as an interactive web form.

  - The idea is that the web form allows the user to define JSON instances
    conforming to JSON Schemas which in turn correspond to L4 classes / data types.

- The `Logical English client library <https://github.com/smucclaw/logical-english-client>`_.

  Given the following:

  - A Logical English server, ie. a server running the
    `Logical English Prolog codebase <https://github.com/smucclaw/LogicalEnglish>`_

    - A publicly available instance maintained by CCLAW can be found at
      `this url <https://le.dev.cclaw.legalese.com/>`_
  
  - A JSON instance,
    like one obtained from the web form

  - A Logical English program,
    like one obtained from the output of the L4 to Logical English transpiler

  - A Logical English query string

  this library allows one to query the Logical English server
  which executes the Logical English as Prolog and returns an explanation
  tree in the form of JSON.
  The library also some built-in facilities for visualising this JSON tree.

More details about these individual projects and how to put them together
can be found in their respective project documentation.

----------------------------------------------------------
Reasoning about classes/data types with constitutive rules
----------------------------------------------------------

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
and graph databases.
(eg:
`TerminusDB <https://terminusdb.com/>`_,
`Datomic <https://www.datomic.com/>`_,
`Stardog <https://www.stardog.com/>`_).
Datalog is a declarative fragment of Prolog well suited for database applications,
and representing data in such a manner facilitates reasoning about them via
constitutive rules, which are interpreted as Prolog rules.

We refer the interested reader to the following resources for more details on
Datalog and graph database:

- https://terminusdb.com/docs/datalog-explanation/ 
- https://blogit.michelin.io/an-introduction-to-datalog/
- https://aws.amazon.com/blogs/database/use-semantic-reasoning-to-infer-new-facts-from-your-rdf-graph-by-integrating-rdfox-with-amazon-neptune/

An example
----------

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
More formally, these triples are called EAV / RDF-triples.
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

  (node_0, name, "Alice")
  (node_0, dob, "1990-01-01")
  (node_0, hobbies, ["reading", "painting"])
  (node_0, address, node_1)
  (node_1, city, "London")
  (node_1, zipcode, "SW1A 1AA")
  (node_1, country, "United Kingdom")

L4 predicates to access attributes (ie. object fields)
------------------------------------------------------

L4 provides the following family of predicates to talk about such triples
arising from objects:

.. csv-table::
    :widths: 15, 15, 5, 15, 15, 15

    "entity's", "attribute_0's", "...", "attribute_n's", "IS", "value"

In the simplest case, this has the following form:

.. csv-table::
    :widths: 15, 15, 5, 15

    "entity's", "attribute", "IS", "value"

Intuitively, such a triple can be viewed as accessing the ``attribute`` value of
``entity`` and then binding it to ``value``. 
More formally, this predicate plays the same role as ``rdf/3`` in the
`SWI-Prolog RDF library <https://www.swi-prolog.org/pldoc/man?section=semweb-rdf11>`_,
so that a collection of triples
(obtained from a corresponding json instance)
forms a Datalog database, over which our Prolog based execution engine
reasons.

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

To illustrate a more complex usage of the predicate, consider the following
rule, which says that ``Person`` lives in
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
For those familiar with SQL, the ``Address`` variable functions as an
implicit join on the value of the ``address`` attribute.

As chaining nested accessor predicates manually in this manner can be
cumbersome, L4 allows one to can collapse multiple layers of nesting into a
single predicate as follows:

.. csv-table::
    :widths: 15, 15, 15, 15, 15, 15

    "GIVEN", "Name", "IS A", "String",,
    , "Country", "IS A", "Country",,
    , "Address", "IS A", "Address",,
    , "Person", "IS A", "Person",,
    "DECIDE", "Name", "lives in", "Country",,
    "IF", "Person's", "name", "IS", "Name",
    "AND", "Person's", "address's", "country", "IS", "Address"