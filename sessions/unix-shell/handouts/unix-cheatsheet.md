# Unix Cheatsheet

## Basic Commands

- `pwd`: print the current directory
- `ls`: list the files in the current directory
- `cd`: change the current directory
- `cat`: print the contents of a file
- `man` will display the help page for a command
- `touch`: create an empty file
- `mv`: move/rename a file or directory
- `cp`: copy a file to a new location
- `rm`: remove a file
- `mkdir`: create a directory

### Examples

```sh
#show current directory
$ pwd
#show files in current directory
$ ls .
# change to the src directory
$ cd ./src
# print the contents of hello.txt
$ cat ./hello.txt.py
# show files cats folder which is found in the parents parent Picture directory
$ ls ../../Pictures/cats
# show the help page for the ls command
$ man ls
# make directory folder-one in the current directory
$ mkdir folder-one
# make directory folder-two in the current directory
$ mkdir folder-two
# make directory backups in the current directory
$ mkdir backups
# make empty file hello.txt in folder-one
$ touch folder-one/hello.txt
# move hello.txt from folder-one to folder-two
$ mv folder-one/hello.txt folder-two
# copy hello.txt to backups directory
$ cp folder-two/hello.txt backups/
# delete hello.txt from folder-two
$ rm folder-two/hello.txt
# delete folder-two and the containing sub-folders and files
$ rm -rf folder-two
```

## Useful Commands

- `echo`: print some text to the screen
- `history`: show list of previously run commands
- `clear`: wipe the screen
- `less`: show the contents of a file in a paginated way
- `head`: display the first `n` lines of input
- `tail`: display the last `n` lines of input
- `grep`: search text in files
- `find`: search a file by name or other properties
- `whereis`: get the location of a program
- `sudo` allows regular users to become root temporarily so they can run privileged commands
- `export` sets environment variable
- `nano` creates a simple text editor
- `vi` creates a vim text editor
- `chmod`: change file permissions
    - Usage: `chmod <target><+/-><access_type> file`
    - E.g `chmod a+rw my_file.py`

### chmod flags

Targets

- `u`: owner
- `g`: group
- `a`: all (everyone)

Access Types:

- `r`: read
- `w`: write
- `x`: execute

### chmod Permission Table

| #   | Permission           | rwx | Binary |
| --- | -------------------- | --- | ------ |
| 7   | read, write, execute | rwx | 111    |
| 6   | read, write          | rw- | 110    |
| 5   | read, execute        | r-x | 101    |
| 4   | read only            | r-- | 100    |
| 3   | write, execute       | -wx | 011    |
| 2   | write only           | -w- | 010    |
| 1   | execute only         | --x | 001    |
| 0   | none                 | --- | 000    |

### Examples

```sh
# search for the "hello" in the folder directory
$ grep "hello" ./folder/*
# flags are -i (case-insensitive) and -r (recursive)
$ grep -ri "hello" ./folder
# search for file named "app.py"
$ find ./ -name "app.py"
# You can also use wildcards
$ find ./ -name "app*"
# look for the location of grep
$ whereis grep
# Everyone can read
$ chmod a+r hello.txt
# Only the owner of the file can write
$ chmod u+w hello.txt
# Everyone (All) can no longer read
$ chmod a-r hello.txt
# root user copy python3 to python-three
$ sudo cp /bin/python3 /bin/python-three
# Print the value of an environment variable
echo $PATH
# Set an environment variable
export MYNEWVAR="hello"
```
