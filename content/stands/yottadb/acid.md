---
title: "ACID Properties"
draft: false
---

# ACID Properties

YottaDB implements transactions with strong Atomic, Consistent, Isolated, Durable (ACID) properties. Consider application logic to move $100 from a savings account to a checking account, which conceptually consists of the following steps:

 - Validate that the accounts exist, that the requested transfer is permitted, that there is sufficient balance, that the transfer request is authenticated, etc.
 - Subtract $100 from the savings account.
 - Add $100 to the checking account.
 - Compute and debit any applicable service charges.
 - Create a record to log the transaction.

Consider that application logic executing concurrently with an update to business rules affecting minimum balances and service charges, and a balance inquiry. Each of the three is implemented as an ACID transaction.

**Atomicity** is the property that the entire transaction happens or none of it happens. For example, in the event of a system malfunction, it should not recover to an intermediate state such as between the withdrawal from savings and the deposit to checking.

**Consistency** is the property that the database should never be observable in a state that is inconsistent (the process of course sees its own data that it is manipulating in a transient state).

**Isolation** is the property that each transaction executes and commits as if it were the only transaction active on the system. For example, from the point of view of the database state change, the money-transfer commits either before or after the business rules update, even if the logic for both executes concurrently.

There is a duality between Consistency and Isolation -- as a practical matter, it is not possible to provide strong Consistency without strong Isolation and vice versa. YottaDB provides strong Consistency and Isolation. Strict [Serializability](https://en.wikipedia.org/wiki/Serializability) implies strong Consistency and Isolation, and vice versa.

**Durability** is the property that once a transaction is committed, the database state change it represents is permanent, even if the computer crashes. YottaDB implements Durability by logging each transaction to a journal file, and “hardening” that journal file to non-volatile storage as part of the logic that commits a transaction.