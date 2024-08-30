# Linux Operating System

### Linux Features & Bash

// Popular Linux Distributions

- Ubuntu: One of the most widely used and 'Beginner'-friendly distributions. It focuses on ease of use, stability, and a large user COMMUNITY.

- Debian: Known for its stability, reliability, and adherence to open-source principles. Debian serves as the base for several other distributions, including Ubuntu.

- Fedora: Developed by the Fedora Project and sponsored by Red Hat. It emphasizes the use of cutting-edge technologies and serves as a TESTING ground for new features that may eventually make their way into Red Hat Enterprise Linux (RHEL).

- CentOS: Based on the source code of Red Hat Enterprise Linux, CentOS aims to provide a free, COMMUNITY-supported alternative to RHEL. It is popular for server deployments.

- Arch Linux: Designed for advanced users who prefer a DIY (do-it-yourself) approach. Arch Linux focuses on simplicity, minimalism, and user-centric customization.

- openSUSE: A COMMUNITY-driven distribution known for its stability, user-friendly configuration tools, and professional-grade features.

- Linux Mint: Built on top of Ubuntu, Linux Mint provides a polished and user-friendly desktop environment, making it an attractive choice for Beginners' transitioning from Windows.

- Manjaro: Based on Arch Linux, Manjaro is known for its user-friendly approach and pre-installed software packages. It offers a balance between cutting-edge software and stability.

Summary
- Ubuntu and Linux Mint are popular among 'Beginners' for their ease of use.
- Fedora and Arch Linux attract more experienced users who want cutting-edge or highly customizable systems.
- Debian and CentOS/Rocky Linux/AlmaLinux are favored in SERVER environments for their stability.

// WSL2 Supported Distributions
- Ubuntu
- Debian (Stable and reliable)
- Kali Linux
- Fedora
- openSUSE
- Alpine Linux

// Package Managers
- apt    => Ubuntu/Debian (and distributions based on them, like Linux Mint and Kali Linux)
- dnf    => Fedora (and also Oracle Linux in newer versions)
- zypper => openSUSE
- apk    => Alpine Linux

### Basic Linux Commands of Linux
sudo apt update -y
sudo apt upgrade -y
sudo apt dist-upgrade -y .....
pwd

ls -l
ll # ls -l plus all .directories 

ls *pipeline.* -l # Wildcard
ls simple? -l

mkdir mydir
mkdir -p mydir/dir1/dir2

cd mydir

cd ~ # Home directory
cd ~/folder1
cd ~

### File operations
touch test.txt
echo "Test Text" > test.txt
cat test.txt
nano test.txt

// More and Less
- Forward Pages: Press `Space` to move forward by one screen.

- Quit: Press `q` to quit the less command.

more test.txt 
- Line by Line: Press `Enter` to move down one line at a time.

less test.txt
- Backward Pages: Press `b` to move backward by one screen.
- Line by Line: Use the `Arrow Up` and `Arrow Down` keys to move up and down one line at a time.
- Search: 
    - Press `/` followed by the search term to search forward, 
    - Press `?` followed by the search term to search backward. 
    - Press `n` to find the next occurrence and
    - Press `N` to find the previous occurrence.

### Copy/Rename/Move/Delete operations for File or Folder
// Copy => cp
cp file1 file2
cp -r folder1/. folder2/ # Existing folder
cp -r folder1/ folder2/ # Non-existing folder

// Rename or Move => mv
mv

// Delete => rm
rm -r 
rm -r mydir

### File/Directory permissions
ls / -l

    drwxr-xr-x   3 root root    4096 Jun 28 22:23 Docker
    lrwxrwxrwx   1 root root       7 Nov 23  2023 bin -> usr/bin
    drwxr-xr-x   2 root root    4096 Apr 18  2022 boot
    drwxr-xr-x  16 root root    3540 Aug 30 09:41 dev
    ...

1. The File Type Indicator:
    - 1st Character: Indicates the type of the file.
        - : Regular file
        d : Directory
        l : Symbolic link (bin -> usr/bin)
        b : Block device file (e.g., a hard drive) => ls -l /dev/sda
        c : Character device file (e.g., a keyboard or a mouse) => ls -l /dev/tty
        p : Named pipe (FIFO) => ls -l /run | grep '^p'
        s : Socket file => ls -l /var/run/docker.sock
2. Owner (User) Permissions:
    - 2nd to 4th Characters: Indicate the permissions for the owner (user) of the file.
        r : Read permission (can view the contents of the file)
        w : Write permission (can modify the contents of the file)
        x : Execute permission (can run the file as a program or script)
        - : No permission    
3. Group Permissions
    - 5th to 7th Characters: Indicate the permissions for the group associated with the file.
       Same as 2.
4. Other Permissions
    - 8th to 10th Characters: Indicate the permissions for others (everyone else).
       Same as 2. 

// Change Owner and Group
echo "Test Text" > test.txt
mkdir test
sudo chown root:root test.txt
sudo chown root:root test

ls -l
    ...
    drwxr-xr-x 2 root         root          4096 Aug 30 18:05 test
    -rw-r--r-- 1 root         root            10 Aug 30 18:05 test.txt
    ...

rm test -r
rm test.txt

### Change Mode
chmod (change mode) is the command to update the read/write/execute permissions for a file/directory
- r = 4, 
- w = 2, 
- x = 1

| rwx  | rwx  | rwx
| 421  | 421  | 421

Examples:
- chmod 777 file/dir -- rwx for root, rwx for owner, rwx for others 
- chmod 764 file/dir -- rwx for root, rw for owner, r for others 
- chmod 755 file/dir -- rwx for root, rx for owner, rx for others
- chmod 400 file/dir -- r for root, for owner/other no permissions
