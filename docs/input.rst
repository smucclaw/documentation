==================
Input
==================

representing propositional logic in L4 (Booleans, AND/OR)

------------------------
Booleans and BoolStructs (returning-specifications.rst)
------------------------


.. topic: Usage Sites

Boolean Structures are used in the following positions in larger expressions:

- In constitutive (Hornlike) rules:

  - in the left and right positions of a `DECIDE ... IF ...` pattern, which constructs *Horn Clauses*.

- In regulative rules:

  - following an `IF` keyword.

  - following a `WHO` keyword

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

-----------------------------------------
Detailed Definition of Boolean Structures
(quickstart-why-use-L4)
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
Boolean connectors from BasicTypes.hs
-----------------------------------------

-- start a boolstruct
toToken "ALWAYS" = pure Always
toToken "NEVER"  = pure Never

-- boolean connectors
toToken "OR" =     pure Or
toToken "AND" =    pure And
toToken "..." =    pure And   -- CNL sugar to allow phrases to follow
toToken "…"   =    pure And   -- CNL sugar to allow phrases to follow -- this is unicode for ellipsis
toToken "UNLESS" = pure Unless
toToken "EXCEPT" = pure Unless
toToken "IF NOT" = pure Unless
toToken "NOT"    = pure MPNot

-----------------------------------------
example: in returning-examples-must-sing.rst
-----------------------------------------

-----------------------------------------
representing ontology in L4 (classes, instances, methods)
-----------------------------------------
    We use DECLARE to set up our classes, our records, our types, our schemas, our ontology, our templates.

    We use DEFINE to instantiate those templates with concrete values: the specific variables of a particular agreement.


-----------------------------------------
representing a bit of legislation / regulation (PDPA)
-----------------------------------------

examples: returning-examples-contract-automaton.rst.txt
docs\returning-examples-pdpa-dbno.rst

-----------------------------------------
returning-specification.rst.txt
-----------------------------------------

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

----------------------------------------
Core Semantics: State Transition Systems (docs\quickstart-why-use-L4.rst)
----------------------------------------

Legislation, regulations, and contracts prescribe processes for
parties to obey: under certain conditions, a person must act in some
way within some deadline; if they succeed, matters proceed one way; if
they fail to act, matters proceed another way.

L4 models these legal and business processes as state transition
systems. Related formalisms include BPMN, DFAs, Petri Nets, and
hierarchical state machines (Harel statecharts).

In L4, regulative, aka prescriptive, rules have the syntax given
below.

.. code-block::

   RegulativeRule      ::= ["UPON"        EventIdentifier]
                            "PARTY"       PartyIdentifier
                           ["IF"          ConditionExpression]
		            DeonticModal     ActionExpression
		           [TemporalModal  DeadlineExpression]
		           [SuccessTransition]
		           [FailureTransition]
		           ["WHERE"       LetBinding]
		      
   EventIdentifier     ::= ParamText
		      
   PartyIdentifier     ::= BoolStruct of ParamText
		      
   ConditionExpression ::= BoolStruct of Relational Predicates
   		      
   DeonticModal        ::= "MUST" | "MAY" | "SHANT"
		      
   ActionExpression    ::= BoolStruct of ParamText
		      
   TemporalModal       ::= "BEFORE" | "AFTER" | "BY" | "ON"
   
   DeadlineExpression  ::= Number ("days" | "weeks" | "months" | "years")
                         | AbsoluteDate

   SuccessTransition   ::= ("THUS" | "HENCE" | "IF FULFILLED") (RuleName | RegulativeRule)

   LetBinding          ::= DecisionRule+

   RuleName            ::= String

The syntax for a `DecisionRule` is given below.

AbsoluteDate syntax is not given here, this is a can of worms to be
explored elsewhere.
   
This syntax is intended to maintain isomorphism with legal source text
which frequently has the form "upon receiving a demand for repayment,
if the borrower is in default, the borrower must repay the outstanding
principal plus any applicable accrued interest to the lender within
five business days."

Under the hood, that English text is trying to express a state
transition. The L4 reorganizes the parts of the sentence according to
a standard format.

.. code-block:: L4

     UPON  demand for repayment
       IF  borrower  IS  in default
    PARTY  borrower
     MUST  repay  the loan amount
              to  the lender
   WITHIN  5  business days
    WHERE  DECIDE  the loan amount  IS  SUM  outstanding principal
                                             any applicable accrued interest

Double-spaces indicate column separations.

.. sidebar:: CS Sidebar

   In a state transition system, events occur in time, changing the
   *current state* to some *next state*. States lead one to another,
   in a directed acyclic graph. They terminate in one of (usually) two
   states: fulfilled, vs breach. In renewable contracts there may be a
   third "final" state which is shorthand for "restart the contract at
   some earlier state, but with certain variables updated, such as
   expiration date."

Concurrency presents a conceptual challenge. Many contracts and
business processes describe multiple "moving parts". If you're
juggling balls with your right hand while spinning plates with your
left, each hand can be naturally modeled as its own state machine; but
showing the system as a whole requires a product composition of every
state on the left with every state on the right. L4's treatment of
this issue is given elsewhere in this documentation.

----------------------------------------
BasicTypes.hs
----------------------------------------

-- start a regulative rule
toToken "EVERY" =  pure Every
toToken "PARTY" =  pure Party
toToken "ALL"   =  pure TokAll -- when parties are treated as a collective, e.g. ALL diners. TokAll means "Token All"

-- deontics
toToken "MUST" =   pure Must
toToken "MAY" =    pure May
toToken "SHANT" =  pure Shant

-- regulative chains
toToken "HENCE" = pure Hence
toToken "THUS"  = pure Hence


-----------------------
representing an insurance agreement (PAU)
-----------------------
docs\returning-examples-home-insurance-clause.rst

-------------------------
representing a financial agreement (Flood & Goodenough)
-----------------------
docs\returning-examples-deontic-and-temporal-logic.rst