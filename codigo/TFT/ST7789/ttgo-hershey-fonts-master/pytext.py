# MIT License
#
# Copyright (c) 2020 Russ Hughes
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

v = '1.1'
    
import st7789py as st7789

def text(display, font, message, row=32, column=0, color=st7789.WHITE):
    '''
    Write `text` on `display` starting on `row` stating in `column` using
    `font` in `color`

    Args:
        display: The display device to write on
        font: The pyfont module to use
        message: The message to write
        row: Row to start at, defaults to 32
        column: Column to start at, defaults to 0
        color: The color to write in
    '''
    from_x = to_x = pos_x = column
    from_y = to_y = pos_y = row

    for char in [ord(char) for char in message]:
        penup = True
        if 32 <= char <= 127:
            data = bytearray(font.get_ch(char))
            length = data[0]
            left = data[1] - 0x52
            right = data[2] - 0x52
            width = right - left

            for vect in range (3, len(data), 2):
                vector_x = data[vect] - 0x52
                vector_y = data[vect+1] - 0x52

                if vector_x == -50:
                    penup = True
                    continue

                if not vect or penup:
                    from_x = pos_x + vector_x - left
                    from_y = pos_y + vector_y
                else:
                    to_x = pos_x + vector_x - left
                    to_y = pos_y + vector_y

                    display.line(from_x, from_y, to_x, to_y, color)

                    from_x = to_x
                    from_y = to_y
                penup = False

            pos_x += width
