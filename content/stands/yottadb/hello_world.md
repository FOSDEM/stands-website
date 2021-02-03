---
title: "Hello World Examples"
draft: false
---

The following sections discuss YottaDB's Multi-Language support via a simple `sayHello` example. Each language uses its own sample program to add a node in the same database. Then the MUPIP EXTRACT command is used to display the contents of that database, successfully showing YottaDB being accessed by different APIs/ wrappers.

## Access from C

YottaDB comes with a [C API](https://docs.yottadb.com/MultiLangProgGuide/cprogram.html) and all you need to use it is the gcc compiler. The `sayhelloC.c` program is downloaded, compiled and run. Notice that it sets a node in the database (the MUPIP EXTRACT command prints database contents):

```bash
yottadbuser@yottadbworkshop:~$ ls -l
total 52
-rw-r--r-- 1 root        root            262 Jan 17  2020 sayhelloC.c
-rwxr-xr-x 1 yottadbuser yottadbuser   47020 Aug 26 14:00 ydbinstall.sh
yottadbuser@yottadbworkshop:~$ gcc $(pkg-config --libs --cflags yottadb) -o sayhelloC sayhelloC.c -lyottadb
yottadbuser@yottadbworkshop:~$ ls -l
total 72
-rwxr-xr-x 1 yottadbuser yottadbuser   16600 Aug 26 14:41 sayhelloC
-rw-r--r-- 1 root        root            262 Jan 17  2020 sayhelloC.c
-rwxr-xr-x 1 yottadbuser yottadbuser   47020 Aug 26 14:00 ydbinstall.sh
yottadbuser@yottadbworkshop:~$ ./sayhelloC
yottadbuser@yottadbworkshop:~$ mupip extract -format=zwr -label="Hello label" -select=hello -stdout
Hello label UTF-8
26-AUG-2020  15:00:13 ZWR
^hello("C")="Hello, world!"
%YDB-I-RECORDSTAT, ^hello:        Key cnt: 1  max subsc len: 10  max rec len: 13  max node len: 27
%YDB-I-RECORDSTAT, TOTAL:         Key cnt: 1  max subsc len: 10  max rec len: 13  max node len: 27
yottadbuser@yottadbworkshop:~$
```

## Access from Go

[Accessing YottaDB from Go](https://docs.yottadb.com/MultiLangProgGuide/goprogram.html) requires the Go yottadb package to be downloaded and installed. The `sayhelloGo.go` program is downloaded, compiled and run. Notice that it too sets a node in the database:

```bash
yottadbuser@yottadbworkshop:~$ go build sayhelloGo.go
yottadbuser@yottadbworkshop:~$ ./sayhelloGo
yottadbuser@yottadbworkshop:~$ mupip extract -format=zwr -label="Hello" -select=hello -stdout
YottaDB MUPIP EXTRACT /usr/local/lib/yottadb/r130/mupip extract -format=zwr -select=hello -stdout UTF-8
26-AUG-2020  15:08:23 ZWR
^hello("C")="Hello, world!"
^hello("Go")="สวัสดีชาวโลก"
%YDB-I-RECORDSTAT, ^hello:        Key cnt: 2  max subsc len: 11  max rec len: 36  max node len: 44
%YDB-I-RECORDSTAT, TOTAL:         Key cnt: 2  max subsc len: 11  max rec len: 36  max node len: 44
yottadbuser@yottadbworkshop:~$
```

## Access from M

YottaDB includes a complete language implementation for M. The `sayhelloM.m` program is downloaded and run (there is no need for a separate compilation step, as there was for C and Go):

```bash
yottadbuser@yottadbworkshop:~/.yottadb$ ls -l r
total 4
-rw-r--r-- 1 yottadbuser yottadbuser 67 Jan 17  2020 sayhelloM.m
yottadbuser@yottadbworkshop:~/.yottadb$ yottadb -run sayhelloM
yottadbuser@yottadbworkshop:~/.yottadb$ mupip extract -format=zwr -label="Hello" -select=hello -stdout
YottaDB MUPIP EXTRACT /usr/local/lib/yottadb/r130/mupip extract -format=zwr -select=hello -stdout UTF-8
26-AUG-2020  15:12:49 ZWR
^hello("C")="Hello, world!"
^hello("Go")="สวัสดีชาวโลก"
^hello("M")="Приветствую, мир!"
%YDB-I-RECORDSTAT, ^hello:        Key cnt: 3  max subsc len: 11  max rec len: 36  max node len: 44
%YDB-I-RECORDSTAT, TOTAL:         Key cnt: 3  max subsc len: 11  max rec len: 36  max node len: 44
yottadbuser@yottadbworkshop:~/.yottadb$
```

## Access from Perl

YottaDB can also be accessed from Perl, which requires the Perl yottadb package to be downloaded and installed, to provide a YottaDB Perl “wrapper”.

The `sayhelloPerl.pl` program is downloaded, marked as an executable and run.

```bash
yottadbuser@yottadbworkshop:~$ ls -l
total 3176
drwxr-xr-x 4 yottadbuser yottadbuser    4096 Aug 26 14:42 go
-rwxr-xr-x 1 yottadbuser yottadbuser   16600 Aug 26 14:41 sayhelloC
-rw-r--r-- 1 root        root            262 Jan 17  2020 sayhelloC.c
-rwxr-xr-x 1 yottadbuser yottadbuser 3164920 Aug 26 14:44 sayhelloGo
-rw-r--r-- 1 yottadbuser yottadbuser     203 Jan 17  2020 sayhelloGo.go
-rw-r--r-- 1 yottadbuser yottadbuser      86 Aug 26 15:21 sayhelloPerl.pl
-rwxr-xr-x 1 yottadbuser yottadbuser   47020 Aug 26 14:00 ydbinstall.sh
yottadbuser@yottadbworkshop:~$ chmod +x sayhelloPerl.pl
yottadbuser@yottadbworkshop:~$ ./sayhelloPerl.pl.
yottadbuser@yottadbworkshop:~$ mupip extract -format=zwr -select=hello -stdout
YottaDB MUPIP EXTRACT /usr/local/lib/yottadb/r130/mupip extract -format=zwr -select=hello -stdout UTF-8
26-AUG-2020  15:24:21 ZWR
^hello("C")="Hello, world!"
^hello("Go")="สวัสดีชาวโลก"
^hello("M")="Приветствую, мир!"
^hello("Perl")="Grüẞ Gott Welt"
%YDB-I-RECORDSTAT, ^hello:        Key cnt: 4  max subsc len: 13  max rec len: 36  max node len: 44
%YDB-I-RECORDSTAT, TOTAL:         Key cnt: 4  max subsc len: 13  max rec len: 36  max node len: 44
yottadbuser@yottadbworkshop:~$
```

## Access from Rust

YottaDB can also be accessed from Rust, using the YottaDB wrapper for Rust [YDBRust](https://gitlab.com/YottaDB/Lang/YDBRust). Run the `say_hello_rust` example, which will add another node in the database:

```bash
yottadbuser@yottadbworkshop:~$ git clone --quiet https://gitlab.com/YottaDB/Lang/YDBRust/ # Do this only once for the Acculturation Guide
yottadbuser@yottadbworkshop:~$ cd YDBRust
yottadbuser@yottadbworkshop:~/YDBRust$ cargo run --quiet --example say_hello_rust # May take some time the first time
yottadbuser@yottadbworkshop:~/YDBRust$ mupip extract -format=zwr -select=hello -stdout
YottaDB MUPIP EXTRACT /usr/local/lib/yottadb/r130/mupip extract -format=zwr -select=hello -stdout UTF-8
28-AUG-2020  15:34:04 ZWR
^hello("C")="Hello, world!"
^hello("Go")="สวัสดีชาวโลก"
^hello("M")="Приветствую, мир!"
^hello("Perl")="Grüẞ Gott Welt"
^hello("Rust")="こんにちは"
%YDB-I-RECORDSTAT, ^hello:        Key cnt: 5  max subsc len: 13  max rec len: 36  max node len: 44
%YDB-I-RECORDSTAT, TOTAL:         Key cnt: 5  max subsc len: 13  max rec len: 36  max node len: 44
yottadbuser@yottadbworkshop:~/YDBRust$
```
