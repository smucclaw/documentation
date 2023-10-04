.. _tour_of_L4:

###########
Why use L4?
###########

* `L4 helps improve access to justice`_
* `L4 helps people understand laws and contracts`_
* `L4 helps legal engineers draft with confidence`_
* `L4 helps enterprises manage their contracts`_
* `L4 helps governments streamline service delivery`_
* `L4 helps laypeople with a Web App`_
* `L4 helps you detect conflicts and loopholes`_
* `L4 helps you visualise legal logic`_
* `L4 can export to multiple formats`_
* `L4 uses spreadsheets for interaction`_
* `L4 contains a package library`_
* `L4 supports Document Assembly`_
* `L4's answers are explainable`_

======================================
L4 helps **improve access** to justice
======================================

The L4 DSL stack improves access to justice and reduces the cost of
developing legal software by giving non-lawyers a "low-code" way to
explore and produce legal "programs".

=================================================
L4 helps people **understand** laws and contracts
=================================================

L4’s **visualizers** graphically depict the rules and logic of legal code to aid comprehension. (See: :ref:`the 'Must Sing' example <eg_mustsing>` for ; or :ref:`the 'Home Insurance' example <eg_rodent>`)

L4’s **scenario explorer** helps engineers and end-users explore a contract by asking “what if?” and “can I?”.

L4’s **explanation engine** offers justifications for verdicts calculated by L4, for transparency.

L4’s **planning engine** helps end-users achieve goals by asking “how to?”.

==================================================
L4 helps legal engineers **draft** with confidence
==================================================

L4 is a DSL: a "low-code" **domain-specific language** designed for the legal domain.

The L4 **ecosystem of tools, libraries, and sample code** helps legal
engineers get productive quickly without reinventing the wheel.

L4’s **drafting IDE** helps legal engineers draft and amend legal code
with confidence, in a low-code programming environment, using
techniques borrowed from programming language theory, compiler design,
and formal methods.

L4’s **ergonomic syntax**
is expressive enough to encode any contract and legislation using familiar keywords and a natural-language syntax

L4’s **app builder** automates the extraction of LegalTech apps
without having to hire a team of developers for efficiency.

L4’s **transpiler** exports to a variety of third-party tools and
languages for interoperability.

===============================================
L4 helps enterprises **manage** their contracts
===============================================

Enterprise users can integrate L4 into their existing **contract
lifecycle management** systems to support more sophisticated "what
if?" queries than their CLM databases allow.

====================================================
L4 helps governments **streamline** service delivery
====================================================

Government agencies innovating with "Rules as Code" can use L4 basis
for automating the generation of citizen-facing web applications and
chatbots.

=================================
L4 helps laypeople with a Web App
=================================

L4 automatically generates a web app that helps end users explore the logic of your legal code.

.. image:: ../images/web-tool-screenshot.png
   :class: with-border

They can use this tool to understand if a law applies to them, or certain contractual conditions are met.

===========================================
L4 helps you detect conflicts and loopholes
===========================================

L4 sanity-checks your programs to detect internal conflicts and loopholes.

The **"formal methods"** components of the L4 toolchain automatically analyze your code for loopholes and inconsistencies.

L4's **unit testing** framework lets you **set up test scenarios** and monitor them as your contracts evolve.

L4's **library** of components makes it easier to **draft legal templates and automatically produce legal documents** for signature.

==================================
L4 helps you visualise legal logic
==================================

L4 generates convenient visualisations of the logic and the moving parts of your "legal program".

To understand complicated **logic** involving words like "and", "or", "unless": view the *circuit diagram* to see how yes/no verdicts depend on input facts.

.. image:: ../images/qualifies-logic.png
    :class: with-border
    :width: 325px

.. image:: ../images/qualifies-boolean-circuit.png
    :class: with border
    :width: 325px

To understand complicated **processes** involving *deadlines and obligations*: view the *state diagram* to see how events change state over time, leading to new obligations for parties. Identify a goal and see what you need to do to achieve it.

.. image:: ../images/L4-visualisation-screenshot.png
    :class: with-border

To understand complicated **rule interactions** like *notwithstanding, subject to*: view the *meta-rule analysis* to see how rules interact. (in development)

