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

As YottaDB replication replicates only logical update information, network bandwidth use is parsimonious compared to techniques such as storage-mirroring. Furthermore, YottaDB can optionally use the standard zlib compression library to further reduce bandwidth used.
