.. _law_cheatsheet:

===================================================
Terms of Art in Programming: A Translation into Law
===================================================

This cheatsheet is for lawyers.

There is a separate cheatsheet for computer scientists here :ref:`cs_cheatsheet`.

We will constantly refer to the example in "A Manual of Style for Contract Drafting" by kenneth Adams, clause 3.320

"If a Government Body grants to Acme a compulsory license to sell a Product in a country on terms more favorable than those in this article 8, then for as long as that compulsory license is in effect the terms of that compulsory license will control."

-----------------------
Expressing Terms of Art
-----------------------

**In Law**
Terms of Art are not explicitly made clear in law.

**In Programming**
A Term of Art is normally made clear through different typography.

Some programming languages differentiate terms of art from other terms through colour highlighting.

In L4, we differentiate terms of art by writing the entire term of art in uppercase.

For example:

- DECLARE is a Term of Art.
- WHEN is a Term of Art.
- Government Body is not a Term of Art.
- Acme is not a Term of Art.

------------------------------
Conditional Clauses: IF...THEN
------------------------------

**In Law**
Conditional clauses modify languages of obligation, discretion, prohibition, and policy. It is not a term of art in Legal English.

When clauses do begin with "If", there is no need to use "then" in the following matrix clause, with some exceptions, one of which is in our running example.

"*If* a Government Body grants to Acme a compulsory license to sell a Product in a country on terms more favorable than those in this article 8, *then* for as long as that compulsory license is in effect the terms of that compulsory license will control."

**In Programming**
IF...THEN is an important term of art. 

Unlike in law, when there is an IF, there must always be a THEN.

IF a Government Body... article 8
THEN for as long as... license will control

------------------------------------
Clauses and Subclauses: Indentations
------------------------------------

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

--------------------------
Types: Categorising Things
--------------------------

**In Law**
There is no explicit concept of a type, but they are present in law.

"If a Government Body grants to **Acme** a compulsory **license** to sell a Product in a country on terms more favorable than those in this article 8, then for as long as that compulsory license is in effect the terms of that compulsory license will control."

Acme is a company. But there are different types of companies, such as a limited company, a private company, or an unlimited company.

In other words, these are different company *types*.

What we are doing is categorising a thing (here a company) into different categories (limited, private, or unlimited).

You can apply the same reasoning to "license", of which there are many types, like a driving license, or a liquor license.

**In Programming**
In the same way, we can categorise things when we program.

In L4, you can explicitly declare or define a type with the DECLARE term of art.

For example, in L4 we'll say something like:

DECLARE Acme IS A Company.

If this type definition is not clear enough for your purpose, we can go into a deeper level of granularity.

DECLARE Acme IS A Limited Company.

This will allow you to compare whether your categorisations of legal objects in your head is the same as your colleague's categorisation of legal objects.

--------------------------
Annotations in Programming
--------------------------

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

-----------------------------------
Defining AND in Law and Programming
-----------------------------------