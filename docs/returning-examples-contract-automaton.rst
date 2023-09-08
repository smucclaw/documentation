################################
3. Contract As Automaton Example
################################

=================================================
Events & Consequences, Obligations vs Permissions
=================================================

`See the L4 Code for this 'Contract As Automaton' example <https://docs.google.com/spreadsheets/d/1leBCZhgDsn-Abg2H_OINGGv-8Gpf9mzuX1RR56v0Sss/edit?pli=1#gid=2000125343>`_

In the :ref:`eg_rodent`, we learned that we can use L4 to formalise a rule. 

The rule was just about short enough to formalise without causing too much mental strain. But what happens when you need to formalise even longer rules, or rules with multiple sections that repeatedly use the same terms and rules? 

This Contract as Automaton example will tackle this issue and teach you how to define terms and rules so that they can be inserted repeatedly in the main formalisation.

Our running example is a loan contract. A loan is repaid in two instalments. The borrower has to stay out of trouble. 

The example comes from a `paper by Mark D. Flood and Oliver R. Goodenough <https://link.springer.com/epdf/10.1007/s10506-021-09300-9>`_, pages 5 and 6. 

-------------------------------------------------
Loan Agreement template and contract commencement
-------------------------------------------------

Consider the following section of the example:

**The Loan**

At the request of Borrower, to be given on June 1, 2014, Lender will advance $1,000 to Borrower no later than June 2, 2014. If Borrower does not make such a request, this agreement will terminate.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Explicitly stating abstract concepts with the DECLARE and HAS keywords
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We need to explicitly state the abstract concepts that are needed to formalise this contract in L4. In this case, we need the concept of a 'loan'. In L4, we can define a 'loan' like this:

.. csv-table::

    "DECLARE", "Loan", "IS AN", "Agreement"
    "HAS", "Lender", "IS A", "Person"
    , "Borrower", "IS A", "Person"
    , "Closing", "IS A", "Date"
    , "Principal", "IS A", "Money"

We can split this table into two parts.

The first part consists only of the first row that has "DECLARE... Agreement".

The second part consists of the rest of the rows, "HAS... Money".

First, we explictly state, by declaring, an abstract thing called a 'loan', and that this 'loan' is an 'agreement'. We chose not to explicitly declare what an 'agreement' is, but we could do so if needed.

Second, we explicitly state that something is a 'loan' only if it contains the items stated after the HAS keyword. In this example, only if there is a:

- 'Lender', who is a person, 
- 'Borrower', who is also a person, 
- 'Closing', that is a date,
- 'Principal', that is some amount of money...

...can we consider something a 'loan'.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Creating objects that are a kind of abstract concept with the DEFINE keyword
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We now have a rigorous definition of an abstract idea called a 'loan'. But all we have now is this one abstract idea. In other words, there is currently no concrete object that is a 'loan'.

Let's create such a concrete object using the DEFINE keyword.

.. csv-table::

    "DEFINE", "F_and_G", "IS A", "Loan"
    "HAS", "Mark", "IS THE", "Lender"
    , "Oliver", "IS THE", "Borrower"
    , "1 June 2014", "IS THE", "Closing"
    , "$1000", "IS THE", "Principal"

Similarly, we can split this table into two parts.

The first part consists only of the first row that has "DEFINE... Loan".

The second part consists of the rest of the rows, "HAS... Principal".

Notice that the definition of a concrete object follows the same pattern as when we declare an abstract idea.

First, we explicitly state, by defining, a concrete thing called an "F_and_G", and that this "F_and_G" is a 'loan'.

Second, we explicitly state that "F_and_G" has the following items:

- "Mark", who is the Lender
- "Oliver", who is the Borrower
- "1 June 2014", which is a Closing (date)
- "$1000", which is the Principal (money)

This "F_and_G" object satisfies the requirements to be a 'loan', and is therefore a 'loan'.

---------------------------------------
Repeated use of defined terms and rules
---------------------------------------