==================================
L4 can export to multiple formats
==================================

L4 code can be exported to languages such as Typescript (Javascript), Python, Prolog, and Haskell.

On the roadmap are other languages like OpenFisca, Catala, Epilog, and
Accord. We prioritize these exporters according to demand so if
there's something you want on the list please contact us!

====================================
L4 uses spreadsheets for interaction
====================================

L4 is low-code. You don't have to install VS Code, Emacs, or Vim. The
IDE is Google Sheets: if you can edit a spreadsheet, you can program
in L4.

=============================
L4 contains a package library
=============================

The L4 package library (currently in development) contains useful components such as

- Calendars (knows about holidays, can count business days)
- Money (knows about currencies)
- Corporate (knows about directors, shareholders, meetings, resolutions)
- Investment Agreements (convertible notes, SAFEs, and other instruments)
- Insurance Policies (knows about risks, coverage, and supplementary add-ons)
- Legislation and Regulation (knows about permitting and compliance)

=============================
L4 supports Document Assembly
=============================

The contract assembly engine helps you generate a document you can
sign after running it past a lawyer for code review.

For investment agreements, L4 also generates all the prerequisite
components such as board resolutions and members' resolutions in
writing.

L4's PDF documents embed the code of the L4 contract for forward
compatibility with contract lifecycle management tools.

The L4 package library will soon contain loan agreements, leasing agreements, and investment agreements.

============================
L4's answers are explainable
============================

L4's answers are *explainable* and *transparent*.

You can ask *"why?"*: Interactively drill down into every decision. 

..
  (TODO: show output of the Explainable monad)

You can ask *"how?"*: if you state a goal you want to achieve, L4 will outline a course of action.

..
  (TODO: show output of planning engine showing how to traverse the state transition graph to achieve a particular goal.)




===================
The Semantics of L4
===================

This section outlines the semantic domains that support L4's
expressivity and generality.

The concepts introduced in this section are implemented throughout the
L4 compiler toolchain.

Familiarity with the underlying ideas behind L4 is essential to any
encoding exercise, just as familiarity with algorithms and data
structures is essential to any programming exercise, and familiarity
with jurisprudential notions of tort and liability is essential to any
contract drafting practice.

L4's semantics fall into three major domains:

- regulative rules are modeled as state transition systems

- constitutive rules are modeled using Boolean logic and simple arithmetic

- data modelling "ontology" borrows ideas from object-oriented programming.

We introduce each of these in turn.

----------------------------------------
Core Semantics: State Transition Systems
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

-----------------------------
Core Semantics: Boolean Logic
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

.. sidebar:: Legal Sidebar

   In law, much drama revolves around the process by
   which the complexity of the real world reduces to binary values:
   guilty or not guilty; claims won or lost. Law has methods for making
   those reductions, such as `bright-line
   <https://en.wikipedia.org/wiki/Bright-line_rule>`_ and `fine-line
   <https://en.wikipedia.org/wiki/Balancing_test>`_ tests.

Real-world use of L4 has shown that these operators are sufficent to
represent large swathes of legal content -- things to do with
**decisions**.

In L4, operators and their arguments are grouped by indentation. In
other languages, parentheses usually play this role; L4 relies on
layout indentation instead due to "low-code" motivations.

.. sidebar:: CS Sidebar

   The day before you turn 21, you can't buy alcohol; the
   day after, you can. if you're driving uphill at 79km/hr, you're a
   good, law-abiding citizen; if, on the downslope, you hit 81km/hr,
   you're breaking the law. These *edge cases* may seem ridiculous, but
   they are an unavoidable possibility in any family of functions of type
   `E2B = Environment -> Boolean`.

Legal writing is often considered complex because a decision may
involve many elements, spread out across multiple pages of text,
separated across section references and "meta-rules" about
applicability.

For example, parking regulations may say:

- if it's a weekend, section 2 applies;
- if it's a weekday, section 3 applies;
- but if you're previously obtained a special permit, section 4 applies notwithstanding sections 2 and 3.

All of these elements can be reduced to Boolean logic. L4 even
automatically puts them in an "infographic" style diagram for easier
comprehension.

