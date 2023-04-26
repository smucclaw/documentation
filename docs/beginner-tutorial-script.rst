============================
Introductory Tutorial Script
============================

    :Author: Wong Meng Weng



Hello
-----

Hello, my name is Meng and

I'm here to teach the basics of L4,

which is a domain-specific language for law

that's meant to help end-users, in the real world,

better handle the complexity of legal regulations and agreements,

by building a "low-code" programming language

that humans can write and computers can read.

It looks like this.

(screenshot: must sing)

That's an example of a very simple rule: everyone who walks and eats or drinks must sing.

A real world example might look like this.

(screenshot: motor insurance contract)

This is a contract for motor insurance.

What about a piece of legislation?

(screenshot: PDPA)

All of these examples are programs written in L4.

Value Prop
----------

Now, this is not going to be an academic presentation.

By the end of this workshop you should be able to formalize contracts or regulations of your own

and you should be able to get some value out of having done that.

What kind of value are we talking about?

You could turn L4 into Python or Javascript.

(screenshot: transpilation to Typescript)

You could get a web application for free that takes an end-user through the logic of your code.

(screenshot: Vue app)

You could build a back-end plugin for ChatGPT that answers questions intelligently about your use case.

(screenshot: mock-up conversation with ChatGPT via plugin about some esoteric detail of an insurance contract.)

Maybe you work for an insurance company that has millions of end-users, and you need something that your call center agents can use.

Or your customers.

Whether they are using a mobile app, or talking to a chatbot powered by an LLM, or asking questions directly to ChatGPT through Bing.

You don't want ChatGPT making up its own answers about how your insurance policies work.

This is something you should control a little more closely.

L4 lets you do that.

Audience
--------

(slide: Audience)

I'm going to assume half of you are in law;

half of you are in CS; and

if that makes you ask "what about the rest?"

you're probably in both law and CS.

About ChatGPT plugins
---------------------

Coming back to this example,

if you've tried ChatGPT,

you've probably been both

impressed by what it can do,

(screenshot: *positive example*)

and astonished by what it *thinks* it can do but is totally and completely wrong about.

(screenshot: *negative example*)

I'm guessing the people at OpenAI knew this was going to happen because they were ready to go with a plugin API.

Wolfram has a plugin. You can ask math questions, science questions, there's a substantial fact base in there which you can query.

(screenshot: Wolfram in use)

So you can think of an L4 backend as providing something similar to Wolfram, but instead of math and science, it's legal questions.

(screenshot: L4 as a ChatGPT plugin)

Hands On Workshop
-----------------

So, in the remaining 45 minutes,

we will get you up and running with L4,

and we will take a quick guided tour of some examples,

and we will encode a very simple piece of legal text,

and we will operationalize that encoding in a bunch of different ways.

Cloning the spreadsheet
~~~~~~~~~~~~~~~~~~~~~~~

(onscreen: bit.ly URL to the spreadsheet)

So, how do you write L4?

There are a couple of options.

You can use a spreadsheet. Google Sheets.

Or you can write L4 in plain text. VS Code, or Emacs, or Vim, up to you.

In this tutorial we will start with a spreadsheet, and come back to the text interface later.

If you go to this link, you will see a tutorial spreadsheet. I want you to make a copy of this spreadsheet for yourself, you can click File, Make a Copy.

There might be a permissions page that you have to click through. If you're not comfortable with this you may want to create a throwaway account.

I will wait a minute for everyone to get through this.

Loading the Sidebar
~~~~~~~~~~~~~~~~~~~

So over here to the right is what we call the sidebar.

The sidebar should have come up for you. If it didn't, try hitting reload on the page.

(We need some instrumentation to monitor the load and see how many new unique hits to the pyrest API backend are coming through, so we know if people are getting this far.)

This sidebar is how you get feedback; all the output of the L4 compiler shows up here in the sidebar.

If the sidebar is not coming up, please ask for help, we have a couple of friendly faces roaming around the room.

Simple example: the Waddington case
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we are looking at a simple example.

This is due to Matthew Waddington, who is a legislative drafter in Jersey and a thought leader in Rules as Code.

He gives us this input:

.. code:: text

    Every person who walks and eats or drinks must sing.

And this is how we encode it, in L4.

Decision Diagrams
~~~~~~~~~~~~~~~~~

.. code:: text

    EVERY Person
      WHO walks
      AND drinks
       OR eats
     MUST sing

Try changing one of those words to something else. You could change eats or drinks to reads or writes, or you could change sing to dance or anything you can think of.

And click in the menu to refresh the sidebar.

Did the diagram change? If you click on the little diagram you should bring up the big version.

Suppose it's not clear what it means to drink. Are we talking booze or soft drinks?

Let's add a section that defines exactly what it means to drink.

In the legalistic style that lawyers know and love.

.. code:: text

    §	What does it mean to drink?
    	drinking
    MEANS   consumes       an alcoholic 
    		   OR  non-alcoholic 
    	beverage 
    AND     whether        in part 
    		   OR  in whole

If we view the markdown or PDF or Word version of this document we see the definition section has grown.

And this would be enough for most people.

If we look at the diagram on the right, we see there's a diagram for qualifies, and a diagram for drinking.

And the web app that comes out of this knows how to ask people about each piece separately.

(screenshot: app with drinking on the left)

(screenshot: app with qualifies on the left)

But that's not good enough for me!

As Steve Krug said,

(screenshot: book cover, Don't Make Me Think)

Don't make me think.

Wouldn't it be nice if we could collapse everything into a single decision graph?

Like this. How would we get there?

(screenshot: combined decision diagram)

Let's do that. Change the subject of the ``MEANS`` clause to ``drinks``:

.. code:: text

    §	What does it mean to drink?
    	drinks
    MEANS   consumes       an alcoholic 
    		   OR  non-alcoholic 
    	beverage 
    AND     whether        in part 
    		   OR  in whole

and now the decision diagram automatically expands to the component details.

And the web app also updates.

Regulative Rules
~~~~~~~~~~~~~~~~

Now let's turn our attention to the diagram above.

The CS people in the room will recognize this as a modified Petri Net. It's a process diagram, a workflow diagram, a flowchart.

And the lawyers in the room might be thinking to themselves, this looks like a duty without a deadline,

so is it really a duty at all?

Let's add a deadline so it becomes very clear when you have to sing.

We'll put in a ``BEFORE`` keyword to say the end of the week.

And the diagram updates.

And now we have something that we could conceivably hand to a graphic designer as a piece of public communication.

How do we operationalize the regulative rules?

Let's have a program that consumes a trace of events, and see if the software determine where we stand.

.. code:: text

    LOG   2023-01-01   Bob walks.
          2023-01-02   Bob eats.
          2023-01-03   Bob consumes an alcoholic beverage, in whole.

The software says: aha, now Bob must sing.

Let's add a line for that:

.. code:: text

    LOG   2023-02-28   Bob sings.

But he is in breach! Why? Because he sang too late. He didn't do it by deadline.

In fact we can turn to the explanation engine to give us this justification: click on some entry in the sidebar.

This shows we have Explainable A.I.

Choice of Exercise
------------------

What do people prefer: do you want to try a computable contract, or do you want to try a Rules as Code exercise?

Contracts or regulations?

Show of hands, please.

Contract exercise
~~~~~~~~~~~~~~~~~

Rules as code exercise
~~~~~~~~~~~~~~~~~~~~~~
