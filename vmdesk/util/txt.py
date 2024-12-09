class Text:
    __slots__ = (
        "beam",
        "indentation",
        "lines")

    def __init__(self, body="", indentation="    "):
        self.beam = [0] * 4
        self.lines = body.split("\n")
        self.indentation = indentation

        y = len(self.lines) - 1
        x = len(self.lines[-1])
        self.select_set(y, x, y, x)
        #|
    def from_string(self, body):
        self.lines[:] = body.split("\n")

        y = len(self.lines) - 1
        x = len(self.lines[-1])
        self.select_set(y, x, y, x)
        #|
    def clear(self):
        self.lines[:] = [""]
        self.select_set(0, 0, 0, 0)
        #|
    def free(self):
        del self.indentation

        self.lines.clear()
        #|

    def as_string(self):
        return "\n".join(self.lines)
        #|
    def copy(self):
        return Text(self.body, self.indentation)
        #|
    def select_set(self, line_start, char_start, line_end, char_end):
        self.beam[:] = line_start, char_start, line_end, char_end
        #|
    def select_set_safe(self, line_start, char_start, line_end, char_end):
        lines = self.lines
        if 0 <= line_start < len(lines): pass
        else:
            line_start = min(max(0, line_start), len(lines) - 1)

        if 0 <= line_end < len(lines): pass
        else:
            line_end = min(max(0, line_end), len(lines) - 1)

        char_start = min(max(0, char_start), len(lines[line_start]))
        char_end = min(max(0, char_end), len(lines[line_end]))

        self.beam[:] = line_start, char_start, line_end, char_end
        #|

    def region_as_string(self):
        y0, x0, y1, x1 = self.beam
        if y0 == y1:
            if x0 > x1:
                return self.lines[y0][x1 : x0]
            return self.lines[y0][x0 : x1]

        if y0 > y1:
            y0, y1 = y1, y0
            x0, x1 = x1, x0

        lines = self.lines
        return "\n".join([lines[y0][x0 : ]] + lines[y0 + 1 : y1] + [lines[y1][ : x1]])
        #|
    # def region_from_string
    def write(self, s):
        beam = self.beam
        lines = self.lines

        newlines = s.split("\n")

        y0, x0, y1, x1 = beam

        if y0 == y1 and x0 == x1: # no selection
            # /* 0txt_write
            if len(newlines) == 1:
                line = lines[y0]
                lines[y0] = line[ : x0] + s + line[x0 : ]
                x0 += len(s)
                beam[1] = x0
                beam[3] = x0
                return y0
            else:
                line = lines[y0]
                x1 = len(newlines[-1])
                newlines[-1] += line[x0 : ]
                newlines[0] = line[ : x0] + newlines[0]

                lines[y0 : y0 + 1] = newlines
                y1 += len(newlines) - 1
                beam[:] = y1, x1, y1, x1
                return None
            # */
        else:
            self.select_clear()
            y0, x0, y1, x1 = beam

            # <<< 1copy (0txt_write,, ${'return y0':'return None'}$)
            if len(newlines) == 1:
                line = lines[y0]
                lines[y0] = line[ : x0] + s + line[x0 : ]
                x0 += len(s)
                beam[1] = x0
                beam[3] = x0
                return None
            else:
                line = lines[y0]
                x1 = len(newlines[-1])
                newlines[-1] += line[x0 : ]
                newlines[0] = line[ : x0] + newlines[0]

                lines[y0 : y0 + 1] = newlines
                y1 += len(newlines) - 1
                beam[:] = y1, x1, y1, x1
                return None
            # >>>
        #|
    def select_clear(self):
        beam = self.beam
        lines = self.lines

        y0, x0, y1, x1 = beam

        if y0 > y1:
            y0, y1 = y1, y0
            x0, x1 = x1, x0
        elif y0 == y1:
            if x0 > x1:
                x0, x1 = x1, x0

            line = lines[y0]
            lines[y0] = line[ : x0] + line[x1 : ]
            beam[:] = y0, x0, y0, x0
            return

        lines[y0] = lines[y0][ : x0] + lines[y1][x1 : ]
        lines[y0 + 1 : y1 + 1] = []
        beam[:] = y0, x0, y0, x0
    #|
    #|


# if __name__ == "__main__":
#     print()
#     tx = """xxx
# xx
# xabc
# defg
# hijx
# xx
# """

#     t = Text(tx)
#     t.select_set(2, 1, 4, 3)
#     print(t.region_as_string())