.. topic: Usage Sites

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

---------------------
Relational Predicates
---------------------

In some places, the `a` type of a BoolStruct contains a Relational Predicate.

Those places are:
  - in regulative rules, following an `IF` keyword.
  - in regulative rules, following a `WHO` keyword
  - in constitutive (Hornlike) rules, in the left and right positions of a `DECIDE ... IF ...` pattern, which constructs *Horn Clauses*.

There are five major subtypes of Relational Predicates.

.. code-block::

   RelationalPredicate ::= RPMultiTerm
		         | RPParamText
		         | RPConstraint
			 | RPnary
		         | RPBoolStructR

We define the semantics and give examples of each type below, in increasing order of complexity.
			 

^^^^^^^^^^
MultiTerms
^^^^^^^^^^
			 
The simplest form of RelationalPredicate is a sequence of cells all on the same line, containing either strings or numbers.
			 
.. code-block::

   RPMultiTerm         ::= [MTExpression]
   MTExpression        ::= MTT  string -- multiterm text
                         | MTI  number -- multiterm integer

In future, date, currency, and floating-point types may be added, using `MTD`, `MTC`, and `MTF` respectively.

.. topic:: Semantics:

	   MultiTerms are used to represent ground terms, or defined terms which themselves expand to BoolStructs of ground terms.

.. topic:: Example:
	   
	   You can buy beer if you are over 21.

.. code-block::

   PARTY you
     MAY buy beer
      IF you are over 21
		
.. list-table:: Example of RelationalPredicate as a MultiTerm
   :header-rows: 1

   * - input:
     - you
     - are
     - over
     - 21
   * - parses to:
     - MTText you
     - MTText are
     - MTText over
     - MTInteger 21

The `Multiterm` value `[MTT you, MTT are, MTT over, MTI 21]` is meant
to be stringified to natural language and put to the end-user as a
question in a user interface:

.. pull-quote::

   Are you over 21?

.. code-block:: prolog

   youAreOver21 :- userInput("you are over 21").

or perhaps, after natural language transformation,

.. code-block:: prolog

   youAreOver21 :- userInput("are you over 21?").

However, if the multiterm appears to the left of an IF in a DECIDE
rule, it is acting as the head of a Horn clause, which means user
input is not needed, because the answer will be computed by the body
of the Horn clause. (User input may still be sought in a user
interface that allows shortcut answering of parent nodes.)
   
.. code-block::

   youAreOver21 :- currentDate - birthDate > 21.

.. code-block:: prolog

   youAreOver21 :- dateDiff(currentDate, birthDate, (Y,M,D)), Y #> 21.


^^^^^^^^^^
ParamTexts
^^^^^^^^^^

The next simplest form is a sequence of cells with extra information on subsequent lines:
       
.. code-block::

   RPParamText          ::= ParamText

   ParamText            ::= TypedMulti
                            [...]

   TypedMulti           ::= MultiTerm  [TypeSig]

   TypeSig              ::= IS A       TypeName
                          | IS ONE OF  MultiTerm
                          | IS LIST OF TypeName

   TypeName             ::= String

The optional `TypeSig` is used to annotate the action, and its parameters, with type signatures. We will not go into detail about those here.
	  
.. topic:: Semantics:

	   ParamText stands for "parameterized text", and is usually used to
	   represent qualified actions, in the object of a deontic modal.

.. list-table:: Example of RelationalPredicate as a ParamText
   :stub-columns: 1

   * - input:
     - PARTY
     - alice
   * -
     - MUST
     - cook
     - food
   * -
     - 
     - with
     - soy sauce
   * -
     - 
     - without
     - peanuts
   * -
     - 
     - using
     - a wok
   * -
     - AND
     - drink
     - beverage
   * -
     - 
     - without
     - alcohol

This matches the expressiveness of a Python function with named arguments:

.. code-block:: python

   cook(food, avec="soy sauce", sans="peanuts", using="a wok")
   drink(beverage, without="alcohol")

(As of 0.9.4.3, L4 is limited to a single ParamText in the action phrase. The parser is being extended to support a boolstruct of paramtexts.)

When a ParamText is used inside a BoolStruct RelationalPredicate, the parameters are passed to the predicate:

