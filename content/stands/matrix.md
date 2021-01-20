---
description: "Matrix (https://matrix.org) is an open protocol for secure, decentralised\
  \ communication - defining an end-to-end-encrypted real-time communication layer\
  \ for the open Web suitable for instant messaging, VoIP, microblogging, forums and\
  \ more.  We publish Matrix as an open standard (https://matrix.org/docs/spec) under\
  \ the open governance of the non-profit Matrix.org Foundation (https://matrix.org/foundation),\
  \ and release Apache-licensed reference implementations of the protocol for server,\
  \ client SDKs, bots, bridges & more.  Some users may recognise Matrix via client\
  \ apps such as Element (https://element.io, formerly Riot).\r\n\r\nMatrix works\
  \ by replicating conversation history across servers which participate in a given\
  \ conversation, ensuring that ownership of the conversation is fully decentralised:\
  \ no single server owns or controls the conversation, just as git repositories are\
  \ cloned equally between all participants.  As a result, you can think of Matrix\
  \ more like a global decentralised object database with realtime pubsub semantics,\
  \ rather than a traditional message-passing protocol.  The protocol defines HTTPS+JSON\
  \ APIs as a baseline, but more efficient transports and encodings are supported\
  \ and encouraged.\r\n\r\nThe public Matrix network on the internet has over 26M\
  \ addressable users spread over ~60K servers, ranging in size from personal RPis\
  \ through to massive deployments for organisations including Mozilla, the Wikimedia\
  \ Foundation, German schools in Schleswig-Holstein & Hamburg, and the entirety of\
  \ the French Government."
layout: stand
logo: stands/matrix/logo.png
new_this_year: "2020 was a busy year for Matrix.\r\n * Mozilla turned off IRC and\
  \ migrated to Matrix in March: https://matrix.org/blog/2020/03/03/moznet-irc-is-dead-long-live-mozilla-matrix\r\
  \n * After loads of testing, we finally turned on end-to-end encryption by default\
  \ for all private rooms in May: https://matrix.org/blog/2020/05/06/cross-signing-and-end-to-end-encryption-by-default-is-here\r\
  \n * We finally fixed our performance problems on the overloaded matrix.org server\
  \ by horizontally sharding Synapse: https://matrix.org/blog/2020/11/03/how-we-fixed-synapses-scalability\r\
  \n * We started to see more academic research emerging on Matrix, particularly analysing\
  \ the properties of state resolution (how we keep Matrix rooms securely replicated\
  \ in a byzantine fault tolerant manner): https://matrix.org/blog/2020/06/16/matrix-decomposition-an-independent-academic-analysis-of-matrix-state-resolution\r\
  \n * Dendrite (our next-gen Golang Matrix server) entered beta in October, steadily\
  \ improving ever since: https://matrix.org/blog/2020/10/08/dendrite-is-entering-beta\r\
  \n * Gitter joined Matrix in October, with native Matrix support launching in December:\
  \ https://matrix.org/blog/2020/12/07/gitter-now-speaks-matrix\r\n * We started working\
  \ on Decentralised Reputation as a mechanism for empowering users to filter out\
  \ abuse or other unwanted content in Matrix (thus *finally* catching up with our\
  \ FOSDEM 2017 talk on the subject: https://archive.fosdem.org/2017/schedule/event/matrix_future/):\
  \ https://matrix.org/blog/2020/10/19/combating-abuse-in-matrix-without-backdoors\r\
  \n * We launched Cerulean, a wildly experimental proof-of-concept to experiment\
  \ with threads demonstrate the viability of twitter-style microblogging on Matrix\
  \ (including an initial implementation of decentralised reputation!): https://matrix.org/blog/2020/12/18/introducing-cerulean\r\
  \n * We got the first messages flowing over Decentralised MLS (Messaging Layer Security),\
  \ giving logarithmic rather than linear complexity E2EE.\r\n\r\nIn 2021, we plan\
  \ to add:\r\n * Spaces - shareable hierarchies of rooms, effectively making Matrix\
  \ a decentralised hierarchical filesystem for realtime data!\r\n * Threads - full\
  \ support for free-form threaded conversations\r\n * Full Social Login (log in via\
  \ Github, Gitlab, or as wide a choice of SSO providers as you like)\r\n * Massively\
  \ improved VoIP\r\n * Voice messages, Location sharing, Custom emoji, Canonical\
  \ DMs...\r\n * ...and reworking E2EE, again, to improve reliability and performance."
showcase: Matrix is an open protocol for secure decentralised communication, aiming
  to bust open the closed proprietary communication silos (Slack, Teams, Discord,
  WhatsApp etc) which have dominated in recent years.  On our stand you'll be able
  to sync via chat & video conference directly with the core Matrix team, get demos
  of all the latest stuff we've been working on, and generally learn how to liberate
  your communication and join the open Matrix communication network.
themes:
- Office suites and productivity
title: Matrix
website: https://matrix.org
show_on_overview: true
---