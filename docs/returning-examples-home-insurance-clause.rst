.. _eg_rodent:

##############################
Home Insurance Clause Example
##############################

`See the L4 code for this 'Rodents and Vermin' example <https://docs.google.com/spreadsheets/d/1leBCZhgDsn-Abg2H_OINGGv-8Gpf9mzuX1RR56v0Sss/edit?pli=1#gid=1206725099>`_

This example focus on a single decision rule drawn from a home insurance policy and its transformations to more easily understood forms.

"We do not cover any loss or damage caused by rodents, insects, vermin or birds. However, this exclusion does not apply to:

    a. loss or damage to your contents caused by birds; or

    b. ensuing covered loss unless any other exclusion applies or where an animal causes water to escape from a household appliance, swimming pool or plumbing, heating or air conditioning system."

Following the method we learned in the "Must Sing" example, we need to:

1. Break the rule up into subclauses separated by keywords like EVERY, WHO, and AND.
2. Write down the nouns and verbs in the cell to the right of the keywords.

Remembering that we use indentation to disambiguate the sentence. An indentation is when the cells next to and below a keyword are blank.

--------------------------------------------------------
Step 1: Breaking the home insurance rule into subclauses
--------------------------------------------------------

"We do not cover any loss or damage caused by rodents, insects, vermin or birds. 
    However, this exclusion does not apply to:
        loss or damage caused by birds; or
        ensuing covered loss
            unless any other exclusion applies
                or where an animal causes water to escape from a household appliance, swimming pool or plumbing, heating or air conditioning system."
                
We can write this rule in two ways, a 'positive' way and a 'negative' way. 

The positive way is where we formalise the rule in a way that tells you that you are covered if the subclauses apply.

The negative way is where we formalise the rule in a way that tells you that you are not covered if the subclauses apply.

.. csv-table:: Covered If
    
    "DECIDE", "Loss or Damage 1", "IS", "Covered"
    "IF", "NOT",                    , "Loss or Damage", "caused by", , "rodents"
        ,      ,                    ,                 ,       ,  "OR", "insects"
        ,      ,                    ,                 ,       ,  "OR", "vermin"
        ,      ,                    ,                 ,       ,  "OR", "birds"
        ,      ,            "UNLESS",                ,        ,      , "Loss or Damage", "IS", "to Contents"
        ,      ,                    ,                , "AND", "Loss or Damage", "IS", "caused by birds"
        ,     ,                     ,            "OR",       , "Loss or Damage", "IS", "ensuing covered loss"
        ,    ,                    ,                 , "UNLESS",         , "any other exclusion applies"
        ,   ,                     ,                 ,        ,      "OR", "any animal caused water to escape from",       , "a household appliance"
        ,   ,                     ,                 ,        ,      ,   ,     "OR", "a swimming pool"
        ,   ,                     ,                 ,        ,      ,   ,     "OR", "a plumbing, heating, or air conditioning system"
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