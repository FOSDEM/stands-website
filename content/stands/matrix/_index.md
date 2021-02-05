---
description: |
  <div style="float:left; padding: 10px"><img src="logo.png" style="max-width: 400px" /></div>
  <p><a href="https://matrix.org">Matrix</a> is an open protocol for secure, decentralised
   communication - defining an end-to-end-encrypted real-time communication layer
   for the open Web suitable for instant messaging, VoIP, microblogging, forums and
   more.  We publish Matrix as an <a href="https://matrix.org/docs/spec">open standard</a> under
   the open governance of the non-profit <a href="https://matrix.org/foundation">Matrix.org Foundation</a>,
   and release Apache-licensed reference implementations of the protocol for server,
   client SDKs, bots, bridges & more.  Some users may recognise Matrix via client
   apps such as Element (https://element.io, formerly Riot).</p>

  <p>Matrix works
   by replicating conversation history across servers which participate in a given
   conversation, ensuring that ownership of the conversation is fully decentralised:
   no single server owns or controls the conversation, just as git repositories are
   cloned equally between all participants.  As a result, you can think of Matrix
   more like a global decentralised object database with realtime pubsub semantics,
   rather than a traditional message-passing protocol.  The protocol defines HTTPS+JSON
   APIs as a baseline, but more efficient transports and encodings are supported
   and encouraged.</p>

  <p>The public Matrix network on the internet has over 26M
   addressable users spread over ~60K servers, ranging in size from personal RPis
   through to massive deployments for organisations including Mozilla, the Wikimedia
   Foundation, German schools in Schleswig-Holstein & Hamburg, and the entirety of
   the French Government.</p>
layout: stand
logo: stands/matrix/logo.png
new_this_year: |
  <p>2020 was a busy year for Matrix.</p>
  <ul>
  <li>Mozilla turned off IRC and
    migrated to Matrix in March: https://matrix.org/blog/2020/03/03/moznet-irc-is-dead-long-live-mozilla-matrix</li>
  <li>After loads of testing, we finally turned on end-to-end encryption by default
    for all private rooms in May: https://matrix.org/blog/2020/05/06/cross-signing-and-end-to-end-encryption-by-default-is-here</li>
  <li>We finally fixed our performance problems on the overloaded matrix.org server
    by horizontally sharding Synapse: https://matrix.org/blog/2020/11/03/how-we-fixed-synapses-scalability</li>
  <li>We started to see more academic research emerging on Matrix, particularly analysing
    the properties of state resolution (how we keep Matrix rooms securely replicated
    in a byzantine fault tolerant manner): https://matrix.org/blog/2020/06/16/matrix-decomposition-an-independent-academic-analysis-of-matrix-state-resolution</li>
  <li>Dendrite (our next-gen Golang Matrix server) entered beta in October, steadily
    improving ever since: https://matrix.org/blog/2020/10/08/dendrite-is-entering-beta</li>
  <li>Gitter joined Matrix in October, with native Matrix support launching in December:
    https://matrix.org/blog/2020/12/07/gitter-now-speaks-matrix</li>
  <li>We started working
    on Decentralised Reputation as a mechanism for empowering users to filter out
    abuse or other unwanted content in Matrix (thus *finally* catching up with our
    FOSDEM 2017 talk on the subject: https://archive.fosdem.org/2017/schedule/event/matrix_future/):
    https://matrix.org/blog/2020/10/19/combating-abuse-in-matrix-without-backdoors</li>
  <li>We launched Cerulean, a wildly experimental proof-of-concept to experiment
    with threads demonstrate the viability of twitter-style microblogging on Matrix
    (including an initial implementation of decentralised reputation!): https://matrix.org/blog/2020/12/18/introducing-cerulean</li>
  <li>We got the first messages flowing over Decentralised MLS (Messaging Layer Security),
    giving logarithmic rather than linear complexity E2EE.</li>
  </ul>
  <p>In 2021, we plan
    to add:</p>
  <ul>
  <li>Spaces - shareable hierarchies of rooms, effectively making Matrix
    a decentralised hierarchical filesystem for realtime data!</li>
  <li>Threads - full
    support for free-form threaded conversations</li>
  <li>Full Social Login (log in via
    Github, Gitlab, or as wide a choice of SSO providers as you like)</li>
  <li>Massively
    improved VoIP</li>
  <li>Voice messages, Location sharing, Custom emoji, Canonical
    DMs...</li>
  <li>...and reworking E2EE, again, to improve reliability and performance.</li>
  </ul>
showcase: |
  <p>Matrix is an open protocol for secure decentralised communication, aiming
  to bust open the closed proprietary communication silos (Slack, Teams, Discord,
  WhatsApp etc) which have dominated in recent years.  On our stand you'll be able
  to sync via chat & video conference directly with the core Matrix team, get demos
  of all the latest stuff we've been working on, and generally learn how to liberate
  your communication and join the open Matrix communication network.</p>
themes:
- Office suites and productivity
title: Matrix
website: https://matrix.org
chatroom: matrix
---