.. code-block: prolog

   ... :- cook(food, [with(soy_sauce), without(peanuts), using(a_wok)]),
          drink(beverage, [without(alcohol)]).


^^^^^^^^^^
Constraints
^^^^^^^^^^^

The next more complex relational predicate involves explicit relation keywords:

.. code-block::

   RPConstraint        ::= MultiTerm Relation MultiTerm

The relations and their semantics are given below:
   
.. list-table:: Relations used in Constraints
   :stub-columns: 1

   * - Relation (keyword)
     - semantics
     - relation constructor
   * - IS
     - equality
     - RPis
   * - <
     - less than
     - RPlt
   * - >
     - greater than
     - RPgt
   * - <=
     - less than or equal to
     - RPlte
   * - >=
     - greater than or equal to
     - RPgte
   * - IN
     - element is a member of a list
     - RPelem
   * - INCLUDES
     - a list contains an element
     - (unimplemented)
   * - BEFORE
     - date comparison
     - RPTC TBefore
   * - AFTER
     - date comparison
     - RPTC TAfter
   * - BY
     - date comparison
     - RPTC TBy
   * - ON
     - date comparison
     - RPTC TOn

.. topic: Semantics
  
The semantics of an RPConstraint predicate depend on the position where it appears.

.. list-table:: In a regulative rule, after an `IF` keyword
   :stub-columns: 1

   * - example
     - case
     - Prolog semantics
   * - X IS Y
     - "Y" is a term defined elsewhere in some constitutive (Hornlike) rule
     - rpis(X,Y) :- y(X).
       Note that `y(X)` itself should be defined elsewhere and able to be expanded. See below remark about Expansion.
   * - X IS Y
     - "X IS Y" is a predicate defined elsewhere in some constitutive (Hornlike) rule
     - rpis(X,Y) :- X = Y.
   * - X IS Y
     - Y is numeric
     - rpis(X,Y) :- X #= Y.
   * - X IS Y
     - Y is a member of an enum defined elsewhere
     - rpis(X,Y) :- X = Y.
   * - X (<, >, <=, >=) Y
     - Y is a defined term with numeric type and a computable value
     - rpis(X,Y) :- X #< Y ... X #> Y ... X #=< Y ... X #>= Y
   * - IN
     - Y is a list type
     - rpin(X,Y) :- memberchk(X, Y).
   * - INCLUDES
     - a list contains an element
     - rpincludes(X,Y) :- memberchk(Y, X).
   * - BEFORE, BY
     - date comparison
     - rpBy(X,Y), rpBefore(X,Y) :- X #< Y. % with some asDate typecasting as needed, implementation-dependent.
   * - AFTER
     - date comparison
     - rpAfter(X,Y) :- X #> Y. % with some asDate typecasting as needed, implementation-dependent.
   * - ON
     - date comparison
     - rpOn(X,Y) :- X #= Y. % with some asDate typecasting as needed, implementation-dependent.


.. list-table:: In a regulative rule, following a `WHO` keyword
   :stub-columns: 1

   * - example
     - case
     - Prolog semantics
   * - PARTY P WHO Y
     - "Y" is a term defined elsewhere in some constitutive (Hornlike) rule
     - rpwho(X,Y) :- y(X).
       Note that `y(X)` itself should be either a ground term to be put to the user as a question, or defined elsewhere and able to be expanded.
   
A `WHO` limb in a regulative rule implicitly uses the PARTY as the subject of the rule.

The `IS` relation is substituted implicitly; other relations are
not available. If you want to use other relations, use an explicit
`IF` and name the party explicitly.

.. list-table:: In a constitutive (Hornlike) rule, in the left position of a `DECIDE ... IF ...` pattern

   * - example
     - case
     - Prolog semantics
   * - DECIDE X IS Y
     - there is no IF part
     - y(X) :- true.
   * - DECIDE X IS Y IF ... rhs ...
     - Y is numeric
     - rpis(X, Y) :- ... rhs ...
   * - DECIDE X IS Y IF ... rhs ...
     - Y is non-numeric
     - rpis(X, Y) :- ... rhs ...


