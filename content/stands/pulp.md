---
description: |
  Pulp is a platform for managing repositories of software packages and making them available to a large number of consumers.
  With Pulp, you can locally mirror all or part of a repository, host your own software packages in repositories, and manage many types of content from multiple sources in one place.
  If you have dozens, hundreds, or thousands of software packages and need a better way to manage them, Pulp can help.

layout: stand
logo: stands/pulp/logo.png
new_this_year: |

  <h4>Pulp Community Updates</h4>
  <p style=\"margin-top: 20px;\"> Watch Robin recall the <a href="https://youtu.be/YMDPtKs7p1c">major changes in the Pulp project</a> over the last year.</p>
  <h4>Pulp Podman Compose</h4>
  <p style=\"margin-top: 20px;\"> Due to popular demand, you can now deploy Pulp with podman compose. For instructions, see <a href="https://pulpproject.org/podman-compose/">Pulp Podman Compose documentation</a> on our website.</p>
  <h4>Deploy Pulp on Openshift</h4>
  <p style=\"margin-top: 20px;\">You can find Pulp Operator on Openshift's <a href="https://operatorhub.io/">Operator Hub</a>. For more information, watch Fabricio's <a href="https://youtu.be/quUdQ1j56I4">Pulp on Openshift Installation Tutorial </a>.</p>
  <h4>Pulp & High Availability</h4>
  <p style=\"margin-top: 20px;\">Pulp’s architecture is designed to offer scalability and high availability. You can scale Pulp’s architecture in whatever way suits your needs. With Pulp, the more you increase your availability, you also increase your capability. The more Pulpcore API processes you deploy, the more API requests you can serve. The more Pulpcore content applications you deploy, the more binary data requests you can serve. The more workers you start, the higher the tasking (syncing, publishing) throughput you deployment can handle. For more information, check out our <a href="https://pulpproject.org/pulp-ha/">High Availability info page</a> </p>
  <h4>Pulp Community Discourse</h4>
  <p style=\"margin-top: 20px;\">As Pulp grows, we need better ways of discussing things. This year, we launched our very first community forum over at <a href="https://discourse.pulpproject.org/">discourse.pulpproject.org/</a>. Please drop by, introduce yourself, ask questions, and tell us what you're doing with Pulp! </p>
  <h4>Pulp Matrix Community</h4>
  <p style=\"margin-top: 20px;\">Since 2021, our primary synchronous communication channel is Matrix. Just like FOSDEM, we enjoy the advantages of a Matrix's rich range of capabilities and open source ethos. Please join our <a href="https://matrix.to/#/#pulp:matrix.org">Pulp room</a> for general Pulp chat. For developer-related chat, join us over on <a href="https://matrix.to/#/#pulp-dev:matrix.org">Pulp-dev</a>. We have a space listing on Matrix. Join our <a href="https://matrix.to/#/!xsNEtFDUoohlnfzVGC:matrix.org?via=matrix.org">Pulp space</a> for a full list of our rooms.</p>
  <h4>Didn't find the content plugin you need?</h4>
  <p style=\"margin-top: 20px;\">Pulp 3 is more stable and robust than ever. If you didn't find a content plugin to match the content type you need, there is a great plugin template you can use to start working with another content type in Pulp. We also have a <a href="https://docs.pulpproject.org/pulpcore/plugins/index.html#plugin-writer-s-guide">Plugin Writers Guide</a> to get you on your way. If you have some questions, feel free to talk to us either in our <a href="https://discourse.pulpproject.org/">discourse.pulpproject.org/</a> or in our our <a href="https://matrix.to/#/#pulp:matrix.org">Pulp room</a>.</p>
  <h4>Pulp Open Floor</h4>
  <p style=\"margin-top: 20px;\"> Every Tuesday at at 10:30 ET (either EST or EDT), we host an Open Floor meeting on our <a href="https://matrix.to/#/#pulp-meeting:matrix.org">Pulp meeting room</a> on Matrix. We welcome anyone to add anything Pulp-related to the <a href="https://hackmd.io/@pulp/triage/edit"> agenda </a> and we can all discuss it there!
  </p>
  <h4>Useful links</h4>
  <p style=\"margin-top: 20px;\"></p>
  <ul style=\"padding-inline-start: 20px;\">
  <li style=\"list-style: none; margin-top: 8px;\><a href="https://pulpproject.org/installation-introduction/">Try Pulp!</a></li>
  <li style=\"list-style: none; margin-top: 8px;\><a href="https://docs.pulpproject.org/pulpcore/">Pulp project docs</a></li>
  <li style=\"list-style: none; margin-top: 8px;\><a href="https://pulpproject.org/get_involved/">Get Involved</a></li>
  </ul>

