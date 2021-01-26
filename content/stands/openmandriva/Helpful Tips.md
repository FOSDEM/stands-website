### Helpful tips for those new to OM Lx or Linux
OpenMandriva is designed to be a unique and independent Community distribution of Linux and direct descendant of Mandriva Linux.

For those new to Linux or OpenMandriva Lx there are a few helpful things to know regarding what is available on installed system, how to add/remove software, and keep you system up to date.

The KDE Plasma desktop is very intuitive and configurable. Use your mouse pointer to hover on each of the desktop and menu panel icons and a Tooltips window pops up telling what each is for. On the far left of the menu panel you will find the Application Launcher. You will want to explore what is available there. Some commonly used applications are in the column on the left and a list with more is on the right. 

For connecting to wifi simply select the icon in menu panel that says Network, select your wifi connection and enter your password.

Also you have already noticed when you logged in for the first time an application called OM-Welcome. OM-Welcome has many handy short cuts and you are encouraged to explore here and use what ever you find useful. In particular you will want to look under OM Features, Configure, and Applications sections. Under OM Features section you will find the om-repo-picker (aka: Software Repository Selector) where you may select additional software repositories (repos) for software that is not in our Main repository. Configuration has some handy options to customize and configure your desktop. Applications section has shortcuts to install some popular applications that are not installed by default. Also in the OM Features page you will see a link to the OM Control Center with more configuration and system administration utilities.

A special note about om-repo-picker (aka: Software Repository Selector). Please read the description of each repository (repo). For instance Unsupported repo is actually Community supported, the Unsupported means not officially supported by OM developers but there is Community support. Pay attention to the Non-free and Restricted repo descriptions. Neither of these has a large number of packages and it is important that user realize the non-free means this is software with closed source code and restrictive licenses. OM developers can not fix or even touch the software code for non-free repo packages. Restricted software may be illegal in some countries. Packages in restricted repo may also have restrictive licenses.

In Application Launcher>Settings there is a utility called SystemSettings. This is the KDE Plasma desktop configuration utility. Look around and see what you may find useful there is a lot you can do in SystemSettings. 

There is an icon in the menu panel called Updates. Updates will pop up when the system detects that there are operating system updates available. This is a part of the KDE Plasma suite of applications called Discover. Discover is also a GUI package manager that is may be used for searching, installing, and removing software. We also provide in Application Launcher>System another GUI package manager called dnfdragora. Users are welcome to use these if they wish. However we recommend that they be used primarily to search for software but not for updating system, removing, and installing software.

Discover and dnfdragora may take a while to display the packages list, so give them a few seconds to load the metadata from the repositories.

Why? Over time the QA team has found that the vast majority of issues involving package management start with "I <did something with Discover>" or "I <did something with dnfdragora>". It is suspected this has more to do with users not paying attention to what they are doing, especially not paying attention to error messages or warnings, than it means something is wrong with either application. Package management from Konsole is very easy and has a magical feature that when things happen the system prints what is happening right before you very eyes! If there is an issue the system will tell you there is an issue and like magic it tells what the issue is. Then you, the user, can decide whether to proceed or ask for assistance. Assistance we provide on our Forum,  #openmandriva-cooker on freenode and #openmandriva-cooker:matrix.org in matrix.

Just doing a few simple commands helps user to get over apprehension of using the Linux command line. Most users will only use this occaisionally but it is very powerful to have this tool at your command.

Here is what we recommend. Go to Application Launcher and find in the list on the left Terminal (Konsole). Konsole is the KDE terminal also called the command line interface (CLI). Do not be afraid, what we are going to do is simple and easy.

In Konsole on the left you will see the $ this is the shell prompt. The $ means you are logged in to the system as user. If you were to see # instead of $ that would mean you were logged in as system administrator (sys admin) or what in Linux folks call root. We will keep you logged in as user for safety but we will invoke some commands as sys admin by using sudo as part of the command we type (or copy and paste). OK, let's update our system. In Konsole type or copy and paste the following:

    sudo dnf clean all ; sudo dnf upgrade

You will be asked for root password, enter that and hit the Enter key. That is not so difficult is it? 

What this command string does is:

- sudo >>> gives the command root (sys admin) privileges if accompanied by root password. In OM Lx the user created when one installs OM Lx is by default given sudo privileges. Any other user would need to be added to the sudo list. That is beyond the scope of this article, if you have a need for doing this please ask us.

- dnf clean all >>> dnf is the CLI package manager OM uses, dnf clean all means that dnf is removing everything left in cache from any previous transactions and also updates the package metadata with the latest metadata in OM repos. This ensures that you will get the latest packages available.

- ; >>> the semi-colon is simply a way one may link multiple commands in to one command string

- dnf upgrade >>> This is the command to upgrade your operating system

Not so difficult to understand either is it? Pay attention to the output especially any error message or warning. If anything happens that you don't know how to handle ask us before proceeding.

Using dnf in Konsole to search, install, and remove packages is just as easy:

    dnf search <keyword> 

    sudo dnf install <package_name>

    sudo dnf remove <package_name>

To check which repos you have enabled:

    dnf repolist

- sudo is not needed for search or repolist commands. Remember that Discover and dnfdragora also may be used to search for software.

To best enjoy your new OpenMandriva Lx operating system don't be afraid to do a little reading and ask questions, we have all been beginners. There is more knowledge available in our Wiki and in Resources section on the Forum.

As always if you have any comments, suggestions, or questions ask us on our Forum, IRC, or Matrix rooms.

For support remember that our OM Forum is basically users that help other users. If a user can help with your issue this is a great place to ask for help. Unfortunately sometimes we encounter issues that need more knowledge and skill. For that we need to get the attention of developers. This is best done with a bug report on our Issue Tracker, or on IRC or Matrix rooms. A bug report is best because it is written and thus hard to ignore or forget. 

OpenMandriva is designed to be a unique and independent Community distribution of Linux and direct descendant of Mandriva Linux. OpenMandriva is a small group of all volunteer, part-time, and unpaid contributors. Things get done when someone in the OM Community volunteers and does it. When people are helping you they are donating their time, knowledge and skill to you. Please be mindful of this.
