#!/usr/bin/env python

#
# Copyright 2024 Chris Josephes
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

'''
Flags represent additional data added to XML output for the purpose
of identifying likely data that will probably need closer scrutiny.

Each album and song has a flag object, which will contain zero or
more flags that will be output as an XML comment with the XML elements.
'''

# pylint: disable=R0903


class AlbumFlags():
    '''
    Flags are warnings that are output in the XML
    so users can identify possible issues with
    the interpreted data.
    '''
    def __init__(self):
        self.flags = []

    def add_flag(self, in_code: int):
        '''
        Add a FlagCode to the array.
        '''
        self.flags.append(in_code)

    def to_xml_comment(self, in_padding: int = 3) -> str:
        '''
        Convert each flag code to an XML comment string value.
        '''
        p_str = ''
        if in_padding > 0:
            p_str = f"{' ' * in_padding}"
        if len(self.flags) > 0:
            flag_string = ''
            for f_code in self.flags:
                flag_string += AlbumFlagCodes.to_str(f_code) + ' '
            return f"{p_str}<!-- EDIT FLAGS: {flag_string} -->\n"
        return ''


class TrackFlags():
    '''
    Flags are warnings that are output in the XML
    so users can identify possible issues with
    the interpreted data.
    '''
    def __init__(self):
        self.flags = []

    def add_flag(self, in_code: int):
        '''
        Add a FlagCode to the array.
        '''
        self.flags.append(in_code)

    def to_xml_comment(self, in_padding: int = 3) -> str:
        '''
        Convert each flag code to an XML comment string value.
        '''
        p_str = ''
        if in_padding > 0:
            p_str = f"{' ' * in_padding}"
        if len(self.flags) > 0:
            flag_string = ''
            for f_code in self.flags:
                flag_string += TrackFlagCodes.to_str(f_code) + ' '
            return f"{p_str}<!-- EDIT FLAGS: {flag_string} -->\n"
        return ''


class AlbumFlagCodes():
    '''
    All flag codes related to albums.
    '''
    p_greatest = 1
    p_hits_compo = 2
    p_soundtrack = 3
    p_score = 4
    p_tribute = 5

    @classmethod
    def to_str(cls, in_code: int) -> str:
        '''
        Convert an album flag code to a usable string.
        '''
        matrix = {AlbumFlagCodes.p_greatest: 'possible_greatest_hits',
                  AlbumFlagCodes.p_hits_compo: 'possible_hits_compilation',
                  AlbumFlagCodes.p_soundtrack: 'possible_soundtrack',
                  AlbumFlagCodes.p_score: 'possible_score',
                  AlbumFlagCodes.p_tribute: 'possible_tribute'}
        if in_code in matrix:
            return matrix[in_code]
        return ''


class TrackFlagCodes():
    '''
    All flag codes related to tracks.
    '''
    d_sq_brackets = 110
    d_parenthesis = 111
    l_group = 120
    p_feat_artist = 130
    p_live = 131
    p_demo = 132
    p_blank_track = 140
    p_bonus_track = 141
    p_genre_country_folk = 150
    m_year = 160
    m_title = 161
    m_album_title = 162
    m_track_artist = 163

    @classmethod
    def to_str(cls, in_code: int) -> str:
        '''
        Convert a flag value to a usable string.
        '''
        matrix = {TrackFlagCodes.d_sq_brackets: 'detected_square_brackets',
                  TrackFlagCodes.d_parenthesis: 'detected_parenthesis',
                  TrackFlagCodes.l_group: 'likely_group_artist',
                  TrackFlagCodes.p_feat_artist: 'possible_featured_artist',
                  TrackFlagCodes.p_live: 'possible_live_performance',
                  TrackFlagCodes.p_demo: 'possible_demo_performance',
                  TrackFlagCodes.p_blank_track: 'possible_blank_track',
                  TrackFlagCodes.p_bonus_track: 'possible_bonus_track',
                  TrackFlagCodes.p_genre_country_folk:
                  'country_and_folk_genre_is_too_vague',
                  TrackFlagCodes.m_year: 'missing_copyright_year',
                  TrackFlagCodes.m_title: 'missing_title',
                  TrackFlagCodes.m_album_title: 'missing_album_title',
                  TrackFlagCodes.m_track_artist: 'missing_artist'}
        if in_code in matrix:
            return matrix[in_code]
        return ''
