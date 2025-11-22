---
meta-description: Documentation for the CoinDCX API
meta-viewport: width=device-width, initial-scale=1, maximum-scale=1
meta-x-ua-compatible: IE=edge,chrome=1
title: API Reference
---

[ NAV ![](images/navbar-cad8cdcb.png)](#)

![](images/logo-09cbe1a4.png)

[python](#)[javascript](#)

- [Terms and Conditions](#terms-and-conditions)
  - [1. DEFINITIONS](#1-definitions)
  - [2. LICENSE GRANT AND AUTHORISED USE](#2-license-grant-and-authorised-use)
  - [3. FEES AND CHARGES](#3-fees-and-charges)
  - [4. OWNERSHIP AND RIGHTS](#4-ownership-and-rights)
  - [5. TERM AND TERMINATION](#5-term-and-termination)
  - [6. REPRESENTATIONS AND WARRANTIES OF THE USER](#6-representations-and-warranties-of-the-user)
  - [7. DISCLAIMER](#7-disclaimer)
  - [8. SECURITY](#8-security)
  - [9. LIMITATION OF LIABILITY](#9-limitation-of-liability)
  - [10. INDEMNITY](#10-indemnity)
  - [11. ARBITRATION](#11-arbitration)
  - [12. GOVERNING LAW AND JURISDICTION](#12-governing-law-and-jurisdiction)
  - [13. MISCELLANEOUS](#13-miscellaneous)
- [Introduction](#introduction)
- [Terminology](#terminology)
  - [Common](#common)
  - [Orders](#orders)
  - [Margin Orders](#margin-orders)
  - [Margin Internal Orders](#margin-internal-orders)
- [Setup](#setup)
- [SPOT API Rate Limits](#spot-api-rate-limits)
- [Public endpoints](#public-endpoints)
  - [Ticker](#ticker)
  - [Markets](#markets)
  - [Markets Details](#markets-details)
  - [Trades](#trades)
  - [Order Book](#order-book)
  - [Candles](#candles)
- [Authentication](#authentication)
- [User](#user)
  - [Get Balances](#get-balances)
  - [Get User Info](#get-user-info)
- [Sub-account Wallet Transfer](#sub-account-wallet-transfer)
  - [Sub Account Transfer](#sub-account-transfer)
  - [Wallet Transfer](#wallet-transfer)
- [Order](#order)
  - [New Order](#new-order)
  - [Create Multiple Orders](#create-multiple-orders)
  - [Order Status](#order-status)
  - [Multiple Order Status](#multiple-order-status)
  - [Active Orders](#active-orders)
  - [Account Trade History](#account-trade-history)
  - [Active Orders Count](#active-orders-count)
  - [Cancel All](#cancel-all)
  - [Cancel Order By Multiple Ids](#cancel-order-by-multiple-ids)
  - [Cancel](#cancel)
  - [Edit Price](#edit-price)
- [Lend Order](#lend-order)
  - [Fetch Orders](#fetch-orders)
  - [Lend](#lend)
  - [Settle](#settle)
- [Margin Order](#margin-order)
  - [Place Order](#place-order)
  - [Cancel Order](#cancel-order)
  - [Exit](#exit)
  - [Edit Target](#edit-target)
  - [Edit Price of Target Order](#edit-price-of-target-order)
  - [Edit SL Price](#edit-sl-price)
  - [Edit SL Price of Trailing Stop Loss](#edit-sl-price-of-trailing-stop-loss)
  - [Add Margin](#add-margin)
  - [Remove Margin](#remove-margin)
  - [Fetch Orders](#fetch-orders-2)
  - [Query Order](#query-order)
- [Pagination](#pagination)
  - [Parameters](#parameters-24)
- [Spot Sockets](#spot-sockets)
  - [Get Balance Update](#get-balance-update)
  - [Get Order Update](#get-order-update)
  - [Get Trade Update](#get-trade-update)
  - [Get Candlestick Info](#get-candlestick-info)
  - [Get Depth Snapshot Info ( Order Book )](#get-depth-snapshot-info-order-book)
  - [Get Depth Update ( Order Book )](#get-depth-update-order-book)
  - [Get Current Prices](#get-current-prices)
  - [Get Price Stats](#get-price-stats)
  - [Get New Trade](#get-new-trade)
  - [Get Price Change ( LTP )](#get-price-change-ltp)
  - [Sample code for Socket Connection](#sample-code-for-socket-connection)
- [Futures End Points](#futures-end-points)
  - [Glossary](#glossary)
  - [Get active instruments](#get-active-instruments)
  - [Get instrument details](#get-instrument-details)
  - [Get instrument Real-time trade history](#get-instrument-real-time-trade-history)
  - [Get instrument orderbook](#get-instrument-orderbook)
  - [Get instrument candlesticks](#get-instrument-candlesticks)
  - [List Orders](#list-orders)
  - [Create Order](#create-order)
  - [Cancel Order](#cancel-order-2)
  - [List Positions](#list-positions)
  - [Get Positions By pairs or positionid](#get-positions-by-pairs-or-positionid)
  - [Update position leverage](#update-position-leverage)
  - [Add Margin](#add-margin-2)
  - [Remove Margin](#remove-margin-2)
  - [Cancel All Open Orders](#cancel-all-open-orders)
  - [Cancel All Open Orders for Position](#cancel-all-open-orders-for-position)
  - [Exit Position](#exit-position)
  - [Create Take Profit and Stop Loss Orders](#create-take-profit-and-stop-loss-orders)
  - [Get Transactions](#get-transactions)
  - [Get Trades](#get-trades)
  - [Get Current Prices RT](#get-current-prices-rt)
  - [Get Pair Stats](#get-pair-stats)
  - [Get Cross Margin Details](#get-cross-margin-details)
  - [Wallet Transfer](#wallet-transfer-2)
  - [Wallet Details](#wallet-details)
  - [Wallet Transactions](#wallet-transactions)
  - [Edit Order](#edit-order)
  - [Change Position Margin Type](#change-position-margin-type)
  - [Get Currency Conversion](#get-currency-conversion)
- [Futures Sockets](#futures-sockets)
  - [Glossary](#glossary-2)
  - [ACCOUNT](#account)
  - [Get Position Update](#get-position-update)
  - [Get Order Update](#get-order-update-2)
  - [Get Balance Update](#get-balance-update-2)
  - [Get Candlestick Data](#get-candlestick-data)
  - [Get Orderbook](#get-orderbook)
  - [Get Current Prices](#get-current-prices-2)
  - [Get New Trade](#get-new-trade-2)
  - [Get LTP Data](#get-ltp-data)
  - [Sample code for Socket Connection](#sample-code-for-socket-connection-2)
- [FAQ](#faq)
- [Errors](#errors)
- [High-Frequency Trading](#high-frequency-trading)


- [Sign Up for a Developer Key](https://coindcx.com/api-dashboard)
- [Documentation Powered by Slate](https://github.com/slatedocs/slate)

# Terms and Conditions

These API License Terms and Conditions (“Terms”) shall govern the use of any ‘Market Data’ and Application Programming Interface (API) of CoinDCX by you, either an individual, association of persons, company, or any legal entity and its respective affiliates (hereinafter referred to as “User”). 
For the purpose of these Terms, ‘Market Data’ shall mean and include all data related to the trading activity on any website, applications or platform owned and operated by Primestack Pte. Limited and/or Neblio Technologies Private Limited or any of their parent company, subsidiaries, or affiliates (collectively referred to as “CoinDCX”) including any data, information made available to the User through the application programming interface of CoinDCX (“CoinDCX API”). The Market Data may include, without limitation, the prices and quantities of orders and transactions executed on any platform/ application of CoinDCX.

The User hereby agrees and acknowledges that upon accessing any CoinDCX API (defined hereinafter), Market Data and/or any other information, service, feature governed by terms contained herein, the User shall be bound by these Terms, as updated, modified, and/or replaced from time to time. The User is required to check for any such amendment, replacement or changes to the terms contained herein and any future use or access to any services covered herein.

### 1. DEFINITIONS

- 1.1. “Affiliate” shall mean any person or entity who is controlled by, under common control with, or controlling the other party. For the purposes of the foregoing, “control” means;
  - (a) the ownership of more than fifty percent (50%) of the voting stock, shares or interests or voting rights of a person or entity, and
  - (b) the power to direct or cause the direction of the management and policies of a person or entity through the ownership of voting securities, by contract or otherwise.
- 1.2. “Applicable Law(s)” shall mean the governing law to which these Terms are subject to and includes but is not limited to all the statutes (including common law statutes), legislations, rules, regulations, treaties, directives, decisions, ordinances, by-laws, notices, injunctions, demands, judgement, circular and any direction, notification issued by statutory authority, regulatory authority, or any judicial/ quasi-judicial authority. Applicable Law shall include any law, regulation, directive or guidelines to which CoinDCX may be subject to.  -     - 1.3. “Application Programming Interface” or “API” is a software intermediary which enables the interaction between two or more applications/ platforms.
    - 1.4. “Algorithmic Trading” (also called automated trading, black-box trading, or algo-trading) means a method which uses a computer program following a defined set of instructions or algorithm to place a trade.
    - 1.5. “CoinDCX API” shall mean and include the public API and/or any data, information related to the trading activity on the CoinDCX platforms made available through https://docs.coindcx.com/ (including Market Data and Data Packages) as amended, modified, replaced at the sole discretion of CoinDCX from time to time.
    - 1.6. “Company Data” means anonymized transactional data pertaining to contracts and other financial instruments, which is accessible through the CoinDCX API.
    - 1.7. “Data Packages” means and includes all the data feeds, tiers, or packages of the Market Data or any other data as may be identified and included by CoinDCX as a part of the CoinDCX API.
    - 1.8. “Intellectual Property Rights” means any patent, copyright, trademark, word mark, service mark, logo, corporate name, internet domain name, industrial design, trade secrets, proprietary rights in any software, application, goodwill of the brand.
    - 1.9. “Licensee” shall mean the User and any person accessing any CoinDCX API or any services or products governed by these Terms.
    - 1.10. “Licensee Data” shall mean and inter alia include all the data, information owned/ controlled by the Licensee in whatever form.
    - 1.11. “High-Frequency Trading” is a type of Algorithmic Trading characterized by high speeds, high turnover rates, and high order-to-trade ratios that leverages high-frequency financial data and electronic trading tools.

### 2. LICENSE GRANT AND AUTHORISED USE

    - 2.1. User hereby understands and acknowledges that upon agreeing to the terms contained herein, the User is granted a non-exclusive, non-transferable, non-assignable, non-sublicensable, revocable, restricted license for usage purpose only in accordance with the Applicable Law(s).
    - 2.2. User hereby agrees that the License granted as per these Terms is only for the authorized use of the CoinDCX API, Market Data and any software provided as per the terms contained herein.
    - 2.3. The User shall always ensure that:
    - a) The User does not alter, manipulate, or misrepresent any CoinDCX API or Market Data
    - b) The User shall not copy, reverse engineer, decompile, disassemble, or attempt to derive the source code, algorithm, structure, of the CoinDCX API or any software provided to the User hereunder.
    - c) The User shall not redistribute, display, or disseminate the Market Data or any data, charts, analytics, research, or other works based on, referring to, or derived from the Market Data to any third party.
    - d) Any use by the Affiliates of User shall be disclosed to CoinDCX and it may involve additional pricing.

      

### 3. FEES AND CHARGES

    - 3.1. The User hereby agrees and acknowledges that presently no fees or charges are levied by CoinDCX for the use of CoinDCX API. However, nothing contained in this section, or these Terms shall restrict or limit the right of CoinDCX to charge fees or levy charges for use of the services captured herein including the CoinDCX APIs.
    - 3.2. CoinDCX shall have a right to waive any fee/ charges based on the use of the CoinDCX API / Market Data by the User(s). 
The User hereby understands and acknowledges that rates/ charges/ fees may differ for Users on account of several factors including but not limited to jurisdiction, scale of use, type of entity etc. and the User waives the right to claim against CoinDCX in this regard.

### 4. OWNERSHIP AND RIGHTS

    - 4.1. The User hereby agrees and acknowledges that CoinDCX shall retain the ownership and the Intellectual Property Rights in all the Company Data, CoinDCX API and Market Data including any software or service provided or granted to the User as per the terms contained herein.
    - 4.2. The User hereby agrees that it shall use the Intellectual Property Rights belonging to CoinDCX strictly according to the terms contained herein and the written instructions as may be provided or published by CoinDCX from time to time. The User may not delete, remove, alter, hide, move any Intellectual Property Rights belonging to CoinDCX which may or may not appear in the CoinDCX API or Market Data. All representations by the User of any Intellectual Property Rights as originally distributed and intended by CoinDCX.

### 5. TERM AND TERMINATION

    - 5.1. These Terms shall be valid unless terminated as per the terms contained hereunder. Any amendment to the pricing terms may be introduced by the parties upon execution of a pricing schedule to incorporate additional terms.
    - 5.2. These Terms may be terminated by CoinDCX without any notice to the User and without assigning any reason. The User understands and agrees that this could affect the User’s right to use any of the services or benefits granted by virtue of these Terms. The User hereby waives any and all rights to claim under this section.
    - 5.3. Termination for breach:
    - User’s access to the CoinDCX API or any Market Data shall be terminated/ revoked by CoinDCX forthwith without any notice to the User in the following cases:
    - a) Breach of any Intellectual Property Rights of CoinDCX or its Affiliates.
    - b) Breach of any terms contained herein.
    - c) Use of the CoinDCX API for any fraudulent, illegal, immoral, or any activity not authorized by CoinDCX.

      

### 6. REPRESENTATIONS AND WARRANTIES OF THE USER

    - The User hereby represents and warrants the following:
    - 6.1. The User has the requisite power, authority, consents, licenses, and authorizations to comply with the Terms.
    - 6.2. Any data, information, material, documents provided to CoinDCX is accurate, true, updated. Further, the User agrees to promptly inform CoinDCX in case of any changes to the document, information or material provided.
    - 6.3. The User shall comply with the Applicable Law(s)
    - 6.4. It has the relevant licenses to conduct any High Frequency Trading or Algorithmic Trading and shall ensure that relevant licenses/ approvals/ consents are obtained if the same is required under any Applicable Law(s).
    - 6.5. The User represents and warrants that it shall comply with the Terms of Use.
    - 6.6. The User hereby represents and warrants that it shall preserve and maintain the information, data and relevant records pertaining to the use of the CoinDCX API/ Market Data for a period of 5 years post termination or expiry of these Terms.
    - 6.7. The User understands and agrees that Company is not acting as an advisor or fiduciary with respect to Licensee and is not providing investment advice, tax advice, legal advice, or other professional advice by allowing Licensee to use the Company API and Company Data. Licensee shall be solely responsible, and Company shall have no responsibility, for any decisions of Licensee or its use of the Company API or Company Data and for Licensee’s compliance with applicable laws and regulations. Without limiting the foregoing, the Company makes no recommendation regarding the purchase or sale of digital assets or any other asset, or any other investment decision or action, taken by Licensee.

### 7. DISCLAIMER

      THE COINDCX API, MARKET DATA (INCLUDING DATA PACKAGES) AND ANY OTHER SERVICE/ SOFTWARE PROVIDED BY COINDCX TO THE USER IS PROVIDED ON AN “AS IS'' AND “AS AVAILABLE” BASIS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED. COINDCX DOES NOT WARRANT THAT THE COINDCX API OR ANY SERVICES PROVIDED HEREUNDER WILL BE SAFE, UNINTERRUPTED, ERROR FREE, OR PROTECT AGAINST ANY HACK, CYBER CRIME OR OTHER THREATS. COINDCX DISCLAIMS ALL OTHER WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE FITNESS, QUALITY, PERFORMANCE, NON-INFRINGEMENT, PURPOSE OF THE COINDCX API OR MARKET DATA OR ANY SOFTWARE OR SERVICE PROVIDED TO THE USER. ACCESS ANY USE OF ANY COINDCX API OR MARKET DATA IS AT THE SOLE RISK OF THE USER AND COINDCX SHALL NOT BE RESPONSIBLE FOR ANY ACTIONS TAKEN BASED ON ANY SOFTWARE OR SERVICE PROVIDED HEREUNDER.

### 8. SECURITY

      The user shall ensure that the information received through APIs, including personally identifiable information is protected from unauthorized access or use and shall promptly report to CoinDCX of any unauthorized access or use of such information to the extent required by applicable law. The User must ensure secure operation of CoinDCX APIs by employing reasonable security measures. The Users shall report any security deficiencies or intrusions at [[email protected]](/cdn-cgi/l/email-protection). 

### 9. LIMITATION OF LIABILITY

      In no event, whether in tort, contract or otherwise, shall CoinDCX or its Affiliates be liable towards the User for any indirect, special, consequential, incidental, punitive, business loss. Under no circumstances or event shall the maximum aggregate liability of CoinDCX towards the User or any of its Affiliates shall exceed INR 1,00,000/- (Rupees One lakh only).

### 10. INDEMNITY

    - The User shall be liable to indemnify, hold harmless and keep CoinDCX and its Affiliates always indemnified for and against any liability, costs, expenses, damages, charges/ fees (including reasonable attorney and legal fees), claims arising or relating to:
    - a) Use of the CoinDCX API/ Market Data or any software provided hereunder
    - b) Breach of any Confidentiality terms or any Intellectual Property Rights of CoinDCX and its Affiliates.
    - c) Any fraudulent use of the CoinDCX API by the User or its Affiliates
    - d) Breach of the terms contained herein

### 11. ARBITRATION

    - 11.1 Any dispute, claim, difference or controversy arising out of, relating to or having any connection with the Terms, including any dispute as to its existence, validity, interpretation, performance, breach or termination or the consequences of its nullity and any dispute relating to any non-contractual obligations arising out of or in connection with it shall be referred to and finally resolved by arbitration administered by the Arbitration Tribunal in accordance with the Arbitration & Reconciliation Act, 1996 as amended, updated, re-enacted from time to time.
    - 11.2. The Language of arbitration shall be English and Mumbai, India shall be the seat and place of Arbitration.

### 12. GOVERNING LAW AND JURISDICTION

      Subject to the Arbitration clause above, these Terms shall be governed by the laws of India and the courts at Mumbai, India shall have exclusive jurisdiction. 

### 13. MISCELLANEOUS

    - 13.1. The User shall not assign any of its obligations, rights under these Terms to any third party. Assignment to Affiliates shall be only after obtaining the prior written consent of CoinDCX.
    - 13.2. Force Majeure - CoinDCX shall not be held responsible for any failure, delay, interruption caused by circumstances outside its control, such as network failure, network connection failure, earthquake, flooding, strikes, embargoes, or any act(s) of the government or any regulatory/ statutory authority.
    - 13.3. The User agrees to pay all the necessary taxes as may be imposed under the Applicable Laws.
    - 13.4. Failure by CoinDCX to exercise or enforce any rights hereunder shall not amount to waiver of those rights.
    - 13.5. Each party is an independent contractor and there shall not be any principal-agent relationship between CoinDCX and the User.

# Introduction

      Welcome to the CoinDCX API!

The base URL for the API calls is `https://api.coindcx.com`, base URL for some public endpoint is `https://public.coindcx.com`. However, it will only be used where it is exclusively mentioned in the documentation. 

       CoinDCX Public APIs can be used for placing different orders like Spot, Margin, Lend and also for getting data related to different markets, candles, user balances etc.

       Whereas Sockets can be used to get continues data related to trades, user balance, Orderbook, Bracket Order Trades, Order updates.
> The python version used for API samples is 3.8 and 3.10.6

# Terminology

### Common

    - `target currency` refers to the asset that is the `quantity` of a symbol.
    - `base currency` refers to the asset that is the `price` of a symbol.
    - `pair` uniquely identifies the market along with its exchange, and is available in market details api.

### Orders

    - `status`: used to denote the current status of the given order. Valid values for status include:


      - `init`: order is just created, but not placed in the orderbook (eg: stop-limit orders whose stop/trigger price hasn't reached)
      - `open`: order is successfully placed in the orderbook
      - `partially_filled`: order is partially filled
      - `filled`: order is completely filled
      - `partially_cancelled`: order is partially filled, but cancelled, thus inactive
      - `cancelled`: order is completely or partially cancelled
      - `rejected`: order is rejected (not placed on the exchange)
      - `untriggered`: order is untriggered (only applies to Futures Take Profit and Stop Loss orders)

      Among these, the open-equivalent status' includes:  
`init, open, partially_filled`  
Orders having any these status can undergo further change (like when they get filled or cancelled).

      And settled or closed-equivalent status' includes:  
`filled, partially_cancelled, cancelled, rejected`  
 Orders having any of these status could not undergo any change.

### Margin Orders

    - `status`: used to denote the current status of the given margin order. Valid values for status include:


      - `init`: order is just created, but not placed in the orderbook
      - `open`: order is successfully placed in the orderbook
      - `partial_entry`: internal entry order is partially filled
      - `partial_close`: internal target order is partially closed
      - `cancelled`: order is completely cancelled
      - `rejected`: order is rejected (not placed on the exchange)
      - `close`: order is completely filled
      - `triggered`: stop variant order triggered at specified stop price

        


    - `order_type`: used to denote the type of order to be placed. Valid values for order_type includes:


      - `market_order`: in this order type we don't specify price; it is executed on the market price
      - `limit_order`: in this order type we specify the price on which order is to be executed
      - `stop_limit`: it is a type of limit order whether we specify stop price and a price, once price reaches stop_price, order is placed on the given price
      - `take_profit`: it is a type of limit order whether we specify stop price and a price, once price reaches stop_price, order is placed on the given price

        


    - Other Terms:


      - `target_price`: The price at which the trader plans to buy/sell or close the order position is called the Target Price. When the Target price is hit, the trade is closed and the trader’s funds are settled according to the P&L incurred. Target price feature is available if the trader checks the Bracket order checkbox.
      - `sl_price`: The price at which the trader wishes to Stop Loss is the SL Price.
      - `stop_price`: It is used in the Stop Variant order, to specify stop price

### Margin Internal Orders

    - `status`for internal orders: used to denote the type of internal orders. Valid values for order_type includes:


      - `initial`: order is just created
      - `open`: order is successfully placed in the orderbook
      - `partially_filled`: order is partially filled
      - `filled`: order is completely filled
      - `cancelled`: order is completely cancelled
      - `rejected`: order is rejected (not placed on the exchange)
      - `partially_cancelled`: order is partially cancelled
      - `untriggered`: stop variant order was not triggered

# Setup

       To access CoinDCX Public APIs and Sockets you will need 

    - Key and Secret
    - Programming and Scripting language (Python and Javascript)
    - Few Libraries (Socket.io, request module, Crypto module)

      Follow below mentioned steps for completing the pre-requisite

      1. You can get your API key and Secret as follows

    - Go to your CoinDCX profile section
    - Click `API dashboard`
    - Click Create API key button and enter label name and check `Bind IP Address to API key` only if you wanna bind the API key with your IP
    - Enter email and SMS OTP
    - Store the Key and Secret visible on the screen

      NOTE: `If the Key is binded with the IP, then these API can only be used with the binded IP and cannot be shared with ony other user having different IP.`

      2. For Public APIs

      a. Javascript:

      We recommend using [ Node.js](https://nodejs.org/en/download/). We recommend that you use v14 and above
You’ll need to have the following 2 Node modules installed to be able to work with our APIs:

    - Request module
    - Crypto module

      b. Python:

      We recommend that you use Python 3.8 and above. We recommend that you do not use Python 2 as it is on its path to be sunset. 
You can install/know more from the [official Python website](https://www.python.org/about/gettingstarted/)

      3. For Sockets

      a. Javascript:

      We recommend using Node.js. We recommend that you use v14 and above
You’ll need to have the following Node modules installed to be able to work with our APIs:
    - Socket.io: Please note only version 2.4.0 of this module would work with our Websockets. 
 Please check this version in package.json


       You can install the specific version by using the command
    - `npm install [[email protected]](/cdn-cgi/l/email-protection)`


      b. Python: 

      We recommend that you use Python 3.8 and above.
We recommend that you do not use Python 2 as it is on its path to be sunset.
You can install/know more from the [official Python website](https://www.python.org/about/gettingstarted/) 

      YAY!!, You are all set to access CoinDCX Public APIs and Sockets

      

# SPOT API Rate Limits

      

| API Name | Rate Limit | Period |
| --- | --- | --- |
| Create Order Multiple | 2000 | 60s |
| Create Order | 2000 | 60s |
| Cancel All | 30 | 60s |
| Multiple Order Status | 2000 | 60s |
| Order Status | 2000 | 60s |
| Cancel Multiple by ID | 300 | 60s |
| Cancel | 2000 | 60s |
| Active Order | 300 | 60s |
| Edit Price | 2000 | 60s |

# Public endpoints

## Ticker

      

    const request = require('request')

    const baseurl = "https://api.coindcx.com"

    request.get(baseurl + "/exchange/ticker",function(error, response, body) {
        console.log(body);
    })

      

    import requests # Install requests module first.

    url = "https://api.coindcx.com/exchange/ticker"

    response = requests.get(url)
    data = response.json()
    print(data)
> Response

      

    [
      {
        "market": "REQBTC",
        "change_24_hour": "-1.621",
        "high": "0.00002799",
        "low": "0.00002626",
        "volume": "14.10",
        "last_price": "0.00002663",
        "bid": "0.00002663",
        "ask": "0.00002669",
        "timestamp": 1524211224
      }
    ]

### HTTP Request

      `GET /exchange/ticker`

### Definitions

    - bid - Highest bid offer in the orderbook
    - ask - Highest ask offer in the orderbook
    - high - 24 hour high
    - low - 24 hour low
    - volume - Volume of the market in last 24 hours.
    - timestamp - Time when this ticker was generated


A ticker is generated once every second

## Markets

      

    const request = require('request')

    const baseurl = "https://api.coindcx.com"

    request.get(baseurl + "/exchange/v1/markets",function(error, response, body) {
        console.log(body);
    })

      

    import requests # Install requests module first.

    url = "https://api.coindcx.com/exchange/v1/markets"

    response = requests.get(url)
    data = response.json()
    print(data)

> Respose:

      

    [
      "SNTBTC",
      "TRXBTC",
      "TRXETH"
      .
      .
    ]

### HTTP Request

      `GET /exchange/v1/markets`

      Returns an array of strings of currently active markets.

## Markets Details

      

    const request = require('request')

    const baseurl = "https://api.coindcx.com"

    request.get(baseurl + "/exchange/v1/markets_details",function(error, response, body) {
        console.log(body);
    })

      

    import requests # Install requests module first.

    url = "https://api.coindcx.com/exchange/v1/markets_details"

    response = requests.get(url)
    data = response.json()
    print(data)
> Response:

      

    [
      {
        "coindcx_name": "SNMBTC",
        "base_currency_short_name": "BTC",
        "target_currency_short_name": "SNM",
        "target_currency_name": "Sonm",
        "base_currency_name": "Bitcoin",
        "min_quantity": 1,
        "max_quantity": 90000000,
        "min_price": 5.66e-7,
        "max_price": 0.0000566,
        "min_notional": 0.001,
        "base_currency_precision": 8,
        "target_currency_precision": 0,
        "step": 1,
        "order_types": [ "take_profit", "stop_limit", "market_order", "limit_order" ],
        "symbol": "SNMBTC",
        "ecode": "B",
        "max_leverage": 3,
        "max_leverage_short": null,
        "pair": "B-SNM_BTC",
        "status": "active"
      }
    ]

### HTTP Request

      `GET /exchange/v1/markets_details`

### Response Param Definitions

| Parameter | Definitions |
| --- | --- |
| min_quantity | It is the minimum quantity of target currency (SNT) for which an order may be placed |
| max_quantity | It is the maximum quantity of target currency (SNT) for which an order may be placed |
| min_notional | It is the minimum amount of base currency (BTC) for which an order may be placed |
| base_currency_precision | Number of decimals accepted for the base currency |
| target_currency_precision | Number of decimals accepted for the target currency |
| step | It is the minimum increment accepted for the target currency |
|  |  |
| pair | It is a string created by (ecode, target_currency_short_name, base_currency_short_name). It can be used to connect to DcxStreams socket for API trading. For example: `B-BTC_USDT`, `I-BTC_INR`, `KC-XYZ_USDT` |
| min_price | It is the minimum Price for which an order may be placed |
| max_price | It is the maximum Price for which an order may be placed |
| order_types | Different type of orders that can be placed for the market. For example: `limit_order`, `market_order` etc |
| max_leverage | It is the max leverage for long positions that is available in this market for margin trading |
| max_leverage_short | It is the max leverage for short positions that is available in this market for margin trading |
| status | This states if a market can be used for trading. Possible values could be `active` or `inactive` |

## Trades

      

    import requests # Install requests module first.

    url = "https://public.coindcx.com/market_data/trade_history?pair=B-BTC_USDT&limit=50" # Replace 'B-BTC_USDT' with your desired market pair.

    response = requests.get(url)
    data = response.json()
    print(data)

      

    const request = require('request')

    const baseurl = "https://public.coindcx.com"

    // Replace the "B-BTC_USDT" with the desired market pair.
    request.get(baseurl + "/market_data/trade_history?pair=B-BTC_USDT&limit=50",function(error, response, body) {
        console.log(body);
    })
> Response

      

    [
      {
        "p": 11603.88,
        "q": 0.023519,
        "s": "BTCUSDT",
        "T": 1565163305770,
        "m": false
      }
    ]

The base URL for Trades API call is https://public.coindcx.com 

### HTTP request

      `GET /market_data/trade_history`

### Query parameters

| Name | Required | Example |
| --- | --- | --- |
| pair | Yes | B-SNT_BTC (`pair` from Market Details API) |
| limit | No | Default: 30; Max: 500 |

      This API provides with a sorted list of most recent 30 trades by default if limit parameter is not passed.

### Definitions

    - p is the trade price
    - q is the quantity
    - s is the market name
    - T is the timestamp of trade
    - m stands for whether the buyer is market maker or not.

## Order Book

      

    const request = require('request')

    const baseurl = "https://public.coindcx.com"

    // Replace the "B-BTC_USDT" with the desired market pair.
    request.get(baseurl + "/market_data/orderbook?pair=B-BTC_USDT",function(error, response, body) {
        console.log(body);
    })

      

    import requests # Install requests module first.

    url = "https://public.coindcx.com/market_data/orderbook?pair=B-BTC_USDT" # Replace 'SNTBTC' with the desired market pair.

    response = requests.get(url)
    data = response.json()
    print(data)

> Response

      

    {
      "bids":{
        "11570.67000000": "0.000871",
        "11570.58000000": "0.001974",
        "11570.02000000": "0.280293",
        "11570.00000000": "5.929216",
        "11569.91000000": "0.000871",
        "11569.89000000": "0.0016",
        ,
        ,
        ,
      },
      "asks":{
       "13900.00000000": "27.04094600",
        "13100.00000000": "15.48547100",
        "12800.00000000": "36.93142200",
        "12200.00000000": "92.04554800",
        "12000.00000000": "72.66595000",
        "11950.00000000": "17.16624600",
        ,
        ,
        ,
      },


The base URL for Order book API call is https://public.coindcx.com 

### HTTP request

      `GET /market_data/orderbook`

### Query parameters

| Name | Required | Example |
| --- | --- | --- |
| pair | Yes | B-BTC_USDT (`pair` from Market Details API) |

## Candles

      

    const request = require('request')

    const baseurl = "https://public.coindcx.com"

    // Replace the "B-BTC_USDT" with the desired market pair.
    request.get(baseurl + "/market_data/candles?pair=B-BTC_USDT&interval=1m",function(error, response, body) {
        console.log(body);
    })

      

    import requests # Install requests module first.

    url = "https://public.coindcx.com/market_data/candles?pair=B-BTC_USDT&interval=1m" # Replace 'SNTBTC' with the desired market pair.

    response = requests.get(url)
    data = response.json()
    print(data)

> Response

      

    [
      {
            "open": 0.011803, // open price
            "high": 0.011803, // highest price
            "low": 0.011803, // lowest price
            "volume": 0.35,  // total volume in terms of target currency (in BTC for B-BTC_USDT)
            "close": 0.011803, // close price
            "time": 1561463700000 //open time in ms
      }
      .
      .
      .
    ],


The base URL for Candles API call is https://public.coindcx.com 

### HTTP request

      `GET /market_data/candles`

### Query parameters

| Name | Required | Example |
| --- | --- | --- |
| pair | Yes | B-BTC_USDT (`pair` from Market Details API) |
| interval | Yes | any of the valid intervals given below |
| startTime | No | timestamp in ms, eg: `1562855417000` |
| endTime | No | timestamp in ms, eg: `1562855417000` |
| limit | No | Default: 500; Max: 1000 |

      This API provides with a sorted list (in descending order according to time key) of candlestick bars for given pair. Candles are uniquely identified by their time.

      **Valid intervals**

      m -> minutes, h -> hours, d -> days, w -> weeks, M -> months

    - `1m`
    - `5m`
    - `15m`
    - `30m`
    - `1h`
    - `2h`
    - `4h`
    - `6h`
    - `8h`
    - `1d`
    - `3d`
    - `1w`
    - `1M`

# Authentication
> To authorize, use this code:
> Sample order creation with auth

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
        "side": "buy",  #Toggle between 'buy' or 'sell'.
      "order_type": "limit_order", #Toggle between a 'market_order' or 'limit_order'.
      "market": "SNTBTC", #Replace 'SNTBTC' with your desired market pair.
      "price_per_unit": 0.03244, #This parameter is only required for a 'limit_order'
      "total_quantity": 400, #Replace this with the quantity you want
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/orders/create"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const   body = {
            "side": "buy",  //Toggle between 'buy' or 'sell'.
            "order_type": "limit_order", //Toggle between a 'market_order' or 'limit_order'.
            "market": "SNTBTC", //Replace 'SNTBTC' with your desired market pair.
            "price_per_unit": "0.03244", //This parameter is only required for a 'limit_order'
            "total_quantity": 400, //Replace this with the quantity you want
            "timestamp": timeStamp
        }

        const payload = new Buffer(JSON.stringify(body)).toString();
        const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

        const options = {
            url: baseurl + "/exchange/v1/orders/create",
            headers: {
                'X-AUTH-APIKEY': key,
                'X-AUTH-SIGNATURE': signature
            },
            json: true,
            body: body
        }

        request.post(options, function(error, response, body) {
            console.log(body);
        })
> Make sure to replace API key and API secret with your own.

Common Notes:
    - All the Authenticated API calls use POST method.
    - Parameters are to be passed as JSON in the request body.
    - Every request must contain a timestamp parameter of when the request was generated. This timestamp is used to validate that the request is not a very old one (due to some lag in any layer) - the request is rejected with an appropriate error if this timestamp deviates too much from the server's time at which it is received to be processed.

      The authentication procedure is as follows:
    - The payload is the parameters object, JSON encoded
`payload = parameters-object -> JSON encode`  
  
    - The signature is the hex digest of an HMAC-SHA256 hash where the message is your payload, and the secret key is your API secret.
`signature = HMAC-SHA256(payload, api-secret).digest('hex')`
  

      After this, You will have to add following headers into all the authenticated requests



| Header Name | Value |
| --- | --- |
| X-AUTH-APIKEY | your-api-key |
| X-AUTH-SIGNATURE | signature |

 You must replace `your-api-key` and `signature` with your personal API key and generated signature respectively.

# User

## Get Balances

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp
    timeStamp = int(round(time.time() * 1000))

    body = {
        "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/users/balances"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json();
    print(data);

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = ""


    const body = {
        "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/users/balances",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(body);
    })
> Response:

      

    [
      {
        "currency": "BTC",
        "balance": 1.167,
        "locked_balance": 2.1
      }
    ]
> Locked balance is the balance currently being used by an open order

      This endpoint retrieves account's balances.

### HTTP Request

      `POST /exchange/v1/users/balances`

## Get User Info

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp
    timeStamp = int(round(time.time() * 1000))

    body = {
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/users/info"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json();
    print(data);

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = ""


    const body = {
      "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
      url: baseurl + "/exchange/v1/users/info",
      headers: {
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
      },
      json: true,
      body: body
    }

    request.post(options, function(error, response, body) {
      console.log(body);
    })
> Response:

      

    [
      {
        "coindcx_id": "fda259ce-22fc-11e9-ba72-ef9b29b5db2b",
        "first_name": "First name",
        "last_name": "Last name",
        "mobile_number": "000000000",
        "email": "[[email protected]](/cdn-cgi/l/email-protection)"
      }
    ]
> coindcx_id is the user id

      This endpoint retrieves user info.

### HTTP Request

      `POST /exchange/v1/users/info`

# Sub-account Wallet Transfer

      The sub-account transfer APIs will enable the user to manage funds between master account & its corresponding sub-accounts

## Sub Account Transfer

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "xxx";     // to be created from api dashboard of the user
    const secret = "xxx"; // to be created from api dashboard of the user


    const body = {
        "from_account_id": "yyyyy",
        "to_account_id": "xxxxxx",
        "currency_short_name": "USDT",
        "amount":1 ,
        "timestamp": timeStamp

    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
      url: baseurl + "/exchange/v1/wallets/sub_account_transfer",
      headers: {
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
      },
      json: true,
      body: body
    }

    request.post(options, function(error, response, body) {
      console.log(body);
    })


      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "xxx"
    secret = "xxx"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')

    # python2
    # secret_bytes = bytes(secret)

    # Generating a timestamp
    timeStamp = int(round(time.time() * 1000))

    body = {
        "timestamp": timeStamp,  # EPOCH timestamp in seconds
        "from_account_id": "xxxxx",
        "to_account_id": "yyyyy",
        "currency_short_name": "USDT",
        "amount": 1,
    }

    json_body = json.dumps(body, separators=(',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/wallets/sub_account_transfer"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data=json_body, headers=headers)
    data = response.json()
    print(json.dumps(data, indent=2))
> Response

      

    {
        "status": "success",
        "message": 200,
        "code": 200
    }


      Using this endpoint,master account can carry out the following fund transfers:
    - Main account spot wallet to sub-account spot wallet
    - Sub-account spot wallet to main account spot wallet
    - One sub-account spot wallet to another sub-account spot wallet


      For security reasons, this endpoint would only be available to users who have created an API key post 12th August, 2024. 

### HTTP Request

      `POST https://api.coindcx.com/exchange/v1/wallets/sub_account_transfer`

### Request Defnitions

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timestamp | Integer | YES | EPOCH timestamp in seconds |
| from_account_id | String | YES | The account from which assets are being transferred (main or sub-account ID) |
| to_account_id | String | YES | The account to which assets are being transferred (main or sub-account ID) |
| currency_short_name | String | YES | The type of asset being transferred (e.g., BTC, ETH). |
| amount | Float | YES | The amount of the asset to transfer |

### Possible Error Codes

| Status Code | Message | Reason |
| --- | --- | --- |
| 422 | Invalid transfer | invalid from_account_id or to_account_id passed |
| 401 | Unauthorized access | Transfer initiated by sub account user |
| 400 | Currency short name not present | Invalid currency_short_name provided |
| 404 | source wallet not found | Source currency wallet is not created for user |
| 404 | destination wallet not found | Destination currency wallet is not created for user |
| 422 | Unverified Sub-Account | Email verification pending for sub account user |
| 400 | Insufficient funds | Amount to be transferred is more than the available wallet balance |
| 422 | Amount should be greater than | Amount should be greater than |
| 422 | Your withdrawals are blocked for another XX hours because you changed your account authentication mode | User is under surveillance |

## Wallet Transfer

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "xxx";
    const secret = "xxx";


    const body = {
        "source_wallet_type" : "spot",
        "destination_wallet_type": "futures",
        "currency_short_name": "USDT",
        "amount": 1,
        "timestamp": timeStamp
    }



    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
      url: baseurl + "/exchange/v1/wallets/transfer",
      headers: {
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
      },
      json: true,
      body: body
    }

    request.post(options, function(error, response, body) {
      console.log(body);
    })


      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "xxx"
    secret = "xxx"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')

    # python2
    # secret_bytes = bytes(secret)

    # Generating a timestamp
    timeStamp = int(round(time.time() * 1000))

    body = {
        "timestamp": timeStamp,  # EPOCH timestamp in seconds
        "source_wallet_type": "futures",
        "destination_wallet_type": "spot",
        "currency_short_name": "USDT",
        "amount": 1,
    }

    json_body = json.dumps(body, separators=(',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/wallets/transfer"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data=json_body, headers=headers)
    data = response.json()
    print(json.dumps(data, indent=2))

> Response

      

    {
        "status": "success",
        "message": 200,
        "code": 200
    }


      Using this endpoint,master account can carry out the following fund transfers:
    - Transfer from spot to futures wallet
    - Transfer from futures to spot wallet


### HTTP Request

      `POST https://api.coindcx.com/exchange/v1/wallets/transfer`

### Request Defnitions

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timestamp | Integer | YES | EPOCH timestamp in seconds |
| source_wallet_type | Enum | YES | The wallet type from which balance has to be transferred (spot / futures) |
| destination_wallet_type | Enum | YES | The wallet type from which balance has to be transferred (spot / futures) |
| currency_short_name | String | YES | The type of asset being transferred (e.g., BTC, ETH). |
| amount | Float | YES | The amount of the asset to transfer |

### Possible Error Codes

| Status Code | Message | Reason |
| --- | --- | --- |
| 422 | Invalid amount | Amount to be transferred should be positive |
| 422 | Invalid currency | Invalid currency_short_name provided |
| 422 | Derivatives Futures Wallet creation is not allowed for currency_short_name: <currency_short_name> | Futures wallet creation not allowed for currency |
| 422 | This feature is not enabled yet. | Futures wallet not enabled for user |
| 404 | Wallet not found | Futures wallet not created for user |
| 400 | Insufficient funds | Amount to be transferred is more than the available wallet balance |

# Order

      Enum definitions for the purpose of order are as follows:

| Name | Values |
| --- | --- |
| side | buy, sell |
| order_type | market_order, limit_order |
| order_status | open, partially_filled, filled, cancelled, rejected, partially_cancelled, init |
| ecode | I, B, HB, KC |

## New Order

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "side": "buy",    #Toggle between 'buy' or 'sell'.
      "order_type": "limit_order", #Toggle between a 'market_order' or 'limit_order'.
      "market": "SNTBTC", #Replace 'SNTBTC' with your desired market pair.
      "price_per_unit": 0.03244, #This parameter is only required for a 'limit_order'
      "total_quantity": 400, #Replace this with the quantity you want
      "timestamp": timeStamp,
      "client_order_id": "2022.02.14-btcinr_1" #Replace this with the client order id you want
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/orders/create"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
        "side": "buy",  //Toggle between 'buy' or 'sell'.
        "order_type": "limit_order", //Toggle between a 'market_order' or 'limit_order'.
        "market": "SNTBTC", //Replace 'SNTBTC' with your desired market.
        "price_per_unit": "0.03244", //This parameter is only required for a 'limit_order'
        "total_quantity": 400, //Replace this with the quantity you want
        "timestamp": timeStamp,
        "client_order_id": "2022.02.14-btcinr_1" //Replace this with the client order id you want
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/orders/create",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(body);
    })

> Response:

      

    {
       "orders":[
         {
            "id":"ead19992-43fd-11e8-b027-bb815bcb14ed",
            "client_order_id": "2022.02.14-btcinr_1",
            "market":"TRXETH",
            "order_type":"limit_order",
            "side":"buy",
            "status":"open",
            "fee_amount":0.0000008,
            "fee":0.1,
            "total_quantity":2,
            "remaining_quantity":2.0,
            "avg_price":0.0,
            "price_per_unit":0.00001567,
            "created_at":"2018-04-19T18:17:28.022Z",
            "updated_at":"2018-04-19T18:17:28.022Z"
         }
       ]
    }

      Use this endpoint to place a new order on the exchange

 You can only have a maximum of **25 open orders** at a time for one specific market

### HTTP Request

      `POST /exchange/v1/orders/create`

### Request Parameters

| Name | Required | Example | Description |
| --- | --- | --- | --- |
| market | Yes | SNTBTC | The trading pair |
| total_quantity | Yes | 1.101 | Quantity to trade |
| price_per_unit | No | 0.082 | Price per unit (not required for market order) |
| side | Yes | buy | Specify buy or sell |
| order_type | Yes | market_order | Order Type |
| client_order_id | No | 2022.02.14-btcinr_1 | Client order id of the order |
| timestamp | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

### Response Parameters

| Name | Description |
| --- | --- |
| id | It's system generated order id |
| client_order_id | It's provided while placing order by the user |
| market | Market for which order has been placed |
| side | Side provided while placing order |
| order_type | Order Type provided while placing order |
| status | This tells the current status of the order. For example: When the order firstly is placed, the status shows `open` |
| fee_amount | Amount of fee charged to the user if the order gets executed and moved to the `filled` status |
| fee | This is a Fee in percentage that is used to calculate `fee_amount` |
| total_quantity | Quantity provided while placing order |
| remaining_quantity | Quantity remaining to be filled |
| avg_price | The price on which the user's order gets executed, it's `0.0` when order is in `open` status |
| price_per_unit | `price_per_unit` provided while placing order |
| created_at | It's a time when order was placed |
| updated_at | It's a time when anything related to the order was updated. For example `avg_price`, `total_quantity`, `status` etc |

## Create Multiple Orders

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "orders": [
      {
        "side": "buy",  #Toggle between 'buy' or 'sell'.
        "order_type": "limit_order", #Toggle between a 'market_order' or 'limit_order'.
        "market": "SNTBTC", #Replace 'SNTBTC' with your desired market pair.
        "price_per_unit": 0.03244, #This parameter is only required for a 'limit_order'
        "total_quantity": 400, #Replace this with the quantity you want
        "timestamp": timeStamp,
        "ecode": "I",
        "client_order_id": "2022.02.14-btcinr_1" #Replace this with the client order id you want
      },
      {
        "side": "buy",  #Toggle between 'buy' or 'sell'.
        "order_type": "limit_order", #Toggle between a 'market_order' or 'limit_order'.
        "market": "SNTBTC", #Replace 'SNTBTC' with your desired market pair.
        "price_per_unit": 0.03244, #This parameter is only required for a 'limit_order'
        "total_quantity": 400, #Replace this with the quantity you want
        "timestamp": timeStamp,
        "ecode": "I"
        }
      ]
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/orders/create_multiple"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {"orders": [{
              "side": "buy",  //Toggle between 'buy' or 'sell'.
              "order_type": "limit_order", //Toggle between a 'market_order' or 'limit_order'.
              "market": "BTCINR", //Replace 'SNTBTC' with your desired market.
              "price_per_unit": "466330", //This parameter is only required for a 'limit_order'
              "total_quantity": 0.01, //Replace this with the quantity you want
              "timestamp": timeStamp,
              "ecode": "I",
              "client_order_id": "2022.02.14-btcinr_1" //Replace this with the client order id you want
            },
            {
              "side": "buy",  //Toggle between 'buy' or 'sell'.
              "order_type": "limit_order", //Toggle between a 'market_order' or 'limit_order'.
              "market": "BTCINR", //Replace 'SNTBTC' with your desired market.
              "price_per_unit": "466330", //This parameter is only required for a 'limit_order'
              "total_quantity": 0.01, //Replace this with the quantity you want
              "timestamp": timeStamp,
              "ecode": "I"
            }
          ]}

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
      url: baseurl + "/exchange/v1/orders/create_multiple",
      headers: {
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
      },
      json: true,
      body: body
    }

    request.post(options, function(error, response, body) {
      console.log(body);
    })

> Response:

      

    {
       "orders":[
         {
            "id":"ead19992-43fd-11e8-b027-bb815bcb14ed",
            "client_order_id": "2022.02.14-btcinr_1",
            "market":"TRXETH",
            "order_type":"limit_order",
            "side":"buy",
            "status":"open",
            "fee_amount":0.0000008,
            "fee":0.1,
            "total_quantity":2,
            "remaining_quantity":2.0,
            "avg_price":0.0,
            "price_per_unit":0.00001567,
            "created_at":"2018-04-19T18:17:28.022Z",
            "updated_at":"2018-04-19T18:17:28.022Z"
         }
       ]
    }

 Multiple ordering API is only supported for CoinDCX INR markets. Set ecode parameter to `I`

      Use this endpoint to place a multiple orders on the exchange

### HTTP Request

      `POST /exchange/v1/orders/create_multiple`

### Parameters in an array of objects

| Name | Required | Example | Description |
| --- | --- | --- | --- |
| market | Yes | SNTBTC | The trading pair |
| total_quantity | Yes | 1.101 | Quantity to trade |
| price_per_unit | No | 0.082 | Price per unit (not required for market order) |
| side | Yes | buy | Specify buy or sell |
| order_type | Yes | market_order | Order Type |
| ecode | Yes | I | Exchange code |
| client_order_id | No | 2022.02.14-btcinr_1 | Client order id of the order |
| timestamp | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

## Order Status

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "id": "ead19992-43fd-11e8-b027-bb815bcb14ed", # Enter your Order ID here.
      # "client_order_id": "2022.02.14-btcinr_1", # Enter your Client Order ID here.
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/orders/status"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
        // "id": "qwd19992-43fd-14e8-b027-bb815bnb14ed", //Replace it with your Order ID.
        "client_order_id": "2022.02.14-btcinr_1", //Replace it with your Client Order ID.
        "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/orders/status",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(body);
    })
> Response:

      

    {
      "id":"ead19992-43fd-11e8-b027-bb815bcb14ed",
      "client_order_id": "2022.02.14-btcinr_1",
      "market":"TRXETH",
      "order_type":"limit_order",
      "side":"buy",
      "status":"open",
      "fee_amount":0.0000008,
      "fee":0.1,
      "total_quantity":2,
      "remaining_quantity":2.0,
      "avg_price":0.0,
      "price_per_unit":0.00001567,
      "created_at":"2018-04-19T18:17:28.022Z",
      "updated_at":"2018-04-19T18:17:28.022Z"
    }

      Use this endpoint to fetch status of any order

### HTTP Request

      `POST /exchange/v1/orders/status`

### Parameters

| Name | Required | Example | Description |
| --- | --- | --- | --- |
| id | No | ead19992-43fd-11e8-b027-bb815bcb14ed | The ID of the order |
| client_order_id | No | 2022.02.14-btcinr_1 | The Client Order ID of the order |
| timestamp | Yes | 1524211224 | When was the request generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

      Note: id or client_order_id one of the paramter is required.

## Multiple Order Status

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      # "ids": ["8a2f4284-c895-11e8-9e00-5b2c002a6ff4", "8a1d1e4c-c895-11e8-9dff-df1480546936"], # Array of Order ids
      "client_order_ids": ["2022.02.14-btcinr_1", "2022.02.14-btcinr_2"], # Array of Client Order ids
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/orders/status_multiple"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "ids": ["8a2f4284-c895-11e8-9e00-5b2c002a6ff4", "8a1d1e4c-c895-11e8-9dff-df1480546936"], // Array of Order ids
      // "client_order_ids": ["2022.02.14-btcinr_1", "2022.02.14-btcinr_2"], // Array of Client Order ids
      "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
      url: baseurl + "/exchange/v1/orders/status_multiple",
      headers: {
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
      },
      json: true,
      body: body
    }

    request.post(options, function(error, response, body) {
      console.log(body);
    })
> Response:

      

    [
      {
        "id":"ead19992-43fd-11e8-b027-bb815bcb14ed",
        "client_order_id": "2022.02.14-btcinr_1",
        "market":"TRXETH",
        "order_type":"limit_order",
        "side":"buy",
        "status":"open",
        "fee_amount":0.0000008,
        "fee":0.1,
        "total_quantity":2,
        "remaining_quantity":2.0,
        "avg_price":0.0,
        "price_per_unit":0.00001567,
        "created_at":"2018-04-19T18:17:28.022Z",
        "updated_at":"2018-04-19T18:17:28.022Z"
      }
    ]

      Use this endpoint to fetch status of any order

### HTTP Request

      `POST /exchange/v1/orders/status_multiple`

### Parameters

| Name | Required | Example | Description |
| --- | --- | --- | --- |
| ids | No | ["ead19992-43fd-11e8-b027-bb815bcb14ed", "8a1d1e4c-c895-11e8-9dff-df1480546936"] | Array of order IDs |
| client_order_ids | No | ["2022.02.14-btcinr_1", "2022.02.14-btcinr_2"] | Array of client order IDs |
| timestamp | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

      Note: id or client_order_id one of the paramter is required.

## Active Orders

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
        "side": "buy", # Toggle between a 'buy' or 'sell' order.
        "market": "SNTBTC", # Replace 'SNTBTC' with your desired market pair.
        "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/orders/active_orders"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
        "side": "buy", //Toggle between 'buy' or 'sell'.
        "market": "SNTBTC", //Replace 'SNTBTC' with your desired market pair.
        "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/orders/active_orders",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(body);
    })
> Response:

      

    [
      {
        "id":"ead19992-43fd-11e8-b027-bb815bcb14ed",
        "client_order_id": "2022.02.14-btcinr_1",
        "market":"TRXETH",
        "order_type":"limit_order",
        "side":"buy",
        "status":"open",
        "fee_amount":0.0000008,
        "fee":0.1,
        "total_quantity":2,
        "remaining_quantity":2.0,
        "avg_price":0.0,
        "price_per_unit":0.00001567,
        "created_at":"2018-04-19T18:17:28.022Z",
        "updated_at":"2018-04-19T18:17:28.022Z"
      }
    ]

      Use this endpoint to fetch active orders

### HTTP Request

      `POST /exchange/v1/orders/active_orders`

### Parameters

| Name | Required | Example | Description |
| --- | --- | --- | --- |
| market | Yes | SNTBTC |  |
| side | No | buy |  |
| timestamp | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

## Account Trade History

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "from_id": 352622,
      "limit": 50,
      "timestamp": timeStamp,
      "sort": "asc",
      "from_timestamp": 1514745000000, # replace this with your from timestamp filter
      "to_timestamp": 1514745000000, # replace this with your to timestamp filter
      "symbol": "BCHBTC" # replace this with your symbol filter
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/orders/trade_history"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "from_id": 352622,
      "limit": 50,
      "timestamp": timestamp,
      "sort": "asc",
      "from_timestamp": 1514745000000, // replace this with your from timestamp filter
      "to_timestamp": 1514745000000, // replace this with your to timestamp filter
      "symbol": "BCHBTC" // replace this with your symbol filter
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
      url: baseurl + "/exchange/v1/orders/trade_history",
      headers: {
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
      },
      json: true,
      body: body
    }

    request.post(options, function(error, response, body) {
      console.log(body);
    })
> Response:

      

    [
      {
        "id":                         564389,
        "order_id":                   "ee060ab6-40ed-11e8-b4b9-3f2ce29cd280",
        "side":                       "buy",
        "fee_amount":                 "0.00001129",
        "ecode":                      "B",
        "quantity":                   67.9,
        "price":                      0.00008272,
        "symbol":                     "SNTBTC",
        "timestamp":                  1533700109811
      }
    ]

      Use this endpoint to fetch trades associated with your account

### HTTP Request

      `POST /exchange/v1/orders/trade_history`

### Parameters

| Name | Required | Example | Description |
| --- | --- | --- | --- |
| limit | No | 100 | Default: 500, Min: 1, Max: 5000 |
| from_id | No | 28473 | Trade ID after which you want the data. If not supplied, trades in ascending order will be returned |
| sort | No | asc | Specify asc or desc to get trades in ascending or descending order, default: asc |
| timestamp | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |
| from_timestamp | No | 1514745000000 | Timestamp after which you want the data. If not supplied, all trades from starting will be returned |
| to_timestamp | No | 1514745000000 | Timestamp before which you want the data. If not supplied, all trades till now will be returned |
| symbol | No | SNTBTC | Symbol for which you want the data. If not supplied, trades from all symbols will be returned |

## Active Orders Count

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "side": "buy", # Toggle between a 'buy' or 'sell' order.
      "market": "SNTBTC", # Replace 'SNTBTC' with your desired market pair.
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/orders/active_orders_count"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
        "side": "buy", //Toggle between 'buy' or 'sell'.
        "market": "SNTBTC", //Replace 'SNTBTC' with your desired market pair.
        "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/orders/active_orders_count",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(body);
    })
> Response:

      

     { count: 1, status: 200 }

      Use this endpoint to fetch active orders count

### HTTP Request

      `POST /exchange/v1/orders/active_orders_count`

### Parameters

| Name | Required | Example | Description |
| --- | --- | --- | --- |
| market | Yes | SNTBTC |  |
| side | No | buy |  |
| timestamp | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

## Cancel All

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "side": "buy", # Toggle between a 'buy' or 'sell' order.
      "market": "SNTBTC", # Replace 'SNTBTC' with your desired market pair.
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/orders/cancel_all"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const   body = {
            "side": "buy", //Toggle between 'buy' or 'sell'. Not compulsory
            "market": "SNTBTC", //Replace 'SNTBTC' with your desired market pair.
            "timestamp": timeStamp
        }

        const payload = new Buffer(JSON.stringify(body)).toString();
        const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

        const options = {
            url: baseurl + "/exchange/v1/orders/cancel_all",
            headers: {
                'X-AUTH-APIKEY': key,
                'X-AUTH-SIGNATURE': signature
            },
            json: true,
            body: body
        }

        request.post(options, function(error, response, body) {
            console.log(body);
        })
> Response:

      



      Use this endpoint to cancel multiple active orders in a single API call

### HTTP Request

      `POST /exchange/v1/orders/cancel_all`

### Parameters

| Name | Required | Example | Description |
| --- | --- | --- | --- |
| market | Yes | SNTBTC |  |
| side | No | buy |  |
| timestamp | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

      Sending side param is optional. You may cancel all the sell orders of SNTBTC by sending  
`{market: "SNTBTC", side  : "sell"}`

      Or you may cancel all your orders in SNTBTC market by sending  
`{market: "SNTBTC"}`

## Cancel Order By Multiple Ids

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "ids": ["8a2f4284-c895-11e8-9e00-5b2c002a6ff4", "8a1d1e4c-c895-11e8-9dff-df1480546936"]
      # "client_order_ids": ["2022.02.14-btcinr_1", "2022.02.14-btcinr_2"] # Array of client_order_ids
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/orders/cancel_by_ids"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
        ids: ["8a2f4284-c895-11e8-9e00-5b2c002a6ff4", "8a1d1e4c-c895-11e8-9dff-df1480546936"] // Array of order_ids
        // client_order_ids: ["2022.02.14-btcinr_1", "2022.02.14-btcinr_2"] // Array of client_order_ids
      }

      const payload = new Buffer(JSON.stringify(body)).toString();
      const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

      const options = {
        url: baseurl + "/exchange/v1/orders/cancel_by_ids",
        headers: {
          'X-AUTH-APIKEY': key,
          'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
      }

      request.post(options, function(error, response, body) {
        console.log(body);
      })
> Response:

      



      Use this endpoint to cancel multiple active orders in a single API call

### HTTP Request

      `POST /exchange/v1/orders/cancel_by_ids`

### Parameters

| Name | Required | Example | Description |
| --- | --- | --- | --- |
| ids | No | ["8a2f4284-c895-11e8-9e00-5b2c002a6ff4", "8a1d1e4c-c895-11e8-9dff-df1480546936"] | Array of order IDs |
| client_order_ids | No | ["2022.02.14-btcinr_1", "2022.02.14-btcinr_2"] | Array of Client Order IDs |

      Note: id or client_order_id one of the paramter is required.

## Cancel

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from CoinDCX website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
        "id": "ead19992-43fd-11e8-b027-bb815bcb14ed", # Enter your Order ID here.
        # "client_order_id": "2022.02.14-btcinr_1", # Enter your Client Order ID here.
        "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/orders/cancel"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
        "id": "ead19992-43fd-11e8-b027-bb815bcb14ed", // Replace this with your Order ID.
        // "client_order_id": "2022.02.14-btcinr_1", // Replace this with your Client Order ID.
        "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/orders/cancel",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(body);
    })

> Response:

      



      Use this endpoint to cancel an active orders

### HTTP Request

      `POST /exchange/v1/orders/cancel`

### Parameters

| Name | Required | Example | Description |
| --- | --- | --- | --- |
| id | No | ead19992-43fd-11e8-b027-bb815bcb14ed | The ID of the order |
| client_order_id | No | 2022.02.14-btcinr_1 | The Client Order ID of the order |
| timestamp | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

      Note: id or client_order_id one of the paramter is required.

## Edit Price

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from CoinDCX website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", # Enter your Order ID here.
      "timestamp": timeStamp,
      "price_per_unit": 123.45 # Enter the new-price here
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/orders/edit"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "XXXX";
    const secret = "YYYY";

    const body = {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", // Enter your Order ID here.
      // "client_order_id": "2022.02.14-btcinr_1", // Replace this with your Client Order ID.
      "timestamp": timeStamp,
      "price_per_unit": 123.45 // Enter the new-price here
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/orders/edit",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(body);
    })

> Response:

      

    {
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "market": "TRXETH",
      "order_type": "limit_order",
      "side": "buy",
      "status": "open",
      "fee_amount": 0.0000008,
      "fee": 0.1,
      "total_quantity": 2,
      "remaining_quantity": 2.0,
      "avg_price": 0.0,
      "price_per_unit": 123.45,
      "created_at": "2020-12-12T18:17:28.022Z",
      "updated_at": "2020-12-12T18:17:28.022Z"
    }

      Use this endpoint to edit the price of an active order

### HTTP Request

      `POST /exchange/v1/orders/edit`

### Parameters

| Name | Required | Example | Description |
| --- | --- | --- | --- |
| id | No | ead19992-43fd-11e8-b027-bb815bcb14ed | The ID of the order |
| client_order_id | No | 2022.02.14-btcinr_1 | The Client Order ID of the order |
| price_per_unit | Yes | 123.45 | New Price for the order |
| timestamp | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

      Note: id or client_order_id one of the paramter is required.

# Lend Order

## Fetch Orders

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/funding/fetch_orders"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/funding/fetch_orders",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(body);
    })
> Response:

      


    [ { "id": "caa1e032-5763-42a5-9684-587bc1a846d8",
        "currency_short_name": "USDT",
        "amount": 0.01,
        "title": "Tether",
        "interest": 0.1,
        "interest_type": "simple",
        "duration": 8,
        "side": "lend",
        "expiry": 1564666811940,
        "status": "close",
        "created_at": 1563975611942,
        "settled_at": 1565615166177 },
      { "id": "1212ad3d-8a5b-4965-9d21-151efc0c84d7",
        "currency_short_name": "BTC",
        "amount": 0.01,
        "title": "Bitcoin",
        "interest": 0.1,
        "interest_type": "simple",
        "duration": 8,
        "side": "lend",
        "expiry": 1564666764834,
        "status": "close",
        "created_at": 1563975564836,
        "settled_at": 1563975597184 } ]

This API supports **Pagination** Refer **[Pagination section](#pagination)** for more details

      Use this endpoint to fetch orders and its details

### HTTP Request

      `POST /exchange/v1/funding/fetch_orders`

### Parameters

| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| timestamp | number | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

## Lend

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "currency_short_name": "BTC",
      "duration": 20,
      "amount": 0.5,
      "timestamp": timeStamp
    }
    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/funding/lend"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "currency_short_name": "BTC",
      "duration": 20,
      "amount": 0.5,
      "timestamp": timeStamp
    },


    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/funding/lend",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(body);
    })

> Response:

      


    [ { "id": "df7d9640-29e8-4731-9fc6-ec2f738507e2",
        "currency_short_name": "XRP",
        "amount": 11,
        "interest": 0.05,
        "title": "Ripple",
        "interest_type": "simple",
        "duration": 20,
        "side": "lend",
        "expiry": 1576069883995,
        "status": "open",
        "created_at": 1574341883998,
        "settled_at": null } ]


      Use this endpoint to lend specified currency on the exchange.

### HTTP Request

      `POST /exchange/v1/funding/lend`

### Parameters

| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| currency_short_name | string | Yes | XRP | The lending currency |
| amount | number | Yes | 11 | Quantity to lend |
| duration | number | Yes | 20 | The Time period for which you want to lend the currency in days |
| timestamp | number | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

## Settle

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from CoinDCX website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "id": "ead19992-43fd-11e8-b027-bb815bcb14ed",
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/funding/settle"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "id": "ead19992-43fd-11e8-b027-bb815bcb14ed",
      "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/funding/settle",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(body);
    })

> Response:

      


    [ { "id": "df7d9640-29e8-4731-9fc6-ec2f738507e2",
        "currency_short_name": "XRP",
        "amount": 11,
        "interest": 0.05,
        "title": "Ripple",
        "interest_type": "simple",
        "duration": 20,
        "side": "lend",
        "expiry": 1576069883995,
        "status": "exit",
        "created_at": 1574341883998,
        "settled_at": 1574342058493 } ]



      Use this endpoint to settle lend order.

### HTTP Request

      `POST /exchange/v1/funding/settle`

### Parameters

| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| id | string | Yes | ead19992-43fd-11e8-b027-bb815bcb14ed | The ID of the order |
| timestamp | number | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

# Margin Order

 Set ecode parameter to `B` for all the api calls wherever necessary

      Enum definitions for the purpose of order are as follows:

| Name | Values |
| --- | --- |
| side | buy, sell |
| order_type | market_order, limit_order, stop_limit, take_profit |
| order_status | init, partial_entry, open, partial_close, close, cancelled, rejected, triggered |
| timestamp | 1524211224 |
| ecode | B |

## Place Order

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "side": "buy",
      "order_type": "limit_order",
      "market": "XRPBTC",
      "price": 0.000025,
      "quantity": 90,
      "ecode": 'B',
      "leverage": 1.0,
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/margin/create"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "side": "buy",
      "order_type": "limit_order",
      "market": "XRPBTC",
      "price": 0.000025,
      "quantity": 90,
      "ecode": 'B',
      "leverage": 1,
      "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/margin/create",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(JSON.stringify(body, null, 2));
    })

> Response:

      

    [{
      "id": "30b5002f-d9c1-413d-8a8d-0fd32b054c9c",
      "side": "sell",
      "status": "init",
      "market": "XRPBTC",
      "order_type": "limit_order",
      "trailing_sl": false,
      "trail_percent": null,
      "avg_entry": 0,
      "avg_exit": 0,
      "fee": 0.02,
      "entry_fee": 0,
      "exit_fee": 0,
      "active_pos": 0,
      "exit_pos": 0,
      "total_pos": 0,
      "quantity": 200,
      "price": 0.000026,
      "sl_price": 0.00005005,
      "target_price": 0,
      "stop_price": 0,
      "pnl": 0,
      "initial_margin": 0.00520208,
      "interest": 0.05,
      "interest_amount": 0,
      "leverage": 1,
      "result": null,
      "created_at": 1568122929782,
      "updated_at": 1568122929782,
      "orders":[{
        "id": 164993,
        "order_type": "limit_order",
        "status": "initial",
        "market": "XRPBTC",
        "side": "sell",
        "avg_price": 0,
        "total_quantity": 200,
        "remaining_quantity": 200,
        "price_per_unit": 0.000026,
        "timestamp": 1568122929880.75,
        "fee": 0.02,
        "fee_amount": 0,
        "filled_quantity": 0,
        "bo_stage": "stage_entry",
        "cancelled_quantity": 0,
        "stop_price": 0
      }]
    }]

      Use this endpoint to place a new order on the exchange.

 You can only have a maximum of **10 open orders** at a time for one specific market

### HTTP Request

      `POST /exchange/v1/margin/create`

### Parameters

| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| market | string | Yes | XRPBTC | The trading pair |
| quantity | number | Yes | 1.101 | Quantity to trade |
| price | number | No | 0.082 | Price per unit (not required for market order, mandatory for rest) |
| leverage | number | No | 1 | Borrowed capital to increase the potential returns |
| side | string | Yes | buy | Specify buy or sell |
| stop_price | number | No | 0.082 | Price to stop the order at(mandatory in case of stop_limit & take_profit) |
| order_type | string | Yes | market_order | Order Type |
| trailing_sl | boolean | No | true | To place order with Trailing Stop Loss |
| target_price | number | No | 0.082 | The price to buy/sell or close the order position |
| ecode | string | Yes | B | Exchange code in which the order will be placed |
| timestamp | number | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

## Cancel Order

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "id": "ead19992-43fd-11e8-b027-bb815bcb14ed",
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/margin/cancel"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "id": "qwd19992-43fd-14e8-b027-bb815bnb14ed",
      "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/margin/cancel",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(body);
    })
> Response:

      

    {
      "message": "Cancellation accepted",
      "status": 200,
      "code": 200
    }


Any order with **order_status** among the following can only be cancelled:   
 init, partial_entry, or triggered

      Use this endpoint to cancel any order.

### HTTP Request

      `POST /exchange/v1/margin/cancel`

### Parameters

| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| id | string | Yes | ead19992-43fd-11e8-b027-bb815bcb14ed | The ID of the order |
| timestamp | number | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

## Exit

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from CoinDCX website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "id": "ead19992-43fd-11e8-b027-bb815bcb14ed",
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/margin/exit"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "id": "ead19992-43fd-11e8-b027-bb815bcb14ed",
      "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/margin/exit",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(body);
    })

> Response:

      

    {
      "message": "Order exit accepted",
      "status": 200,
      "code": 200
    }


Any order with **order_status** among the following can only be exited:   
 open or partial_close

      Use this endpoint to exit any order.

### HTTP Request

      `POST /exchange/v1/margin/exit`

### Parameters

| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| id | string | Yes | ead19992-43fd-11e8-b027-bb815bcb14ed | The ID of the order |
| timestamp | number | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

## Edit Target

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "id": "8a2f4284-c895-11e8-9e00-5b2c002a6ff4",
      "target_price": 0.6,
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/margin/edit_target"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "id": "8a2f4284-c895-11e8-9e00-5b2c002a6ff4",
      "target_price": 0.6,
      "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
      url: baseurl + "/exchange/v1/margin/edit_target",
      headers: {
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
      },
      json: true,
      body: body
    }

    request.post(options, function(error, response, body) {
      console.log(body);
    })
> Response:

      

    {
      "message": "Target price updated",
      "status": 200,
      "code": 200
    }


You can update target price only if order has 0 or 1 target order. For the multiple open targets refer- **[Edit Price of Target Order](#edit-price-of-target-order)** section

      Use this endpoint to edit the target price of any order.

### HTTP Request

      `POST /exchange/v1/margin/edit_target`

### Parameters

| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| id | string | Yes | 8a2f4284-c895-11e8-9e00-5b2c002a6ff4 | ID of the order to edit |
| target_price | number | Yes | 0.082 | The new price to buy/sell or close the order position at |
| timestamp | number | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

## Edit Price of Target Order

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "id": "",
      "target_price": 0.00026,
      "itpo_id": "",
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/margin/edit_price_of_target_order"

    headers = {
      'Content-Type': 'application/json',
      'X-AUTH-APIKEY': key,
      'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "id": "",
      "target_price": 0.00026,
      "itpo_id": "",
      "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/margin/edit_price_of_target_order",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(body);
    })
> Response:

      

    {
      "message": "Target price updated",
      "status": 200,
      "code": 200
    }

      Use this endpoint to edit price of internal target order.

### HTTP Request

      `POST /exchange/v1/margin/edit_price_of_target_order`

### Parameters

| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| id | string | Yes | ead19992-43fd-11e8-b027-bb815bcb14ed |  |
| target_price | number | Yes | 0.082 | The new price to buy/sell or close the order position at |
| itpo_id | string | Yes | 164968 | ID of internal order to edit |
| timestamp | number | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

## Edit SL Price

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "id" : "",
      "sl_price": 0.06,
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/margin/edit_sl"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "id" : "",
      "sl_price": 0.06,
      "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
      url: baseurl + "/exchange/v1/margin/edit_sl",
      headers: {
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
      },
      json: true,
      body: body
    }

    request.post(options, function(error, response, body) {
      console.log(body);
    })
> Response:

      

    {
      "message": "SL price updated",
      "status": 200,
      "code": 200
    }

Only for orders where **trailing_sl is false**

      Use this endpoint to edit stop loss price of a bracket order.

### HTTP Request

      `POST /exchange/v1/margin/edit_sl`

### Parameters

| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| id | string | Yes | ead19992-43fd-11e8-b027-bb815bcb14ed | ID of Margin Order |
| sl_price | number | Yes | 0.082 | The price to Stop Loss at |
| timestamp | number | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

## Edit SL Price of Trailing Stop Loss

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "id" : "",
      "sl_price": 0.06,
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/margin/edit_trailing_sl"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "id" : "",
      "sl_price": 0.06,
      "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
      url: baseurl + "/exchange/v1/margin/edit_trailing_sl",
      headers: {
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
      },
      json: true,
      body: body
    }

    request.post(options, function(error, response, body) {
      console.log(body);
    })
> Response

      

    {
      "message": "Trailing SL price updated",
      "status": 200,
      "code": 200
    }

Only for orders where **trailing_sl is true**

      Use this endpoint to edit stop loss price of a trailing stop loss order.

### HTTP Request

      `POST /exchange/v1/margin/edit_trailing_sl`

### Parameters

| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| id | string | Yes | ead19992-43fd-11e8-b027-bb815bcb14ed | ID of Margin Order |
| sl_price | number | Yes | 0.082 | The new price to Stop Loss at |
| timestamp | number | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

## Add Margin

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "id" : "",
      "amount": 0.06,
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/margin/add_margin"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "id" : "",
      "amount": 0.06,
      "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
      url: baseurl + "/exchange/v1/margin/add_margin",
      headers: {
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
      },
      json: true,
      body: body
    }

    request.post(options, function(error, response, body) {
      console.log(body);
    })
> Response

      

    {
      "message": "Margin added successfully",
      "status": 200,
      "code": 200
    }

      Use this endpoint to add a particular amount to your margin order, decreasing the effective leverage.

### HTTP Request

      `POST /exchange/v1/margin/add_margin`

### Parameters

| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| id | string | Yes | ead19992-43fd-11e8-b027-bb815bcb14ed | ID of Margin Order |
| amount | number | Yes | 0.06 | Amount to add in the margin to decrease effective leverage |
| timestamp | number | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

## Remove Margin

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "id" : "",
      "amount": 0.06, initial margin.
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/margin/remove_margin"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "id" : "",
      "amount": 0.06,
      "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
      url: baseurl + "/exchange/v1/margin/remove_margin",
      headers: {
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
      },
      json: true,
      body: body
    }

    request.post(options, function(error, response, body) {
      console.log(body);
    })
> Response

      

    {
      "message": "Margin removed successfully",
      "status": 200,
      "code": 200
    }

      Use this endpoint to remove a particular amount from your Margin order, increasing the effective leverage.

### HTTP Request

      `POST /exchange/v1/margin/remove_margin`

### Parameters

| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| id | string | Yes | ead19992-43fd-11e8-b027-bb815bcb14ed | ID of Margin Order |
| amount | number | Yes | 0.06 | Amount to remove from the margin to increase effective leverage |
| timestamp | number | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

## Fetch Orders

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "details": True,
      "market": "LTCBTC",
      "status":"close",
      "size":20,
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/margin/fetch_orders"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "details": true,
      "market": "LTCBTC",
      "status":"open",
      "size":20,
      "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/margin/fetch_orders",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(JSON.stringify(body, null, 2));
    })
> Response:

      

    [{
        "id": "30b5002f-d9c1-413d-8a8d-0fd32b054c9c",
        "side": "sell",
        "status": "rejected",
        "market": "XRPBTC",
        "order_type": "limit_order",
        "trailing_sl": false,
        "trail_percent": null,
        "avg_entry": 0,
        "avg_exit": 0,
        "fee": 0.02,
        "entry_fee": 0,
        "exit_fee": 0,
        "active_pos": 0,
        "exit_pos": 0,
        "total_pos": 0,
        "quantity": 200,
        "price": 0.000026,
        "sl_price": 0.00005005,
        "target_price": 0,
        "stop_price": 0,
        "pnl": 0,
        "initial_margin": 0,
        "interest": 0.05,
        "interest_amount": 0,
        "leverage": 1,
        "result": null,
        "created_at": 1568122929782,
        "updated_at": 1568122930404,
        "orders": [{
          "id": 164993,
          "order_type": "limit_order",
          "status": "rejected",
          "market": "XRPBTC",
          "side": "sell",
          "avg_price": 0,
          "total_quantity": 200,
          "remaining_quantity": 200,
          "price_per_unit": 0.000026,
          "timestamp": 1568122929880.75,
          "fee": 0.02,
          "fee_amount": 0,
          "filled_quantity": 0,
          "bo_stage": "stage_entry",
          "cancelled_quantity": 0,
          "stop_price": 0
        }]
      },
      {
        "id": "e45cd26a-32e9-4d20-b230-a8933046f4eb",
        "side": "sell",
        "status": "rejected",
        "market": "XRPBTC",
        "order_type": "limit_order",
        "trailing_sl": false,
        "trail_percent": null,
        "avg_entry": 0,
        "avg_exit": 0,
        "fee": 0.02,
        "entry_fee": 0,
        "exit_fee": 0,
        "active_pos": 0,
        "exit_pos": 0,
        "total_pos": 0,
        "quantity": 200,
        "price": 0.000026,
        "sl_price": 0.00005005,
        "target_price": 0,
        "stop_price": 0,
        "pnl": 0,
        "initial_margin": 0,
        "interest": 0.05,
        "interest_amount": 0,
        "leverage": 1,
        "result": null,
        "created_at": 1568122721421,
        "updated_at": 1568122721905,
        "orders": [{
          "id": 164993,
          "order_type": "limit_order",
          "status": "rejected",
          "market": "XRPBTC",
          "side": "sell",
          "avg_price": 0,
          "total_quantity": 200,
          "remaining_quantity": 200,
          "price_per_unit": 0.000026,
          "timestamp": 1568122929880.75,
          "fee": 0.02,
          "fee_amount": 0,
          "filled_quantity": 0,
          "bo_stage": "stage_entry",
          "cancelled_quantity": 0,
          "stop_price": 0
        }]
      }
    ]

This API supports **Pagination** Refer **[Pagination section](#pagination)** for more details

      Use this endpoint to fetch orders and optionally its details which include all buy/sell related orders

### HTTP Request

      `POST /exchange/v1/margin/fetch_orders`

### Parameters

| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| market | string | No | XRPBTC | The trading pair, default: Orders for all market |
| details | boolean | No | false | Whether you want detailed information or not, default: false |
| status | string | No | init,open,close,rejected,cancelled,      partial_entry,partial_close,triggered | The status of the order, default: All orders |
| size | number | No | 20 | Number of records per page, default: 10 |
| timestamp | number | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

## Query Order

      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    body = {
      "details": true,
      "id": "30b5002f-d9c1-413d-8a8d-0fd32b054c9c",
      "timestamp": timeStamp
    }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/margin/order"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "details": true,
      "id": "30b5002f-d9c1-413d-8a8d-0fd32b054c9c",
      "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/margin/order",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(JSON.stringify(body, null, 2));
    })
> Response:

      

    [{
        "id": "30b5002f-d9c1-413d-8a8d-0fd32b054c9c",
        "side": "sell",
        "status": "rejected",
        "market": "XRPBTC",
        "order_type": "limit_order",
        "trailing_sl": false,
        "trail_percent": null,
        "avg_entry": 0,
        "avg_exit": 0,
        "fee": 0.02,
        "entry_fee": 0,
        "exit_fee": 0,
        "active_pos": 0,
        "exit_pos": 0,
        "total_pos": 0,
        "quantity": 200,
        "price": 0.000026,
        "sl_price": 0.00005005,
        "target_price": 0,
        "stop_price": 0,
        "pnl": 0,
        "initial_margin": 0,
        "interest": 0.05,
        "interest_amount": 0,
        "leverage": 1,
        "result": null,
        "created_at": 1568122929782,
        "updated_at": 1568122930404,
        "orders": [{
          "id": 164993,
          "order_type": "limit_order",
          "status": "rejected",
          "market": "XRPBTC",
          "side": "sell",
          "avg_price": 0,
          "total_quantity": 200,
          "remaining_quantity": 200,
          "price_per_unit": 0.000026,
          "timestamp": 1568122929880.75,
          "fee": 0.02,
          "fee_amount": 0,
          "filled_quantity": 0,
          "bo_stage": "stage_entry",
          "cancelled_quantity": 0,
          "stop_price": 0
        }]
      }
    ]


      Use this endpoint to query specific order and optionally its details.

### HTTP Request

      `POST /exchange/v1/margin/order`

### Parameters

| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| id | string | Yes | 30b5002f-d9c1-413d-8a8d-0fd32b054c9c | Id of the order |
| details | boolean | No | false | Whether you want detailed information or not, default: false |
| timestamp | number | Yes | 1524211224 | Timestamp at which the request was generated [(see 'Common Notes' under 'Authentication' heading to read more)](#authentication) |

# Pagination

      Get the pagination details in the response header

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
      "details": true,
      "market": "LTCBTC",
      "page": 2,
      "size": 5,
      "timestamp": timeStamp
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/margin/fetch_orders",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(body);
    })


### Parameters

| Name | Description |
| --- | --- |
| page | Page number to fetch. Pagination starts at page 1 |
| size | Number of records per page; Default: 100, Max: 1000 |
> Response Headers

      

    {
      date: 'Wed, 11 Sep 2019 09:38:19 GMT',
      'content-type': 'application/json; charset=utf-8',
      'transfer-encoding': 'chunked',
      connection: 'close',
      status: '200 OK',
      'x-frame-options': 'SAMEORIGIN',
      'x-xss-protection': '1; mode=block',
      'x-content-type-options': 'nosniff',
      'x-pagination': '{"total":29,"total_pages":6,"first_page":false,"last_page":false,"previous_page":1,"next_page":3,"out_of_bounds":false,"offset":5}',
      .
      .
      .
      .
    }

# Spot Sockets

      There are two types of channels


    1. Private (requires authentication)
    2. Public (doesn’t require authentication)

       PUBLIC 

      To connect to public socket

      Refer to the right panel.

       Below chart states the channel to event flow

![Socket channel flow](images/spot_new_sock-ee7e3ada.svg)

      

    import socketio

    def my_headers():
        return {"origin": "*"}

    socketEndpoint = 'https://stream.coindcx.com'
    sio = socketio.Client()

    sio.connect(socketEndpoint, transports = 'websocket')

    # Listen update on channelName
    @sio.on('channelName')
    def on_message(response):
        print(response.data)

    # leave a channel
    sio.emit('leave', { 'channelName' : channelName })

    # Successfull connection
    @sio.event
    def connect():
        sio.emit('join', { 'channelName': 'channelName' })
        print("I'm connected!")

    # Connection error
    @sio.event
    def connect_error(data):
        print("The connection failed!")


      

    import io from 'socket.io-client';

    const socketEndpoint = "https://stream.coindcx.com";

    const socket = io.connect(socketEndpoint, {
      transports: ['websocket'],
      origin: '*',
    });


    //Listen update on channelName
    socket.on('eventName', (response) => {
      console.log(response.data);
    });

    socket.connect();

    // client-side
    socket.on("connect", () => {
      console.log(socket.id,'coindcx'); // x8WIv7-mJelg7on_ALbx
      //Join Channel
      socket.emit('join', {
        'channelName': "channelName",
      });
    });

    // leave a channel
    socket.emit('leave', {
      'channelName': "channelName"
    });

    //These examples has been tested on the following socket.io versions :
    // 1. socket.io-2.3.1.js
    // 2. socket.io-2.3.0.js
    // 3. socket.io-2.2.0.js 
    // 4. socket.io-1.0.0.js 

## Get Balance Update

      

    import socketio
    import hmac
    import hashlib
    import json

    socketEndpoint = 'wss://stream.coindcx.com'
    sio = socketio.Client()

    key = "xxx"
    secret = "xxx"

    secret_bytes = bytes(secret, encoding='utf-8')
    channelName = "coindcx"
    body = {"channel": channelName}
    json_body = json.dumps(body, separators=(',', ':'))
    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    @sio.event
    def connect():
        print("I'm connected!")
        sio.emit('join', {'channelName': channelName, 'authSignature': signature, 'apiKey': key})


    @sio.on('balance-update')
    def on_message(response):
        print("balance-update Response !!!")
        print(response)

    def main():
        try:
            sio.connect(socketEndpoint, transports='websocket')
            while True:
                sio.event('balance-update', {'channelName': channelName})
        except Exception as e:
            print(f"Error connecting to the server: {e}")
            raise


    # Run the main function
    if __name__ == '__main__':
        main()

      

    //For commonJS(NPM)

    // const io = require("socket.io-client");
    // const crypto = require('crypto');

    // ES6 import or TypeScript

    import { Socket, io } from 'socket.io-client';
    import crypto from 'crypto';

    const socketEndpoint = "wss://stream.coindcx.com";

    // Connect to server.
    const socket = io(socketEndpoint, {
      transports: ['websocket']
    });

    const secret = "xxx";
    const key = "xxx";

    const body = { channel: "coindcx" };
    const payload = Buffer.from(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    socket.on("connect", () => {
      // Join channel
      socket.emit('join', {
        'channelName': "coindcx",
        'authSignature': signature,
        'apiKey' : key
      });

    });

    // Listen for updates on "eventName"
    socket.on("balance-update", (response) => {
      console.log(response.data);
    });

    // In order to leave a channel
    socket.emit('leave', {
      'channelName': 'coindcx'
    });

    // NOTE: Make sure you are using a version of socket.io-client that supports the features you need.
> Get Balance Update response:

      

    [
       {
          "id":"102a7916-a622-11ee-bd36-479d3cf6751b",
          "balance":"265.01745775027309",
          "locked_balance":"258.600771",
          "currency_id":"cfe01e2a-f1af-4e52-9696-9a19d9a8eb4f",
          "currency_short_name":"INR"
       }
    ]

### Definitions

    - **Channel:** coindcx (Private).
    - **Event:** balance-update
    - **Description:** This Event gives the wallet balance information whenever there is a change in wallet balance

### Response


    - `id`: Wallet Id
    - `balance`: usable balance
    - `locked_balance`: balance currently being used by an open order
    - `currency_short_name`: currency like LTC, BTC etc.


## Get Order Update

      

    import socketio
    import hmac
    import hashlib
    import json

    socketEndpoint = 'wss://stream.coindcx.com'
    sio = socketio.Client()

    key = "xxx"
    secret = "xxx"

    secret_bytes = bytes(secret, encoding='utf-8')
    channelName = "coindcx"
    body = {"channel": channelName}
    json_body = json.dumps(body, separators=(',', ':'))
    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()


    @sio.event
    def connect():
        print("I'm connected!")
        sio.emit('join', {'channelName': channelName, 'authSignature': signature, 'apiKey': key})


    @sio.on('order-update')
    def on_message(response):
        print("order-update Response !!!")
        print(response)


    def main():
        try:
            sio.connect(socketEndpoint, transports='websocket')
            while True:
                sio.event('order-update', {'channelName': channelName})
        except Exception as e:
            print(f"Error connecting to the server: {e}")
            raise


    # Run the main function
    if __name__ == '__main__':
        main()

      

    //For commonJS(NPM)

    // const io = require("socket.io-client");
    // const crypto = require('crypto');

    // ES6 import or TypeScript

    import { Socket, io } from 'socket.io-client';
    import crypto from 'crypto';

    const socketEndpoint = "wss://stream.coindcx.com";

    // Connect to server.
    const socket = io(socketEndpoint, {
      transports: ['websocket']
    });

    const secret = "xxx";
    const key = "xxx";

    const body = { channel: "coindcx" };
    const payload = Buffer.from(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    socket.on("connect", () => {
      // Join channel
      socket.emit('join', {
        'channelName': "coindcx",
        'authSignature': signature,
        'apiKey' : key
      });

    });

    // Listen for updates on "eventName"
    socket.on("order-update", (response) => {
      console.log(response.data);
    });

    // In order to leave a channel
    socket.emit('leave', {
      'channelName': 'coindcx'
    });

    // NOTE: Make sure you are using a version of socket.io-client that supports the features you need.
> Get Order Update response:

      

    [
       {
          "id":"f6b68656-091c-11ef-92dc-67ec5900cddc",
          "client_order_id":null,
          "order_type":"market_order",
          "side":"buy",
          "status":"filled",
          "fee_amount":1.286714,
          "fee":0.5,
          "maker_fee":0.5,
          "taker_fee":0.5,
          "total_quantity":2.86,
          "remaining_quantity":0,
          "source":"web",
          "base_currency_name":"Indian Rupee",
          "target_currency_name":"Tether",
          "base_currency_short_name":"INR",
          "target_currency_short_name":"USDT",
          "base_currency_precision":2,
          "target_currency_precision":2,
          "avg_price":89.98,
          "price_per_unit":89.97,
          "stop_price":0,
          "market":"USDTINR",
          "time_in_force":"good_till_cancel",
          "created_at":1714720547465,
          "updated_at":1714720547805
       }
    ]


### Definitions

    - **Channel:** coindcx (Private).
    - **Event:** order-update
    - **Description:** This Event gives the order info whenever there is a change in order status

### Response


    - `id`: unique order identifier (uuid)
    - `client_order_id`: client order id of the order
    - `order_type`: the order type
    - `side`: whether the order is a buy order or a sell order
    - `status`: the current [status](https://docs.coindcx.com/?javascript#common)
    - `fee_amount`: total fee amount charged so far (in base-currency)
    - `fee`: deprecated - do not refer - will be removed soon
    - `maker_fee`: the fee (in percentage) to be charged for maker-trades for this order
    - `taker_fee`: the fee (in percentage) to be charged for taker-trades for this order
    - `total_quantity`: total quantity
    - `remaining_quantity`: pending (unfilled/uncancelled) quantity
    - `source`: deprecated - do not refer - will be removed soon
    - `base_currency_name`: deprecated - do not refer - will be removed soon
    - `target_currency_name`: deprecated - do not refer - will be removed soon
    - `base_currency_short_name`: deprecated - do not refer - will be removed soon
    - `target_currency_short_name`: deprecated - do not refer - will be removed soon
    - `base_currency_precision`: deprecated - do not refer - will be removed soon
    - `target_currency_precision`: deprecated - do not refer - will be removed soon
    - `avg_price`: avg-execution price so far
    - `price_per_unit`: specified limit price
    - `stop_price`: specified stop price (applicable for stop-variant orders)
    - `market`: symbol
    - `time_in_force`: just contains one value for now, which is `good_till_cancel`
    - `created_at`: the timestamp for order creation
    - `updated_at`: the latest timestamp specifying when the order was updated


## Get Trade Update

      

    import socketio
    import hmac
    import hashlib
    import json

    socketEndpoint = 'wss://stream.coindcx.com'
    sio = socketio.Client()

    key = "xxx"
    secret = "xxx"

    secret_bytes = bytes(secret, encoding='utf-8')
    channelName = "coindcx"
    body = {"channel": channelName}
    json_body = json.dumps(body, separators=(',', ':'))
    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()


    @sio.event
    def connect():
        print("I'm connected!")
        sio.emit('join', {'channelName': channelName, 'authSignature': signature, 'apiKey': key})


    @sio.on('trade-update')
    def on_message(response):
        print("trade-update Response !!!")
        print(response)


    def main():
        try:
            sio.connect(socketEndpoint, transports='websocket')
            while True:
                sio.event('trade-update', {'channelName': channelName})
        except Exception as e:
            print(f"Error connecting to the server: {e}")
            raise


    # Run the main function
    if __name__ == '__main__':
        main()

      

    //For commonJS(NPM)

    // const io = require("socket.io-client");
    // const crypto = require('crypto');

    // ES6 import or TypeScript

    import { Socket, io } from 'socket.io-client';
    import crypto from 'crypto';

    const socketEndpoint = "wss://stream.coindcx.com";

    // Connect to server.
    const socket = io(socketEndpoint, {
      transports: ['websocket']
    });

    const secret = "xxx";
    const key = "xxx";

    const body = { channel: "coindcx" };
    const payload = Buffer.from(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    socket.on("connect", () => {
      // Join channel
      socket.emit('join', {
        'channelName': "coindcx",
        'authSignature': signature,
        'apiKey' : key
      });

    });

    // Listen for updates on "eventName"
    socket.on("trade-update", (response) => {
      console.log(response.data);
    });

    // In order to leave a channel
    socket.emit('leave', {
      'channelName': 'coindcx'
    });

    // NOTE: Make sure you are using a version of socket.io-client that supports the features you need.
> Get Trade Update response:

      

    [
       {
          "o":"f6b68656-091c-11ef-92dc-67ec5900cddc",
          "c":null,
          "t":"108263519",
          "s":"USDTINR",
          "p":"89.98",
          "q":"2.86",
          "T":1714720547635.6172,
          "m":false,
          "f":"1.286714",
          "e":"I",
          "x":"filled"
       }
    ]


### Definitions

    - **Channel:** coindcx (Private).
    - **Event:** trade-update
    - **Description:** This Event gives the trade info whenever trades are executed.

### Response


    - `o`: system generated order id
    - `c`: client order id
    - `t`: trade id
    - `s`: symbol/market (USDTINR)
    - `p`: price
    - `q`: quantity
    - `T`: timestamp
    - `m`: whether the buyer is market maker or not.
    - `f`: fee amount
    - `e`: exchange identifier
    - `x`: status


## Get Candlestick Info

      

    import socketio

    socketEndpoint = 'wss://stream.coindcx.com'
    sio = socketio.Client()


    @sio.event
    def connect():
        print("I'm connected!")
        sio.emit('join', {'channelName': "B-BTC_USDT_1m"})


    @sio.on('candlestick')
    def on_message(response):
        print("candlestick Response !!!")
        print(response)


    def main():
        try:
            sio.connect(socketEndpoint, transports='websocket')
            while True:
                sio.event('candlestick', {'channelName': "B-BTC_USDT_1m"})
        except Exception as e:
            print(f"Error connecting to the server: {e}")
            raise


    # Run the main function
    if __name__ == '__main__':
        main()

      

    //For commonJS(NPM)

    // const io = require("socket.io-client");
    // const crypto = require('crypto');

    // ES6 import or TypeScript

    import { Socket, io } from 'socket.io-client';
    import crypto from 'crypto';

    const socketEndpoint = "wss://stream.coindcx.com";

    // Connect to server.
    const socket = io(socketEndpoint, {
      transports: ['websocket']
    });

    socket.on("connect", () => {
      // Join channel
      socket.emit('join', {
        'channelName': "B-BTC_USDT_1m"
      });

    });

    // Listen for updates on "eventName"
    socket.on("'candlestick", (response) => {
      console.log(response.data);
    });

    // In order to leave a channel
    socket.emit('leave', {
      'channelName': 'B-BTC_USDT_1m'
    });

    // NOTE: Make sure you are using a version of socket.io-client that supports the features you need.
> Get Candlestick response:

      

    {
            "t": 1717075560000,
            "T": 1717075619999,
            "s": "BTCUSDT",
            "i": "1m",
            "f": 3619173860,
            "L": 3619175261,
            "o": "68292.00000000",
            "c": "68273.44000000",
            "h": "68292.00000000",
            "l": "68273.43000000",
            "v": "10.37494000",
            "n": 1402,
            "x": false,
            "q": "708461.81457520",
            "V": "0.38858000",
            "Q": "26534.68106390",
            "B": "0",
            "ecode": "B",
            "channel": "B-BTC_USDT_1m",
            "pr": "spot"
        }


      The set of candlestick resolutions available are ["1m", "5m", "15m", "30m", "1h", "4h", "8h", "1d", "3d", "1w", "1M"]. For example, for 15 minute candle please connect to channel {pair}_15m.

### Definitions


    - **Channel:** {pair}_1m ( Use 'pair' from Markets details API response. )
    - **Event:** candlestick
    - **Description:** This event provides information on the current candlestick bars for a given pair at the resolution.


### Response


    - `t`: start timestamp
    - `T`: close timestamp
    - `s`: symbol
    - `i`: candle period
  
    - `f `: first trade ID
  
    - `L`: last trade ID
    - `o`: open
    - `c`: close
    - `h`: high
    - `l`: low
    - `v`: Base asset volume
    - `n`: number of trades
    - `x`: current candle has been completed Y/N
  
    - `q`: completed trade amount (in quote asset)
    - `V`: Taker buy base asset volume
    - `Q`: taker trade amount(in quote asset)
    - `B`: first trade ID
  
    - `ecode`: exchange code
  
    - `channel`: Channel Name
    - `pr`: product


## Get Depth Snapshot Info ( Order Book )

      

    import socketio

    socketEndpoint = 'wss://stream.coindcx.com'
    sio = socketio.Client()


    @sio.event
    def connect():
        print("I'm connected!")
        sio.emit('join', {'channelName': "B-BTC_USDT@orderbook@20"})


    @sio.on('depth-snapshot')
    def on_message(response):
        print("depth-snapshot Response !!!")
        print(response)


    def main():
        try:
            sio.connect(socketEndpoint, transports='websocket')
            while True:
                sio.event('depth-snapshot', {'channelName': "B-BTC_USDT@orderbook@20"})
        except Exception as e:
            print(f"Error connecting to the server: {e}")
            raise


    # Run the main function
    if __name__ == '__main__':
        main()

      

    //For commonJS(NPM)

    // const io = require("socket.io-client");
    // const crypto = require('crypto');

    // ES6 import or TypeScript

    import { Socket, io } from 'socket.io-client';
    import crypto from 'crypto';

    const socketEndpoint = "wss://stream.coindcx.com";

    // Connect to server.
    const socket = io(socketEndpoint, {
      transports: ['websocket']
    });

    socket.on("connect", () => {
      // Join channel
      socket.emit('join', {
        'channelName': "B-BTC_USDT@orderbook@20"
      });

    });

    // Listen for updates on "eventName"
    socket.on("depth-snapshot", (response) => {
      console.log(response.data);
    });

    // In order to leave a channel
    socket.emit('leave', {
      'channelName': 'B-BTC_USDT@orderbook@20'
    });

    // NOTE: Make sure you are using a version of socket.io-client that supports the features you need.
> Get Depth Snapshot response:

      

    {
       "ts":1715885479864,
       "vs":35623836,
       "asks":{
          "65110":"0.2561",
          "65114":"0.0786",
          "65109.99":"0.09215",
          "65110.8":"0.00998",
          "65110.91":"0.01037",
          "65111.02":"0.00215",
          "65111.24":"0.00461"
       },
       "bids":{
          "65108":"0.0786",
          "65109":"0.00008",
          "65109.98":"12.5249",
          "65109.84":"0.09215",
          "65109.31":"0.00015",
          "65109.29":"0.2"
       },
       "pr":"spot",
       "s":"BTCUSDT"
    }

      {pair}@orderbook@50, Here 50 denotes, the depth of the order book the other possible values are 10 and 20.

### Definitions

    - **Channel:** {pair}@orderbook@20 ( Use 'pair' from Markets details API response. )
    - **Event:** depth-snapshot
    - **Description:** This event gives the changes in the orderbook data of the pair as a snapshot.

### Response


    - `vs`: version
    - `ts`: timestamp
    - `pr`: product
    - `s`: symbol(currency)


## Get Depth Update ( Order Book )

      

    import socketio

    socketEndpoint = 'wss://stream.coindcx.com'
    sio = socketio.Client()


    @sio.event
    def connect():
        print("I'm connected!")
        sio.emit('join', {'channelName': "B-BTC_USDT@orderbook@20"})


    @sio.on('depth-update')
    def on_message(response):
        print("depth-update Response !!!")
        print(response)


    def main():
        try:
            sio.connect(socketEndpoint, transports='websocket')
            while True:
                sio.event('depth-update', {'channelName': "B-BTC_USDT@orderbook@20"})
        except Exception as e:
            print(f"Error connecting to the server: {e}")
            raise


    # Run the main function
    if __name__ == '__main__':
        main()

      

    //For commonJS(NPM)

    // const io = require("socket.io-client");
    // const crypto = require('crypto');

    // ES6 import or TypeScript

    import { Socket, io } from 'socket.io-client';
    import crypto from 'crypto';

    const socketEndpoint = "wss://stream.coindcx.com";

    // Connect to server.
    const socket = io(socketEndpoint, {
      transports: ['websocket']
    });

    socket.on("connect", () => {
      // Join channel
      socket.emit('join', {
        'channelName': "B-BTC_USDT@orderbook@20"
      });

    });

    // Listen for updates on "eventName"
    socket.on("depth-update", (response) => {
      console.log(response.data);
    });

    // In order to leave a channel
    socket.emit('leave', {
      'channelName': 'B-BTC_USDT@orderbook@20'
    });

    // NOTE: Make sure you are using a version of socket.io-client that supports the features you need.

> Get Depth Snapshot response:

      

    {
       "ts":1714653301197,
       "vs":10037615,
       "asks":{
          "0.10828":"260",
          "0.10834":"9866.0606",
          "0.1085":"23769.6456",
          "0.10899":"347.2024",
          "0.109":"133711.3629",
          "0.10901":"32941.0265",
          "0.10829":"0.0",
          "0.10836":"0.0",
          "0.10838":"0.0",
          "0.10845":"0.0"
       },
       "bids":{
          "0.10758":"38692.1224",
          "0.10757":"23141",
          "0.10747":"1731.4441",
          "0.10736":"0.0"
       },
       "E":1714653301194,
       "pr":"spot",
       "s":"BTCUSDT"
    }


      {pair}@orderbook@50, Here 50 denotes, the depth of the order book the other possible values are 10 and 20.

### Definitions

    - **Channel:** {pair}@orderbook@20 ( Use 'pair' from Markets details API response. )
    - **Event:** depth-update
    - **Description:** This Event gives the changes in the orderbook data of the pair when the depth of the orderbook changes.

### Response


    - `vs`: version
    - `ts`: timestamp
    - `pr`: product
    - `E`: Event time
    - `s`: symbol(currency)


## Get Current Prices

      

    import socketio

    socketEndpoint = 'wss://stream.coindcx.com'
    sio = socketio.Client()


    @sio.event
    def connect():
        print("I'm connected!")
        sio.emit('join', {'channelName': "currentPrices@spot@10s"})


    @sio.on('currentPrices@spot#update')
    def on_message(response):
        print("currentPrices@spot#update Response !!!")
        print(response)


    def main():
        try:
            sio.connect(socketEndpoint, transports='websocket')
            while True:
                sio.event('currentPrices@spot#update', {'channelName': "currentPrices@spot@10s"})
        except Exception as e:
            print(f"Error connecting to the server: {e}")
            raise


    # Run the main function
    if __name__ == '__main__':
        main()

      

    //For commonJS(NPM)

    // const io = require("socket.io-client");
    // const crypto = require('crypto');

    // ES6 import or TypeScript

    import { Socket, io } from 'socket.io-client';
    import crypto from 'crypto';

    const socketEndpoint = "wss://stream.coindcx.com";

    // Connect to server.
    const socket = io(socketEndpoint, {
      transports: ['websocket']
    });

    socket.on("connect", () => {
      // Join channel
      socket.emit('join', {
        'channelName': "currentPrices@spot@10s"
      });

    });

    // Listen for updates on "eventName"
    socket.on("currentPrices@spot#update", (response) => {
      console.log(response.data);
    });

    // In order to leave a channel
    socket.emit('leave', {
      'channelName': 'currentPrices@spot@10s'
    });

    // NOTE: Make sure you are using a version of socket.io-client that supports the features you need.

> Get Current Prices response:

      

    {
       "vs":6114777,
       "ts":1714653300622,
       "pr":"spot",
       "prices":{
          "XAUTUSDT":2307.77,
          "INJUSDT":23.35,
          "ONGUSDT":0.5334,
          "MOVRUSDT":12.335,
          "TRACUSDT":0.8529,
          "HIFLUFUSDT":0.001513,
          "BEAMXUSDT":0.0237,
          "BABYUSDT":0.002283,
          "SAOUSDT":0.002034,
          "CVXUSDT":2.478
       }
    }


      currentPrices@spot@10s, Here 10 denotes, the interval at which the prices can be fetched, the other possible value is 1s and 10s.

### Definitions

    - **Channel:** currentPrices@spot@10s
    - **Event:** currentPrices@spot#update
    - **Description:** This Event gives the current prices of the pairs whose price got updated in the last 1s/10s.

### Response


    - `vs`: version
    - `ts`: timestamp
    - `pr`: product


## Get Price Stats

      

    import socketio

    socketEndpoint = 'wss://stream.coindcx.com'
    sio = socketio.Client()


    @sio.event
    def connect():
        print("I'm connected!")
        sio.emit('join', {'channelName': "priceStats@spot@60s"})


    @sio.on('priceStats@spot#update')
    def on_message(response):
        print("priceStats@spot#update Response !!!")
        print(response)


    def main():
        try:
            sio.connect(socketEndpoint, transports='websocket')
            while True:
                sio.event('priceStats@spot#update', {'channelName': "priceStats@spot@60s"})
        except Exception as e:
            print(f"Error connecting to the server: {e}")
            raise


    # Run the main function
    if __name__ == '__main__':
        main()

      

    //For commonJS(NPM)

    // const io = require("socket.io-client");
    // const crypto = require('crypto');

    // ES6 import or TypeScript

    import { Socket, io } from 'socket.io-client';
    import crypto from 'crypto';

    const socketEndpoint = "wss://stream.coindcx.com";

    // Connect to server.
    const socket = io(socketEndpoint, {
      transports: ['websocket']
    });

    socket.on("connect", () => {
      // Join channel
      socket.emit('join', {
        'channelName': "priceStats@spot@60s"
      });

    });

    // Listen for updates on "eventName"
    socket.on("priceStats@spot#update", (response) => {
      console.log(response.data);
    });

    // In order to leave a channel
    socket.emit('leave', {
      'channelName': 'priceStats@spot@60s'
    });

    // NOTE: Make sure you are using a version of socket.io-client that supports the features you need.

> Get Price Stat response:

      

    {
       "vs":1006039,
       "ts":1716358680710,
       "pr":"spot",
       "stats":{
          "HISAND33USDT":{
             "v":4074970.9761
          },
          "ENSUSDT":{
             "pc":3.48,
             "v":103333815.5488
          },
          "DOTBTC":{
             "v":16.52801718,
             "pc":2.647
          },
          "ISLMUSDT":{
             "v":10588293.415
          }
       }
    }



      priceStats@spot@60s, Here 60 denotes, the interval at which the prices can be fetched.

### Definitions

    - **Channel:** priceStats@spot@60s
    - **Event:** priceStats@spot#update
    - **Description:** This Event gives the 24hrs price change of pairs whose price got updated in the last 60s.

### Response


    - `vs`: version
    - `ts`: timestamp
    - `pr`: product
    - `pc`: price change percent
    - `v`: volume 24h


## Get New Trade

      

    import socketio

    socketEndpoint = 'wss://stream.coindcx.com'
    sio = socketio.Client()


    @sio.event
    def connect():
        print("I'm connected!")
        sio.emit('join', {'channelName': "B-BTC_USDT@trades"})


    @sio.on('new-trade')
    def on_message(response):
        print("new-trade Response !!!")
        print(response)


    def main():
        try:
            sio.connect(socketEndpoint, transports='websocket')
            while True:
                sio.event('new-trade', {'channelName': "B-BTC_USDT@trades"})
        except Exception as e:
            print(f"Error connecting to the server: {e}")
            raise


    # Run the main function
    if __name__ == '__main__':
        main()

      

    //For commonJS(NPM)

    // const io = require("socket.io-client");
    // const crypto = require('crypto');

    // ES6 import or TypeScript

    import { Socket, io } from 'socket.io-client';
    import crypto from 'crypto';

    const socketEndpoint = "wss://stream.coindcx.com";

    // Connect to server.
    const socket = io(socketEndpoint, {
      transports: ['websocket']
    });

    socket.on("connect", () => {
      // Join channel
      socket.emit('join', {
        'channelName': "B-BTC_USDT@trades"
      });

    });

    // Listen for updates on "eventName"
    socket.on("new-trade", (response) => {
      console.log(response.data);
    });

    // In order to leave a channel
    socket.emit('leave', {
      'channelName': 'B-BTC_USDT@trades'
    });

    // NOTE: Make sure you are using a version of socket.io-client that supports the features you need.


> Get New Trade response:

      

    {
       "T":"1714653304357",
       "p":"0.10804",
       "q":"1050.4254",
       "m":0,
       "s":"B-BTC_USDT",
       "pr":"spot"
    }


### Definitions

    - **Channel:** {pair}@trades
    - **Event:** new-trade
    - **Description:** This Event gives the latest trade info of the given pair.

### Response


    - `m`: whether the buyer is market maker or not
    - `p`: trade price
    - `q`: quantity
    - `T`: timestamp of trade
    - `s`: symbol(currency)


## Get Price Change ( LTP )

      

    import socketio

    socketEndpoint = 'wss://stream.coindcx.com'
    sio = socketio.Client()


    @sio.event
    def connect():
        print("I'm connected!")
        sio.emit('join', {'channelName': "B-BTC_USDT@prices"})


    @sio.on('price-change')
    def on_message(response):
        print("price-change Response !!!")
        print(response)


    def main():
        try:
            sio.connect(socketEndpoint, transports='websocket')
            while True:
                sio.event('price-change', {'channelName': "B-BTC_USDT@prices"})
        except Exception as e:
            print(f"Error connecting to the server: {e}")
            raise


    # Run the main function
    if __name__ == '__main__':
        main()

      

    //For commonJS(NPM)

    // const io = require("socket.io-client");
    // const crypto = require('crypto');

    // ES6 import or TypeScript

    import { Socket, io } from 'socket.io-client';
    import crypto from 'crypto';

    const socketEndpoint = "wss://stream.coindcx.com";

    // Connect to server.
    const socket = io(socketEndpoint, {
      transports: ['websocket']
    });

    socket.on("connect", () => {
      // Join channel
      socket.emit('join', {
        'channelName': "B-BTC_USDT@prices"
      });

    });

    // Listen for updates on "eventName"
    socket.on("price-change", (response) => {
      console.log(response.data);
    });

    // In order to leave a channel
    socket.emit('leave', {
      'channelName': 'B-BTC_USDT@prices'
    });

    // NOTE: Make sure you are using a version of socket.io-client that supports the features you need.

> Get New Trade response:

      

    {
       "T":"1714653304357",
       "p":"0.10804",
       "pr":"spot"
    }

### Definitions

    - **Channel:** {pair}@prices
    - **Event:** price-change
    - **Description:** This Event gives the latest price info of a pair whenever there is a price change.

### Response


    - `p`: trade price
    - `T`: timestamp of trade
    - `pr`: Product(spot)


## Sample code for Socket Connection

      

    import socketio
    import hmac
    import hashlib
    import json
    import time
    import asyncio
    from datetime import datetime

    socketEndpoint = 'wss://stream.coindcx.com'
    sio = socketio.AsyncClient(logger=True, engineio_logger=True)

    key = "xxx"
    secret = "xxx"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    channelName = "coindcx"
    body = {"channel": channelName}
    json_body = json.dumps(body, separators=(',', ':'))
    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()


    async def ping_task():
        while True:
            await asyncio.sleep(25)
            try:
                await sio.emit('ping', {'data': 'Ping message'})
            except Exception as e:
                print(f"Error sending ping: {e}")


    @sio.event
    async def connect():
        print("I'm connected!")
        # Get the current time
        current_time = datetime.now()

        # Format and print the current time
        print("Connected Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
        await sio.emit('join', {'channelName': "coindcx", 'authSignature': signature, 'apiKey': key})


    @sio.on('balance-update')
    async def on_message(response):
        # Get the current time
        current_time = datetime.now()

        # Format and print the current time
        print("balance-update Change Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
        print("balance-update Change Response !!!")
        print(response)


    async def main():
        try:
            await sio.connect(socketEndpoint, transports='websocket')
            # Wait for the connection to be established
            asyncio.create_task(ping_task())

            await sio.wait()
            while True:
                time.sleep(1)
                sio.event('balance-update', {'channelName': "coindcx"})

        except Exception as e:
            print(f"Error connecting to the server: {e}")
            raise  # re-raise the exception to see the full traceback


    # Run the main function
    if __name__ == '__main__':
        asyncio.run(main())

      

    // Dependencies for the Typescript :
    // npm install -g typescript
    // npm install -g ts-node
    // tsconfig.json file has the below data in it
    //      {
    //     "compilerOptions": {
    //       "module": "commonjs",
    //       "target": "es6",
    //       "moduleResolution": "node",
    //       "esModuleInterop": true,
    //       "types": [ "node" ],
    //     }
    // } 
        // npm install socket.io-client @types/socket.io-client --save
        // npm install @types/node --save-dev
    // command to run the ts file : ts-node file_name.ts 

        // Dependencies for the Node :
    // Install Node from : https://nodejs.org/en/download
    // npm install ws
    // npm install socket.io-client


    //For commonJS(NPM)

    // const io = require("socket.io-client");
    // const crypto = require('crypto');


    /// ES6 import or TypeScript

    import { Socket, io } from 'socket.io-client';
    import crypto from 'crypto';

    const socketEndpoint = "wss://stream.coindcx.com";

    // Connect to server.
    const socket = io(socketEndpoint, {
      transports: ['websocket']
    });

    const secret = "xxx";
    const key = "xxx";

    const body = { channel: "coindcx" };
    const payload = Buffer.from(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    socket.on("connect", () => {
      // Join channel
      socket.emit('join', {
        'channelName': "coindcx",
        'authSignature': signature,
        'apiKey' : key
      });

    });

    // Listen for updates on "eventName"
    socket.on("balance-update", (response) => {
      console.log(response.data);
    });

    // In order to leave a channel
    socket.emit('leave', {
      'channelName': 'coindcx'
    });

    // NOTE: Make sure you are using a version of socket.io-client that supports the features you need.

> Response:

      



### Note

    - Websocket connection implementation with ping check : Ping check is required to keep the socket connection alive.
    - **Only Private channels need authentication.**
    - Python Packages Required : python-socketio[client]
    - APPLE MAC Issue : Certificate verify failed: unable to get local issuer certificate or Mac OSX python ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749) -> **Fix for the issue : Will be fixed by installing the "Install Certificates.command"**

# Futures End Points

## Glossary

    - e - is the Event type
    - p - price (LTP)
    - q - quantity (trade quantity)
    - pr - product (futures)
    - f - futures
    - s - spot
    - T - timestamp
    - m - is maker. Boolean value that would be true if its maker and false if its taker
    - RT - range timestamp
    - ts - timestamp
    - vs - version
    - Ets - event timestamp as given by TPE (applicable to candlesticks data)
    - i - Interval
    - E - event timestamp (applicable to order book data)
    - pST - price sent time
    - v - volume 24h
    - ls - last price
    - pc - price change percent
    - btST - TPE Tick send time
    - mp - mark price
    - bmST - TPE mark price send time (The timestamp at which Third-Party exchange sent this event)

## Get active instruments

      

    const request = require('request')

    // Use this url to get the USDT active instruments
    url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/active_instruments?margin_currency_short_name[]=USDT"

    // Use this url to get the INR active instruments
    //url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/active_instruments?margin_currency_short_name[]=INR"


    request.get(url,function(error, response, body) {
        console.log(body);
    })

      

    import json

    import requests  # Install requests module first.

    # Use this url to get the USDT active instruments
    url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/active_instruments?margin_currency_short_name[]=USDT"

    # Use this url to get the INR active instruments
    #url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/active_instruments?margin_currency_short_name[]=INR"

    response = requests.get(url)
    data = response.json()
    print(json.dumps(data, indent=2))
> Response

      

    [
        "B-VANRY_USDT",
        "B-BOME_USDT",
        "B-BTCDOM_USDT",
        "B-IOTX_USDT",
        "B-LPT_USDT",
        "B-ENA_USDT",
        "B-GMT_USDT",
        "B-APE_USDT",
        "B-WOO_USDT",
        "B-ASTR_USDT",
        "B-GMX_USDT",
        "B-TLM_USDT",
       ]

      Use this endpoint to fetch the list of all active Futures instruments.

### HTTP Request

      `GET https://api.coindcx.com/exchange/v1/derivatives/futures/data/active_instruments?margin_currency_short_name[]={futures_margin_mode}`

## Get instrument details

      

    const request = require('request')

    // Use this url to get the INR active instrument info
    //url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/instrument?pair=B-BTC_USDT&margin_currency_short_name=INR"

    // Use this url to get the USDT active instrument info
    url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/instrument?pair=B-BTC_USDT&margin_currency_short_name=USDT"


    request.get(url ,function(error, response, body) {
        console.log(body);})

      

    import requests  # Install requests module first.

    # Use this url to get the INR active instrument info
    #url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/instrument?pair=B-BTC_USDT&margin_currency_short_name=INR"

    # Use this url to get the USDT active instrument info
    url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/instrument?pair=B-BTC_USDT&margin_currency_short_name=USDT"
    response = requests.get(url)
    data = response.json()
    print(data)
> Response

      

    {
       "instrument":{
          "settle_currency_short_name":"USDT",
          "quote_currency_short_name":"USDT",
          "position_currency_short_name":"AAVE",
          "underlying_currency_short_name":"AAVE",
          "status":"active",
          "pair":"B-AAVE_USDT",
          "kind":"perpetual",
          "settlement":"never",
          "max_leverage_long":10.0,
          "max_leverage_short":10.0,
          "unit_contract_value":1.0,
          "price_increment":0.01,
          "quantity_increment":0.1,
          "min_trade_size":0.1,
          "min_price":4.557,
          "max_price":2878.2,
          "min_quantity":0.1,
          "max_quantity":950000.0,
          "min_notional":6.0,
          "maker_fee":0.025,
          "taker_fee":0.075,
          "safety_percentage":2.0,
          "quanto_to_settle_multiplier":1.0,
          "is_inverse":false,
          "is_quanto":false,
          "allow_post_only":false,
          "allow_hidden":false,
          "max_market_order_quantity":1250.0,
          "funding_frequency":8,
          "max_notional":320000.0,
          "expiry_time":2548162800000,
          "exit_only":false,
          "multiplier_up":8.0,
          "multiplier_down":8.0,
          "liquidation_fee": 1.0,
          "margin_currency_short_name": "USDT",
          "time_in_force_options":[
             "good_till_cancel",
             "immediate_or_cancel",
             "fill_or_kill"
          ],
          "order_types":[
             "market_order",
             "limit_order",
             "stop_limit",
             "take_profit_limit",
             "stop_market",
             "take_profit_market"
          ],
          "dynamic_position_leverage_details":{
             "5":15000000.0,
             "8":5000000.0,
             "10":1000000.0,
             "15":500000.0,
             "20":100000.0,
             "25":50000.0
          },
          "dynamic_safety_margin_details":{
             "50000":1.5,
             "100000":2.0,
             "500000":3.0,
             "1000000":5.0,
             "5000000":6.0,
             "15000000":10.0
          }
       }
    }


      Use this endpoint to fetch the all the details of the instrument

### HTTP Request

      `GET https://api.coindcx.com/exchange/v1/derivatives/futures/data/instrument?pair={instrument}&margin_currency_short_name={futures_margin_mode}`

### Response Defnitions

      

| Key | Description |
| --- | --- |
| settle_currency_short_name | Currency in which you buy/sell futures contracts |
| quote_currency_short_name | Currency in which you see the price of the futures contract |
| position_currency_short_name | Underlying crypto on which the futures contract is created |
| underlying_currency_short_name | Underlying crypto on which the futures contract is created |
| status | Status of the instrument. Possible values are “active“ and “inactive“. |
| pair | Instrument Pair name. This is the format in which the input of the pairs will be given in any API request. |
| kind | CoinDCX only supports perpetual contracts for now, so this value will always be “perpetual” |
| settlement | This will be the settlement date of the contract. It will be “never” for perpetual contracts |
| max_leverage_long | Ignore this |
| max_leverage_short | Ignore this |
| unit_contract_value | This will be equal to 1 for all the Perpetual futures |
| price_increment | If price increment is 0.1 then price inputs for limit order can be x, x+0.1, x+0.1*2, x+0.1*3, etc |
| quantity_increment | If qty increment is 0.1 then qty inputs for an order can be x, x+0.1, x+0.1*2, x+0.1*3, etc |
| min_trade_size | This is the minimum quantity of a trade that can be settled on exchange. |
| min_price | Minimum amount to enter the position |
| max_price | Maximum amount to enter the position |
| min_quantity | Minimum quantity to enter the position |
| max_quantity | Maximum quantity to enter the position |
| min_notional | Minimum value you can purchase for a symbol |
| maker_fee | Maker fees mean when you add liquidity to the market by placing a new order that isn’t immediately matched. |
| taker_fee | Taker fees mean when you remove liquidity by filling an existing order. |
| safety_percentage | Ignore this |
| quanto_to_settle_multiplier | Ignore this. This will be equal to 1 |
| is_inverse | Ignore this. This will be false |
| is_quanto | Ignore this. This will be false |
| allow_post_only | Ignore this |
| allow_hidden | Ignore this |
| max_market_order_quantity | This gives the maximum allowed quantity in a market order |
| funding_frequency | Number of hours after which funding happens. If the value is 8 that means the funding happens every 8 hours. |
| max_notional | Ignore this |
| exit_only | If this is true then you can’t place fresh orders to take a new position or add more to an existing position. Although you can reduce your existing positions and cancel your open orders. If you already have open orders to add positions, they will not be impacted. |
| multiplier_up | This denotes how aggressive your limit buy orders can be placed compared to LTP. For example if the LTP is 100 and you want to place a buy order. The limit price has to be between minPrice and LTP*(1+multiplierUp/100) |
| multiplier_down | This denotes how aggressive your limit sell orders can be placed compared to LTP. For example if the LTP is 100 and you want to place a sell order. The limit price has to be between maxPrice and LTP*(1-multiplierDown/100) |
| liquidation_fee | This denotes Applicable fee if the trade received for the order is a trade for the liquidation order |
| dynamic_position_leverage_details | Sample response:  {   "5":15000000.0,  "8":5000000.0,  "10":1000000.0,  "15":500000.0,  "20":100000.0,  "25":50000.0  }  This gives you the max allowed leverage for a given position size. So for example if your positions size is 120K which is higher than 100K and less than 500K USDT, then max allowed leverage is 15x |
| dynamic_safety_margin_details | Sample response:  {  "50000":1.5,  "100000":2.0,  "500000":3.0,  "1000000":5.0,  "5000000":6.0,  "15000000":10.0  }  This gives you the calculation for maintenance margin of the position. In the above example, if you have a position size of 60K USDT, then your maintenance margin will be 50K*1.5% + 10K*2% = 950 USDT.Your position will be liquidated when the margin available in your position goes below 950 USDT. Liquidation price is calculated using this number and will be updated in the get position endpoint |
| expiry_time | Ignore this |
| time_in_force_options | Time in force indicates how long your order will remain active before it is executed or expired. Possible values are good_till_cancel, immediate_or_cancel, fill_or_kill |
| margin_currency_short_name | Futures margin mode |



## Get instrument Real-time trade history

      

    const request = require('request')
    const url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/trades?pair={instrument_name}"
    //const sample_url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/trades?pair=B-MKR_USDT"
    request.get(url ,function(error, response, body) {
        console.log(body);})

      

    import requests  # Install requests module first.
    url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/trades?pair={instrument_name}"
    #sample_url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/trades?pair=B-MKR_USDT"
    response = requests.get(url)
    data = response.json()
    print(data)
> Response

      

    [
        {
            "price": 1.1702,
            "quantity": 22000,
            "timestamp": 1675037938736,
            "is_maker": true
        },
        {
            "price": 1.1702,
            "quantity": 38000,
            "timestamp": 1675037950130,
            "is_maker": true
        }
    ]


      Use this endpoint to fetch the real time trade history details of the instrument.While rest APIs exist for this, we recommend using [Futures Websockets](https://docs.coindcx.com/#futures-sockets)

### HTTP Request

      `GET https://api.coindcx.com/exchange/v1/derivatives/futures/data/trades?pair={instrument_name}`

### Response Defnitions

      

| KEY | DESCRIPTION |
| --- | --- |
| price | Price of the trade update |
| quantity | Quantity of the trade update |
| timestamp | EPOCH timestamp of the event |
| is_maker | If the trade is maker then this value will be “true” |



## Get instrument orderbook

      

    const request = require('request')
    const url = "https://public.coindcx.com/market_data/v3/orderbook/{instrument}-futures/50"
    //const sample_url = "public.coindcx.com/market_data/v3/orderbook/B-MKR_USDT-futures/50"
    //Here 50 denotes, the depth of the order book the other possible values are 10 and 20
    request.get(url ,function(error, response, body) {
        console.log(body);})

      

    import requests  # Install requests module first.

    url = "https://public.coindcx.com/market_data/v3/orderbook/{instrument}-futures/50"
    #sample_url = "public.coindcx.com/market_data/v3/orderbook/B-MKR_USDT-futures/50"
    #Here 50 denotes, the depth of the order book the other possible values are 10 and 20
    response = requests.get(url)
    data = response.json()
    print(data)
> Response

      

    {
        "ts": 1705483019891,
        "vs": 27570132,
        "asks": {
            "2001": "2.145",
            "2002": "4.453",
            "2003": "2.997"
        },
        "bids": {
            "1995": "2.618",
            "1996": "1.55"
        }
    }


      Use this endpoint to fetch the depth of the order book details of the instrument.While rest APIs exist for this, we recommend using [Futures Websockets](https://docs.coindcx.com/#futures-sockets) Here 50 denotes, the depth of the order book the other possible values are 10 and 20

### HTTP Request

      `GET https://public.coindcx.com/market_data/v3/orderbook/{instrument}-futures/50`

### Response Defnitions

      

| KEY | DESCRIPTION |
| --- | --- |
| ts | Epoch timestamp |
| vs | Version |
| asks | List of ask price and quantity |
| bids | List of bid price and quantity |



## Get instrument candlesticks

      

    const request = require('request')
    const url = "https://public.coindcx.com/market_data/candlesticks?pair={pair}&from={from}&to={to}&resolution={resolution}&pcode=f"
    request.get(url ,function(error, response, body) {
        console.log(body);})

      

    import requests
    url = "https://public.coindcx.com/market_data/candlesticks"
    query_params = {
        "pair": "B-MKR_USDT",
        "from": 1704100940,
        "to": 1705483340,
        "resolution": "1D",  # '1' OR '5' OR '60' OR '1D'
        "pcode": "f"
    }
    response = requests.get(url, params=query_params)
    if response.status_code == 200:
        data = response.json()
        # Process the data as needed
        print(data)
    else:
        print(f"Error: {response.status_code}, {response.text}")
> Response

      

    {
       "s":"ok",
       "data":[
          {
             "open":1654.2,
             "high":1933.5,
             "low":1616.5,
             "volume":114433.544,
             "close":1831.9,
             "time":1704153600000
          },
          {
             "open":1832.2,
             "high":1961,
             "low":1438,
             "volume":158441.387,
             "close":1807.6,
             "time":1704240000000
          }
       ]
    }


      Use this endpoint to fetch the candlestick bars for a symbol. Klines are uniquely identified by their open time of the instrument.While rest APIs exist for this, we recommend using [Futures Websockets](https://docs.coindcx.com/#futures-sockets)

### HTTP Request

      `GET https://public.coindcx.com/market_data/candlesticks?pair={pair}&from={from}&to={to}&resolution={resolution}&pcode=f`

### Request Defnitions

      

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pair | String | YES | Name of the pair |
| from | Integer | YES | EPOCH start timestamp of the required candlestick in seconds |
| to | Integer | YES | EPOCH end timestamp of the required candlestick in seconds |
| resolution | String | YES | '1' OR '5' OR '60' OR '1D' for 1min, 5min, 1hour, 1day respectively |
| pcode | String | YES | Static value “f” to be used here. It denotes product = futures |



### Response Defnitions

      

| KEY | DESCRIPTION |
| --- | --- |
| s | status |
| open | The first recorded trading price of the pair within that particular timeframe. |
| high | The highest recorded trading price of the pair within that particular timeframe. |
| low | The lowest recorded trading price of the pair within that particular timeframe. |
| volume | Total volume in terms of the quantity of the pair. |
| close | The last recorded trading price of the pair within that particular timeframe. |
| time | EPOCH timestamp of the open time. |



## List Orders

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
    "timestamp": timeStamp , // EPOCH timestamp in seconds
    "status": "open", // Comma separated statuses as open,filled,cancelled
    "side": "buy", // buy OR sell
    "page": "1", // no.of pages needed
    "size": "10", // no.of records needed
    "margin_currency_short_name": ["INR", "USDT"]
    }
    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')
    const options = {
        url: baseurl + "/exchange/v1/derivatives/futures/orders",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }
    request.post(options, function(error, response, body) {
        console.log(body);
    })


      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp
    timeStamp = int(round(time.time() * 1000))

    body = {
            "timestamp": timeStamp , # EPOCH timestamp in seconds
            "status": "open", # Comma separated statuses as open,filled,cancelled
            "side": "buy", # buy OR sell
            "page": "1", #// no.of pages needed
            "size": "10", #// no.of records needed
        "margin_currency_short_name": ["INR", "USDT"]
            }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/derivatives/futures/orders"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)
> Response

      

    [
       {
          "id":"714d2080-1fe3-4c6e-ba81-9d2ac9a46003",
          "pair":"B-ETH_USDT",
          "side":"buy",
          "status":"open",
          "order_type":"limit_order",
          "stop_trigger_instruction":"last_price",
          "notification":"no_notification",
          "leverage":20.0,
          "maker_fee":0.025,
          "taker_fee":0.075,
          "fee_amount":0.0,
          "price":2037.69,
          "stop_price":0.0,
          "avg_price":0.0,
          "total_quantity":0.019,
          "remaining_quantity":0.019,
          "cancelled_quantity":0.0,
          "ideal_margin":1.93870920825,
          "order_category":"None",
          "stage":"default",
          "group_id":"None",
          "liquidation_fee": null,
          "position_margin_type": "crossed",
          "display_message":"ETH limit buy order placed!",
          "group_status":"None",
          "metatags": null,
          "created_at":1705565256365,
          "updated_at":1705565256940,
          "margin_currency_short_name": "INR",
          "settlement_currency_conversion_price": 89.0,
          "take_profit_price": 64000.0,
          "stop_loss_price": 61000.0,
       },
       {
          "id":"ffb261ae-8010-4cec-b6e9-c111e0cc0c10",
          "pair":"B-ID_USDT",
          "side":"buy",
          "status":"filled",
          "order_type":"market_order",
          "stop_trigger_instruction":"last_price",
          "notification":"no_notification",
          "leverage":10.0,
          "maker_fee":0.025,
          "taker_fee":0.075,
          "fee_amount":0.011181375,
          "price":0.3312,
          "stop_price":0.0,
          "avg_price":0.3313,
          "total_quantity":45.0,
          "remaining_quantity":0.0,
          "cancelled_quantity":0.0,
          "ideal_margin":1.4926356,
          "order_category":"None",
          "stage":"default",
          "group_id":"None",
          "liquidation_fee": null,
          "position_margin_type": "crossed",
          "display_message":"ID market buy order filled!",
          "group_status":"None",
          "metatags": null,
          "created_at":1705565061504,
          "updated_at":1705565062462,
          "margin_currency_short_name": "INR",
          "settlement_currency_conversion_price": 89.0,
          "take_profit_price": null,
          "stop_loss_price": null,
       }
    ]

      Use this endpoint to fetch the list of orders based on the status ( open,filled,cancelled ) and side ( buy OR sell )

### HTTP Request

      `POST https://api.coindcx.com/exchange/v1/derivatives/futures/orders`

### Request Defnitions

      

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timestamp | Integer | YES | EPOCH timestamp in seconds |
| status | string | YES | Comma separated statuses as open, filled, partially_filled, partially_cancelled, cancelled, rejected, untriggered |
| side | string | YES | buy OR sell |
| page | string | YES | Required page number |
| size | string | YES | Number of records needed per page |
| margin_currency_short_name | Array | OPTIONAL | Futures margin mode.     Default value - ["USDT"]. Possible values INR & USDT. |



### Response Defnitions

      **Note :** fee_amount and ideal_margin values are in USDT for INR Futures.

| KEY | DESCRIPTION |
| --- | --- |
| id | Order id |
| pair | Instrument Pair (Format: B-ETH_USDT) |
| side | Order side. Possible values are buy or sell |
| status | Order status. Possible values are:      OPEN - The order has been accepted and is in open status    PARTIALLY_FILLED - Order which is partially filled and the remaining quantity is open    FILLED - The order has been completely filled    CANCELED - The order has been canceled    PARTIALLY_CANCELED - Order which is partially filled and the remaining quantity has been cancelled    REJECTED - The order was not accepted by the system    UNTRIGGERED - TP or SL orders which are not triggered yet |
| order_type | Order type. Possible values are:      limit - A type of order where the execution price will be no worse than the order's set price. The execution price is limited to be the set price or better.    market - A type of order where the user buys or sells an asset at the best available prices and liquidity until the order is fully filled or the order book's liquidity is exhausted.    stop_market - Once the market price hits the stopPrice, a market order is placed on the order book.    stop_limit - Once the market price hits the stopPrice, a limit order is placed on the order book at the limit price.    take_profit_market - Once the market price hits the stopPrice, a market order is placed on the order book.    take_profit_limit - Once the market price hits the stopPrice, a limit order is placed on the order book at the limit price. |
| stop_trigger_instruction | Ignore this |
| notification | Possible options: no_notification, email_notification. Email notification will send email notification once the order is filled. |
| leverage | This is the leverage at which the order was placed |
| maker_fee | Fee charged when the order is executed as maker |
| taker_fee | Fee charged when the order is executed as taker |
| fee_amount | Amount of fee charged on an order. This shows the fee charged only for the executed part of the order |
| price | Limit price at which the limit order was placed. For market order, this will be the market price at the time when the market order was placed |
| stop_price | Trigger price of take profit or stop loss order |
| avg_price | Average execution price of the order on the exchange. It can be different compared to “price” due to liquidity in the order books |
| total_quantity | Total quantity of the order placed |
| remaining_quantity | Remaining quantity of the order which is still open and can be executed in the future |
| cancelled_quantity | Quantity of the order which is cancelled and will not be executed |
| ideal_margin | Ignore this |
| order_category | Ignore this |
| stage | default - Standard limit, market, stop limit, stop market, take profit limit, or take profit market order    exit - Quick exit which closes the entire position    liquidate - Order which was created by the system to liquidate a futures position    tpsl_exit - Take profit or stop loss order which was placed to close the entire futures position |
| group_id | Group id used when a large order is split into smaller parts. All split parts will have the same group id |
| liquidation_fee | Applicable fee if the trade received for the order is a trade for the liquidation order |
| position_margin_type | “crossed” if the order was placed for cross margin position. “Isolated” if the order is placed for isolated margin position. Please consider NULL also as isolated. |
| display_message | Ignore this |
| group_status | Ignore this |
| created_at | Timestamp at which the order was created |
| margin_currency_short_name | Futures margin mode |
| settlement_currency_conversion_price | USDT <> INR conversion price for the order. This is relevant only for INR margined Orders. |
| updated_at | Last updated timestamp of the order |
| take_profit_price | **Take Profit Trigger:** Once your order begins to fill, this take profit trigger will update any existing open TP/SL order and will apply to your entire position. Note: Take profit triggers attached to reduce-only orders will be ignored. |
| stop_loss_price | **Stop Loss Trigger:** Once your order begins to fill, this stop loss trigger will update any existing open TP/SL order and will apply to your entire position. Note: Stop loss triggers attached to reduce-only orders will be ignored. |



## Create Order

      

    const request = require('request')
    const crypto = require('crypto')

    const baseurl = "https://api.coindcx.com"

    const timeStamp = Math.floor(Date.now());
    // To check if the timestamp is correct
    console.log(timeStamp);

    // Place your API key and secret below. You can generate it from the website.
    const key = "";
    const secret = "";


    const body = {
    "timestamp": timeStamp , // EPOCH timestamp in seconds
    "order": {
    "side": "enum", // buy OR sell
    "pair": "string", // instrument.string
    "order_type": "enum", // market_order OR limit_order 
    "price": "numeric",
    "stop_price": "numeric",
    "total_quantity": "numeric",
    "leverage": "integer",
    "notification": "enum", // no_notification OR email_notification OR push_notification
    "time_in_force": "enum", // good_till_cancel OR fill_or_kill OR immediate_or_cancel
    "hidden": "boolean",
    "post_only": "boolean",
    "margin_currency_short_name": ["INR", "USDT"],
    "take_profit_price": "float",
    "stop_loss_price": "float"
    }
    }

    const payload = new Buffer(JSON.stringify(body)).toString();
    const signature = crypto.createHmac('sha256', secret).update(payload).digest('hex')

    const options = {
        url: baseurl + "/exchange/v1/derivatives/futures/orders/create",
        headers: {
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        },
        json: true,
        body: body
    }

    request.post(options, function(error, response, body) {
        console.log(body);
    })


      

    import hmac
    import hashlib
    import base64
    import json
    import time
    import requests

    # Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
    key = "XXXX"
    secret = "YYYY"

    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # python2
    secret_bytes = bytes(secret)

    # Generating a timestamp
    timeStamp = int(round(time.time() * 1000))

    body = {
            "timestamp":timeStamp , # EPOCH timestamp in seconds
            "order": {
            "side": "sell", # buy OR sell
            "pair": "B-ID_USDT", # instrument.string
            "order_type": "market_order", # market_order OR limit_order 
            "price": "0.2962", #numeric value
        "stop_price": "0.2962", #numeric value
            "total_quantity": 33, #numerice value
            "leverage": 10, #numerice value
            "notification": "email_notification", # no_notification OR email_notification OR push_notification
            "time_in_force": "good_till_cancel", # good_till_cancel OR fill_or_kill OR immediate_or_cancel
            "hidden": False, # True or False
            "post_only": False, # True or False
        "take_profit_price": 64000.0,
        "stop_loss_price": 61000.0
            }
            }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/derivatives/futures/orders/create"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    print(data)
> Response

      

    [
       {
          "id":"c87ca633-6218-44ea-900b-e86981358cbd",
          "pair":"B-ID_USDT",
          "side":"sell",
          "status":"initial",
          "order_type":"market_order",
          "notification":"email_notification",
          "leverage":10.0,
          "maker_fee":0.025,
          "taker_fee":0.075,
          "fee_amount":0.0,
          "price":0.2966,
          "avg_price":0.0,
          "total_quantity":33.0,
          "remaining_quantity":33.0,
          "cancelled_quantity":0.0,
          "ideal_margin":0.98024817,
          "order_category":"None",
          "stage":"default",
          "group_id":"None",
          "take_profit_price": 64000.0,
          "stop_loss_price": 61000.0,
          "liquidation_fee": null,
          "position_margin_type": "crossed",
          "display_message":"None",
          "group_status":"None",
          "margin_currency_short_name" : "INR",
          "settlement_currency_conversion_price": 89.0,
          "created_at":1705647376759,
          "updated_at":1705647376759,
          "take_profit_price": 64000.0,
          "stop_loss_price": 61000.0
       }
    ]


      Use this endpoint to create an order by passing the necessary parameters.

### HTTP Request

      `POST https://api.coindcx.com/exchange/v1/derivatives/futures/orders/create`

### NOTE

      *** "Do not include 'time_in _force' parameter for market orders."
    - Buy Orders:
      - Stop Limit:
        - Stop price must be greater than LTP.
        - Limit price must be greater than stop price.
      - Take Profit Limit:
        - Stop price must be less than LTP.
        - Limit price must be greater than stop price and less than LTP.
    - Sell Orders:
      - Stop Limit:
        - Stop price must be less than LTP.
        - Limit price must be less than stop price.
      - Take Profit Limit:
        - Stop price must be greater than LTP.
        - Limit price must be less than stop price and greater than LTP.


### Request Defnitions

      **Note :** Cross margin mode is only supported on USDT margined Futures at the moment. 

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timestamp | Integer | YES | Latest epoch timestamp when the order is placed. Orders with a delay of more than 10 seconds will be rejected. |
| side | String | YES | buy OR sell |
| pair | String | YES | Pair name (format: B-ETH_USDT) |
| order_type | String | YES | market, limit, stop_limit, stop_market, take_profit_limit, take_profit_market |
| price | Integer | YES | Order Price (limit price for limit, stop limit, and take profit limit orders). Keep this NULL for market orders. |
| stop_price | Integer | YES | Stop Price (stop_limit, stop_market, take_profit_limit, take_profit_market orders). stop_price is the trigger price of the order. |
| total_quantity | Integer | YES | Order total quantity |
| leverage | Integer | OPTIONAL | This is the leverage at which you want to take a position. Should match the leverage of the position. Preferably set before placing the order to avoid rejection. |
| notification | String | YES | no_notification OR email_notification. Set as email_notification to receive an email once the order is filled. |
| time_in_force | String | OPTIONAL | Possible values: good_till_cancel, fill_or_kill, immediate_or_cancel. Default is good_till_cancel if not provided. Should be null for market orders. |
| hidden | Boolean | NO | Ignore this (Not supported at the moment) |
| post_only | Boolean | NO | Ignore this (Not supported at the moment) |
| margin_currency_short_name | String | OPTIONAL | Futures margin mode.     Default value - "USDT". Possible values INR & USDT. |
| position_margin_type | String | OPTIONAL | isolated, crossed.    If position margin type is not passed, it considers the margin type of the position as default. |
| take_profit_price | Decimal | OPTIONAL | Take profit price. This value should only be sent for **market_order, limit_order**. These values will not be accepted for orders that reduce the position size (Note that no error will be raised in such cases) |
| stop_loss_price | Decimal | OPTIONAL | Stop loss price. This value should only be sent for **market_order, limit_order**. These values will not be accepted for orders that reduce the position size (Note that no error will be raised in such cases) |



### Possible Error Codes

| Status Code | Message | Reason |
| --- | --- | --- |
| 422 | Order leverage must be equal to position leverage | When the leverage specified for an order does not match the leverage of the current position. |
| 422 | Quantity for limit variant orders should be less than 9500.0 | Total quantity for a limit order exceeds the maximum allowed limit. |
| 422 | Quantity for market variant orders should be less than 9500.0 | Total quantity for a market order exceeds the maximum allowed market order quantity. |
| 400 | Price is out of permissible range | If limit price or stop price mentioned is out of range i.e. price > max_price || price td> |