showcase: |
  <p>
  <h3>What can I do with Pulp?</h3>
  <p>
  <video width="80%" controls>
    <source src="https://ftp.fau.de/fosdem/2021/stands/pulp/pulp_video2.mp4" type="video/mp4">
  </video>
  </p>
  <p style=\"margin-top: 20px;\">If you want a centralized tool to take full control of your software packages, blend and curate content types to suit your exact requirements, and distribute them throughout your organization, Pulp can help. For an overview of Pulp's workflows, check out our <a href="https://pulpproject.org/pulp-workflow-overview/">workflow overview.</a></p>
  <h4>Host Your Own Container registry</h4>
  <p style=\"margin-top: 20px;\">If you want to avoid relying on third parties whose subscription models and rate limits can change at any time, you can host your own container registry with <a href="https://github.com/pulp/pulp_container/">Pulp Container </a>. With Pulp container, you can also build your own containers, publish, and distribute them throughout your organization or to your customers. For more information, see <a href="https://opensource.com/article/21/5/container-management-pulp">5 reasons to host your container registry with Pulp </a></p>
  <h4>Manage upgrades to your Edge devices</h4>
  <p style=\"margin-top: 20px;\"> The OSTree plugin for Pulp allows users to manage OSTree repositories from which their Edge devices can download updates. <a href="bit.ly/pulp_ostree">Learn more here</a>. <p>
  <h4>Host Your Own Ansible Galaxy</h4>
  <p style=\"margin-top: 20px;\"><a href="https://github.com/ansible/galaxy_ng">Ansible Galaxy_NG </a> is Pulp plugin to support hosting your very own Ansible Galaxy server. For more information, see Brian Bouterse's talk <a href="https://video.fosdem.org/2021/D.infra/hostyourownansiblegalaxy.mp4">Host Your Own Ansible Galaxy </a></p>
  <h4>Host Your Own PyPI</h4>
  <p style=\"margin-top: 20px;\">You can mirror the whole of PyPI, install and manage Pulp-hosted Python content on clients using `pip`, and much more. For more information, see <a href="https://www.youtube.com/watch?v=yxPHEHNJwO4">Host Your Own PyPI workshop</a>. </p>
  <h4>Control dependencies & Create Reproducible Environments</h4>
  <p style=\"margin-top: 20px;\">With Pulp, you have full control over dependencies and can curate your content to optimise for your environmental needs.</p>
  <h4>Multiple Content Types</h4>
  <p style=\"margin-top: 20px;\">Pulp is the only FOSS content management project that has support for both <a href="https://docs.pulpproject.org/pulp_rpm/">RPM</a> and <a href="https://docs.pulpproject.org/pulp_deb/">Debian</a> repositories. As you can probably tell, Pulp doesn't stop there either! Pulp has a wide range of available content plugins. Add a plugin from the available content types or use our plugin template to <a href="https://docs.pulpproject.org/pulpcore/plugins/plugin-writer/index.html">write your own plugin!</a> - it's not hard!</p>
  <h4>Pulp for CI/CD</h4>
  <p style=\"margin-top: 20px;\">You can take full control over version pinning, promotion, and distribution of your content throughout all stages of the development lifestyle environment, for example <i>Dev</i>, <i>Staging</i>, <i>Production</i>, and promote content from one environment to another so that you can ensure stability and repeatability at all times. For more information, see <a href="https://pulpproject.org/pulp-workflow-overview/#pulp-for-cicd">Pulp for CI/CD</a>.
  </p>
  <h4>Manage your Pulp Deployment with Ansible</h4>
  <p style=\"margin-top: 20px;\"><a href="https://pulpproject.org/pulp-squeezer/">Pulp Squeezer</a> is an Ansible collection you can use to fetch, upload, organize, and distribute File, Ansible, and Python content.</p>
themes:
- System administration
title: 'Pulp'
website: https://www.pulpproject.org/
show_on_overview: true
chatroom: pulp
---