.. list-table:: In a constitutive (Hornlike) rule, in the right position of a `DECIDE ... IF ...` pattern

   * - example
     - case
     - Prolog semantics
   * - DECIDE foo IF 
     - there is no IF part
     - y(X) :- true.
   * - DECIDE X IS Y IF ... rhs ...
     - Y is numeric
     - rpis(X, Y) :- ... rhs ...
   * - DECIDE X IS Y IF ... rhs ...
     - Y is non-numeric
     - rpis(X, Y) :- ... rhs ...


.. topic: Internals Documentation: parsing RPConstraints to Haskell datatypes

   The following example shows how an RPConstraint is parsed.
  
.. list-table:: Example of Parsing a RelationalPredicate as an RPConstraint
   :widths: 20 20 20 20 20
   :stub-columns: 1

   * - input:
     - foo
     - bar
     - IS
     - 123
   * - parses to:
     - MTText foo
     - MTText bar
     - RPis
     - MTInteger 123

   
.. code-block::

   RPConstraint         ::= RPMultiTerm RPRelation RPMultiTerm


.. list-table:: Example of RelationalPredicate as an RPConstraint
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - input:
     - foo
     - bar
     - IS
     - 123
   * - parses to:
     - MTText foo
     - MTText bar
     - RPis
     - MTInteger 123

^^^^^^
RPnary
^^^^^^

RPnary constructors are the most general form of expression; in fact they are s-expressions.

.. code-block::

   RPnary     ::= Relation (List of Relational Predicates, newline-separated)

This allows us to say things in a Lispy form, like `(SUM 1 2 (MAX 3 4))`.

The permitted relational operators are as in the Constraints table above, plus

.. list-table:: Relations used in RPnary
   :stub-columns: 1

   * - Relation (keyword)
     - semantics
     - relation constructor
   * - &&
     - all are true
     - RPall
   * - ||
     - any are true
     - RPany


.. list-table:: Example of RelationalPredicate as an RPNary
   :widths: 33 33 33
   :header-rows: 0

   * - MTText foo
     - MTText bar
     - MTInteger 123


^^^^^^^^^^^^^
RPBoolStructR
^^^^^^^^^^^^^

This form is too heavyweight and is likely to be deprecated.

---------------------------------
Expansion
---------------------------------

Constitutive (Hornlike) rules define Relational Predicates, which can then be expanded at the points of use.

For example:

.. code-block::

   DECIDE you may pass
       IF horse IS NOT made of coconuts
      AND bird  IS swallow

   DECIDE bird  IS swallow
       IF bird  IS African swallow
       OR bird  IS European swallow

Semantically, we may think of the first rule as desugaring to:
       
.. code-block:: prolog

   youMayPass :- \+ madeOfCoconuts(horse), swallow(bird).

The second rule desugars to

.. code-block:: prolog

   swallow(bird) :-  africanSwallow(bird).
   swallow(bird) :- europeanSwallow(bird).

In a transpiler toolchain which does not operationally rely on Prolog
directly, the same expansion can be performed by the Interpreter
component or by the transpiler itself. The current
`LS/XPile/Interpreter.hs` does perform the equivalent expansion
transformation, relying on equational reasoning to substitute as
though the encoding had originally written:

.. code-block::

   DECIDE you may pass
       IF horse IS NOT made of coconuts
      AND     bird IS African swallow
          OR  bird IS European swallow

If the rest of the ruleset is silent about the further technicalities
of what constitutes an African or European swallow, the question of
`europeanSwallow(bird)` becomes a ground predicate which is put to the
user for input.

---------------------------------
Classifiers and Output Categories
---------------------------------

Suppose: if you were going less than 20km/hr over the limit, one
penalty applies; if you were going more than 20km/hr over the limit,
another penalty applies.

These are, essentially, switch statements writ large. A theoretician
might say that law reintroduces shades of gray to black-and-white
decisions by specializing decision outcomes based on real-valued
logic. More on this in our section on decision tables and trees.

Here's how we express the speeding penalties in L4:

.. code-block::

    DECIDE penalty IS none     IF excess speed <=   0    km/hr
          "        "  warning     "  "         <=  20    km/hr
          "        "  small fine  "  "         <=  40    km/hr
          "        "    big fine  "  "         <=  60    km/hr
          "        "  time travel "  "         IS 141.62 km/hr
          "        "  jail        "  "         >   60    km/hr

