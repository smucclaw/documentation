.. _eg_motor_insurance:

##############################
Motor Insurance Clause Example
##############################

================================================================
Entity Relations, Ontology Inference, and Predicate Logic Syntax
================================================================

`See the L4 code for this 'Motor Insurance' example <https://docs.google.com/spreadsheets/d/1leBCZhgDsn-Abg2H_OINGGv-8Gpf9mzuX1RR56v0Sss/edit?pli=1#gid=2061671536>`_

This example is taken from the `Compk Language Benchmark <https://docs.google.com/document/d/1BUP-byDd7K9kaK-ulkRDH3lHawiBDcwGI_1VvuxYFdM/edit#heading=h.458tgyo2s290>`_. The example proper begins at "Motor Breakdown Policy".

This example is too long to be reproduced here. Instead, you will find notes on how to read and navigate the example. We hope the previous examples together with the notes below provide enough guidance to read this L4 formalisation of a motor insurance clause.

Remember that you can expand and collapse sections of the L4 encoding through the "+" and "-" signs found to the far left of the spreadsheet.

-------------------------------------------
The Structure of the Motor Insurance Clause
-------------------------------------------

The motor insurance clause is split into four major sections. The L4 formalisation of these sections are aligned with the relevant legal clauses found on the right of the page.

1. § Motor Breakdown Policy
   
 - This line names the policy being formalised.

2. §§ Meaning of Words

 - This section defines the meaning of the terms used in this contract. It is divided into several subsections marked by "§§§". The subsubsections "Excess Satisfied" and "Excess Required" are subsubsections marked by "§§§§". This is the longest part of the formalisation.

3. §§ Section B - Misfuelling

 - This section consists of the conditional clause that determines when and what the insurer pays for.

4. §§ Section C - General Exclusions

 - This section details the situations which the insurer will not pay for.



..
    (Nemo: Everything below is the old stuff. I removed it from this example page on 12 May 2023. I'm keeping it here in case we want to use it again.)
    Entity R1elations, Ontology Inference, and Convenient Syntax for Predicate Logic.

    Concepts introduced:

    1. Combining regulative and constitutive rules

    2. Guards in state transitions

    Keywords introduced:

        - DECIDE
        - UNLESS
        - WHO
        - WHICH
        - WHEN
        - IF
        - TYPICALLY