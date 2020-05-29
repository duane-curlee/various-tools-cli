# About my CLI tools
Various tools for the command-line interface

<dl>
  <dt>arcem.py</dt>
  <dd>As in 'ARCive thEM', Python based command-line tool for creating zip files</dd>
  <dt>dir-time.py</dt>
  <dd>Displays the three date and time stamps on files and folders</dd>
  <dt>du.py</dt>
  <dd>some-what like the Unix/Linux du command</dd>
  <dt>empty-these.py</dt>
  <dd>Removes all items from the folders you specify on the command line</dd>
  <dt>file_exists_case.py</dt>
  <dd>Checks to see if a file exists, and is case sensitive</dd>
</dl>

## About arcem.py
arcem.py, as in 'ARCive thEM', or "archive 'em", is a Python based
command line tool for creating zip files for archiving. You specify the
files and/or folders on the command line to include, and this tool will
place a zip file in your current working directory with this filename
format:

backup-(date-time-stamp).zip

All paths within the zip file will stay relevent-pathed, as you specified
on the command line.

### About my standard date and time stamp
The date and time stamp will be in this format:

year-month-day-hour-minute-second

Sample: backup-2020-05-25-14-07-38.zip

Which is May 25, 2020, at 2:07pm and 38 seconds.

Year is always 4-digit, all others are 2-digits. This way, the zip file
will show when the archive was created, yet the operating system's date
and time stamp will change and show when the archive was last modified.
Also this format allows the backup files to be sorted based on age when
listed.

## About dir-time.py
Displays these three date and time stamps on files and folders:

1. File creation
2. Last modification
3. Last Access

It's useful for debugging software that uses these date and time
stamps, such as my own photo-importer.py program. This is still
under construction, check back for updates.

### Sample output
```
$ python dir-time.py *.py
=== file: dir-time.py ===
When created:  Mon Apr  8 20:17:08 2019
Last modified: Thu Apr 11 21:27:06 2019
Last accessed: Fri Apr 12 13:49:33 2019
=== file: photo-import-cli.py ===
When created:  Mon Apr  8 11:17:31 2019
Last modified: Fri Apr 12 13:48:15 2019
Last accessed: Fri Apr 12 13:48:17 2019
```

## About empty-these.py
Removes all files and folders from the folders you specify on the
command line, but it will not remove the folders you specified.
It will not prompt if you are sure, so be sure before you execute.

This utility will only empty whole directories, it does not delete
individual files. Wildcards are accepted, be careful with them.

## About file\_exists\_case.py
This utility checks to see if a file exists, and is also case sensitive.
This is very handy on a Microsoft Windows platform, which is not a
case-sensitive operating system. This is unneeded on Linux and Apple
computers.

This script file\_exist\_case.py only exists to preserve the function
file\_exists\_case() which can be copied to your own Python script if
you need this funtionality. This function accepts a filename only, not a
folder name, it then does a case-sensetive exisitance check, and returns
True or False.
