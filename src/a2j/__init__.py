"""
https://github.com/Deasilsoft/a2j

Copyright (c) 2020-2023 Deasilsoft

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from .cache import create_cache, delete_cache, get_cache_path, read_cache
from .commands import get_match_commands, get_summary_commands
from .constant import CACHE_DIRECTORY, METHODS, RECORD_DIRECTORY
from .encoder import JSONEncoder
from .errors import invalid_commands_error, invalid_method_error, no_commands_error, no_record_error, parsing_record_error
from .minimap import create_minimap, get_minimap_object_colors, get_minimap_player_colors, get_minimap_terrain_colors
from .parser import parse_record
from .util import get_invalid_commands, get_record_path, get_valid_commands, get_version, handle_record, is_record, is_valid_command, is_valid_method
