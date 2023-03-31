.. _keywords:

###################
Language Quickstart
###################


How to think about legal with L4
================================

Legal writing may appear complex, but it is almost entirely composed
from simple elements:

- **decisions**, which deal with yes/no (and sometimes numerical) questions, and
- **deontics**, which deal with the changing obligations of parties over time.
  
L4 gives non-lawyers and computers an easier way to understand
contracts and laws by breaking down complicated legal writing to the
above elements, written in a standard *rule* format. Well-formed rules
can be processed by computer and form the basis for further useful
activity.

The L4 method of analysis and formalization is suitable for laws and
regulations running for hundreds of pages -- and for simple contracts
that can be summed up in a single paragraph.

In a simple example, Bob buys a beer from Alice. There is a legal
minumum age for alcohol purchases. Alice expects to be paid within 30
days.

How might we analyze this using L4? We break it down into *decision*
and *deontic* elements -- and supply the *data* to operate on.

.. list-table::
   :header-rows: 0

   * - :ref:`Decision<Decisions lie at the heart of Constitutive Rules>`
     - Give a yes-or-no answer to a question involving one or more factors.

       | ``DECIDE alcohol purchase IS valid WHEN Buyer age >= 21``

   * - :ref:`Deontics<Deontics and Deadlines lie at the heart of Regulative Rules>`
     - Draw up the rights and obligations of parties, with deadlines.

       | ``PARTY Buyer MUST pay Seller BEFORE 30 days``

(Too bad the name `"D" was already taken <https://en.wikipedia.org/wiki/D_(programming_language)>`_. :-)

These are the essentials of L4. We compose them to form clauses and
contracts, rules and regulations. When reading a legal text, it is
important to learn to recognize these bones under the skin.

If you are tasked with translating an existing piece of legal writing
into L4, you can begin by asking yourself, as you read the text: "what
kind of rule does this paragraph express?" Almost all of the time, the
answer will be one of the above types of rules.

A few other types of rules play supporting roles. The specifics of a
case are represented as `DATA`:

.. list-table::
   :header-rows: 0

   * - :ref:`Data<Data values are concrete>`
     - Set out the specifics of a particular case.

       | ``DATA  Buyer       IS A Natural Person``
       | ``HAS   Bob         IS THE Name``
       | ``"     1970-01-01  IS THE Birthdate``
       | ``DATA  Seller IS A Natural Person``
       | ``HAS   Alice  IS THE Name``

To add rigour, data can be be explicitly structured with
**declarations**:

.. list-table::
   :header-rows: 0

   * - :ref:`Declarations<Declarations are abstract>`
     - give general structure to particular data values.

       | ``DECLARE Natural Person``
       | ``HAS     Name      IS A String``
       | ``"       Birthdate IS A Date``

For example, getting from a birthdate to an age requires a decision
rule, which we will give later. Rules like this apply generally, so
for reusability L4 packages them in library modules that can be
imported.

Scenario rules allow drafters to check their logic against concrete
examples:

.. list-table::
   :header-rows: 0

   * - :ref:`Demonstrations<Demonstrating the rules with Scenarios>`
     - help check if a ruleset is behaving correctly.

       | ``GIVEN Bob age IS 19 EXPECT alcohol purchase IS NOT valid``


Sometimes, legal text includes passages that, technically, go
without saying, but still have to be said for non-technical
reasons. We `DISPLAY` those passages:

.. list-table::
   :header-rows: 0

   * - :ref:`Display Rules<Display rules are useful for boilerplate>`
     - Display text is usually passed through verbatim.

       | ``DISPLAY For the avoidance of doubt, this rule does not apply to the purchase of non-alcoholic drinks.``

Definitions allow us to give short names to things. Those things can
themselves be other rules or simply strings of text for subsequent
human interpretation.
       
