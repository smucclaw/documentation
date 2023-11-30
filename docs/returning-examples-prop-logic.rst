
.. _eg_prop_logic:

###############################
1. Propositional Logic Examples
###############################

.. _eg_must_sing:

**************
Must Sing Rule
**************

`See the L4 code for this 'Must Sing' example <https://docs.google.com/spreadsheets/d/1WyzDqaVTcicDa2K_mzS_SGtLZL4SnzzfYHUDdtBDxUA/edit#gid=1373864401>`_

This example gives an overview of how to write a simple rule in L4 using the simple rule: "Every person who walks and eats or drinks must sing".

We thank Matthew Waddington for originally authoring the case from which this example is drawn.

This chapter begins with a very simple rule, which is the input and is the contract we want to formalise:

"Every person who walks and eats or drinks must sing".

Notice that there is ambiguity in thie sentence. We could mean:

1. Every person who walks and (eats or drinks) must sing.
2. Every person who (walks and eats) or drinks must sing.


The brackets disambiguate the sentence.

In interpretation 1, people who walk and people who eat or drink must sing. This is the interpretation shown in the google spreadsheet example.

We write interpretation 1 in L4 like this:

.. csv-table:: Must Sing Rule interpretation 1 in L4

    "EVERY", "Person"
      "WHO", "walks"
      "AND",           , "eats"
           ,       "OR", "drinks"
     "MUST", "sing"

In interpretation 2, people who walk and eat or people who drink must sing.

We write interpretation 2 in L4 like this:

.. csv-table:: Must Sing Rule interpretation 2 in L4

    "EVERY", "Person"
      "WHO",        , "walks"
           ,   "AND", "eats"
       "OR",   "drinks"
     "MUST",   "sing"

We transformed the rule into L4 with the following method:

1. Break the rule up into subclauses separated by keywords like EVERY, WHO, and AND.
2. Write down the nouns ("Person") and verbs ("walks", "eats", "drinks") in the cell to the right of the keywords.

We use indentation to disambiguate the sentence. An indentation is when the cells next to and below a keyword are blank.


.. _eg_rodents_vermin:

*********************
Home Insurance Clause
*********************

`See the L4 code for this 'Home Insurance' example, labelled as 'Rodents and Vermin' <https://docs.google.com/spreadsheets/d/1WyzDqaVTcicDa2K_mzS_SGtLZL4SnzzfYHUDdtBDxUA/edit#gid=1663223809>`_

This example focus on a single decision rule drawn from a home insurance policy and its transformations to more easily understood forms.

"We do not cover any loss or damage caused by rodents, insects, vermin or birds. However, this exclusion does not apply to:

    a. loss or damage to your contents caused by birds; or

    b. ensuing covered loss unless any other exclusion applies or where an animal causes water to escape from a household appliance, swimming pool or plumbing, heating or air conditioning system."

Following the method we learned in the "Must Sing" example, we need to:

1. Break the rule up into subclauses separated by keywords like EVERY, WHO, and AND.
2. Write down the nouns and verbs in the cell to the right of the keywords.

Remembering that we use indentation to disambiguate the sentence. An indentation is when the cells next to and below a keyword are blank.

------------------------------------------------
Breaking the home insurance rule into subclauses
------------------------------------------------

    ``"We do not cover any loss or damage caused by rodents, insects, vermin or birds.
    However, this exclusion does not apply to:``

        ``loss or damage caused by birds; or``

            ``ensuing covered loss``

            ``unless any other exclusion applies``

                ``or where an animal causes water to escape from a household appliance, swimming pool or plumbing, heating or air conditioning system."``

----------------------------------------------
The two ways to encode the home insurance rule
----------------------------------------------

We can write this rule in two ways, a 'positive' way and a 'negative' way.

The positive way is where we formalise the rule in a way that tells you that you are covered if the subclauses apply. Another way of saying this is "the damage is covered if..."

The negative way is where we formalise the rule in a way that tells you that you are not covered if the subclauses apply. Another way of saying this is "the damage is not covered if..."

Below is the table for the positive case, "the damage is covered if..." The rows and columns are numbered for convenience and reference.

-----------------------------------------------------------
Encoding of the positive version of the home insurance rule
-----------------------------------------------------------

.. csv-table:: The damage is covered if...

    , "1", "2", "3", "4", "5", "6", "7", "8", "9"
    "1", "DECIDE", "Loss or Damage 1", "IS", "Covered"
    "2", "IF", "NOT",                    , "Loss or Damage", "caused by", "rodents"
    "3",      ,                    ,                 ,       ,  "OR", "insects"
    "4",      ,                    ,                 ,       ,  "OR", "vermin"
    "5",      ,                    ,                 ,       ,  "OR", "birds"
    "6",     ,             "UNLESS",            ,       , "Loss or Damage", "IS", "ensuing covered loss"
    "7",      ,            ,           "OR",        , "Loss or Damage", "IS", "to Contents"
    "8",      ,                    ,                , "AND", "Loss or Damage", "IS", "caused by birds"
    "9",    ,                    ,                 , "UNLESS",         , "any other exclusion applies"
    "10",   ,                     ,                 ,        ,      "OR", "any animal caused water to escape from",       , "a household appliance"
    "11",   ,                     ,                 ,        ,      ,   ,     "OR", "a swimming pool"
    "12",   ,                     ,                 ,        ,      ,   ,     "OR", "a plumbing, heating, or air conditioning system"

