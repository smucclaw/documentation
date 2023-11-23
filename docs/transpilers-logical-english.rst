================================
L4 to Logical English transpiler
================================

How to write L4 that translates to Logical English (LE); or, how L4 gets translated to LE
=========================================================================================

The following explains how the ``L4->LE`` transpiler translates L4 to LE with examples. 
If you are in a rush, ignore the explanations and just skim the examples.

This is meant to be a more intuitive, high-level discussion that's aimed at 
helping someone new to the Logical-English-y fragment of L4 
get started with writing L4 that can transpile smoothly to Logical English;
for a more comprehensive and rigorous specification and discussion, 
see `Syntax and Denotational Semantics of L4 Relational Predicates <https://www.overleaf.com/9757591584pqqqyhhrxbpq#6a4a4a>`_.
This discussion is also meant to be about the *syntax* and *semantics* of this fragment,
rather than about the *implementation* of the ``L4->LE`` transpiler; 
for the latter, see `TODO <>` instead.


The following discussion does however assume some understanding 
of the :ref:`generic L4 syntax and concepts <law_understand_l4>` 
and basic logic programming concepts.

Simple Horn clauses
-------------------

.. csv-table::
    :header: "GIVEN", "x", "IS A", "Animal"
    :widths: 15, 5, 15, 15

    "DECIDE", "x", "is an aquatic animal",
    "IF", "x", "lives in water"

This simple Horn gets translated to a .le file, parts of which look like the following

.. code-block:: le

    the target language is: prolog.

    the templates are:
        *a x* is an aquatic animal,
        *a x* lives in water.

    the knowledge base encoding includes:
        a x is an aquatic animal
        if x lives in water

Note that

- the indented block below "the templates are:" 
    - consists of the *templates* or *natural language annotations*
        for the Logical English output. These templates declare to the downstream LE engine what the predicates
        that will be used in the LE program are.
- the indented stuff below "the knowledge base encoding includes:"
    - consists of the Logical English *rules* and *facts*.
- the "the target language is: prolog." declaration tells the Logical English compiler that this should subsequently be transformed in turn into Prolog.

Logical English is, in this way, used merely as a wrapper around Prolog.

Variables or argument places in the predicates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In particular, the argument places or variable indicators in the templates
are marked by asterisks. So, for example, ``*a x* lives in water`` has 
one argument place; i.e., this predicate corresponds to the 
one-argument-place Prolog predicate ``lives_in_water``.

Now, you might wonder: why is it that in the LE output, we know that this is predicate
with just one argument place? In particular, what is it in the L4 that indicates this?

The answer is, it has to do with the ``GIVEN`` L4 keyword. Whenever you want to 
declare that something is a variable in your L4 constitutive rule, you have to declare it as a ``GIVEN`` variable.

So, e.g., if you want to write the equivalent of this Prolog

.. code-block:: prolog
    
    grandparent(X, Z) :- parent(X, Y ), parent(Y, Z)

you should write in L4

.. csv-table::
   :header: "GIVEN", "x", "", "", 
   :widths: 15, 10, 10, 30, 30

   "", "y", "", "", 
   "", "z", "", "", 
   "DECIDE", "x", "is grandparent of", "z"
   "IF", "x", "is parent of", "y"
   "AND", "y", "is parent of", "z"


This will get transpiled to this LE rule

.. code-block:: le

    a x is grandparent of a z
    if x is parent of a y
    and y is parent of z.

(Exercise for the reader: what would the corresponding LE template(s) look like?)


The other things you need to get Boolean Prolog compound terms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that we've seen a basic example with ``AND``, let's talk about ``OR`` and indentation.

What if you wanted to encode the following, more complicated rule? 

In English::

  a data breach with a organization harms an individual 
  if (i) it exposed data from the individual 
  and (ii) it either relates to the name of the individual 
            or to an account the individual had with the organization

