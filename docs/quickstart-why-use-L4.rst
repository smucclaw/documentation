.. _tour_of_L4:

###########
Why use L4?
###########

**The L4 DSL stack improves access to justice and reduces the cost of
developing legal software by giving non-lawyers a "low-code" way to
explore and produce legal "programs".**

----------------------------------------------------------
L4 helps people **understand** complicated legal documents
----------------------------------------------------------

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

-----------------------------------------------------
L4 helps large enterprises **manage** their contracts
-----------------------------------------------------

Enterprise users can integrate L4 into their existing **contract
lifecycle management** systems to support more sophisticated "what
if?" queries than their CLM databases allow.

----------------------------------------------------
L4 helps governments **streamline** service delivery
----------------------------------------------------

Government agencies innovating with "Rules as Code" can use L4 basis
for automating the generation of citizen-facing web applications and
chatbots.

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

The "formal methods" components of the L4 toolchain automatically analyzes your program for loopholes and inconsistencies.

L4's unit test framework lets you set up test scenarios and monitor them as your contracts evolve.

L4's library of components makes it easier to **draft legal templates and automatically produce legal documents** for signature.


-----------------------
L4 generates a web tool
-----------------------

L4 automatically generates a web app that helps end users explore the logic of your "legal program".

.. image:: ../images/web-tool-screenshot.png
   :class: with-border

-------------------------------------------------------
L4's diagram ouput can be converted to multiple formats
-------------------------------------------------------
The diagrammatic output can be converted to a language you need such as Haskell.

------------------------------------
L4 uses spreadsheets for interaction
------------------------------------

L4 uses a spreadsheet interface to allow lawyers to interact with L4 in an environment that they are comfortable in.

-----------------------------
L4 contains a package library
-----------------------------

The L4 package library contains encodings of insurance policies based on those offered by major insurers. 

In addition to contracts, L4's package library also contains encodings of legislation and regulation in the areas of data privacy and building permission.

The available contracts allows you to generate a document you can sign after running it past a lawyer for review.

The L4 package library will soon contain loan agreements, leasing agreements, and investment agreements.
