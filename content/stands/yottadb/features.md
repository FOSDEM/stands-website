---
title: "Features"
draft: false
---

# Features

## Business Continuity

YottaDB’s business continuity and real-time replication features keep even Internet-scale applications continuously available not just in the face of unplanned events, but also planned events, such as application upgrades and even schema changes.

[Learn More](/stands/yottadb/business_continuity)

## Daemon-less

YottaDB operates using a daemon-less engine. Why?

 - With a daemon, failure of a daemon process stalls the operation of multiple processes and perhaps even multiple applications.
 - With a daemon, a daemon process typically has to operate with elevated privileges compared to an application process, and furthermore the link between application and daemon must be secured.
 - Communication between application logic and a database daemon adds latency and increases response times.
 - A daemon is an additional process that consumes system resources, even if only an incremental amount.

[Learn More](/stands/yottadb/in_memory_engine)

## Security

With a philosophy that complexity is the enemy of security, the simply-explained YottaDB security model is based on the mature and easily understood [user-group-world](https://en.wikipedia.org/wiki/File-system_permissions) permissions for processes to access database files. Security can be further enhanced with layered controls like [SELinux](https://en.wikipedia.org/wiki/Security-Enhanced_Linux).

## Multi-Language Database Access

{{< figure src="/stands/yottadb/multi-lang-db-access.svg" width="50%" height="50%">}}

While the historic roots of YottaDB are in the M language, YottaDB extends the tight integration of the language with the database to other languages. As C is the lingua franca of programming languages (in that all programming languages have the ability to call a C API), YottaDB’s C language API extends the database engine to all programming languages. Through the C API, bindings (called "wrappers") exist to natively access YottaDB concurrently also from Go, Perl, and Rust. Community developed wrappers from C++, node.js, and Python are under development and at various levels of usability and maturity, with all expected soon.

[Learn More](/stands/yottadb/hello_world)

## Optimistic Concurrency Control

Unlike most high-end transactional database engines, YottaDB uses Optimistic Concurrency Control (OCC) to implement ACID transactions. Since transactions do not typically collide, optimistic techniques scale up better than pessimistic techniques such as locking.

[Learn More](/stands/yottadb/occ)

## Strongly ACID transactions

ACID transactions are YottaDB's strong suit, and give applications a data source they can rely on.

[Learn More](/stands/yottadb/acid)