To illustrate the `IS` keyword, we've added a special case for cars
moving at exactly 88 miles per hour.
 
In predicate logic notation, we rewrite the above L4 rules to:

.. code-block::

    penalty(ExcessSpeed, warning    ) :- ExcessSpeed =< 20.
    penalty(ExcessSpeed, smallFine  ) :- ExcessSpeed =< 40.
    penalty(ExcessSpeed, bigFine    ) :- ExcessSpeed =< 60.
    penalty(ExcessSpeed, timeTravel ) :- ExcessSpeed IS 141.62.
    penalty(ExcessSpeed, jail       ) :- ExcessSpeed >  60.

To the left of the `IF` keyword, the `IS` keyword creates a *predicate
relation*, defining the `penalty` predicate as a *relation* between
`excess speed` and the output variable which ranges from a warning to
jail.

To the right of the `IF` keyword, an `IS` keyword is treated as value
equality, similar to `==` in Javascript or Python or other languages.

The details of the syntactic transformation are given separately in
*Prolog Transpiler Documentation*.

*CS Sidebar:* For now, we note that such decisions have type `Classifier =
[(E2B,Category)] -> Environment -> Category`. Given some preconfigured
mapping of Boolean case to outcome category, given some specific
environment, a classifier returns the penalty that applies in this
case.

*Operational Semantics*: L4 builds on the essential semantics of
Prolog. Negation as failure and the closed world assumption are
relevant. Upcoming *Prolog Transpiler Documentation* will address what
this means in practice. There are some other minor edge cases: for
example, even in classical logic, it is possible for both a statement
and its seeming "opposite" to be true. (See `vacuous truth
<https://en.wikipedia.org/wiki/Vacuous_truth>`_). In practice these do
not present major concerns for L4.

--------------
Unknown Values
--------------

In a perfect world, Boolean values have one of two values: true or
false. In the real world, variables are sometimes unknown: to reflect
missing information and optional values.

For example, if a user filling out a form did not give their
birthdate, then the perfectly reasonable yes-or-no question "Is the
user over 21?" cannot be answered with a true or false value!

In practice, a JSON structure might omit the `birthdate` attribute, so
it is *undefined*; an `over21()` method might return a value of
*null*. Either way, these neither-true-nor-false values demand a
`ternary logic <https://en.wikipedia.org/wiki/Three-valued_logic>_`
that goes beyond the underlying foundational logic.

In the simple case of a web form, we could slap input validation on
the birthdate field, and make it the user's job to always give a date.

Real-world scenarios often present unknown values. SQL databases may
have `columns which are typed boolean
<https://www.postgresql.org/docs/current/datatype-boolean.html>`_, but
without a `NOT NULL` constraint, allowing three values, not two.

In delicate situations we might want to omit a line of questioning if
it is unnecessary or irrelevant: "birthdate, fine, but do you really
need to know my race?"

"We're only asking because certain discounts might be available if ..."

"Never mind the discounts, let's just skip past that question, shall
we? Especially since the biggest discounts apply to someone over 65,
which I am, regardless of race."

*CS Sidebar*: A typed language might deal with these possibilities by
explicitly using an `Optional<Boolean>` type. In L4, all ostensibly
Boolean values are automatically wrapped in Optional, to anticipate
missing-data scenarios. The specific variant of ternary logic used in
L4 evaluation is from Łukasiewicz's Ł3 logic.

-----------------------------
Footnote: Abducible Variables
-----------------------------

Abducible variables are variables whose values "rise to the occasion":
for example, a quadratic equation `y = x^2 - 4` might have two
roots: at the occasion `y = 0`, one solution that arises is `x = 2`;
but another solution is `x = -2`. So `x` doesn't have one just value:
in this equation it has two. For some other value of `y`, though, `x`
migth have one solution; or even none.

Similarly, in some legal scenarios, people might say, "well, without
knowing the specifics" -- not knowing the exact value of `y` to solve
for -- one can still make certain assertions. For example, you could
give your answer as an inequality: south of `-4` on the y axis, there
are no solutions at all, no values of `x` which satisfy the formula