.. list-table::
   :header-rows: 0

   * - :ref:`Define<Defined terms are aliases>`
     - Legal texts use defined terms to serve as aliases to longer concepts, and to stand certain concepts in relationship to one another.

       | ``DEFINE Doctor MEANS a registered medical professional``
       | ``DEFINE alcohol purchase INCLUDES beer purchase``

The remainder of this document explores the above rule types.

But first, another "D":

Disclaimer
----------

**If you are a law student, or a lawyer, or some other member of the legal profession**:
Nothing in this document is more authoritative than what you learned in school and in practice.
School and practice prepare you to work with law *as it currently exists today*.
L4 paints a picture of law as it *could* exist in the future.
As for whether the law *should* take this form, that is something we can discuss at the end of the tutorial.



Decisions lie at the heart of Constitutive Rules
------------------------------------------------

All rules involve decisions in some way.

One rule decides that a person is allowed to buy alcohol if they are
of age.

Another rule decides that an insurance policy should pay out if a
claimed risk is covered.

Another decides that a plan to build a house with six storeys is
not permissible.

.. code-block:: l4

   EVERY Person   WHOSE age >= 21   MAY Buy Alcohol
   GIVEN Risk PARTY Insurer MUST Pay   WHEN Risk IS Covered
   GIVEN HousePlan DECIDE NOT Permitted   WHEN Storeys >= 3

Decisions are central to **constitutive rules**. According to John
Searle, a rule is a *constitutive* rule if, in some context `C`, it
decides that some thing `X` counts as a special thing `Y` if certain
requirements `Z` are met. (See what I did there?) Constitutive rules
create *institutional facts*.

A decision can be as simple as first establishing whether a rule
applies at all, and who it applies to.

A student is a prefect if she has been so appointed by the principal.
A car is eligible for an electric-vehicle rebate if it is of a certain
make and model. A person counts as married if they have signed their
name to a particular document before a particular person (well, two
particular persons).

Context matters. In one jurisdiction, a 20-year-old might be allowed
to buy alcohol, but not in another. A student changing schools might
have been a prefect in their old school, but they aren't automatically
a prefect in their new school.

Some scholars like to say that constitutive rules "cannot be broken".
The closest thing to breaking a constitutive or definitional rule
arises when the rule establishes validity: an alcohol purchase is
invalid when the buyer is under 21; but the actual rule-breaking
occurs when the invalid purchase proceeds.

A qualification rule is a special case of a constitutive rule. It
requires that *every* thing that meets certain criteria must also meet
other additional criteria: for example, a building regulation may
require that every door that is an emergency exit must be openable
outwards. Every swimming pool that is outdoors and in the ground must
be fenced and gated. Every car that is sold after a certain year must
meet a certain fuel economy standard.

Decisions often involve *defaults*. Legal writing tends to go from
general to specific: the default cases is stated first, followed by
exceptions. Software programs tend to go the other way: exceptional
cases are written first, followed by the default case. The pattern is
essentially the same, just mirrored.

Deontic Duties lie at the heart of Regulative Rules
---------------------------------------------------

Deontics come in three flavours: obligation, permission, and prohibition.

Alice *must* do something, perform some action: obligation.

Bob *may* do something: permission.

Carol *mustn't* do something: prohibition.

.. code-block:: l4

   PARTY Alice MUST  DO some action
   PARTY Bob   MAY   DO some action HENCE PARTY Barb MUST respond
   PARTY Carol SHANT DO some action   

Permission and prohibition can, `traditionally <https://plato.stanford.edu/entries/logic-deontic/#TradScheModaAnal>`_, be defined in terms of obligation.

How do we redefine prohibition in terms of obligation? By saying that
one is obligated to *not* do the prohibited thing.

.. math::

    Shant(act) \Rightarrow Must (\lnot act)

Permission can also be re-phrased in terms of obligation.

Simply: permission to do something means there is no obligation to not do it.

.. math::

    May(act) \Rightarrow \lnot Must (\lnot act)

More complexly: A legal text could state that Party A `MAY` perform
some action; and if they do, Party B `MUST` respond in some way. Often
this implies that if the text did not explicitly give Party A the
`MAY`, then the obligation would not have existed on Party B.

