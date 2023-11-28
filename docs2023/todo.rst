####
Pain Points with current Documentation
####


####
Documentation Component: Quickstart and Tutorial
####

Getting the spreadsheet working.

"But I hate spreadsheets!" --> link to Future Directions, VS Code.

####
Documentation Component: For the Rule Engineer
####

Introduction to encoding existing rules to produce a rule engine that can be queried via API.

See how the Vue web app coems up.


####
Documentation Component: For the Law Student
####

Introduction to structured thinking and how software can help identify and eliminate ambiguities.


####
Documentation Component: For the Computer Scientist
####

L4 is a specification language with translational semantics.

This section discusses the semantics and logic of L4.

Partial evaluation enables the runtime to reduce the size of the interview dynamically.


####
Documentation Component: Language Reference
####

Syntax Guide

- Propositionals and Booleans: 20 Questions, Truth or Dare
- Predicates and Arithmetic: Show Me The Money
- Contracts as State Transition Systems: Temporal, Deontic, and Epistemic Modals


####
Proposed New Documentation Structure
####

cloning the spreadsheet and getting the L4 menu item and the sidebar to be visible at all

Representing things in L4 (the "input" track)
representing propositional logic in L4 (Booleans, AND/OR)
representing predicate logic in L4 (Numbers and Booleans, + - * / any all sum product ? : )
representing modal logic in L4 (state transitions, deontics (must/may/shant), temporal (deadlines), transitions (if satisfied, if not satisfied), a theory of causation)
representing ontology in L4 (classes, instances, methods)
representing a bit of legislation / regulation (PDPA)
representing an insurance agreement (PAU)
representing a financial agreement (Flood & Goodenough)

The next section can be about getting useful things out of L4 (the "output" track)
auto-generation of a web app
auto-generation of boolean circuit diagrams
auto-generation of an AST evaluation tree/graph
auto-generation of software libraries representing the legal logic as operational business logic
auto-generation of natural language
model checking for property violations
tests: property based testing, specific scenario tests, unit tests
useful compiler warnings and error messages

I would propose that a quickstart guide could cover part 1 of each of the above tracks:
you have gotten your feet wet with L4 and can see the value of doing things the L4 way
as an "end of chapter exercise", you were able to tweak an existing rule to match a revised specification
as an "end of chapter exercise", you were able to write a new rule from scratch and use the tooling to support that
as an "end of chapter exercise", you were able to get the system to build a new Vue web app and run it

One additional track, the "internals" track for developers


####
Future Directions
####

If you prefer VS Code

