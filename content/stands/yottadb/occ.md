---
title: "Optimistic Concurrency Control"
draft: false
---

# Optimistic Concurrency Control

Unlike most high-end transactional database engines, YottaDB uses [Optimistic Concurrency Control](http://daslab.seas.harvard.edu/reading-group/papers/kung.pdf) (OCC) to implement [ACID](https://en.wikipedia.org/wiki/ACID) transactions. Since transactions do not typically collide, optimistic techniques scale up better than other techniques. OCC and the daemon-less architecture reinforce each other to provide the extreme level of scalability that YottaDB users have come to expect.

## How YottaDB OCC Works

Every database records a transaction number in its file header. Each database block header records the database transaction number when that block was last updated. When a process is inside a transaction:

 - The database engine tracks the file and block number of each database block read, and the transaction number of that block. Since a block to be updated must first be read, this list includes blocks to be updated.
 - When application logic updates the database, the update is retained in process-private memory and does not update the database. The update is visible to subsequently application logic within the process, but is not visible to any other process until the transaction commits.
 - When the application logic signals that it is ready to commit the transaction, the database engine checks whether any block read within the transaction has a higher transaction number than that it has recorded. If none has — the typical case — the engine commits the transaction.
 - If even one block has been updated since the process read it, the database engine discards its work and restarts the transaction logic. This restart is transparent to the application logic, which does not need to be coded to be aware of YottaDB transaction processing. This simplifies application code and improves maintainability. In the most common case, where a collision results from a random overlapping update by a concurrent process, it is able to commit on the second attempt.
 - If the second attempt also fails to commit, the engine makes a third attempt, and if that fails, the engine concludes that pathological application logic is causing the collisions, and makes a fourth and final attempt during which updates by other processes are blocked, allowing the transaction to commit. [Applications should be written to avoid pathological colliding concurrent transactions; YottaDB provides tools and support services for application developers to identify such pathology should it occur.]