This example shows how defined terms and rules can be defined separately and used in other rules.

In this case, *Repayment* is defined in a separate section and used in the main definition of the condition that needs to be fulfilled.

This example uses a slightly simplified example from the LegalSS spreadsheet and does not consider "§ Contract Commencement" on lines 41-48.

.. csv-table:: Condition to trigger Repayment

    "§", "*Condition*"
    "PARTY", "Lender"
    "MUST", "remit principal"
    "", "in the amount of $1000"
    "", "to Borrower"
    "WITHIN", "1 day"
    "HENCE", "*Repayment*"

The condition above says that the lender must remit a principal of $1000 to the Borrower within one day, or else (hence) *Repayment* will be triggered.

The "§" symbol is a section symbol which gives a name to the L4 section below the "§" symbol.

In this example, *Repayment* is defined as follows:

.. csv-table:: Definition of Repayment

    "§§", "*Repayment*"
    , "Repayment"
    "MEANS", "Main - Repay in two halves"
    "AND", "Side - Keep taxes paid"

The definition of *Repayment* above says that the borrower has to repay the principal in two halves while also keeping their taxes paid.

Notice the use of the "§" symbol again, but this time with two of them together, "§§". This means that this is a subsection, like a clause and subclause in law. If we follow the analogy, then "§" is, say, section 1, and "§§" is section 1.1.

In this case, "§§" means that the L4 section beneath "§§" can be inserted into any L4 section that has a "§" label.

---------------------------------------------------
The differences between DECIDE, DECLARE, and DEFINE
---------------------------------------------------

- DECIDE is where you state explicitly what format you've chosen to formalise. 

    In the :ref:`eg_rodent`, we decided to formalise a positive version of the contract, telling others that "the loss or damage is covered if..." instead of "the loss or damage is not covered if...".

- DECLARE is where you state explicitly what abstract concepts that are needed in formalising the contract. In this example, we need a concept of a 'loan', which is abstract because the idea of a 'loan' is a mental idea. But what exactly is a 'loan'?

    In this example, something is a 'loan' when there is a 'Lender' that is a person, a 'Borrower' that is a person, a 'Closing' that is a Date, and a 'Principal' that is Money.

- DEFINE is where you state explicitly a collection of 'stuff' is actually a type of abstract concept. 

    In this example, the "stuff" is something called an "F_and_G" which is a 'loan' type. This "F_and_G" is a collection of 'stuff' you can point to, in this case, a "Mark" which is a Lender, an "Oliver" which is a Borrower, a "1 June 2014" which is a Closing, and "$1000" which is a Principal amount.


