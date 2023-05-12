.. _law_understand_l4:

==========================
Using Law to Understand L4
==========================

This explanation page is for lawyers.

There is a separate L4 language specification for developers here :ref:`cs_specification`.

We will constantly refer to the example in "A Manual of Style for Contract Drafting" by kenneth Adams, clause 3.320

"If a Government Body grants to Acme a compulsory license to sell a Product in a country on terms more favorable than those in this article 8, then for as long as that compulsory license is in effect the terms of that compulsory license will control."

This language reference is separated into two parts, with the first part, part A, being an explanation of how to navigate programming. The second part, part B, is an explanation of keywords.

------------------------------
Part A: Navigating Programming
------------------------------

~~~~~~~~
keywords
~~~~~~~~

**In Law**

Keywords, like "condition" or "warrant", are not explicitly made clear in a contract, although you can find legal definitions of keywords in a dictionary.

**In Programming**

An keyword is normally made clear through different typography.

Some programming languages differentiate keywords from other terms through colour highlighting.

In L4, we differentiate keyword by writing the entire keyword in uppercase.

For example:

- DECLARE is a keyword.
- WHEN is a keyword.
- IS A is an keyword.
- Government Body is not a keyword.
- Acme is not a keyword.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Conditional Clauses: IF...THEN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**In Law**

Conditional clauses modify languages of obligation, discretion, prohibition, and policy. It is not an keyword in Legal English.

When clauses do begin with "If", there is no need to use "then" in the following matrix clause, with some exceptions, one of which is in our running example.

"*If* a Government Body grants to Acme a compulsory license to sell a Product in a country on terms more favorable than those in this article 8, *then* for as long as that compulsory license is in effect the terms of that compulsory license will control."

**In Programming**

IF...THEN is an important keyword.

Unlike in law, when there is an IF, there must always be a THEN.

IF a Government Body... article 8
THEN for as long as... license will control

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Clauses and Subclauses: Indentations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**In Law**

A clause is a subdivision of a document. We can also have a number of subclauses that modify or expand upon the clause.

For example, our running example comes from clause 3.320, which is clause 3 with subclause 3, subsubclause 2, subsubsubclause 0.

We explicitly number clauses in Law.

**In Programming**

The equivalent of a clause in programming is an expression. We can break expressions down into subexpressions.

In L4, we explicitly leave an indentation, which is a fixed amount of spacing from the left aligned text, like this:

If a Government Body... article 8
    THEN for as long as... license will control

In this case, the THEN subexpression is indented with 4 spaces.

~~~~~~~~~~~~~~~~~~~~~~~~~~
Types: Categorising Things
~~~~~~~~~~~~~~~~~~~~~~~~~~

**In Law**

There is no explicit concept of a type, but they are present in law.

"If a Government Body grants to **Acme** a compulsory **license** to sell a Product in a country on terms more favorable than those in this article 8, then for as long as that compulsory license is in effect the terms of that compulsory license will control."

Acme is a company. But there are different types of companies, such as a limited company, a private company, or an unlimited company.

These are different company *types*.

What we are doing is categorising a thing (a company) into different categories (limited, private, or unlimited).

You can apply the same reasoning to "license", of which there are many types, like a driving license, or a liquor license.

**In Programming**

In the same way, we can categorise things when we program.

In L4, you can explicitly declare or define a type with the DECLARE keyword.

For example, in L4 we'll say something like:

DECLARE Acme IS A Company.

If this type definition is not clear enough for your purpose, we can go into a deeper level of granularity.

DECLARE Acme IS A Limited Company.

This will allow you to compare whether your categorisations of legal objects in your head is the same as your colleague's categorisation of legal objects.

~~~~~~~~~~~~~~~~~~~~~~~~~~
Annotations in Programming
~~~~~~~~~~~~~~~~~~~~~~~~~~

**In Law**

When we, as lawyers, are given a contract, we annotate the contract with notes about how the contract works, how it relates to the case we are working on, and so on. One way of doing this is to print out the contract and annotate the contract on the page margins.

Importantly, these annotations are not part of the contract itself and is ignored when a contract is executed.

**In Programming**

The equivalent of an annotation in programming is a comment.

To leave notes about how our program works, why we wrote the program in this or that way, and so on, we leave *comments*.

Like annotations, these comments are not part of the program itself and is ignored when a program is executed.

In L4, we leave comments with two backward slashes.

// This clause affects our case because the Government Body did 
// grant Acme a compulsory license to sell a product in a coutnry on terms more favorable than those.
"If a Government Body grants to Acme a compulsory license to sell a Product in a country on terms more favorable than those in this article 8, then for as long as that compulsory license is in effect the terms of that compulsory license will control."

Notice that you can have multiple lines of comments with two backward slashes. This will help with readability.

----------------
Part B: Keywords
----------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ambiguity in AND and OR in Law and Programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**In Law**

'And', 'Or', and 'And/Or' are important words in law that carry ambiguity.

- 'And' is usually unambiguous, but there are cases where 'And' is ambiguous, such as in 'John and Mary shall notify Acme'. It can mean either 'John and Mary shall individually notify Acme' or 'John and Mary shall, collectively, notifiy Acme'.

- 'Or' in 'John or Mary shall notify Acme' can be inclusive 'Or', meaning both John and Mary shall notify Acme, or exclusive 'Or', meaning either John or Mary, but not both John and Mary, shall notify Acme.

- 'And/Or' means A or B or both A and B. For example, 'John And/Or Mary shall notify Acme' means "John or Mary or both John and Mary shall notify Acme"

**In Programming**

AND and OR are important keywords in programming. 

- There is no AND/OR phrase in programming.

- AND means both clauses on the left and right of AND must be included for the entire clause to be true.

- OR is always inclusive OR except when specifically defined otherwise.



