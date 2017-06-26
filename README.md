This is just a mirror/copy of DropWatch via rpmfind to make it buildable/usable on Ubuntu (debian?)

[source](https://rpmfind.net/linux/rpm2html/search.php?query=dropwatch)

- Building in Ubuntu (16.04)
----

install binutils, readline, nl-3, nl-genl-3

[github upstream](https://github.com/pavel-odintsov/drop_watch)
need different kernel for 14.04 [src](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1660634)

```
$ ldd dropwatch
linux-vdso.so.1 =>  (0x00007fffb47ff000)
libbfd-2.24-system.so => not found
libreadline.so.6 => /lib/x86_64-linux-gnu/libreadline.so.6 (0x00007fec40031000)
libnl-3.so.200 => /lib/libnl-3.so.200 (0x00007fec3fe18000)
libnl-genl-3.so.200 => /lib/libnl-genl-3.so.200 (0x00007fec3fc13000)
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fec3f854000)
libtinfo.so.5 => /lib/x86_64-linux-gnu/libtinfo.so.5 (0x00007fec3f62c000)
libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fec3f40f000)
libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fec3f113000)
/lib64/ld-linux-x86-64.so.2 (0x00007fec4027c000)
```
