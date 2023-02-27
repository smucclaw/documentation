.. _keywords:

###################
Language Quickstart
###################


How to think about legal with L4
================================

L4 helps people express the underlying logic of legal rules.

The big idea is to simplify the complicated, without losing accuracy.

L4 organizes around elementary patterns:

* Decisions
* Deontics and Deadlines
* Definitions

These are the essentials. We compose them to form clauses and
contracts, rules and regulations. When reading a legal text, it is
important to learn to recognize these bones under the skin.

There are a few other supporting elements. We will come to those later.

Disclaimer
----------

**If you are a law student, or a lawyer, or some other member of the legal profession**:
Nothing in this document is more authoritative than what you learned in school and in practice.
School and practice prepare you to work with law *as it currently exists today*.
L4 paints a picture of law as it *could* exist in the future.
As for whether the law *should* take this form, that is something we can discuss at the end of the tutorial.


Decisions
---------

All rules involve decisions in some way.

One rule decides that a person is allowed to buy alcohol if they are
of age.

Another rule decides that an insurance policy should pay out if a
claimed risk is covered.

Another decides that a plan to build a house with six storeys is
not permissible.

.. code-block:: l4

   EVERY Person WHOSE age >= 21 MAY Buy Alcohol
   GIVEN Risk PARTY Insurer MUST Pay WHEN Risk IS Covered
   GIVEN HousePlan DECIDE NOT Permitted WHEN Storeys >= 3

Decisions are central to **constitutive rules**. According to John
Searle, a rule is a *constitutive* rule if, in some context `C`, it
decides that some thing `X` counts as a special thing `Y`. (See what I
did there?) Constitutive rules create *institutional facts*.

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

Deontics
--------

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
`MAY`, then the obligation would by default have existed on Party B.

*Deontics* are central to regulative rules, also called prescriptive
rules.

Regulative rules only apply to legal actors -- parties to a contract,
or persons under the law -- individuals and corporations.

Constitutive vs Prescriptive Rules
----------------------------------

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

"Road tax must be paid by the owner of a vehicle" sounds like a
regulative rule, but it actually unpacks to a constitutive and a
regulative.

Why? Because in an uncommon case, a vehicle owner could counter: "oh,
I don't drive that car, I'm keeping it in storage until I can sell it
to a museum. So I don't have to pay road tax."

So the rule is really two rules:

* For a vehicle to be legally operable on a public road, a valid
  registration must be in force for that vehicle. (Constitutive)
* To obtain a valid registration, the owner of the vehicle must pay
  the appropriate fees. (Regulative)

This gets into *scope goals*. We'll return to that later.

Definitions
-----------

*Definitions* bind names to things. In laws and contracts we are used
to seeing defined terms; these are analogous to *variables* in
programs, which give us ways to refer to concepts and values by name.

NOTE: If you are a law student or a lawyer: this tutorial is not
intended to replace anything taught in law school! L4 simply offers a
structured way to organize legal rules, in a way that can be processed
by a computer. Most people might agree to accept the calculations
performed by the computer. Some might not. If those who do not are in
a position of power, it would be better to rely on your legal training
to tell you what to do.


======================================
Keywords: Declarations and Definitions
======================================

This chapter introduces a handful of L4 keywords. 

-----------------------------------------------------------------
DECLARE and DEFINE, for data types and values, and HAS-Attributes
-----------------------------------------------------------------

DECLARE and DEFINE have to do with data types and values.

If you are familiar with Object-Oriented Programming, you will find the DECLARE and DEFINE concepts familiar.

We use DECLARE to set up our:

    - classes
    - records
    - types
    - schemas
    - ontology
    - templates

We use DEFINE to instantiate those templates with concrete values: the specific variables of a particular agreement.

These declarations and definitions are automatically exported to the programming language of your choice, lessening the burden of programming downstream.

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

    Variable Definition	::=	DEFINE		Value Term		[Type Signature	]	//class-object instantiation				
				HAS		MultiTerm		[Type Signature	]							
						[ ... ]														

Variable definitions with the DEFINE keyword follow the same format as DECLARE.

In Detail
^^^^^^^^^

The syntax for DEFINEs and DECLAREs contains a counterintuitive detail.

A DECLARE rule begins with the name of the type, then the optional supertype.
It goes on to give the names of the attribute fields, then their types.
So far, this ordering is consistent with most other OOPy languages.

For instance, here's how we say it in Typescript:

