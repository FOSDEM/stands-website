---
title: "In-Memory Engine"
draft: false
---

# In-Memory Engine

At the core of YottaDB is a daemon-less key-value database engine that executes within the address space of the application process, which makes in-memory calls to a YottaDB API. Combining the database engine and application logic in a single process yields several benefits:

## Robustness

A simpler architecture means that in the event of abnormal process termination or other process failure, the other processes of the application can continue. With a daemon, failure of a daemon process stalls the operation of multiple processes and perhaps even multiple applications.

## Security

Complexity is the enemy of security. With YottaDB’s daemon-less architecture, the security model is based on the mature, clearly documented, and well understood user-group-world permissions for processes to access database files, and is amenable to additional layered access controls such as [SELinux](https://en.wikipedia.org/wiki/Security-Enhanced_Linux) or [AppArmor](https://gitlab.com/apparmor/apparmor).

## Simplicity

The first process to open a database file sets up the control structures to manage it, and the last process to close the file cleans up the control structures. There is no daemon to start, stop, or tune.

## Scalability

With YottaDB’s database engine, processes cooperate with one another to manage the database, and the achievable throughput is limited by the underlying computing platform, rather than the potential single-point bottleneck of a daemon.

## Multi-Language Database Access

With the database engine in a shared library that executes within the address space of each process, application developers are free to develop applications in the language of their choice.