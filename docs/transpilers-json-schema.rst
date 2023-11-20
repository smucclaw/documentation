============================
L4 to JSON Schema transpiler
============================

`JSON Schema <https://json-schema.org/>`_ is a format to describe the *structure* of data.
This document describes the transpiler from L4 into JSON Schema.


General example
===============

Suppose we have L4 classes defined as follows.

.. csv-table::
    :widths: 8, 12, 8, 15

    "DECLARE", "Address",,
    "HAS", "city", "IS A", "String"
    , "zipcode", "IS A", "String"
    , "country", "IS A", "String"
    ,,,
    "DECLARE", "Person",,
    "HAS", "name", "IS A", "String"
    , "age", "IS A", "Integer"
    , "address", "IS A", "Address"

Note that only type declarations are transpiled. This is because JSON Schema is only describing the structure of the data; other transpilers take care of transforming the actual rules.

The rules are transpiled into JSON Schema from Haskell representation, which is the result of the initial parsing.

These L4 declarations translate into the following JSON Schema.

.. code-block:: json-object

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

Data types
----------

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

(All of the \*Name types are just aliases for string-like types, omitted here for brevity.)

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
^^^^^^^^^^^^^^^

The types Boolean, Integer, String and Number are primitives in both L4 and JSON Schema.

List
^^^^

The ``LIST OF`` keyword in L4 translates into an array. Adding the following field into the type declaration of Person

.. csv-table::
    :widths: 8, 12, 8, 15, 15

    "DECLARE", "Person",,,
    "HAS", "name", "IS A",, "String"
    , "address", "IS A",, "Address"
    , "prevAdrs", "IS", "LIST OF", "Address"

results in the following line in the JSON Schema.

.. code-block:: json-object

    "prevAdrs": {
        "type": "array",
        "items": {"$ref": "#/$defs/Address"}
    }

Date
^^^^

Date translates into a string with formatting information. Again adding a new field in L4

.. csv-table::
    :widths: 8, 12, 8, 15, 15

    "DECLARE", "Person",,,
    "HAS", "birthday", "IS A", "Date"

becomes as follows in the JSON Schema

.. code-block:: json-object

    "birthday": {
        "type": "string",
        "format": "date"
    }

Reference
^^^^^^^^^

The ``FTRef`` type defines *references*. This is used for custom types, which are implemented as objects in the JSON Schema.
As we saw previously, the Address field of a Person is a reference.

.. csv-table::
    :widths: 8, 12, 8, 15

    "DECLARE", "Address",,
    "HAS", … ,,
    ,,,
    "DECLARE", "Person",,
    "HAS", "address", "IS A", "Address"


.. code-block:: json-object

    "Person": {
        "type": "object",
        "properties": {
            …
            "address": {"$ref": "#/$defs/Address"}
    }


A parent object will have fields as an array. We do the same thing with each field: get the name, and type.
The rule names in L4 are written with spaces. In the JSON Schema, we're using snake case for the names as these will interact with various backends.


Enum
^^^^

Finally, we can define an enumeration type in L4.

.. csv-table::
    :widths: 8, 12, 8, 8, 12

    "DECLARE", "UniqueID", "IS", "ONE OF", "SocialSecurityNumber"
    , , , , "DriversLicense"

The translation into JSON Schema looks as follows.

.. code-block:: json-object

    "UniqueID": {
      "type": "string",
      "enum": ["SocialSecurityNumber", "DriversLicense"]}
    }

These are the basic correspondences between the types in L4 and JSON Schema. Next, we take a more specific example, and explain how the generated schema is used to build a web form.

From Schema to Web Form
=======================

To generate a JSON Schema that works for a web form, we have a few assumptions:

- Top level has to be an object called ``Web_Form``.
- The transpiler picks the top level object in order, but there is a later step that inserts ``Web_Form`` as the top level object. (TODO: what later step? Where does it happen?)
- In order to be present in the generated form, a reference has to be a property of the ``Web_Form`` object or its children.

So in the following L4 declarations, the type ``UnusedType`` is declared, but not used anywhere.

.. csv-table::
    :widths: 8, 12, 8, 12

    DECLARE, Web_Form,,
    HAS, claim_type, IS A, Claim
    ,,,
    DECLARE, Claim,,
    HAS, …, ,
    ,,,
    DECLARE, UnusedType,,
    HAS, unusedField, IS A, Boolean

It is, however, present in the initial schema. But since ``UnusedType`` is not a property of ``Web_Form`` nor any of its children, it won't be shown in the generated form.

.. code-block:: json-object

    {"$schema":"http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties":{"toplevel":{"$ref": "#/$defs/Web_Form"}},
        "$defs": {
            "Web_Form": {
                "type": "object",
                "properties": {"claim_type": {"$ref": "#/$defs/Claim"}}
            }
            "Claim": {
                "type": "object",
                "properties": { … }
            }
            …
            "UnusedType": {
                "type": "object",
                "properties": {"unusedField": {"type": "boolean"}}
            }
        }
    }

Note that if the type was using a nonexistent reference, then the web form would crash. So the following does not work, even though ``UnusedType`` is equally unused as the previous.

.. csv-table::
    :widths: 8, 12, 8, 12

    DECLARE, UnusedType,,
    HAS, unusedField, IS A, UndefinedReference

.. code-block:: json-object

    {"$schema":"http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties":{"toplevel":{"$ref": "#/$defs/Web_Form"}},
        "$defs": {
            …
            "UnusedType": {
                "type": "object",
                "properties": {"unusedField": {"$ref": "#/$defs/UndefinedReference"}}
            }
        }
    }


Form Generation
---------------

TODO: should the text from this (private repo) https://github.com/smucclaw/usecases/blob/main/jsonforms-vue-seed/README.md#form-generation be copied over to this documentation? Or is it out of scope for the transpiler?