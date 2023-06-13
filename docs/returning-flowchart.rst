========================================
Functionally Enhanced Flowcharts and Law
========================================

* `Flowcharts represent both statics and dynamics`_
* `A flowchart's output feeds into a document intended for printing`_
* `Why a functionality enhanced flowchart is preferable`_
* `How software engineers can add functionalities to flowcharts`_

----------------------------------------------
Flowcharts represent both statics and dynamics
----------------------------------------------

People often reach for flowcharts when formalising the law.

People use flowcharts to represent the statics: these are really decision trees.

People use flowcharts to represent the dynamics: these are really state diagrams.

Most flowcharts couple the two representations together.

----------------------------------------------------------------
A flowchart's output feeds into a document intended for printing
----------------------------------------------------------------

Flowcharts tend to be drawn in a simple drawing app, at the level of syntax, not semantics. Flowcharts are drawn with boxes with text and arrows with nearby text.

People often produce a web interview from such a flowchart in a direct and imperative form. Then the output of the interview feeds into a document assembly system. Often, such documents are intended to be finally embodied on paper.

----------------------------------------------------
Why a functionality enhanced flowchart is preferable
----------------------------------------------------

Flowcharts are not the best way to represent decision logic because the availability of user-provided information does not always match the pre-determined order of questions.

This approach is more amenable to automated verification. It can check which edge cases are lacking, and make interfaces interactive by letting users hide irrelevant subtrees.

The end-user can trace their way through the flowchart and examine alternative routes.

------------------------------------------------------------
How software engineers can add functionalities to flowcharts
------------------------------------------------------------

A less imperative and more declarative approach preserves all the features of flowcharts, while adding functionality.

- Statics are extracted to decision tables and diagrams, in DMN / DRD format.

- Dynamics are left in the flowchart, and upgraded with swimlanes and deadlines to look more like BPMN format.

At this point we can reconstruct the original flowchart, but from a less tightly coupled source.

From these elements we can extract an interview.

The results of the interview can be submitted digitally.

Isomorphism can be preserved when the authoritative version of the rules are written in a higher-level language.