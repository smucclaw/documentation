.. _tour_of_L4:

###########
Why use L4?
###########

**The L4 DSL stack improves access to justice and reduces the cost of
developing legal software by giving non-lawyers a "low-code" way to
explore and produce legal "programs".**

-------------------------------------------------
L4 helps people **understand** laws and contracts
-------------------------------------------------

L4’s **visualizers** graphically depict the rules and logic of legal code to aid comprehension. (See: :ref:`the 'must sing' example <eg_mustsing>` for ; or :ref:`the Rodent Insurance example <eg_rodent>`)

L4’s **scenario explorer** helps engineers and end-users explore a contract by asking “what if?” and “can I?”.

L4’s **explanation engine** offers justifications for verdicts calculated by L4, for transparency.

L4’s **planning engine** helps end-users achieve goals by asking “how to?”.

--------------------------------------------------
L4 helps legal engineers **draft** with confidence
--------------------------------------------------

L4 is a DSL: a "low-code" **domain-specific language** designed for the legal domain.

The L4 **ecosystem of tools, libraries, and sample code** helps legal
engineers get productive quickly without reinventing the wheel.

L4’s **drafting IDE** helps legal engineers draft and amend legal code
with confidence, in a low-code programming environment, using
techniques borrowed from programming language theory, compiler design,
and formal methods.

L4’s **ergonomic syntax** is designed to express patterns frequently
found in legal writing using familiar keywords and a natural-language
syntax.

L4’s **app builder** automates the extraction of LegalTech apps
without having to hire a team of developers for efficiency.

L4’s **transpiler** exports to a variety of third-party tools and
languages for interoperability.

-----------------------------------------------
L4 helps enterprises **manage** their contracts
-----------------------------------------------

Enterprise users can integrate L4 into their existing **contract
lifecycle management** systems to support more sophisticated "what
if?" queries than their CLM databases allow.

----------------------------------------------------
L4 helps governments **streamline** service delivery
----------------------------------------------------

Government agencies innovating with "Rules as Code" can use L4 basis
for automating the generation of citizen-facing web applications and
chatbots.

L4's Features in Detail
=======================

This section shows screenshots of specific features supporting the benefits listed above.

--------------------
Understanding Legal
--------------------

L4 generates convenient visualizations of the logic and the moving parts of your "legal program".

To understand complicated **logic** involving words like "and", "or", "unless": view the *circuit diagram* to see how yes/no verdicts depend on input facts.

(todo: insert image showing the MUSTSING "qualifies" logic and the boolean circuit diagram)

To understand complicated **processes** involving *deadlines and obligations*: view the *state diagram* to see how events change state over time, leading to new obligations for parties. Identify a goal and see what you need to do to achieve it.

.. image:: ../images/L4-visualisation-screenshot.png
    :class: with-border

To understand complicated **rule interactions** like *notwithstanding, subject to*: view the *meta-rule analysis* to see how rules interact. (in development)

----------------
Explaining Legal
----------------

L4's answers are *explainable* and *transparent*.

You can ask *"why?"*: Interactively drill down into every decision. 

(TODO: show output of the Explainable monad)

You can ask *"how?"*: if you state a goal you want to achieve, L4 will outline a course of action.

(TODO: show output of planning engine showing how to traverse the state transition graph to achieve a particular goal.)

--------------------
A Compiler for Legal
--------------------

L4 sanity-checks your programs to detect internal conflicts and loopholes.

The **"formal methods"** components of the L4 toolchain automatically analyze your code for loopholes and inconsistencies.

L4's **unit testing** framework lets you **set up test scenarios** and monitor them as your contracts evolve.

L4's **library** of components makes it easier to **draft legal templates and automatically produce legal documents** for signature.


-------------------
The Web App Builder
-------------------

L4 automatically generates a web app that helps end users explore the logic of your legal code.

.. image:: ../images/web-tool-screenshot.png
   :class: with-border

They can use this tool to understand if a law applies to them, or certain contractual conditions are met.
	   
----------------------------------
L4 can export to  multiple formats
----------------------------------

L4 code can be exported to languages such as Typescript (Javascript), Python, Prolog, and Haskell.

On the roadmap are other languages like OpenFisca, Catala, Epilog, and
Accord. We prioritize these exporters according to demand so if
there's something you want on the list please contact us!

------------------------------------
L4 uses spreadsheets for interaction
------------------------------------

L4 is low-code. You don't have to install VS Code, Emacs, or Vim. The
IDE is Google Sheets: if you can edit a spreadsheet, you can program
in L4.

-----------------------------
L4 contains a package library
-----------------------------

The L4 package library (currently in development) contains useful components such as

- Calendars (knows about holidays, can count business days)
- Money (knows about currencies)
- Corporate (knows about directors, shareholders, meetings, resolutions)
- Investment Agreements (convertible notes, SAFEs, and other instruments)
- Insurance Policies (knows about risks, coverage, and supplementary add-ons)
- Legislation and Regulation (knows about permitting and compliance)

L4 supports Document Assembly
-----------------------------

The contract assembly engine helps you generate a document you can
sign (after running it past a lawyer for code review, of course).

For investment agreements, L4 also generates all the prerequisite
components such as board resolutions and members' resolutions in
writing.

L4's PDF documents embed the code of the L4 contract for forward
compatibility with contract lifecycle management tools.

The L4 package library will soon contain loan agreements, leasing agreements, and investment agreements.

The Semantics of L4
===================

This section outlines the semantic domains that support L4's expressivity and generality.

Boolean Logic
-------------
:keywords:`AND OR NOT UNLESS IF THEN ELSE`

First-Order Logic
-----------------
:keywords:`IS`

Arithmetic
----------
:keywords:`plus minus times divide abs min max <= < > >=`

Object-Oriented Classes and Instances
-------------------------------------
:keywords:`ontology`

Type Checking and Inference
---------------------------
:keywords:`type annotations are optional`

Regulative Rules
----------------
:keywords:`PARTY X … MUST DO … Y`
obligations and communications between parties are represented as state transition systems

Constitutive Rules
------------------
:keywords:`DECIDE X … WHEN Y`

Qualifying Rules
----------------
:keywords:`EVERY X … MUST BE … Y`

Deontic Modals
--------------
:keywords:`MUST MAY SHANT DO`
the language of permission and obligation

Temporal Modals
---------------
:keywords:`BEFORE AFTER BY WITHIN UNTIL`
time is of the essence

Relational Predicates
---------------------
:keywords:`IS NOT`
one thing stands in a certain relation to another

Default Logic
-------------
:keywords:`WHEN OTHERWISE`
exceptions and defaults

Defeasible Logic
----------------
:keywords:`NOTWITHSTANDING, SUBJECT TO`
meta-rule relations

Lambda Calculus
---------------
:keywords:`GIVEN LET DEFINE`

Unit Testing
------------
:keywords:`SCENARIO GIVEN EXPECT`
Partial Evaluation reduces a ruleset to a residual.

Formal Methods
--------------
:keywords:`ASSERT TRACE`
Find loopholes and mistakes in the code

Natural Language Generation
---------------------------
supports the translation of code into multiple natural languages to support interfaces


