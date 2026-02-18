# Linux 命令行综合教程

欢迎来到 Linux 的世界！本教程将指导您从零开始，逐步掌握强大而高效的 Linux 命令行。无论您是开发者、系统管理员，还是对技术充满好奇的用户，命令行都将是您不可或缺的工具。

---

## 目录
1.  [第一部分：在 Windows 上安装 Linux (WSL) 与入门](#part-1-installing-linux-on-windows)
2.  [第二部分：核心概念与获取帮助](#part-2-core-concepts-and-getting-help)
3.  [第三部分：文件与目录操作命令大全](#part-3-file-and-directory-operations)
4.  [第四部分：文本查看与处理](#part-4-text-viewing-and-processing)
5.  [第五部分：权限管理](#part-5-permission-management)
6.  [第六部分：进程管理](#part-6-process-management)
7.  [第七部分：系统与网络](#part-7-system-and-networking)
8.  [第八部分：软件包管理](#part-8-package-management)
9.  [附录：常用命令速查表](#appendix-cheatsheet)

---

### Part 1: Installing Linux on Windows
#### (第一部分：在 Windows 上安装 Linux 与入门)

本节整合自您的原有教程，为初学者提供了在 Windows 系统上快速体验 Linux 的方法。

在现代 Windows 机器上安装 Linux 的最简单方法是使用 **WSL (Windows Subsystem for Linux)**。它允许您直接在 Windows 上运行一个完整的 Linux 环境，而无需单独的虚拟机或双启动。

**步骤 1：以管理员身份打开 Windows Terminal 并运行安装命令。**

在“开始”菜单中搜索“Terminal”或“PowerShell”，右键单击它，选择“以管理员身份运行”。然后输入以下命令并按 Enter：

```powershell
wsl --install
```
该命令将自动下载并安装运行 Linux 所需的组件，以及默认的 **Ubuntu** 发行版。

**步骤 2：设置您的 Linux 用户名和密码。**

安装完成后，重启计算机。重启后，系统会自动完成 Ubuntu 的安装，并提示您为新的 Linux 系统创建用户名和密码。

_注意：输入密码时，屏幕上不会显示任何字符。这是 Linux 的一项正常安全功能。_

**步骤 3：基础命令入门**

设置完成后，您将看到 Linux 命令提示符，通常类似于 `your_username@hostname:~$`。这里有一些最基本的命令让您入门：

| 命令      | 完整名称                    | 功能描述                                     |
| :------ | :---------------------- | :--------------------------------------- |
| `ls`    | List                    | 列出当前目录下的文件和文件夹。                          |
| `pwd`   | Print Working Directory | 显示您当前所在的完整路径。                            |
| `cd`    | Change Directory        | 切换目录。`cd ..` 返回上一级，`cd ~` 返回主目录。         |
| `mkdir` | Make Directory          | 创建一个新的目录。例如 `mkdir my_project`。          |
| `touch` | Touch                   | 创建一个空文件。例如 `touch notes.txt`。            |
| `rm`    | Remove                  | 删除文件。例如 `rm notes.txt`。**此操作不可逆，请谨慎使用！** |
| `rmdir` | Remove Directory        | 删除一个 **空** 目录。                           |
| `clear` | Clear                   | 清空终端屏幕上的所有内容。                            |

---

### Part 2: Core Concepts and Getting Help
#### (第二部分：核心概念与获取帮助)

- **命令结构**: `command [options] [arguments]` (命令 [选项] [参数])
  - `command`: 您要执行的程序，如 `ls`。
  - `options`: 通常以 `-` 或 `--` 开头，用于调整命令的行为，如 `ls -l`。
  - `arguments`: 命令操作的对象，通常是文件或目录名。
- **获取帮助**:
  - `man <command>`: (manual) 显示一个命令最详尽的说明手册。例如 `man ls`。按 `q` 退出。
  - `<command> --help`: 显示一个命令的简明用法和选项列表。

---

### Part 3: File and Directory Operations
#### (第三部分：文件与目录操作命令大全)

| 命令 | 功能描述 | 常用示例 |
| :--- | :--- | :--- |
| `ls -a` | 列出所有文件，包括以 `.` 开头的隐藏文件。 | `ls -a` |
| `ls -l` | (long) 以长格式详细列出文件信息（权限、所有者、大小、修改日期）。 | `ls -l` |
| `ls -h` | (human-readable) 配合 `-l` 使用，以易于阅读的格式（如 KB, MB）显示文件大小。 | `ls -lh` |
| `cp` | (Copy) 复制文件或目录。 | `cp source.txt destination.txt` (复制文件)<br>`cp -r source_dir/ dest_dir/` (递归复制目录) |
| `mv` | (Move) 移动文件/目录，或对其进行重命名。 | `mv old_name.txt new_name.txt` (重命名)<br>`mv my_file.txt ../` (移动到上级目录) |
| `find` | 在指定目录中查找文件。 | `find . -name "*.js"` (查找当前目录下所有 .js 文件)<br>`find /home -user bob` (查找/home下属于bob的文件) |
| `locate` | 快速定位文件（基于数据库，比 `find` 快但可能不是最新的）。 | `locate my_document.pdf` |

---

### Part 4: Text Viewing and Processing
#### (第四部分：文本查看与处理)

| 命令         | 功能描述                                                   | 常用示例                                                                            |               |                            |
| :--------- | :----------------------------------------------------- | :------------------------------------------------------------------------------ | ------------- | -------------------------- |
| `cat`      | (Concatenate) 查看小型文件的全部内容。                             | `cat file.txt`                                                                  |               |                            |
| `less`     | 以可翻页的方式查看大型文件（推荐）。                                     | `less long_log.log` (使用箭头键导航, 按 `q` 退出)                                         |               |                            |
| `head`     | 查看文件的前N行（默认10行）。                                       | `head -n 20 file.txt` (查看前20行)                                                  |               |                            |
| `tail`     | 查看文件的后N行（默认10行）。                                       | `tail -n 50 file.txt` (查看后50行)<br>`tail -f app.log` (实时跟踪文件更新)                  |               |                            |
| `grep`     | (Global Regular Expression Print) 在文本中搜索匹配的行。          | `grep "error" app.log` (查找包含"error"的行)<br>`grep -i "hello" file.txt` (-i 忽略大小写) |               |                            |
| `          | `                                                      | **管道 (Pipe)**：将一个命令的输出作为另一个命令的输入。                                               | `cat data.txt | grep "user_id"` (在文件内容中搜索) |
| `>` / `>>` | **重定向 (Redirection)**：`>` 将输出写入文件（覆盖），`>>` 将输出追加到文件末尾。 | `ls -l > file_list.txt` (将列表保存到文件)                                              |               |                            |
| `wc`       | (Word Count) 统计文件的行数、单词数和字符数。                          | `wc -l file.txt` (只统计行数)                                                        |               |                            |

---

### Part 5: Permission Management
#### (第五部分：权限管理)

使用 `ls -l` 时，您会看到类似 `-rwxr-xr--` 的字符串。这代表了文件的权限。

- **r**: 读 (read)
- **w**: 写 (write)
- **x**: 执行 (execute)
- **前3位**: 文件所有者 (user) 的权限
- **中3位**: 文件所属组 (group) 的权限
- **后3位**: 其他用户 (others) 的权限

| 命令 | 功能描述 | 常用示例 |
| :--- | :--- | :--- |
| `chmod`| (Change Mode) 修改文件或目录的权限。 | `chmod +x script.sh` (为脚本添加执行权限)<br>`chmod 755 my_script.sh` (使用数字模式设置权限) |
| `chown`| (Change Owner) 修改文件或目录的所有者和所属组。 | `chown bob:developers file.txt` (所有者改为bob, 组改为developers) |

---

### Part 6: Process Management
#### (第六部分：进程管理)

| 命令 | 功能描述 | 常用示例 |
| :--- | :--- | :--- |
| `ps` | (Process Status) 显示当前用户的活动进程。 | `ps aux` (显示系统上所有进程的详细信息) |
| `top` | 动态实时地显示系统进程和资源占用情况（CPU、内存）。按 `q` 退出。 | `top` |
| `kill` | 向进程发送信号，通常用于终止进程。 | `kill 12345` (终止进程ID为12345的进程) |
| `pkill`| 根据进程名终止进程。 | `pkill nginx` |
| `&` | 在命令末尾添加 `&`，使命令在后台运行。 | `./my_long_script.sh &` |

---

### Part 7: System and Networking
#### (第七部分：系统与网络)

| 命令 | 功能描述 | 常用示例 |
| :--- | :--- | :--- |
| `df` | (Disk Free) 显示磁盘空间使用情况。 | `df -h` |
| `du` | (Disk Usage) 显示文件或目录的磁盘占用大小。 | `du -sh /path/to/dir` (-s 总结, -h 人性化) |
| `free` | 显示系统内存使用情况。 | `free -h` |
| `ping` | 测试与另一台主机的网络连接。 | `ping google.com` |
| `ssh` | (Secure Shell) 安全地远程登录到另一台主机。 | `ssh user@remote_host` |
| `scp` | (Secure Copy) 在本地和远程主机之间安全地复制文件。 | `scp local_file.txt user@remote:/home/user/` |

---

### Part 8: Package Management
#### (第八部分：软件包管理)

大多数 Linux 发行版都有自己的包管理器，用于安装、更新和删除软件。

- **Debian/Ubuntu (使用 APT)**
  - `sudo apt update`: 更新可用软件包列表。
  - `sudo apt upgrade`: 升级所有已安装的软件包。
  - `sudo apt install <package_name>`: 安装一个新软件。
  - `sudo apt remove <package_name>`: 卸载一个软件。
  - `sudo apt search <keyword>`: 搜索软件包。

- **RedHat/CentOS (使用 YUM/DNF)**
  - `sudo dnf update`: 更新所有已安装的软件包。
  - `sudo dnf install <package_name>`: 安装一个新软件。
  - `sudo dnf remove <package_name>`: 卸载一个软件。
  - `sudo dnf search <keyword>`: 搜索软件包。

---

### Appendix: Cheatsheet
#### (附录：常用命令速查表)

| 类别 | 命令 |
| :--- | :--- |
| **文件/目录** | `ls`, `cd`, `pwd`, `cp`, `mv`, `rm`, `mkdir`, `find` |
| **文本处理** | `cat`, `less`, `head`, `tail`, `grep`, `wc`, `sort` |
| **系统/进程** | `top`, `ps`, `kill`, `df`, `du`, `free`, `uname` |
| **网络** | `ping`, `ssh`, `scp`, `wget`, `curl` |
| **权限** | `chmod`, `chown`, `sudo` |

恭喜！您已经完成了 Linux 命令行综合教程。最好的学习方法是不断实践，尝试在日常工作中使用这些命令来解决实际问题。
