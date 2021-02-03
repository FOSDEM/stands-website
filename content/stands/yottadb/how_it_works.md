---
title: "How It Works"
draft: false
---

# How It Works

## Data Structure: Key-Value Tuples

The fundamental core data structure provided by YottaDB is key-value tuples.

Following is a set of key-value tuples:

```
["Capital","Belgium","Brussels"]
["Capital","Thailand","Bangkok"]
["Capital","USA","Washington, DC"]
```

Each of the above tuples is called a `node`.
In an *n*-tuple, the first *n*-1 items are keys, and the last item is the value associated with the keys.
Data in YottaDB is always ordered according to the keys.

YottaDB itself assigns no meaning to the data in each node. But using meaningful keys improves application maintainability.

For example:

```
["Capital","Belgium","Brussels"]
["Capital","Thailand","Bangkok"]
["Capital","USA","Washington, DC"]
["Population","Belgium",1367000]
["Population","Thailand",8414000]
["Population","USA",325737000]
```

As YottaDB assigns no inherent meaning to the keys or values, its key value structure lends itself to implementing Variety.

For example, if an application wishes to add historical census results under “Population”, the following is a perfectly valid set of tuples:

```
["Capital","Belgium","Brussels"]
["Capital","Thailand","Bangkok"]
["Capital","USA","Washington, DC"]
["Population","Belgium",1367000]
["Population","Thailand",8414000]
["Population","USA",325737000]
["Population","USA",17900802,3929326]
["Population","USA",18000804,5308483]
…
["Population","USA",20100401,308745538]
```

In the above example, the application designer has chosen to represent date in the form `yyyymmdd`.

The `first key` is called a `variable`, and the remaining keys are called `subscripts`,e.g., Captial("Belgium")="Brussels".

The set of all nodes under a variable is called a `tree` (so in the example, there are two trees, one under Capital and the other under Population).
The set of all nodes under a variable and a leading set of its subscripts is called a `subtree` (e.g., Population(“USA”) is a subtree of the Population tree).

With this representation, the Population tree can be written as follows:

```
Population("Belgium")=1367000
Population("Thailand")=8414000
Population("USA")=325737000
Population("USA",17900802)=3929326
Population("USA",18000804)=5308483
…
Population("USA",20100401)=308745538
```

And visualized thus:

![Population Tree Visualization](/stands/yottadb/population-tree-viz.png)

## Persistence

In YottaDB, persistence is a property of a variable, visible in the variable name. Prefixing a variable name with a caret(^) makes its data persist beyond the lifetime of a process.

Shared, persistent nodes in a database are called global variable nodes. Nodes that are private to a process with the lifetime of the process are called local variable nodes.

## Transaction Processing

YottaDB implements transactions with strong Atomic, Consistent, Isolated, Durable ([ACID](https://en.wikipedia.org/wiki/ACID)) properties.