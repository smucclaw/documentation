.. _law_understand_l4:

==========================
Using Law to Understand L4
==========================

This explanation page is meant to provide an introduction to L4 assuming you are coming from law and with little to no prior knowledge in programming. There is a more formal language specification found here :ref:`cs_specification`.

This language reference is separated into two parts, with the first part, part A, being an explanation of how to navigate programming. The second part, part B, is an explanation of keywords.

We will constantly refer to the example in "A Manual of Style for Contract Drafting" by kenneth Adams, clause 3.320

"If a Government Body grants to Acme a compulsory license to sell a Product in a country on terms more favorable than those in this article 8, then for as long as that compulsory license is in effect the terms of that compulsory license will control."

------------------------------
Part A: Navigating Programming
------------------------------

~~~~~~~~~~~~~~~~~~~~~~~
keywords in Programming
~~~~~~~~~~~~~~~~~~~~~~~

A keyword is normally made clear through different typography.

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

Conditional clauses modify languages of obligation, discretion, prohibition, and policy. It is not an keyword in Legal English.

When clauses do begin with "If", there is no need to use "then" in the clause, with some exceptions, one of which is in our running example.

"*If* a Government Body grants to Acme a compulsory license to sell a Product in a country on terms more favorable than those in this article 8, *then* for as long as that compulsory license is in effect the terms of that compulsory license will control."

IF...THEN is an important keyword.

Unlike in law, when there is an IF, there must always be a THEN. Programming languages demand that keywords are used in a strictly prescribed way.

IF a Government Body... article 8
THEN for as long as... license will control

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Clauses and Subclauses: Indentations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A clause is a subdivision of a document. We can also have a number of subclauses that modify or expand upon the clause.

For example, our running example comes from clause 3.320, which is clause 3 with subclause 3, subsubclause 2, subsubsubclause 0.

We explicitly number clauses in Law.

The equivalent of a clause in programming is an expression. We can break expressions down into subexpressions.

In L4, we explicitly leave an indentation, which is a fixed amount of spacing from the left aligned text, like this:

If a Government Body... article 8
    THEN for as long as... license will control

In this case, the THEN subexpression is indented with 4 spaces. Indentation is important in L4 and in some other programming languages like Python, just like how clauses and subclausing are important in law.

~~~~~~~~~~~~~~~~~~~~~~~~~~
Types: Categorising Things
~~~~~~~~~~~~~~~~~~~~~~~~~~

In our running clause, Acme is a company. But there are different types of companies, such as a limited company, a private company, or an unlimited company. Beyond companies, there are many different entity types: partnerships, sole proprietors, natural persons, and so on.

These are different company *types*.

What we are doing is categorising a thing (a company) into different categories (limited, private, or unlimited).

You can apply the same reasoning to "license", of which there are many types, like a driving license, or a liquor license. We see that the notion of types does not just include entities, but can apply to attributes and relations and more. 

In L4, you can explicitly declare or define a type with the DECLARE keyword.

A type in L4 is declared through the following statement: 

DECLARE Acme IS A Company.

Notice that the words DECLARE and IS A are fully capitalised because they are keywords that will trigger specific functions in L4's compiler.

If this type definition is not clear enough for your purpose, we can go into a deeper level of granularity.

DECLARE Acme IS A Limited Company.

This will allow you to compare whether your categorisations of legal objects in your head is the same as your colleague's categorisation of legal objects.

~~~~~~~~~~~~~~~~~~~~~~~~~
Variables: Giving Options
~~~~~~~~~~~~~~~~~~~~~~~~~

Let's look at a contract template taken from the `safe financing documents from ycombinator <https://www.ycombinator.com/documents>`_.

"THIS CERTIFIES THAT in exchange for the payment by [Investor Name] (the “Investor”) of $[_____________] (the “Purchase Amount”) on or about [Date of Safe], [Company Name], a [State of Incorporation] corporation (the “Company”), issues to the Investor the right to certain shares of the Company’s Capital Stock, subject to the terms described below

This Safe is one of the forms available at `http://ycombinator.com/documents <http://ycombinator.com/documents>`_ and the Company and the Investor agree that neither one has modified the form, except to fill in blanks and bracketed terms. "

Notice the words in square brackets:

- [Investor Name]
- [_____________]
- [Date of Safe]
- [Company Name]
- [State of Incorporation]

You can, and are supposed to, replace the words inside the square brackets with the name, amount of money, date, company name, and state of incorporation for your specific situation.

The square brackets work the same way as variables in programming. You can name your variables in L4 and in programming. While you can name them with arbitrary letters like "x" and "y", it is good practice to use representative, informative names like "InvestorName". It is generally good practice not to leave spaces when using variable names.

Notice that the variables names in programming get longer the further down the list you go, but they also become more descriptive.

We can combine the idea of variables with the idea of types that we learned in the previous section.

Let's say we have a variable "InvestorName". We intuitively expect that "InvestorName" should be replaced by a name, which is some number of words. If we replaced "InvestorName" with the number 5, like this: "...for the payment by 5 (the "Investor")", we just know that we've replaced "InvestorName" with the wrong type of thing. 

In this case, we've wrongly replaced "InvestorName" with a number rather than some number of words.

~~~~~~~~~~~~~~~~~~~~~~~~~~
Annotations in Programming
~~~~~~~~~~~~~~~~~~~~~~~~~~

When we, as lawyers, are given a contract, we annotate the contract with notes about how the contract works with comments. Importantly, these comments are not part of the contract itself and is ignored when a contract is executed.

In L4, we leave comments with two backward slashes. These comments are not part of the program itself and is ignored when a program is executed.

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

In everyday parlance and to some extent in law, 'And', 'Or', and 'And/Or' are important words in law that carry ambiguity.

- 'And' is usually unambiguous, but there are cases where 'And' is ambiguous, such as in 'John and Mary shall notify Acme'. It can mean either 'John and Mary shall individually notify Acme' or 'John and Mary shall, collectively, notifiy Acme'.

- 'Or' in 'John or Mary shall notify Acme' can be inclusive 'Or', meaning both John and Mary shall notify Acme, or exclusive 'Or', meaning either John or Mary, but not both John and Mary, shall notify Acme.

- 'And/Or' means A or B or both A and B. For example, 'John And/Or Mary shall notify Acme' means "John or Mary or both John and Mary shall notify Acme"

AND and OR are important keywords in programming. 

- There is no AND/OR phrase in programming.

- AND means both clauses on the left and right of AND must be included for the entire clause to be true.

- OR is always inclusive OR except when specifically defined otherwise.