*Deontics* are central to regulative rules, also called prescriptive
rules.

Regulative rules only apply to legal actors -- parties to a contract,
or persons under the law -- individuals and corporations.

Deadlines go hand-in-hand with Deontics
---------------------------------------

An obligation is nothing without a deadline: things have to happen by a certain time, else do they really have to happen at all?

L4's temporal keywords help define deadlines for regulative rules:

.. code-block:: bnf

    Temporal Constraint ::= (BEFORE | AFTER | BY | WITHIN | UNTIL) Temporal Spec				

A regulative rule without a temporal constraint is incomplete. L4 substitutes "EVENTUALLY" but will issue a warning so you are conscious that a deadline is missing.


Review: Constitutive vs Prescriptive/Regulative Rules
-----------------------------------------------------

Before we get into definitions and declarations, a quick recap of what
we've discussed so far, from a slightly different angle. Let's go over
the two basic types of rules.

A regulative rule says that a *person* **must do**.

A constitutive rule says that a *thing* **must be**.

This is clear when we talk about inanimate objects or actions.

* To be a sandwich, a food item must be a filling surrounded on both sides by bread.
* To be champagne, a wine must be from one of five special viticultural districts in France; otherwise, it's just sparkling wine.
* To be accepted by the court, a document must be formatted in a certain way.

Confusion sometimes arises when the subject of a constitutive rule is a person.

To buy alcohol, a person must be 21 years of age.

To practise law, a person must be called to the bar.

To log in, a person must be in possession of a 2FA authenticator device.

The confusion arises because achieving validity usually requires the
person to take some action first. To be called to the bar, a person
has to do quite a few things first. But to arrive at 21 years of age,
a person just has to hang in there.

Sometimes a "must be" statement is really an indirect version of a
"must do" statement, because there's a "by" involved.
*Taxes must be filed by employed individuals* is really
*Employed individuals must do their taxes.*

We might call those statements "deontics in disguise" -- if you have
ever been exhorted against the use of the passive voice, this is
partly what they were getting at.

Other statements really do lie at the border of constitutive and
regulative rules, and need to be unpacked.

Compliance Rules
^^^^^^^^^^^^^^^^

"No vehicle may be operated whose road tax is not properly paid up"
sounds like a regulative rule, but it actually unpacks to three rules:
a constitutive, a regulative, and a *compliance* rule.

Why? Because in an uncommon case, a vehicle owner could counter: "oh,
that car doesn't get driven, the engine's been taken out and I'm
keeping it in storage until I can sell the chassis to a museum. So I
don't have to pay road tax."

The rule is really three rules:

* Every vehicle that legally operates on a public road must be
  in valid tax-paid status. (Compliance Rule)

* To be valid, road tax must be paid up for the current year.
  (Constitutive)

* Every driver shall not operate any vehicle whose road tax is not paid.
  (Regulative)

Compliance rules and constitutive rules are similar!

Constitutive rules state that an X counts as a Y when it meets certain
criteria. Very often, the Y is simply that it is a *valid*, or
*qualifying*, X in some way.

- A thing is a piece of paper if it is rectangular and thin and is
  made from wood pulp and has a light background.

- A piece of paper is a train ticket if text, formatted in a certain
  way, was printed on that paper by some authorized agent or machine.

- A train ticket is a *valid train ticket* if it matches the train the
  passenger is actually on, and if it matches the passenger -- for
  instance, a youth ticket would be invalid for an adult passenger.

Compliance rules state that *every* X (within a certain scope) must be a Y.

We're still working on the syntax of qualifying rules, but they are
likely to follow the syntax of regulative rules, but with the
mandatory keywords `BE` or `HAVE` instead of `DO`.

Regulative: `PARTY P1 MUST DO pay P2`

Constitutive: `DECIDE ticket IS valid WHEN passenger name IS ticket name`

