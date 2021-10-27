# Bendford analysis of Ethereum transaction

The python script `script.py` extract from already downloaded archive file the ethereum transaction. The values of those transactions will then been classified by the their first digit (e.g __10__ will be classified under __1__).

We will then show the distribution of the amounts starting by either __1__, __2__, __3__, __4__, __5__, __6__, __7__, __8__ and __9__.

It will allow us to answer the question: does ethereum's transaction value follow [bendford's law](https://en.wikipedia.org/wiki/Benford%27s_law) ?

## Why ?

Because I have watched Netflix's Connected during lockdown.

## Sample

The sample data is from Blockchair (https://gz.blockchair.com/ethereum/transactions/)

I have the data for several years, contact me if you are interested.

## How to use it ?

You will need python3 installed.
```bash
$ python3 script.py
```
or
```bash
$ python3 script.py &> output.txt &
```

## Result

This is the result on the sample data (first month of Ethereum running).

```
Total count : 80664

Transaction `value` first digit distribution

    1 : 29344 (36.38%)
    2 : 12022 (14.9%)
    3 : 7596 (9.42%)
    4 : 8631 (10.7%)
    5 : 7572 (9.39%)
    6 : 3698 (4.58%)
    7 : 3292 (4.08%)
    8 : 3041 (3.77%)
    9 : 5468 (6.78%)



Transaction `fee` first digit distribution

    1 : 75007 (92.99%)
    2 : 4134 (5.12%)
    3 : 541 (0.67%)
    4 : 215 (0.27%)
    5 : 297 (0.37%)
    6 : 344 (0.43%)
    7 : 35 (0.04%)
    8 : 32 (0.04%)
    9 : 59 (0.07%)



Transaction `gas_used` first digit distribution

    1 : 457 (0.57%)
    2 : 78306 (97.08%)
    3 : 370 (0.46%)
    4 : 282 (0.35%)
    5 : 866 (1.07%)
    6 : 36 (0.04%)
    7 : 20 (0.02%)
    8 : 59 (0.07%)
    9 : 268 (0.33%)
```

## What's next ?

This script will be run against a bigger sample of data (from 2015 to 2020).

It could be interesting to check the amount being moved to top 10 smart contract.

