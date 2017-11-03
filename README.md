Pyxrad
======

This repository contains scripts useful for querying and obtaining data from the Amazon Web Services NEXRAD archive.

The `example()` script contains an example sequence to use all of the functions. 

Functions
---------

### `get_filenames(year, month, day, hour, location)`

This function queries AWS for NEXRAD data on a given hour and date for a certain NEXRAD location identifier (starts with a K). Note that each input must be a string and zero-padded where appropriate. For example, 02 UTC on March 1st, 2012 for KMAF would be called as `get_filenames('2012','03','01','02','KMAF')`.

The output is the returned XML body from the AWS query.

### `parse_xml(content)`

This function takes the returned XML from `get_filenames` and extracts all of the file names.

The output is a list of full file names on AWS for the given date, hour, and location.

### `get_files(filelist, save_path='')`

This function downloads files supplied in a `filelist` list. An optional `save_path` will specify the path where files should be saved; by default, files will be downloaded into the current working directory.

The output is a list of files saved with their local paths.