Compliance: `EVERY passenger on a train MUST BE in possession of a valid ticket OR BE a railway employee in valid uniform`

So when the train conductor walks through the train, they are testing
for compliance. There are two ways to comply: wear a valid uniform or
hold a valid ticket. In legal writing, the notion of "validity" is
often so obvious that it is implicit and goes unsaid; but in L4, we
prefer to be explicit and say it.


Or else what?
^^^^^^^^^^^^^

Regulative rules often carry an implicit "or what?"

If we say: "you must move your car by 8am" the "or what" is: "or it
may get towed, and you will have to pay a fine."

You could ask "or what" again: "and if you don't pay the fine, you may
never get your car back."

This gets into *scope goals*. We'll return to that later.

Data values are concrete
------------------------

Specific cases involve individuals: the buyer and seller are Bob and
Alice, the price is $100, the car is painted pink. These facts are
recorded in `DATA` rules.

`DATA` rules are used when you concretize a particular concrete
template to an instance that is expected to actually be signed.

They give concrete particulars to an abstract template: for instance,
a contract might talk about a Buyer and a Seller in the abstract, and
later particularize those parties in an Annex with name, address, and
identifying numbers. The material in that Annex would be recorded as
`DATA` rules.


Declarations are abstract
-------------------------

Where data values talk about concrete "variables", declarations talk
about abstract "types".

If you're an object-oriented programmer, you can think of a
declaration as a class, and a data value as an instance variable.

If you're a functional programmer, you can think of declarations as
types, and data as values in those types.

If you spend a lot of time with JSON, you can think of declarations as
a schema, and a data value as a JSON object satisfying that schema.

If you have a database background, you can think of a declaration as a
database or table schema, and a data value as a row inserted into
the table.

What are definitions?
---------------------

*Definitions* bind names to things.

In laws and contracts we are used to seeing defined terms; these are
analogous to *aliases* in programs, which give us ways to refer to
concepts and values by name.

Defined terms sometimes "ground out" to a string of words which has
meaning to a human, but not to a computer. Sometimes they represent a
punt: "Doctor means a registered medical professional" is good enough
for the contract to make sense, but anyone relying on that definition
to scrutinize a particular individual claiming to be a doctor may want
to consult the relevant offically approved register just to be sure.
Operationally, such a lookup *may* be facilitated by software, but it
doesn't have to be for the contract itself to work.


Keywords: Declarations and Data
===============================

This chapter introduces a handful of L4 keywords. 

DECLARE and DATA, for data types and values, and HAS-Attributes
---------------------------------------------------------------

DECLARE and DATA have to do with data types and values.

If you are familiar with Object-Oriented Programming, you will find the DECLARE and DATA concepts familiar.

We use DECLARE to set up our:

    - classes
    - records
    - types
    - schemas
    - ontology
    - templates

We use DATA to instantiate those templates with concrete values: the specific variables of a particular agreement.

These declarations and data values are automatically exported to the programming language of your choice, lessening the burden of programming downstream.

Consider the following code

.. code-block:: bnf

    Type Declaration	::=		DECLARE			MultiTerm			  [Type Signature]	
					[Has-Attribute  ]								
					[       ...     ]							
																		
    Has-Attribute	::=		HAS			MultiTerm			  [Type Signature]	
					[       ...     ]
					[Has-Attribute	]	

This syntax rule means you can have multiple HAS-Attributes, listed on subsequent lines. For convenience, only the first HAS keyword is necessary; subsequent lines don't need it.

HAS-Attributes can nest, such that one record declaration can contain another.
For example:

.. code-block:: bnf

    Variable       	::=	DATA		Value Term		[Type Signature	]	//class-object instantiation				
				HAS		MultiTerm		[Type Signature	]							
						[ ... ]														

Variable instantiations with the DATA keyword follow the same format as DECLARE.

In Detail
^^^^^^^^^

The syntax for DECLAREs and DATA contains a counterintuitive detail.