.. code-block:: typescript

    class Money {
      amount   : Integer;
      currency : Currency;
    }

You might object: "why /class/ and not /interface/?" Fair enough; you can think of it as an interface too.

We would say it in much the same way in L4:

.. code-block:: l4

    DECLARE Money
    HAS amount    IS AN Integer
        currency  IS A  Currency

No surprises so far.

In Typescript, we would instantiate a variable into the class:

.. code-block:: typescript

    let price : Money = {
      amount   : 100,
      currency : usd
    }

In Typescript, as in Javascript, JSON, Python, etc, the name of the attribute is followed by the value. Every language with records does it this way.

In L4, attribute values come first, and are followed by the names!

A DEFINE rule gives the name of the variable, then the type.
The attributes then give the value of the variable, then the name.

.. code-block:: l4

    DEFINE price IS A Money
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
    HAS amount    IS AN Integer
        currency  IS A  Currency
        HAS       unitName     IS A String
                  subUnitName  IS A String
                  subUnitScale IS AN Integer
                  region       IS A String

This desugars to:

.. code-block:: l4

    DECLARE Money
    HAS amount    IS AN Integer
        currency  IS A  Currency

    DECLARE Currency
    HAS unitName     IS A String
        subUnitName  IS A String
        subUnitScale IS AN Integer
        region       IS A String

In technical terms, we might say we have hoisted `Currency` to the top level.

Following the pattern of the original nesting, one might `DEFINE` like so:

.. code-block:: l4

    DEFINE price IS A Money
    HAS 100      IS THE amount
        tnd      IS A   currency
        HAS dinar   IS THE unitName
            millime IS THE subUnitName
            1000    IS THE subUnitScale
            Tunisia IS THE region

This is the philosophy of "inline-ism" at work: we are encountering
the Tunisian dinar for the first time in this rule, and so we define
it as we go. This is a natural reading.

And, as with the `DECLARE`, we hoist it to the top:

Nesting, by the way, goes to the right, immediately below.

A more formalist style might insist on writing these things separately:

.. code-block:: l4

    DEFINE price IS A Money
    HAS 100      IS THE amount
        tnd      IS THE Currency

    DEFINE tnd  IS A Currency
    HAS dinar   IS THE unitName
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

But in the `DEFINE`,

.. code-block:: l4

    DEFINE myFirstLine
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

    DEFINE myFirstLine
    HAS start
        HAS 1 IS THE x
	    2 IS THE y
        end
	HAS 5 IS THE x
	    6 IS THE y
        green IS THE color

So the rules are these:

* DECLARE rules can use as many nested `HAS` as desired. In desugaring, declared attribute fields that have nested sub-attributes are hoisted to top-level. The standard syntax is `HAS fieldname IS A Type`.

* DEFINE rules follow the same nested `HAS` structure as their original `DECLARE`s.

* If a HAS attribute does not have further HAS children beneath it, is always formatted as `HAS label IS THE fieldname`.

* If a HAS attribute does have further HAS children nested within it, and it is given simply as `HAS fieldname`, it is not hoisted; this is usually what you want.

* If a HAS attribute does have further HAS children nested within it, and it is given as `HAS label IS A fieldname`, then `label` is hoisted to top level.

---------------------------------------------------------
BY and WITHIN for Temporal Constraints such as Deadlines
---------------------------------------------------------

The BY and WITHIN keywords set deadlines

.. code-block:: bnf

    Temporal Constraint ::= (BEFORE | AFTER | BY | WITHIN | UNTIL) Temporal Spec				

A regulative rule without a temporal constraint is incomplete. L4 substitutes "EVENTUALLY" but will issue a warning so you are conscious that a deadline is missing.

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

L4 uses HENCE instead of THEN, and LEST instead of ELSE, to connect regulative rules, based on whether the preceding rule was satisfied.

.. code-block:: bnf

    Regulative Connector ::=	(HENCE | LEST)		
                            Rule Label | Regulative Rule				

Individual regulative rules connect with one another to form a graph, or a flowchart, describing a workflow.

----------------------
The Semantics of rules
----------------------

The semantics of a rule are as follows:

.. code-block:: bnf

    [Attribute Constraint   ]							
    [Conditional Constraint ]							
    [Upon Trigger	    ]							
    [HENCE				Rule Label | Regulative Rule ]	
    [LEST				Rule Label | Regulative Rule ]	
    [WHERE				Constitutive Rule							
                                        [   ...     ]                ]	