For example: the rules might say, if it's a weekend, you can park for
free after 12pm; if it's a weekday, you can park for free after 6pm.
That allows some amount of reasoning: if you're just looking to park
at 8pm, that's always free; but if you want to park at 10am, we need
to know which day of the week you're looking at before we can tell you
if you need to buy a ticket.

How is this relevant to L4 developers? 99% of the time, you won't need
to worry about this: L4 figures out abducible variables on its own and
presents them intelligently in the course of deriving an answer set.
This is documented so an L4 internals engineer can understand how L4's
semantic model supports abductive reasoning.

*Math sidebar*: `y = x^2 - 4` has no solutions ... unless we're
allowing `x` to be an imaginary number, in which case we give
`2i, -2i` as the answer. See? Even in mathematics, "it depends".

---------------------
Predicate Expressions
---------------------

All decision expressions are reducible to Prolog predicates, and
conform to the semantics of those predicates.

Note that Prolog is slightly order-dependent, in that if the user
terminates a query after the first answer, order matters.

-----------------
Modal Expressions
-----------------

L4 uses special keywords for the following classes of modal expressions.

Currently supported in the language:

deontic
  - MUST
  - MAY
  - SHANT

temporal
  - BEFORE
  - AFTER
  - WITHIN
  - BY

Slated for consideration in the future:
    
power
  - PROCURE
  - PROVIDE

epistemic
  - BELIEVES
  - KNOWS
  - NOTIFY

causal
  - CAUSES
  - DUETO

These modals reduce to the core forms of L4 expressions: Boolean
Logic, and State Transition Systems.

For example, a contract might say: if Party P1 comes to believe that
some event E1 has occurred, which was caused by an event E2, then
Party P1 must procure that its subsidiary P1A must notify Party P2
within 5 working days.

The triggering state transition is that Event E1 happened.

The "outcome" is the procurement of a notification to P2. It has to be
procured because P1 controls P1A, but P1A is not a party to the
contract, so P1 has to kick off some internal process to make sure P1A
carries out the notification.

The condition is that Event E1 was caused by Event E2.

.. code-block::

     UPON E1
       IF P1 BELIEVES E2 CAUSED E1
    PARTY P1
     MUST PROCURE    PARTY P1A
		      MUST NOTIFY P2