A DECLARE rule begins with the name of the type, then the optional supertype.
It goes on to give the names of the attribute fields, then their types.
So far, this ordering is consistent with most other OOPy languages.

For instance, here's how we say it in Typescript:

.. code-block:: typescript

    class Money {
      amount   : number;
      currency : Currency;
    }

You might object: "why /class/ and not /interface/?" Fair enough; you can think of it as an interface too.

We would say it in much the same way in L4:

.. code-block:: l4

    DECLARE Money
    HAS amount    IS A Number
        currency  IS A Currency

No surprises so far.

In Typescript, we would instantiate a variable into the class:

.. code-block:: typescript

    let price : Money = {
      amount   : 100,
      currency : usd
    }

In Typescript, as in Javascript, JSON, Python, etc, the name of the attribute is followed by the value. Every language with records or dictionaries does it this way.

In L4, attribute values come first, and are followed by the names!

A DATA rule gives the name of the variable, then the type.
The attributes then give the value of the variable, then the name.

.. code-block:: l4

    DATA price IS A Money
    HAS 100      IS THE amount
        USD      IS THE currency

This probably feels backward to what you are used to.

There is a good reason for this: conceptually, the specialization/subtyping "hierarchy" goes something like
superclass -> subclass -> instance record -> attribute name -> attribute value.

Arguably, if the type of ~amount~ is ~Integer~, then the "type" of 100 is ~amount~.

Internal dev note: In practice, this means the Interpreter,
PrettyPrinter, and transpilers need be careful about destructuring
TypeSigs, because your instincts may not serve you in L4.

Second issue: records can continue to nest.

.. code-block:: l4

    DECLARE Money
    HAS amount    IS A Number
        currency  IS A Currency
        HAS       unitName     IS A String
                  subUnitName  IS A String
                  subUnitScale IS AN Integer
                  region       IS A String

This desugars to:

.. code-block:: l4

    DECLARE Money
    HAS amount    IS A Number
        currency  IS A Currency

    DECLARE Currency
    HAS unitName     IS A String
        subUnitName  IS A String
        subUnitScale IS AN Integer
        region       IS A String

In technical terms, we might say we have hoisted `Currency` to the top level.

Following the pattern of the original nesting, one might `DATA` like so:

.. code-block:: l4

    DATA price   IS A Money
    HAS  100      IS THE amount
         tnd      IS A   currency
         HAS dinar   IS THE unitName
             millime IS THE subUnitName
             1000    IS THE subUnitScale
             Tunisia IS THE region

This is the philosophy of "inline-ism" at work: we are encountering
the Tunisian dinar for the first time in this rule, and so we define
it as we go. This is a natural reading.

And, as with the `DECLARE`, we hoist it to the top. A `DATA` rule is
scoped to the entire L4 module in which it is defined.

Nesting, by the way, goes to the right, immediately below.

A more formalist style might insist on writing these things separately:

.. code-block:: l4

    DATA price    IS A   Money
    HAS  100      IS THE amount
         tnd      IS THE Currency

    DATA tnd     IS A   Currency
    HAS  dinar   IS THE unitName
         millime IS THE subUnitName
         1000    IS THE subUnitScale
         Tunisia IS THE region

Hoisting the `tnd` to the top-level makes sense. As globals go,
currencies are long-lived enough to stay stable over the course of a
particular L4 specification.

Indeed, the L4 compiler does desugar nested definitions that are
phrased in the above form.

Now we know a top-level global value: `tnd`, which we can reuse later.

But what about nesting sub-records that are not to be hoisted?

Suppose we have a line type:

.. code-block:: l4

    DECLARE line
    HAS start IS A Point
        HAS x IS A Number
            y IS A Number
	end   IS A Point
        color IS A String

From this `DECLARE`, we hoist `Point` to top-level:
	
.. code-block:: l4

    DECLARE line
    HAS start IS A Point
	end   IS A Point
        color IS A String

    DECLARE Point
    HAS x IS A Number
        y IS A Number

