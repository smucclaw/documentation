==================
Input
==================

-----------------------------------------
Representing Ontology in L4 (classes, instances, methods)
-----------------------------------------
We use DECLARE to set up our classes, our records, our types, our schemas, our ontology, our templates.

We use DEFINE to instantiate those templates with concrete values: the specific variables of a particular agreement.

------------------------
Representing Propositional Logic in L4: Booleans, AND/OR
------------------------
-----------------------------
Core Semantics: Boolean Logic (quickstart-why-use-L4)
-----------------------------

L4's decision logic is based on Boolean logic. Most programming
languages offer an "if/then/else" construct. The "if" condition is
Boolean-valued. It may rely in turn on numeric or other computation
(e.g. `1024 >= 42`) but the terms reduce to true or false.

L4's basic Boolean operators, borrowed from `propositional logic <https://en.wikipedia.org/wiki/Propositional_calculus>`_, are:

- `AND`
- `OR`
- `NOT`
- `UNLESS` (merely shorthand -- "syntactic sugar" -- for `AND NOT`)

L4's list-oriented Boolean operators, borrowed from `predicate logic <https://en.wikipedia.org/wiki/First-order_logic>`_, are:

- `ANY`
- `ALL`

-----------------------------
When are Boolean Structures used
-----------------------------

Boolean Structures are used in the following positions in larger expressions:

- In constitutive (Hornlike) rules:

  - in the left and right positions of a `DECIDE ... IF ...` pattern, which constructs *Horn Clauses*.

- In regulative rules:

  - following an `IF` keyword.

  - following a `WHO` keyword

-----------------------------------------
Detailed Definition of Boolean Structures
-----------------------------------------
    
.. topic: BNF
   
   The BNF for a Boolean Structure is:

.. code-block::

    BoolStruct    a  ::=               UnaBoolStruct a
                         [BinaryBoolOp UnaBoolStruct a]
                         [...]
    BinaryBoolOp     ::= AND | OR | UNLESS
    UnaBoolStruct a  ::= NOT UnaBoolStruct

    a                ::= RelationalPredicate
                       | ParamText

The `a` type is algebraic and in practice is filled by two types: **RelationalPredicates** and **ParamTexts**, described in detail below.
		       
Note that L4 is whitespace-sensitive, so in the first definition
above, the newlines are significant:

.. list-table:: Example of Multiline Boolean Structure

   * - DECIDE
     - output
     - 
   * - IF
     - 
     - foo
   * - IF
     - 
     - foo
   * - AND
     - 
     - bar
   * - OR
     - 
     - baz

The remainder of this section focuses on the elemental
**RelationalPredicates** and **ParamTexts** that can appear within the
Boolean Structure, or **BoolStruct** for short.

.. code-block:: bnf
    
    Boolish	         ::= (TRUE | FALSE | Yes | No)

    BoolStruct Expression::= Expression		
    "BSE"		    | BSE AND BSE
                            | BSE OR  BSE
                            | NOT     BSE
                            | (Expression)	

    BoolStructR          ::= BoolStruct      Relational Predicate



representing arithmetic and predicate logic in L4 (Numbers and Booleans, + - * / any all sum product ? : )
representing modal logic in L4 (state transitions, deontics (must/may/shant), temporal (deadlines), transitions (if satisfied, if not satisfied), a theory of causation)

-----------------------------------------
L4 Boolean Keywords Reference
-----------------------------------------

-- start a boolstruct
 "ALWAYS"
 "NEVER"

-- boolean connectors
 "OR"
 "AND"
 "..."
 "…" 
 "UNLESS"
 "EXCEPT"
 "IF NOT"
 "NOT"   

-----------------------------------------
Example :doc:`Must Sing <returning-examples-must-sing>`
-----------------------------------------


-----------------------------------------
Representing Legislation / Regulation
-----------------------------------------

