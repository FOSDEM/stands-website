---
title: "Business Continuity"
draft: false
---

# Business Continuity

While Durability is based on recovering application state from persistent non-volatile storage, business continuity of an application requires recovery of application state even in the face of loss of that non-volatile storage, e.g., the unplanned loss of a data center or a geography. In the event of unplanned loss of a data center or a geography, a mission critical application should continue to be available from another data center.

YottaDB achieves business continuity with real-time replication. Transactions are processed on a single instance for serialization performance (serialization is slower when it the decision making required for strict serialization is distributed over multiple instances). As journal records are written to journal files, those updates are streamed in real time to as many as 16 secondary instances. Each of those 16 secondary instances can stream the updates it receives in real time to 16 more instances (for up to 256 tertiary instances), and so on, without any limit imposed by YottaDB.

In the event of loss of the instance in that primary role, any of the instances to which it is replicating can be switched from a secondary (or tertiary, or other downstream role) to the primary role. When the instance in the original primary role is recovered, it operates in a secondary role, and catches up with transactions processed by the instance that took over the primary role.

Given the strict serialization requirements of demanding applications such as banking core processing, YottaDB provides mechanisms for an application to restore strict serialization after such an outage.

The operation of the primary instance that originates updates is unaffected by the state of any replication connection or secondary instance receiving updates. The instances share no hardware or software resources, and thus one instance is unaffected by any other instance.

---
**NOTE**

With n instances, it is possible to provide business continuity in the face of at most n-1 unplanned outages. Since the number of instances is always a finite number, absolute business continuity does not exist, and the number of instances becomes a business decision rather than a technical decision resulting from a YottaDB limit.

---

YottaDB replication provides logical equivalence between multiple databases. One type of replication is Business Continuity (BC) replication.

BC replication provides business continuity for systems of record. Updates applied at an originating instance replicate in near real-time to a replicating instance.To help ensure this consistency, BC replication prohibits locally generated database updates on a replicating secondary instance. For example, with instances named A and B, business logic processed on instance A can be streamed to instance B so that should A ever go down, B can immediately take over and provide continuity. In order to ensure that B produces results consistent with A, B can contain only material state information that is also in A.

In the following illustration, A is the originating primary instance and B and C are its replicating instances. C is also a propagating primary instance because it further replicates to D. This BC replication configuration can also be described as a B←A→C→D configuration.

{{< figure src="/stands/yottadb/bc_repl.gif" alt="Business Continuity Replication">}}

BC replication is intended for mission-critical applications that must be available 24 hours a day, 365 days a year, in the face of both unplanned events (such as system crashes) as well as planned events (such as system and software upgrades).

As YottaDB replication replicates only logical update information, network bandwidth use is parsimonious compared to techniques such as storage-mirroring. Furthermore, YottaDB can optionally use the standard [zlib](https://zlib.net/) compression library to further reduce bandwidth used.

