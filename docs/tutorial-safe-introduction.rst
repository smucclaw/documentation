########################
1. Tutorial Introduction
########################

This tutorial is composed of six parts, one introduction, four pages corresponding to the four discrete events that can happen in the contract, and a final page putting the contract together:

1. Introduction (This page)
2. Equity Financing
3. Liquidity Event
4. Dissolution Event
5. Liquidation Priority
6. Putting the contract together

===================================================
Encoding a SAFE: Simple Agreement for Future Equity
===================================================

In this tutorial, we will guide you in encoding a commonly used contract template, a Simple Agreement for Future Equity (SAFE).

We will be using one of the `contract templates found in the ycombinator website <https://www.ycombinator.com/documents>`_.

Any of the SAFE documents will do, since the template is the same. For this tutorial, we will refer to the first document, "`Safe: Valuation Cap, no Discount <https://www.ycombinator.com/assets/ycdc/Postmoney%20Safe%20-%20Valuation%20Cap%20Only%20-%20FINAL-f2a64add6d21039ab347ee2e7194141a4239e364ffed54bad0fe9cf623bf1691.docx>`_". This is a link that will download a Microsoft Word .docx file into your computer.

=========================
The Structure of the SAFE
=========================

The SAFE has five parts to it:

1. Events, which details the consequences when certain conditions are met,
2. Definitions, which contains the definitions of terms used in this contract template,
3. Company Representations,
4. Investor Representations,
5. Miscellaneous.

As of May 2023, we will not be encoding sections 3, 4, and 5 in this tutorial.

======================
Events that can happen
======================

There are four events or conditions that lead to obligations or consequences being placed on certain parties.

1. Equity Financing,
2. Liquidity Event,
3. Dissolution Event,
4. Liquidation Priority.

We will be exploring these events in depth in their respective pages.

===========================
Method of encoding the SAFE
===========================

We will follow a set of steps that are an expansion of the steps we find in :ref:`eg_mustsing`

1. Read the contract,
2. Break the contract up into parts,
3. Encode the definitions into L4,
4. Encode the events into L4.