..
    (Nemo: Everything below is the old stuff. I removed it from this example page on 12 May 2023. I'm keeping it here in case we want to use it again.)
    Concepts introduced:

    1. Events and consequences

    2. Obligations vs permissions

    3. Process workflow diagrams

    Keywords introduced:

        - DECLARE
        - DEFINE
        - HAS
        - IS A
        - DO
        - HENCE
        - LEST
        - MAY
        - BY
        - WITHIN

    Some of the earliest written agreements, carved in stone millennia ago, deal with the lending of property. Following in this tradition, this chapter formalizes a simple financial agreement in L4. 

    The ruleset weaves multiple regulative rules together, in series and in parallel. It shows how a "flowchart"-style diagram is automatically generated from the ruleset.
    Such diagrams give people an alternative way to understand legal documents: visually instead of textually.

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Declarations and Definitions
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This chapter introduces a handful of keywords. DECLARE and DEFINE have to do with data types and values.

    If you are familiar with Object-Oriented Programming, from languages like Python, Java, C++, or Javascript, you will find the DECLARE and DEFINE concepts familiar.

    We use DECLARE to set up our classes, our records, our types, our schemas, our ontology, our templates.

    We use DEFINE to instantiate those templates with concrete values: the specific variables of a particular agreement.

    These declarations and definitions are automatically exported to the programming language of your choice, lessening the burden of programming downstream. Some call this "model-driven engineering"; others, "low-code".

    .. code-block:: bnf

        Type Declaration ::= DECLARE    MultiTerm   [Type Signature]	
                            [   Has-Attribute       ]
                            [       ...             ]								
                                                                            
        Has-Attribute    ::= HAS        MultiTerm   [Type Signature]	
                            [   ...                 ]
                            [   Has-Attribute       ]								

    This syntax rule means you can have multiple HAS-Attributes, listed on subsequent lines. For convenience, only the first HAS keyword is necessary; subsequent lines don't need it. 

    HAS-Attributes can nest, such that one record declaration can contain another.
    For example:

    .. code-block:: bnf

        DECLARE     Point								
        HAS         position x          IS A        Number			
                    position y          IS A        Number			
                    details             IS A        PointDetail			
                    HAS	color       IS ONE OF   Red Green Blue
                        value       IS A        Number			
                        onHover     IS A        String			

    We'll talk more about the elementary data-types of L4 later: sum types, product types, lists, and dictionaries. We'll also talk about type inference and type checking.

    .. code-block:: bnf

        Variable Definition ::= DEFINE      Value Term  [Type Signature]    // class-object instantiation
                                HAS         MultiTerm   [Type Signature]			
                                            [ ... ]										

    Variable definitions with the DEFINE keyword follow the same format as DECLARE.

    ~~~~~~~~~
    Deadlines
    ~~~~~~~~~

    This chapter also introduces temporal constraints: the BY and WITHIN keywords set deadlines.

    .. code-block:: bnf

        Temporal Constraint ::= (BEFORE | AFTER | BY | WITHIN | UNTIL)  Temporal Spec		

    A regulative rule without a temporal constraint is incomplete. L4 substitutes "EVENTUALLY" but will issue a warning so you are conscious that a deadline is missing.

    ~~~~~~~~
    Deontics
    ~~~~~~~~

    Laws and contracts impose obligations and prohibitions on persons, and grant permissions.

    These ideas are central to deontic logic, and underlie L4's keywords MUST, SHANT, and MAY, respectively.

    .. code-block:: bnf

        Deontic Keyword ::= MUST | MAY | SHANT

    Within the context of a single rule, these deontic keywords specify different consequences for the satisfaction or violation of the rule.

    The two fundamental consequences in L4 are FULFILLED and BREACH.

    .. code-block:: bnf

                If the actor does not perform the action 
                by the deadline                             If the actor performs 
                                                            the action by the deadline	
                                    
        MUST        BREACHED                                FULFILLED	
        SHANT       FULFILLED                               BREACHED	
        MAY	        FULFILLED                               FULFILLED	

    We observe that a MAY rule is permissive: if you do it, fine! If you don't, fine!

    l4's workflow diagrams follow a convention: a rule that is satisfied proceeds to the bottom right, while a rule that is violated proceeds to the bottom left. The "happy path" therefore runs along the right side of a diagram. A MAY rule shows action to the right, and inaction to the left.

    ~~~~~~~~~~~
    Connections
    ~~~~~~~~~~~

    Ordinary programming languages use the IF ... THEN ... ELSE construct to connect blocks of code, based on whether the conditions in the IF were met.
    L4 uses HENCE instead of THEN, and LEST instead of ELSE, to connect regulative rules, based on whether the preceding rule was satisfied.

    .. code-block:: bnf

        Regulative Connector ::= HENCE | LEST   Rule Label | Regulative Rule

    Individual regulative rules connect with one another to form a graph, or a flowchart, describing a workflow.

    What are the semantics of a rule?

    .. code-block:: bnf

        [Attribute Constraint               ]						
        [Conditional Constraint             ]						
        [Upon Trigger                       ]						
        [HENCE  Rule Label | Regulative Rule]
        [LEST   Rule Label | Regulative Rule]
        [WHERE  Constitutive Rule
                [ ... ]                     ]