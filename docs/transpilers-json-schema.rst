============================
L4 to JSON Schema transpiler
============================

`JSON Schema https://json-schema.org/`_ is a format to describe the *structure* of data.
This document describes the transpiler from L4 into JSON Schema.


Simple example
===============

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
    , "address", "IS A",, "Address"

Note that only type declarations are transpiled. This is because JSON Schema is only describing the structure of the data; other transpilers take care of transforming the actual rules.

The rules are transpiled into JSON Schema from Haskell representation, which is the result of the initial parsing.

These L4 declarations translate into the following JSON Schema.

.. code-block:: json
    {"$schema":"http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties":{"toplevel":{"$ref": "#/$defs/Person"}},
        "$defs": {"Address": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string"},
                        "zipcode": {"type": "string"},
                        "country": {"type": "string"}}},
                  "Person": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "age": {"type": "integer"},
                        "address": {"$ref": "#/$defs/Address"}}}}}

The original L4 contains two custom types, ``Address`` and ``Person``, which each contain fields of basic and custom types.
The HAS relation (``Person HAS name``) of L4 translates into properties of the parent object in the JSON schema ("name" as a key in ``Person.properties``).
Basic types like integers and strings are primitives in both L4 and JSON Schema, and custom types like Person and Address are handled as *references*.

TODO: clarify Maryam's original points
- The entry point is the function ``rulesToJsonSchema``, which takes the first rule as the parent/root ("top level") of the JSON Schema.
- If a reference is parsed but is not a property of the parent object, it won't be present in the form that's generated from the JSON Schema.

Data types
==========

The type declarations of the original L4 rules are transpiled into records and enums in the JSON Schema. This is represented internally as the following Haskell data type.

.. code-block:: haskell
    data JSchemaExp
        = ExpTypeRecord
            { typeName :: TypeName       -- Text
            , fields :: [Field]
            }
        | ExpTypeEnum
            { typeName :: TypeName       -- Text
            , enums :: [ConstructorName] -- Text
            }

A ``Field`` consists of a field name and type, as follows:

.. code-block:: haskell
    data Field = Field
        { fieldName :: FieldName  -- Text
        , fieldType :: FieldType
        }

(All of the \*Name types are just aliases for strings, omitted here for brevity.)

The main type ``FieldType`` defines all the types of fields in the schema:

.. code-block:: haskell
    data FieldType =
        FTBoolean
        | FTNumber
        | FTString
        | FTRef TypeName  -- TypeName=Text
        | FTList FieldType
        | FTDate
        | FTInteger
        | FTEnum [FieldName] -- FieldName=Text

Below, we explain the types.

Primitive types
---------------

The types Boolean, Integer, String and Number are primitives in both L4 and JSON Schema.

List
----

The ``LIST OF`` keyword in L4 translates into an array. Adding the following field into the type declaration of Person

.. csv-table::
    :widths: 15, 15, 10, 15, 15

    "DECLARE", "Person",,,
    "HAS", "name", "IS A",, "String"
    , "address", "IS A",, "Address"
    , "prevAdrs", "IS", "LIST OF", "Address"

results in the following line in the JSON Schema.

.. code-block:: json
    "prevAdrs": {
        "type": "array",
        "items": {"$ref": "#/$defs/Address"}
    }

Date
----

Date translates into a string with formatting information. Again adding a new field in L4

.. csv-table::
    :widths: 15, 15, 10, 15, 15

    "DECLARE", "Person",,,
    "HAS", "birthday", "IS A", "Date"

becomes as follows in the JSON Schema

.. code-block:: json
    "birthday": {
        "type": "string",
        "format": "date"
    }

Reference
---------

The ``FTRef`` type defines *references*. This is used for custom types, which are implemented as objects in the JSON Schema.
As we saw previously, the Address field of a Person is a reference.

.. code-block:: json
    "Person": {
        "type": "object",
        "properties": {
            …
            "address": {"$ref": "#/$defs/Address"}
    }


A parent object will have fields as an array. We do the same thing with each field: get the name, and type.
The rule names in L4 are written with spaces. In the JSON Schema, we're using snake case for the names as these will interact with various backends.


Enum
----

Finally, we can define an enumeration type in L4.

.. csv-table::
    :widths: 15, 15, 10, 15, 15

    "DECLARE", "UniqueID", "IS", "ONE OF", "SocialSecurityNumber"
    , , , , "DriversLicense"

The translation into JSON Schema looks as follows.

.. code block:: json
    "UniqueID": {
      "type": "string",
      "enum": ["SocialSecurityNumber", "DriversLicense"]}
    }

--


Below is Maryam's text, TODO expand on it

Entry point is ``rulesToJsonSchema``.
(a note: rulestoUISchema isn't used and should be deprecated from all things that reference it)