-----------------------------
Understanding the L4 encoding
-----------------------------

This table looks very daunting, but we can split it into a few major subsections.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Step 1: Declare what version of the rule you're encoding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first step is to decide what version of the contract you're encoding with the DECIDE keyword. In this case, we decided that we are encoding the positive vesion of the contract, "the damge is covered if..."

We see this decision in the first row, where we see "DECIDE Loss or damage 1 IS Covered".

.. csv-table:: Step 1

    "1", "DECIDE", "Loss or Damage 1", "IS", "Covered"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Step 2: Create the encoding one subclause at a time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

^^^^^^^^^^^^^^^
First subclause
^^^^^^^^^^^^^^^

The original home insurance rule states that the rule is an exclusion that does not apply in certain cases, like damage caused by rodents, insects, vermin, or birds.

Since we're encoding a positive version of this rule, we say "The damage is covered IF the damage is NOT caused by rodents, insects, vermin, or birds."

We see this encoding from rows 2 to 5 of the encoding.

.. csv-table:: First subclause

    "2", "IF", "NOT", "Loss or Damage", "caused by","rodents"
                     "3",                 ,       ,  "OR", "insects"
                     "4",                 ,       ,  "OR", "vermin"
                     "5",                 ,       ,  "OR", "birds"

^^^^^^^^^^^^^^^^
Second subclause
^^^^^^^^^^^^^^^^

The second subclause can be split into two subsubclauses.

.. csv-table:: Second subclause, subsubclause 1

    "6",     ,             "UNLESS",            ,       , "Loss or Damage", "IS", "ensuing covered loss"
    "7",      ,            ,           "OR",        , "Loss or Damage", "IS", "to Contents"
    "8",      ,                    ,                , "AND", "Loss or Damage", "IS", "caused by birds"

.. csv-table:: Second subclause, subsubclause 2

    "9",    ,                    ,                 , "UNLESS",         , "any other exclusion applies"
    "10",   ,                     ,                 ,        ,      "OR", "any animal caused water to escape from",       , "a household appliance"
    "11",   ,                     ,                 ,        ,      ,   ,     "OR", "a swimming pool"
    "12",   ,                     ,                 ,        ,      ,   ,     "OR", "a plumbing, heating, or air conditioning system"

..
    Nemo note, 12 May 2023: I am pausing writing more stuff here because of a post in #documentation-and-guides where I suggest that indentation should flow from left to right, never backwards. If this is the case, then I can write about it above.

    The rule can be that subclauses with "or" as in "loss or damage", which suggests that the clause can be broken down further, should be moved to later, so we can read the rule as:

    ensuing covered loss; or
        loss or damage caused by birds



..
    (Nemo: Everything below is the old stuff. I removed it from this example page on 11 May 2023. I'm keeping it here in case we want to use it again.)
    Decisions express first-order logic, functions, predicates, judgements, and calculation in general.

    Concepts introduced:

    1. Boolean Structures in detail.

    2. Visualization as an electrical circuit diagram.

    Keywords introduced:

    - ``DECIDE``
    - ``WHEN``
    - ``UNLESS``
    - ``AND``
    - ``OR``
    - ``NOT``

    ~~~~~~~~~
    Decisions
    ~~~~~~~~~

    Decisions express first-order logic, functions, predicates, judgements, and calculation in general.

    .. code-block:: bnf

        Hornlike ::= [GIVEN        ParamText            ]
                    DECIDE       RelationalPredicate
                    [WHEN | IF    Boolean Structure    ]

    If you happen to know Prolog, you will be familiar with the notion of a Horn clause.

    ``head(param1, param2, …) :- body1(param3, param4), body2(param5, param6).``

    The head, to the left of the ``:-`` symbol, is the conclusion of the rule.

    The body, to the right of the ``:-`` symbol, contains the list of predicates that, when satisfied, conclude that the head of the rule is true.

    In L4, the relational predicate on the ``DECIDE`` line gives the conclusion of the rule.

    The Boolean Structure introduced by the ``WHEN`` keyword gives the conditions of the rule.

    The keywords ``WHEN`` and ``IF`` are synonymous in a ``DECIDE`` context.

    The ``GIVEN`` keyword provides other arguments to the decision rule, and is conjoined with the ``WHEN | IF`` material.

    The expression context of the ``GIVEN`` and ``WHEN | IF`` includes the history available to the calling context. For example, if the decision is being evaluated for the purposes of executing a certain regulative rule, the trace prior to that state transition is available to the DECIDE rule.

    Constitutive rules using ``WHEN`` are a subset of Hornlike rules that use ``DECIDE``.

    ~~~~~~~~~~~~~~~~~
    Decision Diagrams
    ~~~~~~~~~~~~~~~~~

    Visualization of a decision rule produces a "circuit diagram": it is based on electrical circuit diagrams. If you can find a path from the left side of the diagram to the right, where the relevant terms have the required values,
    the overall value of the decision diagram is true.

    This is useful because it shows the "big picture" of a legal construct, and suggests ways to short-circuit a particular decision rule.
