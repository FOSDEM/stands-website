---
description: "
<div style=\"float:left; padding: 10px\"><img src=\"logo.png\" style=\"max-width: 400px\" /></div>
<a href=\"https://www.theforeman.org\">Foreman</a> is an open source project that helps system administrators manage servers throughout their lifecycle, from provisioning and configuration to orchestration and monitoring. Using Puppet, Chef, Salt, Ansible and Foreman's smart proxy architecture, you can easily automate repetitive tasks, quickly deploy applications, and proactively manage change, both on-premise with VMs and bare-metal or in the cloud. </p>
<p>Foreman provides comprehensive, interaction facilities including a web frontend, CLI and RESTful API which enables you to build higher level business logic on top of a solid foundation. Foreman is a mature project, deployed in many organizations, managing from 10s to 10,000s of servers.</p>
"
layout: stand
logo: /stands/foreman/logo.png
new_this_year: "

"
showcase: "
<p style=\"margin-top: 20px;\">Foreman has one talk this year in the Infra Management devroom:</p>
<ul>
<li><a href=\"https://fosdem.org/2022/schedule/event/foreman_katello_leapp_elevate/\">Migrating Foreman/Katello from EL7 to EL8 using LEAPP/ELevate</a></li>
</ul>
<ul>
<h3>Foreman Workflows</h3>
<p>Let's take a look at some of the most common Foreman workflows.</p>
<h4>Provisioning</h4>
<div class=\"row\">
    <div class=\"col-md-8\">
        <p>Foreman provides full management of PXE configuration of PXELinux, Grub, Grub2 and iPXE for maximum network boot flexibility.</p>
        <p>Initiate unattended provisioning of various Operating Systems via extensive set of templates and snippets maintained by the community.</p>
        <p>Integrate with hypervisors like VMWare vCenter, Red Hat Enterprise Virtualization, oVirt or libvirt to create instances directly from Foreman UI/API/CLI either from images or via PXE..</p>
        <p>Integrate with clouds like OpenStack, Rackspace, Amazon EC2 or Google Compute Engine directly from Foreman UI/API/CLI.</p>
        <p>Provisioning templates which create network configuration for installed hosts including bonding, bridging and VLAN trunk support.</p>
        <p>Take a look at our <a href=\"https://docs.theforeman.org/nightly/Provisioning_Guide/index-foreman.html\">provisioning docs</a> for a full overview of provisioning capabilities in Foreman!</p>
    </div>
    <div class=\"col-md-4\">
        <img style=\"width: 100%; height: auto; float: right;\" src=\"/stands/foreman/provisioning.png\">
    </div>
</div>
<h4>Configuration</h4>
<div class=\"row\">
    <div class=\"col-md-8\">
        <p>Using configuration management (Puppet, Ansible, Chef and Salt are supported), you can easily automate repetitive tasks.</p>
        <p>You can run arbitrary commands or scripts on remote hosts using different providers, such as SSH or Ansible. This includes scheduling future runs, recurring execution, concurrency control, watching the progress and output live. </p>
        <p>Foreman ships with many configuration and remote execution templates maintained by the community.</p>
        <p>Foreman has a flexible parameters engine for hosts and associated objects (subnets, domains, host groups) with dynamically generated hierarchical Key/Value maps called Smart Variables/Class Parameters.</p>
        <p>Ability to import and parse Puppet source code base and recognize class parameters for deep mapping integration through the application.</p>
        <p> Marek Hulan recently authored <a href=\"https://theforeman.org/2020/12/how-to-start-with-foreman.html\">  a getting started with Foreman </a> blog and followed it up with <a href=\"https://theforeman.org/2021/01/updating-foreman-inventory-with-system-facts.html\">  Updating Foreman inventory with system facts </a> post that focuses on configuration management. Take a look.</p>
        <p> Check out our <a href=\"https://docs.theforeman.org/nightly/Configuring_Ansible/index-foreman.html\">Configuring Foreman with Ansible docs</a></p> and our <a href=\"https://theforeman.org/plugins/\">plugin docs</a>.</p>               
    </div>
    <div class=\"col-md-4\">
        <img style=\"width: 100%; height: auto;\" src=\"/stands/foreman/configuration.png\">
    </div>
</div>
<h4>Monitoring</h4>
<div class=\"row\">
    <div class=\"col-md-8\">
        <p>Fully configurable dashboard with widgets and statistics.</p>
        <p>With report templates you can generate custom text reports based on data that are available in Foreman. The output can be csv, yaml, json. Templates can contain additional logic and the report can be customized when it’s generated.</p>
        <p>Track changes in Foreman infrastructure over time, including key Foreman resources or facts.</p>
        <p>Inventory of facts reported by configuration management agents (Facter, Ansible, Salt grains).</p>
    </div>
    <div class=\"col-md-4\">
        <img style=\"width: 100%; height: auto;\" src=\"/stands/foreman/monitoring.png\">
    </div>
</div>

<h4>Content Management (Katello plugin)</h4>
<div class=\"row\">
    <div class=\"col-md-8\">
        <p>Create, organize, and manage local Yum, Debian and Puppet repositories. Sync remote repositories or upload content directly to build a library of content that serves as the basis for building custom builds of your content.</p>
        <p> Take your local content and filter out packages, errata and puppet modules to create custom builds into units called Content Views. Make your custom builds available to your hosts by moving it through environment paths that mimic traditional development workflows (Dev → QE → Stage → Production).</p>
        <p>Use your locally managed content to install package and errata updates to a host or group of hosts. For example, Content Hosts could be grouped by function, department or business unit.</p>
        <p>Inventory of facts reported by configuration management agents (Facter, Ansible, Salt grains).</p>
        <p>Create and maintain a Standard Operating Environment (SOE).</p>
    </div>
    <p>
    <div class=\"col-md-4\">
        <img style=\"width: 100%; height: auto;\" src=\"/stands/foreman/katello.png\">
    </div>
</div>
<h5>Managing CentOS Stream Servers with Foreman</h5>
<p>
<video width=\"70%\" controls>
  <source src=\"http://bofh.nikhef.nl/events/FOSDEM/2021/stands/foreman/foreman_video3.mp4\" type=\"video/mp4\">
</video>
</p>


"
themes:
- System administration
title: Foreman
website: https://theforeman.org
chatroom: foreman
---