But in the `DATA`,

.. code-block:: l4

    DATA myFirstLine
    HAS p1    IS THE start
        HAS 1 IS THE x
	    2 IS THE y
        p2    IS THE end
	HAS 5 IS THE x
	    6 IS THE y
	green IS THE color

We don't want to hoist `p1` and `p2`, the `start` and the `end`, to top-level; that would make no sense.

(Green doesn't get hoisted because `green` it has no sub-attributes.)

Solution: leave the `start` and `end` fields unnamed. We remove the `p1` and `p2` bindings:

.. code-block:: l4

    DATA myFirstLine
    HAS start
        HAS 1 IS THE x
	    2 IS THE y
        end
	HAS 5 IS THE x
	    6 IS THE y
        green IS THE color

So the rules are these:

* DECLARE rules can use as many nested `HAS` as desired. In desugaring, declared attribute fields that have nested sub-attributes are hoisted to top-level. The standard syntax is `HAS fieldname IS A Type`.

* DATA rules follow the same nested `HAS` structure as their original `DECLARE`s.

* If a HAS attribute does not have further HAS children beneath it, is always formatted as `HAS label IS THE fieldname`.

* If a HAS attribute does have further HAS children nested within it, and it is given simply as `HAS fieldname`, it is not hoisted; this is usually what you want.

* If a HAS attribute does have further HAS children nested within it, and it is given as `HAS label IS A fieldname`, then `label` is hoisted to top level.


Further Syntactic Sugar
^^^^^^^^^^^^^^^^^^^^^^^

In a future version of the language we will support this as well.

.. code-block:: l4

    DATA myFirstLine
    HAS  start x 1 y 2
         end   x 5 y 6
         color green

We might entertain a RelationalPredicate form where instead of saying `IS A`
we say `IS`: 
	
.. code-block:: l4

    DATA myFirstLine
    HAS  start x IS 1
	       y IS 2
         end   x IS 5
               y IS 6
         color   IS green

----------------------------------------------------
MUST, SHANT, and MAY for obligations and permissions
----------------------------------------------------

Laws and contracts impose *obligations* and *prohibitions* on persons, and grant *permissions*. These ideas are central to *deontic logic*, and underlie L4's keywords MUST, SHANT, and MAY, respectively.

.. code-block:: bnf
    
    Deontic Keyword ::= (MUST | MAY | SHANT)	

Within the context of a single rule, these deontic keywords specify different consequences for the satisfaction or violation of the rule.

-------------------------------------------
FULFILLED and BREACH for consequences in L4
-------------------------------------------

The two fundamental consequences in L4 are FULFILLED and BREACH.

.. code-block:: bnf

                    If the actor does not perform the action by the deadline            If the actor performs the action by the deadline								
        MUST		    BREACHED                                                            		    FULFILLED								
        SHANT		    FULFILLED										    BREACHED								
        MAY		    FULFILLED										    FULFILLED								

We observe that a MAY rule is permissive: if you do it, fine! If you don't, fine!

L4's workflow diagrams follow a convention: a rule that is satisfied proceeds to the bottom right, while a rule that is violated proceeds to the bottom left. The ""happy path"" therefore runs along the right side of a diagram.

A MAY rule shows action to the right, and inaction to the left.

------------------------------------------------------------------
HENCE and LEST for regulative rules and connecting blocks of code
------------------------------------------------------------------

Ordinary programming languages use the IF … THEN … ELSE construct to connect blocks of code, based on whether the conditions in the IF were met.

L4 uses THUS instead of THEN, and LEST instead of ELSE, to connect regulative rules, based on whether the preceding rule was satisfied.

.. code-block:: bnf

    Regulative Connector ::=	(THUS | LEST)		
                                 Rule Label | Regulative Rule				

Individual regulative rules connect with one another to form a graph, or a flowchart, describing a workflow.

Putting it all together
=======================

Enough theory. Let's explore encoding your first contract!

