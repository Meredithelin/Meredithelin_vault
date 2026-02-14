###### Gemini said

Welcome to the world of Linux! This tutorial will guide you through installing Linux on your Windows computer using a tool called Windows Subsystem for Linux (WSL) and then provide a basic guide to using the command line.  
欢迎来到 Linux 的世界！本教程将指导您使用名为 Windows 子系统 Linux 版 (WSL) 的工具在 Windows 计算机上安装 Linux，然后提供使用命令行的基本指南。

### Part 1: Installing Linux on Windows  
第一部分：在 Windows 上安装 Linux

The easiest way to get Linux on a modern Windows machine is using WSL. It allows you to run a Linux environment directly on Windows, without the need for a separate virtual machine or dual-booting.  
在现代 Windows 机器上安装 Linux 的最简单方法是使用 WSL。它允许您直接在 Windows 上运行 Linux 环境，而无需单独的虚拟机或双启动。

**Step 1: Open Windows Terminal and run the installation command.  
步骤 1：打开 Windows 终端并运行安装命令。**

First, you'll need to open the "Windows Terminal" (or "PowerShell") as an administrator. You can do this by searching for "Terminal" in your Start menu, right-clicking it, and selecting "Run as administrator". Once the terminal window is open, type the following command and press Enter:  
首先，您需要以管理员身份打开“Windows 终端”（或“PowerShell”）。您可以通过在“开始”菜单中搜索“终端”，右键单击它，然后选择“以管理员身份运行”来完成此操作。终端窗口打开后，输入以下命令并按 Enter 键：

`wsl --install`

This command will download and install the necessary components for running Linux, as well as the default Ubuntu distribution.  
该命令将下载并安装运行 Linux 所需的组件，以及默认的 Ubuntu 发行版。

![的图片](https://lh3.googleusercontent.com/gg-dl/AOI_d__42FGhSMQNxMngG0BnzosgYMt4Ckf3Yni4ZzCOTAzOS-Ta7QcG0JCOnkYRQa9CL0Fn9WjPbKJA5dhtCP7lgMrqDCZEvmJ3jI7yXLd_o9g4sZrtc_1TnEySKiedGVFYJZOIPvGOq70qDu6Q-lya2kpgrhGLZ7g359EV_ByhsWgtQOSB1w=s1024-rj)

**Step 2: Set up your Linux username and password.  
步骤 2：设置您的 Linux 用户名和密码。**

After the installation is complete, you will need to restart your computer. Once you've restarted, a new terminal window will open automatically, showing the installation of the Ubuntu distribution. You will be prompted to create a username and password for your new Linux system.  
安装完成后，您需要重启计算机。重启后，会自动打开一个新的终端窗口，显示 Ubuntu 发行版的安装过程。系统会提示您为新的 Linux 系统创建用户名和密码。

Enter a username and press Enter. Then, enter a password and press Enter. You'll need to enter the password again to confirm it.  
输入用户名并按回车键。然后，输入密码并按回车键。您需要再次输入密码进行确认。

_Note: When you type your password, no characters will appear on the screen. This is a normal security feature in Linux.  
注意：输入密码时，屏幕上不会显示任何字符。这是 Linux 系统的一项正常安全功能。_

![的图片](https://lh3.googleusercontent.com/gg-dl/AOI_d_9o2dnin66rFQR3Sa3SsMVOgSs8QevAV4Tb-gjd4IwoMLms__qkDJpoUz6flpsEJLMa98ffwmf3p19Exr53t-gwsXq8QCS-biEzwMJ6iune9lOsHTM-XP_0Lmc72u4NpacKMETk7iRbU-GsuBvr8kdLORc2sB4MVYa__WSpcT488xtg=s1024-rj)

### Part 2: Basic Linux Command-Line Guide  
第二部分：Linux 命令行基础指南

Once you've set up your username and password, you'll be presented with the Linux command prompt, which usually looks like `username@hostname:~$`. This is where you'll interact with your new Linux system.  
设置好用户名和密码后，您将看到 Linux 命令提示符，通常类似于 `username@hostname:~$` 。您将在这里与您的新 Linux 系统进行交互。

**Your First Command: `ls`  
你的第一个命令： `ls`**

The `ls` command stands for "list" and is used to see the files and directories in your current location. Type `ls` and press Enter. You will see a list of the default directories in your home folder, such as `Desktop`, `Documents`, and `Downloads`.  
`ls` 命令代表“列表”，用于查看当前位置的文件和目录。输入 `ls` 并按 Enter 键。您将看到主文件夹中的默认目录列表，例如 `Desktop` 、 `Documents` 和 `Downloads` 。

![的图片](https://lh3.googleusercontent.com/gg-dl/AOI_d__KMgW54OfifgdSmpVNS6TT8uT5tXjNEky3YglwML397zQvifMhDNZakb-yc9cX-fu4VbmAp0YI_P518AMWgUOXgM3VMWmP1xlIfvTo90nhEfuShe6gr8LI_VV-n2CvBq6mjzxft1C92MTBynU9xPQU3WLu_gIuKKWUF_JAbNZgWdHzMQ=s1024-rj)

Here are a few more essential commands to get you started:  
以下是一些帮助您入门的基本命令：

- **`pwd` (Print Working Directory):** This command tells you where you are currently located in the file system. For example, it might output `/home/username`.  
    **`pwd` （打印工作目录）：** 此命令会告诉您当前在文件系统中的位置。例如，它可能会输出 `/home/username` 。
    
- **`cd` (Change Directory):** This command is used to navigate between directories. For instance, to go into your "Documents" folder, you would type `cd Documents`. To go back up one level, you can type `cd ..`.  
    **`cd` （更改目录）：** 此命令用于在目录之间导航。例如，要进入“文档”文件夹，您可以输入 `cd Documents` 。要返回上一级目录，您可以输入 `cd ..`
    
- **`mkdir` (Make Directory):** This command creates a new directory. To create a folder named "my_project", you would type `mkdir my_project`.  
    **`mkdir` （创建目录）：** 此命令创建一个新目录。要创建一个名为“my_project”的文件夹，您可以键入 `mkdir my_project` 。
    
- **`touch`:** This command is used to create an empty file. To create a file named "notes.txt", you would type `touch notes.txt`.  
    **`touch` ：** 此命令用于创建空文件。要创建名为“notes.txt”的文件，您可以输入 `touch notes.txt` 。
    
- **`rm` (Remove):** This command deletes files. To delete the "notes.txt" file you just created, you would type `rm notes.txt`. **Be careful with this command, as deleted files cannot be easily recovered.**  
    **`rm` （删除）：** 此命令会删除文件。要删除刚刚创建的“notes.txt”文件，您可以输入 `rm notes.txt` 。 **请谨慎使用此命令，因为删除的文件不容易恢复。**
    
- **`clear`:** This command clears the terminal screen, giving you a clean slate.  
    **`clear` ：** 此命令清除终端屏幕，使您获得一个干净的界面。
    

Congratulations! You have successfully installed Linux on your Windows machine and learned the very basics of using the command line. As you continue to explore, you'll find that the command line is a powerful tool for managing your system and getting things done.  
恭喜！您已成功在 Windows 计算机上安装了 Linux，并掌握了命令行使用的基本知识。随着您不断探索，您会发现命令行是管理系统和完成任务的强大工具。