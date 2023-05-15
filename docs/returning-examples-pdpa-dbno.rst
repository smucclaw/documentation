################################
Data Breach Notification Example
################################

============================
Encoding of Real Legislation
============================

`See the L4 code for this 'PDPA DBNO' example <https://docs.google.com/spreadsheets/d/1leBCZhgDsn-Abg2H_OINGGv-8Gpf9mzuX1RR56v0Sss/edit?pli=1#gid=1779650637>`_

This example is a formalisation of actual legislation, `Singapore's Personal Data Protection Act <https://sso.agc.gov.sg/Act/PDPA2012>`_ (known in this example as PDPA DBNO).

Like the :ref:`eg_motor_insurance`, this example is too long to be reproduced here. Instead, notes will be provided below to help you understand the L4 encoding.

Remember that you can expand and collapse sections of the L4 encoding through the "+" and "-" signs found to the far left of the spreadsheet.

Many of the lines in this example have been commented out with the "//" symbol found on column A. They have been marked by a very light shade of grey to be less intrusive. Remember that anything to the right of a comment is ignored by L4 and is not considered part of the code.

-----------------------
Goal of the L4 encoding
-----------------------

The goal of this encoding is to provide an encoding that will ultimately provide a guide for laypersons to:

1. Know whether a data breach has occurred,
2. Know their obligations and how soon they should act to carry out those obligations.

In this example, the obligation is to notify the "`Personal Data Protection Commission Singapore (PDPC) <https://www.pdpc.gov.sg/>`_".

-----------------------------------------------------
Structure of the L4 encoding of the PDPA DBNO example
-----------------------------------------------------

The PDPA DBNO structure is split into three major sections. The relevant (sub)clauses of the Act have been marked to the left of the L4 encoding, in column E.

1. Phase 1: Assess

 - This section defines what a data breach is and when a data breach has occurred. It has two sections, "§ Assessment", which details who should assess when a data breach occurs, and "§ NDB Qualification", which details what a Notifiable Data Breach (NDB) is.

 - "§ Assessment" has two subsubsections:

   -  "§ PDPC query with demand", which explains that the PDPC can demand an explanation from you,
   -  "§ Respond to PDPC", which explains that you must explain any inaction on your part.

2. Phase 2: Notify

 - This section explains when you have to notify the PDPC and the kinds of events that constitute a notifiable data breach. It has the section "§ Notification", which is divided into five subsections, one of which can be expanded or collapsed:

   - "§§ Notify PDPC", which explains when you have to notify the PDPC,
   - "§§ PDPC prohibit notify individuals", This expandable/collapsable section details unique situations when you cannot notify the people affected by the data breach,
   - "§§ Cannot notify individual", which briefly formalises the rule that you should not notify the people affected by the data breach,
   - "§§ Notify Individuals", which explains that you must notify the people affected by the data breach within 3 days,
   - "§§ Notify and explain", which states what happens when you are late. In this case, you must notify the people affected by the data breach and provide an explanation to the PDPC as to why you were late.

3. § Part 1 of the Schedule

 - This section is a list of situations that detail what type of data breach it is. For example, the data breach could be related to a breach of identifiable data for children, or the data breach could be related to the net worth of an individual.

The sections beneath "§ Part 1 of the Schedule" are commented out and are not run by the LegalSS spreadsheet.

..
    (Nemo: Everything below is the old stuff. I removed it from this example page on 12 May 2023. I'm keeping it here in case we want to use it again.)
    Concepts introduced:

    1. Reference and Expansion

    2. Temporal Keywords

    3. State transitions

    Keywords introduced:

        - DECIDE
        - UNLESS
        - WHO
        - WHICH
        - WHEN
        - IF
        - TYPICALLY

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Petri Net representation of PDPA DBNO
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    We will continue our examination of the PDPA DBNO case with a deep dive into Petri Nets; it is intended to be a Petri Net representation of the PDPA DBNO example.

    Concepts introduced:

    1. Workflow diagrams in detail

    2. BPMN used in industry

    3. Process algebras

    Keywords introduced:

        - HENCE