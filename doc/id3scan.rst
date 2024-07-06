=======================
musisscan.tools.id3scan
=======================

NAME
----

id3scan - scan files for ID3 metadata to build XML structures

SYNOPSIS
--------

::

  id3scan [-h] [--musicpath PATH]
         [--outdir PATH]
         [--write/--no-write]
         [--split-xml/--no-split-xml]
         [--overwrite/--no-overwrite]
         [--flags/--noflags]
         [--debug/--no-debug]

DESCRIPTION
-----------

Recursively scans a directory of music files and (if directed) writes out XML containing the music metadata.

OPTIONS
-------

``-h|--help``
    Help output

``--musicpath PATH``
    Path to scan for media files

``--outdir PATH``
    Directory to write the XML files.  If unspecified, it will not write out anything.

``--write``
    Writes out XML files based on the scanned ID3 metadata.

``--split-xml``
    Splits the XML data into 3 or more separate files (audiocd, album, cd indexes) that reference
    each other using XML XInclude.  Otherwise, all elements are written to a single album file.

``--overwrite``
    If existing XML files are already in the output path, they will be overwritten.

``--flags``
    If specified, additional XML comments will be embedded in the file containing
    hints about the data, such as whether a song has a featured guest artist,
    or if a track is just filler material from the source CD.

``--debug``
    Report any additional debugging information.

USAGE
-----

By default, the code will only scan music files that are found under the selected path.  It will
not write any output unless the write flag is specified; so it's possible to use the tool
to perform a dry-run before writing any output.

The destination directory of the XML files should be away from the music library.  For every
music album, the program will generate one (or more) XML files, so be aware of the scope of
your scanning operation.

The program will output statistics on how many files it discovered, and how many files it has
created.  It will also provide a list of all of the files created.

The output XML files are designed to be rough drafts of the final data.  For example, the
ID3 tag for a song artist doesn't identify whether the value is a single artist, a group,
or multiple artists.  The XML schema allows for clarity where the data can be edited to
correctly identify multiple artists, or distinguish between an individual artist and a group.

If you don't like the results of your editing, it's possible to just delete the data
and re-generate it by running the id3scan again.

FLAGS
-----

Flags are embedded information in the XML comments that provide information on
how the software has interpreted the metadata

``possible_greatest_hits``
    The album could possibly be a greatest hits album.

``possible_hits_compilation``
    The album could be a compilation of hits from one or more artists.

``possible_soundtrack``
    The album is possibly a soundtrack from a film, television show, or play.

``possible_score```
    The album is possible a musical score from a film, television show, or play.

``detected_square_brackets``
    Square brackets were detected in the title of the track, suggesting extra
    metadata could be embedded in the title.

``detected_parenthesis``
    Parenthesis were detected in the title of the track, suggesting a
    possible sub-title, or additional metadata embedded in the title.

``likely_group_artist``
    The artist name value has key words that indicate the artist may be
    a musical group (instead of an individual)

``possible_featured_artist``
    The artist name or song title may indicate that a featured artist is
    performing on this track.

``possible_live_performance``
    Words in the song title suggest that the performance could be a live
    recording, instead of a studio recording.

``possible_demo_recording``
    Words in the song title suggest that the performance could be a demo
    recording, instead of a studio recording.

``possible_blank_track``
    The track is possibly a blank track that contains no actual music.

``country_and_folk_genre_is_too_vague``
    The metadata genre value for the track is "Country & Folk", which
    actually is two different genres.  The value should be changed to
    the more accurate value.



ENVIRONMENT VARIABLES
---------------------

``MUSICPATH``
    The default path to the media repository if it isn't defined on the command line.
