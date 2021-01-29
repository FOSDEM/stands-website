## General Information
FOSDEM 2021

Welcome to the OpenMandriva stand
### OpenMandriva: What is it? What started it?
OpenMandriva Lx is an rpm based linux distribution with its roots in Gael Duvals Mandrake distribution which eventually became Mandriva. When Mandriva closed, the OpenMandriva Association was formed as a charitable body charged with continuing the work of Mandrake/Mandriva in the open source arena. We have continued to produce new releases of OpenMandriva since 2013.
### Why we are Different
What is it about OpenMandriva that makes it different from other distributions on Linux?

Probably the most radical aspect of the distribution is the fact that all the main packages (including the kernel) are compiled with the ‘clang’ compiler and linker which is based on the LLVM compiler infrastructure. The advantage of clang is that it is far more adaptable to new architectures and we take advantage of this: we have distribution builds for 5 different architectures in progress these include the up and coming aarch64 based processors as well as the znver1 that enhances the speed of the AMD RYZEN based processors.  We even have a build for the PinePhone.

Other advantages that accrue from the use of the clang compiler are that of compilation speed. This is crucial in production of distributions as there is a large body (1000’s of packages) of code to compile anew for each release. This contributes to our ability to provide very up to date releases of the main body of software used in our releases.
### Our Repositories
The distribution is maintained in three repositories.

Rock, the stable branch, is created at release and is only subject to minor updates. This is repository intended for those who use a Linux distribution in their daily work and thus require the best possible stability. Updates to this repo are usually the kernel and hardware drivers where appropriate and minor bug fixes.

For the more adventurous we provide a ‘rolling’ repository. This repository receives regular updates during the life span of the Rock release. This repository receives regular updates of the entire software stack. It is stable, but may suffer occasional issues during major updates. The users of this repo should keep in touch with our forums or our channels on IRC where major updates are flagged.

The source of the updates come from out third repository ‘cooker’. This repo is the where the development of the distro takes place, this is an unstable repository and can be broken at any time. Anyone may run it but you must be prepared for breakage; that said, it does not occur often. When after a development campaign the cooker repository is considered stable it is copied to rolling.

Within the main repositories there are other sub-repos, the main ones being ‘non-free’ and ‘unsupported’.
The non-free repository contains software which does not comply with OpenSource principle, for example NVidia graphics drivers.
The unsupported repository contains the original ‘contrib’ packages set from Mandrake/Mandriva. The packages in this repository are rebuilt before each release however they are not actively maintained except by those who use use specific packages from that repo. This repo is a great place for fledgling package builders to cut their teeth in the art of software building and packaging. The unsupported repo is an absorbing resource as it contains many interesting and obscure packages and is to some extent a history of open source software.
### For Developers and Packagers
Development takes place in cooker, new packages are created or updated and built on our own infrastructure called ABF (automated build farm) . The build farm is we think unique in that it uses a distributed modular approach to building packages. The structure is such that there is a core controller which distributes jobs to ‘build nodes’ this build nodes can be situated anywhere on the internet which means anyone with an internet connection can provide computing power to the core network which helps greatly when we completely rebuild the repositories in preparation for a new release. The builders are based on the docker technology and as such nodes are easily built and connected. ABF is also connected to GitHub where our package build code is stored.
Anyone can open an account on ABF and create packages in their own personal repositories, those wishing to build packages for the main repositories should join our IRC group #openmandriva-cooker@freenode. This group is set up automatically when starting the konversation IRC app.
### What’s in it for you.
So what do we offer you?
The KDE Plasma desktop with all its bells and whistles, a clean modern elegantly styled desktop;  it is fast and stable and a joy to use.
A friendly and welcoming developer community in which it is easy to participate whatever the level of your skill.
Access to an advanced build environment where you can generate your own packages or work on the main distribution.
For the users, a Discourse forum where like minded people can meet and become friends.
Most of all we continue the tradition of Free and Open software which was expounded by Gael Duval the founder of Mandrake/Mandriva.
#### Postscript:
A quote from Brazil in our irc channel today.
*<euzao> well, I think of the distros that come from Mandrake, OpenMandriva seems to be the most cutting edge one. And it is faster than Arch.*