Why is it useful to dedicate specific keywords to some of these
relations? Wouldn't it be enough to simply say something like, `IF
PartyA knows PartyB blah blah`? Well, if PartyB had previously sent
PartyA a formal notice, then the contract could make use of that
information concluding that PartyA knows whatever PartyB told it; and
to make that bit of reasoning happen in the system, it helps to make
`KNOWS` a full keyword.
		      
Here we see that the `PROCURE` keyword is a unary operator of type
`Regulative Rule -> Action` so it can return as the argument to the
`MUST` keyword.

Those expressions that reduce to Boolean logic are rewritten to predicate form:

.. code-block::

   causes(E2, E1, ...) :- ....

Sometimes the system has enough information to compute causation. If,
for example, E2 and E1 are explicitly connected in some state
transition sequence, and the history of the contract (the "trace")
shows that E2 preceded E1, and the reasoner is satisfied that E1 would
not have happened if E2 had not happened, then that predicate would be
computed as satisfied:

.. code-block::

   causes(E2, E1, ...) :- matchTrace(ContractHistory, precedes(E2, E1)).

Other times, human input is required, and the expression reduces to a
query in some interactive UI.

.. code-block::

   causes(E2, E1, ...) :- userInput(["did", E2, "cause", E1]).

How is `CAUSED` as a keyword different from `caused` as a lower-case
term? In the latter case, where user input is required, there is no
difference -- if the encoding had used `caused`, lower case, L4 would
transpile exactly the same relation. The only difference is that L4
would not examine the contract trace to automatically determine
causation.

------------------------------------------------
Core Semantics: Data Modelling is similar to OOP
------------------------------------------------

.. code-block:: BNF

   ClassDeclaration      ::= "DECLARE" ClassName "IS A" SuperClassName
                             "HAS" AttributeDeclaration+

   ClassName             ::= String

   SuperClassname        ::= ClassName

   AttributeDeclaration  ::= AttributeName [ "IS" TypeDetail TypeSpec ]
                            ["HAS" AttributeDeclaration+]

   TypeDetail            ::= "A" | "LIST OF" | "ONE OF"

   AttributeName         ::= string

   TypeSpec              ::= "number" | "string" | ClassName

This provides a syntax for modeling classes as records with attributes, which can themselves be records with attributes.

In this example, we define a class to represent a person-like entity
with a name, id number, and details containing address and
preferences.

.. code-block:: L4

   DECLARE SubClass IS A SuperClass
       HAS name     IS A string
           idNum    IS A number
	   details
	       HAS preferences
	                   HAS sizePref  IS ONE OF small  medium  large
	                       colorPref IS ONE OF red    green   blue
	           address IS AN Address
	               HAS deliveryDetails IS LIST OF string

    DECLARE SuperClass

    DECLARE Address
        HAS line1   IS A           string
	    line2   IS AN OPTIONAL string
	    state   IS A           string
	    city    IS A           string
	    country IS A           string

In a language like Typescript, this becomes:

.. code-block:: typescript

   class SuperClass { }

   enum sizePrefEnum  { small, medium, large }
   enum colorPrefEnum { red,   green,  blue  }

   class SubClass extends SuperClass {
     name  : string;
     idNum : number;
     details : {
       preferences: {
         sizePref  : sizePrefEnum;
	 colorPref : colorPrefEnum;
       };
       address : Address & {
         deliveryDetails: string[];
       }
     };
   }

   class Address {
       line1   : string;
       line2  ?:  string;
       city    : string;
       state   : string;
       country : string;
   }

Defining an instance of that class can be done like this:

.. code-block :: BNF

   DEFINE MyEntity IS A SubClass
      HAS Alice Apple   IS THE Name
          1234567       IS THE idNum
	  medium        IS THE details's preferences's sizePref
	  red           IS THE "         "             colorPref
	  1 west way    IS THE details's address's line1
          octopus city  IS THE details's address's city
	  AA            IS THE state
	  Barbieland    IS THE country
	  deliveryDetails IS don't ring bell
                             don't wake the dog
This expands to:

const myInstance : SubClass = {
    name : "my name",
    idNum : 1234,
g    details : {
	preferences: {
	    sizePref : sizePrefEnum.medium,
	    colorPref : colorPrefEnum.red
	},
	address : {
	    line1 : "1 west way",
	    city  : "octopus city",
	    state : "AA",
	    country : "Barbieland",
	    deliveryDetails : ["don't ring bell", "don't wake the dog"]
	}
    }
}

Yes, L4 does reverse the convention of "name: value"; if you look at
the `IS THE` lines you will see the value comes first. This was done
deliberately for usability reasons.

However, the traditional syntax is still supported -- note the
`deliveryDetails` line.


.. note::
   Regarding the address, this is a trivial example. If you were doing this in the real world, you would `know better <https://www.mjt.me.uk/posts/falsehoods-programmers-believe-about-addresses/>`_.

---------------------------------
Syntax Note: the Ditto Convention
---------------------------------

In the spreadsheet syntax, a `"` double-quote is replaced by the first
nonempty cell above. This affords "ditto syntax" which turns out to be
a pretty user-friendly way to write structured things with less "ink
on the page".

.. todo
    -------------
    Default Logic
    -------------

    :keyword:`WHEN OTHERWISE`

    Exceptions and defaults

    ----------------
    Defeasible Logic
    ----------------

    :keyword:`NOTWITHSTANDING, SUBJECT TO`

    Meta-rule relations

    ---------------
    Lambda Calculus
    ---------------

    :keyword:`GIVEN LET DEFINE`

    ------------
    Unit Testing
    ------------

    :keyword:`SCENARIO GIVEN EXPECT`

    Partial Evaluation reduces a ruleset to a residual.


    Formal Methods
    --------------
    :keyword:`ASSERT TRACE`

    Find loopholes and mistakes in the code

    ---------------------------
    Natural Language Generation
    ---------------------------

    Supports the translation of code into multiple natural languages to support interfaces