There are various ways to model this, but let's suppose 
you wanted to treat ``data breach``, ``organization``, and ``individual`` as variables.

You can encode this in L4, for LE (and thence to Prolog), with

+--------+--------------+-------------+--------------+------------------------+-----------------------+------------+----------+--------------+
| GIVEN  | data breach  |             | IS A         | Data Breach            |                       |            |          |              |
+========+==============+=============+==============+========================+=======================+============+==========+==============+
|        | organization |             | IS A         | Organization           |                       |            |          |              |
+--------+--------------+-------------+--------------+------------------------+-----------------------+------------+----------+--------------+
|        | individual   |             | IS A         | Person                 |                       |            |          |              |
+--------+--------------+-------------+--------------+------------------------+-----------------------+------------+----------+--------------+
| DECIDE | data breach  | with        | organization | harms                  | individual            |            |          |              |
+--------+--------------+-------------+--------------+------------------------+-----------------------+------------+----------+--------------+
| IF     | data breach  | with        | organization | exposed data from      | individual            |            |          |              |
+--------+--------------+-------------+--------------+------------------------+-----------------------+------------+----------+--------------+
| AND    | data breach  | with        | organization | related to the name of | individual            |            |          |              |
+--------+--------------+-------------+--------------+------------------------+-----------------------+------------+----------+--------------+
|        | OR           | data breach | with         | organization           | relates to an account | individual | had with | organization |
+--------+--------------+-------------+--------------+------------------------+-----------------------+------------+----------+--------------+

It's worth noting (yet again) that indentation in L4 matters: 
that's how we make it clear that this has the form ``(p if q and (r or s))`` 
as opposed to the form ``(p if (q and r) or s)``.


Negation as failure also works the way you might expect:

.. csv-table::
    :header: "GIVEN", "person", "IS A", "Person"
    :widths: 15, 5, 15, 15

    "DECIDE", "person", "qualifies for this country's benefits",
    "IF", "person", "is citizen"
    "AND", "NOT", "person", "is citizen of any other country"


gets transpiled into this LE rule 

.. code-block:: le

    a person qualifies for this country's benefits
    if person is citizen
    and it is not the case that 
        person is citizen of any other country.

(Exercise for the reader: what would the corresponding LE template(s) look like?)

Working with dates when transpiling to LE (in broad brush strokes)
------------------------------------------------------------------

You'll want to be able to work with dates in a 'first-class' way,
when modelling contracts and legislation. Fortunately, you can write L4 constitutive rules 
that involve dates, e.g.:

+---------------------+----------------------------------+---------------------+--------------+
| GIVEN               | date of application              |                     |              |
+=====================+==================================+=====================+==============+
| DECIDE              | you do not qualify for our fabulous     |                     |              |
|                     | grant                            |                     |              |
+---------------------+----------------------------------+---------------------+--------------+
| IF                  | date of application              | is after           | 2023-10-30   |
+---------------------+----------------------------------+---------------------+--------------+

(Suppose 2023-10-30 is the deadline. Note that dates must be in YY-MM-DD format.)

This gets transformed to this Logical English rule

.. code-block:: le

  you do not qualify for our fabulous grant
  if a date of application is after 2023-10-30.
  
before being handled in turn by Joe Watt's date-related Logical English predicates `(see our fork of Logical English) <https://github.com/smucclaw/LogicalEnglish/pull/8>`_ 
and `Prolog date library <https://github.com/smucclaw/LogicalEnglish/blob/main/declarative_date_time/declarative_date_time.pl>`_.

We just discussed *after*, but there's also *within* and *before*. You can also ask whether a date is a certain number of days or weeks or months before/after/within some other date; for more information on those predicates, or on how the date-related functionality works, see `Syntax and Denotational Semantics of L4 Relational Predicates (for LE) <https://www.overleaf.com/9757591584pqqqyhhrxbpq#6a4a4a>`_.

Doing arithmetic in L4, with LE as the target  
---------------------------------------------




Exercises
---------





