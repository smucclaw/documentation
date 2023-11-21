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

Theoretical background
----------------------

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
This idea originates from the world of Datalog and graph databases.
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

so that for instance, a ``Person`` is an entity which has a ``dob`` attribute
(representing his/her date of birth), which has as a value, a ``Date`` object.

an instance of these can be viewed as a collection of triples of the form
``(entity, attribute, value)``.

We can view this class diagram as specifying an edge-labelled directed graph
as in the following Java syntax:

.. code-block:: java

  public class ClassGraph {
    public enum Entity {
      Person, Address
    }

    public enum Attribute {
      address, name, dob, hobbies,
      city, zipcode, country
    }
    
    public static class Edge {
      Entity entity;
      Attribute attribute;
      Object value;
    }

    Edge[] edges;

    public ClassGraph(Edge[] edges) {
      this.edges = edges;
    }
  }

.. Such an edge-labelled directed graph can be represented by a collection of
  triples of the form

Then given the following json instance conforming to the above JSON schema:

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

we can visualize this as a graph via its corresponding
`UML object diagram <https://en.wikipedia.org/wiki/Object_diagram>`_. 

gets transformed into the following Logical English program:

.. code-block:: text

  node-1's name is Alice.
  node-1's age is 25.
  node-1's hobbies is node-2.
  node-1's address is node-3.
  reading is in node-2.
  painting is in node-2.
  node-3's city is London.
  node-3's zipcode is SW1A 1AA.
  node-3's country is United Kingdom.

which as L4 facts, looks like:

.. csv-table::
    :widths: 15, 15, 15, 5, 15

    "DECIDE", "node-1's", "name", "IS", "Alice"
    "DECIDE", "node-1's", "age", "IS", "25"
    "DECIDE", "node-1's", "hobbies", "IS", "node-2"
    "DECIDE", "node-1's", "address", "IS", "node-3"
    "DECIDE", "reading", "IS", "IN", "node-2"
    "DECIDE", "painting", "IS", "IN", "node-2"
    "DECIDE", "node-3's", "city", "IS", "London"
    "DECIDE", "node-3's", "zipcode", "IS", "SW1A 1AA"
    "DECIDE", "node-3's", "country", "IS", "United Kingdom"

The ``entity's attribute IS value`` predicate in L4

[TODO] Talk about:

- Objects (ie instances of classes) as nodes of graph
- EAV as labelled edges
- Nested accessors
- Lists being transformed into the ``_ IS IN _`` predicates.

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