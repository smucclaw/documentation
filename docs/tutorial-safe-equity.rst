#####################################
2. Tutorial Encoding Equity Financing
#####################################

This tutorial is composed of six parts, one introduction, four pages corresponding to the four discrete events that can happen in the contract, and a final page putting the contract together:

1. Introduction 
2. Equity Financing (This page)
3. Liquidity Event
4. Dissolution Event
5. Liquidation Priority
6. Putting the contract together

=====================================
Reminder: Method of encoding the SAFE
=====================================

We will follow a set of steps that are an expansion of the steps we find in :ref:`eg_mustsing`

1. Read the contract,
2. Break the contract up into parts,
3. Encode the definitions into L4,
4. Encode the events into L4.


----------------------------
Step 1: Reading the contract
----------------------------

Let's look at the event we're interested in defining. Terms that are defined in the definitions section are enclosed within asteriks "*" and are not part of the original contract template.

    ``(a) Equity Financing. If there is an *Equity Financing* before the termination of this *Safe*, on the initial closing of such *Equity Financing*, this *Safe* will automatically convert into the greater of: (1) the number of shares of *Standard Preferred Stock* equal to the Purchase Amount divided by the lowest price per share of the *Standard Preferred Stock*; or (2) the number of shares of *Safe Preferred Stock* equal to the Purchase Amount divided by the *Safe Price*.``  

        ``In connection with the automatic conversion of this *Safe* into shares of *Standard Preferred Stock* or *Safe Preferred Stock*, the Investor will execute and deliver to the Company all of the transaction documents related to the *Equity Financing*; provided, that such documents (i) are the same documents to be entered into with the purchasers of *Standard Preferred Stock*, with appropriate variations for the *Safe Preferred Stock* if applicable, and (ii) have customary exceptions to any drag-along applicable to the Investor, including (without limitation) limited representations, warranties, liability and indemnification obligations for the Investor.``

We have a few definitions that we're interested in and that we will encode in step 3.

- Equity Financing
- Safe
- Standard Preferred Stock
- Safe Preferred Stock
- Safe Price

"Company" and "Investor" are defined at the top of the contract template:

    ``THIS CERTIFIES THAT in exchange for the payment by [Investor Name] (the “Investor”) of $[_____________] (the “Purchase Amount”) on or about [Date of Safe], [Company Name], a [State of Incorporation] corporation (the “Company”), issues to the Investor the right to certain shares of the Company’s Capital Stock, subject to the terms described below.``

and they differ for each contract.

In this tutorial, we will not define "Company" or "Investor" explicitly.

-------------------------------------------
Step 2: Break the contract up into sections
-------------------------------------------

Let's break this contract up into different sections. A good first draft is to split the contract based on the lettering and numbering.

Terms defined in the contract are still highlighted with asteriks "*".

    ``(a) Equity Financing. If there is an *Equity Financing* before the termination of this *Safe*, on the initial closing of such *Equity Financing*, this *Safe* will automatically convert into the greater of:``
    
    ``(1) the number of shares of *Standard Preferred Stock* equal to the Purchase Amount divided by the lowest price per share of the *Standard Preferred Stock*; or`` 
    
    ``(2) the number of shares of *Safe Preferred Stock* equal to the Purchase Amount divided by the *Safe Price*.``  

        ``In connection with the automatic conversion of this *Safe* into shares of *Standard Preferred Stock* or *Safe Preferred Stock*, the Investor will execute and deliver to the Company all of the transaction documents related to the *Equity Financing*; provided, that such documents`` 
        
        ``(i) are the same documents to be entered into with the purchasers of *Standard Preferred Stock*, with appropriate variations for the *Safe Preferred Stock* if applicable, and``
        
        ``(ii) have customary exceptions to any drag-along applicable to the Investor, including (without limitation) limited representations, warranties, liability and indemnification obligations for the Investor.``

--------------------------------------
Step 3: Encode the definitions into L4
--------------------------------------

There are twenty definitions found in this contract template. We will not be encoding all the definitions at once. Instead, we'll focus on the definitions that are relevant to this part of the contract.

- Equity Financing
- Safe
- Standard Preferred Stock
- Safe Preferred Stock
- Safe Price

We encode the definitions first because this allows us to get a more rigorous sense of this Equity Financing sitation.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Encoding the definition of "Equity Financing"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    ``“Equity Financing” means a bona fide transaction or series of transactions with the principal purpose of raising capital, pursuant to which the Company issues and sells Preferred Stock at a fixed valuation, including but not limited to, a pre-money or post-money valuation.``