Example :doc:`Contract as Automaton (Deontic and Temporal Logic): <returning-examples-contract-automaton>`
Example :doc:`PDPA <returning-examples-pdpa-dbno>`

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Regulative Rules: EVERY, WHERE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bnf

    Regulative Rule	::=	EVERY | PARTY	Entity Label						
					[Subject Constraint]						
					[Attribute Constraint]						
					[Conditional Constraint]						
					[Upon Trigger]						
					    Deontic Action Temporal | Deontic Temporal Action					
					[WHERE	         Constitutive Rule						
							        [...]				]

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Regulative Rules: MUST, MAY, and SHANT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bnf

    Obligation Case ::= PARTY     MUST               ...
                        WITHIN    deadline
                        IF FULFILLED                 ...
                        IF VIOLATED                  ...
    
    Permission Case ::= PARTY     MAY                ...
                        WITHIN    deadline
                        IF EXERCISED                 ...
                        IF NOT EXERCISED             ...

    Prohibition Case ::= PARTY    SHANT              ...
                         WITHIN   deadline
                         IF PROHIBITION VIOLATED     ...
                         IF PROHIBITION NOT VIOLATED ...

.. Old Syntax: HENCE/LEST, replaced by MUST, MAY, and SHANT
                    [HENCE	         Rule Label | Regulative Rule]
					[LEST	         Rule Label | Regulative Rule]

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Constitutive Rule and Hornlike Rule
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hornlike clauses have the form: Head if Body

.. code-block:: bnf

    Constitutive Rule ::= [GIVEN  MultiTerm]					
    Hornlike Rule     ::= [Upon   Trigger  ]												
			    DECIDE          Relational Predicate  [AKA Alias] [Typically Boolish]
			  | IS	            BoolStructR															
			  | MEANS           BoolStructR															
			  | HAS		    Relational Predicate															
			  | INCLUDES        Set Group															
			    WHEN            RelationalPredicate BoolStruct															

~~~~~~~~~~~~~~~~~~~~~
Compact Constitutives
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bnf

    Compact Constitutives ::= [GIVEN        MultiTerm]					
                              [Upon Trigger          ]					
			      DECIDE	    Relational Predicate    WHEN	Relational Predicate		
										[ ... ]								
					|   Relational Predicate    OTHERWISE | GENERALLY

----------------
Labels and Names
----------------

.. code-block:: bnf

    Entity Label    ::= Aliasable Name		

    Aliasable Name  ::= MultiTerm [AKA MultiTerm]	 
    // in future – extend to BoolStruct of SetGroup							

------------------------------
Constraints and 'Upon Trigger'
------------------------------

.. code-block:: bnf

    Subject Constraint      ::= WHO             RelationalPredicate BoolStruct	        
    //evaluated against the subject of the rule

    Attribute Constraint    ::= WHOSE           RelationalPredicate BoolStruct

    Conditional Constraint  ::= (WHEN | IF)	RelationalPredicate BoolStruct
                                [UNLESS         RelationalPredicate BoolStruct]

.. code-block:: bnf

    Upon Trigger ::= UPON		Aliasable Name			

--------
Deontics
--------

.. code-block:: bnf

    Deontic Temporal Action	::=	Deontic Keyword             Temporal Constraint			
                                        -> | DO		            Action Expression			

    Deontic Keyword	        ::=	(MUST | MAY | SHANT)

A semantically equivalent syntactic alternative allows the temporal keyword to line up with the other keywords:

.. code-block:: bnf

    Deontic Action Temporal ::= Deontic Keyword            Action Expression		
                                Temporal Constraint						

.. code-block:: bnf

    Temporal Constraint     ::=	(BEFORE | AFTER | BY | UNTIL)   Temporal Spec



----------------------------------------
L4 Regulative Keywords Reference
----------------------------------------

-- start a regulative rule
"EVERY"
"PARTY"
"ALL"

-- deontics
"MUST" 
"MAY"  
"SHANT"

-- regulative chains
"HENCE"
"THUS" 

-----------------------------------------
Further reading on the :doc:`Full L4 Language Specification <returning-specification>`.
-----------------------------------------

-----------------------------------------
Other Examples
-----------------------------------------


Example: :doc:`representing an insurance agreement <returning-examples-home-insurance-clause>`



Example: :doc:`representing a financial agreement (Flood & Goodenough)<returning-examples-deontic-and-temporal-logic>`

