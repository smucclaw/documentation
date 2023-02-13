.. _keywords:

######################
Language Specification
######################


How to think about legal wtih L4
================================

L4 offers a method for formalizing legal concepts into logic borrowed from computer science.

The essence of the method is to simplify the complicated, without losing accuracy.

Simplification means breaking things down to their elements, and then building them back up in a structured way.

L4 breaks legal writing down to the following elementary patterns:

Decisions.

Deontics.

Definitions.

These are the essentials. We compose them to form rules; clauses; entire contracts; regulations; legislation.

There are a few other elements, which arise less frequently. We will come to those later.

Let's start with decisions.

All rules involve decisions in some way.

One rule decides that a person is allowed to buy alcohol if they are
of age.

Another rule decides that an insurance policy should pay out if a
covered risk is claimed.

Another decides that a plan to build a house with a six-meter roof is
not permissible.

Decisions are central to **constitutive rules**. A rule is a
*constitutive* rule if it determines that a thing counts as a special
thing. Constitutive rules create *institutional facts*.

A student is a prefect if she has been appointed as one by the
principal. A person counts as married if they have signed their name
to a particular document before a particular person. A car is eligible
for an electric-vehicle rebate if it is of a certain make and model. A
person is eligible to buy alcohol if they have been born before a
certain date. A snack is Kosher for Passover if it was made without
certain ingredients.

A qualification rule is a special case of a constitutive rule. It
requires that every thing within a certain scope must be a certain
way: for example, a building regulation may require that every
emergency exit door must open outwards. Every swimming pool must be
fenced and gated. Every car must be equipped with seatbelts.

Decisions often involve *defaults*. Legal writing tends to go from
general to specific: the default cases is stated first, followed by
exceptions. Software programs tend to go the other way: exceptional
cases are written first, followed by the default case. The pattern is
essentially the same, just mirrored.

*Deontics* refer to rules that impose obligations (or grant permissions) on certain parties.

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