Since this is a definition, we will use the MEANS keyword, which states that something is defined in a certain way.

In this section, Equity Financing is either a bona fide transaction OR a series of transactions.

.. csv-table:: Encoding "Equity Financing"

    "Equity Financing", "MEANS",      ,"bona fide transaction or series of transactions with the principal purpose of raising capital"
                      ,        , "AND", "pursuant to which the Company issues and sells Preferred Stock at a fixed valuation, including but not limited to, a pre-money or post-money valuation"
    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Encoding the definition of "Safe"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    ``“Safe” means an instrument containing a future right to shares of *Capital Stock*, similar in form and content to this instrument, purchased by investors for the purpose of funding the Company’s business operations.  References to “this Safe” mean this specific instrument.``

We see that we need to define Capital Stock. We make a note of this and put it aside for now.

.. csv-table:: Encoding "Safe"

    "Safe", "MEANS", "an instrument containing a future right to shares of Capital Stock, similar in form and content to this instrument, purchased by investors for the purpose of funding the Company’s business operations."

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Encoding the definition of "Capital Stock"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We now encode "Capital Stock"

    ``“Capital Stock” means the capital stock of the Company, including, without limitation, the “Common Stock” and the “Preferred Stock.”``

Common Stock and Preferred Stock are capitalised, but they're not defined explicitly in the contract template.

.. csv-table:: Encoding "Capital Stock"

    "Capital Stock", "MEANS", "the capital stock of the Company, including, without limitation, the "Common Stock" and the "Preferred Stock".

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Encoding the definitions of "Standard Preferred Stock", "Safe Preferred Stock", and "Safe Price"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    ``“Standard Preferred Stock” means the shares of the series of Preferred Stock issued to the investors investing new money in the Company in connection with the initial closing of the Equity Financing.``

.. csv-table:: Encoding "Standard Preferred Stock"

    "Standard Preferred Stock", "MEANS", "the shares of the series of Preferred Stock issued to the investors investing new money in the Company in connection with the initial closing of the Equity Financing."

We encode Safe Preferred Stock.

    ``“Safe Preferred Stock” means the shares of the series of Preferred Stock issued to the Investor in an Equity Financing, having the identical rights, privileges, preferences, seniority, liquidation multiple and restrictions as the shares of Standard Preferred Stock, except that any price-based preferences (such as the per share liquidation amount, initial conversion price and per share dividend amount) will be based on the Safe Price.``

.. csv-table:: Encoding "Safe Preferred Stock"

    "Safe Preferred Stock", "MEANS", "the shares of the series of Preferred Stock issued to the Investor in an Equity Financing, having the identical rights, privileges, preferences, seniority, liquidation multiple and restrictions as the shares of Standard Preferred Stock, except that any price-based preferences (such as the per share liquidation amount, initial conversion price and per share dividend amount) will be based on the Safe Price."

We encode "Safe Price".

    ``“Safe Price” means the price per share equal to the Post-Money Valuation Cap divided by the Company Capitalization.``

.. csv-table:: Encoding "Safe Price"

    "Safe Price", "MEANS", "the price per share equal to the Post-Money Valuation Cap divided by the Company Capitalization."

-------------------------------------------------
Step 4: Encode the Equity Financing event into L4
-------------------------------------------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Encoding the condition and the consequence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``(a) Equity Financing. If there is an *Equity Financing* before the termination of this *Safe*, on the initial closing of such *Equity Financing*, this *Safe* will automatically convert into the greater of:``

This section has a condition and a consequence. 

"If there is an Equity Financing before the termination of this *Safe*, on the initial closing of such Equity Financing," is the condition, 

and "this *Safe* will automatically convert into the greater of:" is the consequence.

An "Equity Financing" is an event that is not explicitly we know that we need an "IF" keyword.

.. csv-table:: Encoding the Conditional

    "UPON", "an Equity Financing"
    "BEFORE", "the termination of this SAFE"
    "AND", "on the initial closing of such Equity Financing"
    "HENCE", "this Safe will automatically convert into the greater of"

We now encode the consequence itself.

    ``(1) the number of shares of Standard Preferred Stock equal to the Purchase Amount divided by the lowest price per share of the Standard Preferred Stock; or (2) the number of shares of Safe Preferred Stock equal to the Purchase Amount divided by the Safe Price.``

