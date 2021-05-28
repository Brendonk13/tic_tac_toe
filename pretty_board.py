
class pretty_board:

    def __init__(self, rows):
        self.rows = rows
        self.horizontal_line = ['─' * 3] * 3
        self.prettyify()

    def __str__(self):
        return self.pretty_rows

    def prettyify(self):
        self.pretty_rows = self.top() + self.middle() + self.bottom()

    def middle(self):
        return f'{self.middle_border()}'.join(
            self.pretty(row)
            for row in self.rows
        )

    def pretty(self, row):
        return self.with_borders(
                column if column
                else ' '
                for column in row
        )

    def with_borders(self, pretty_row):
        # add borders in between columns and at the ends
        return '│ ' + ' │ '.join(pretty_row) + ' │'


    def top(self):
        middle = '┬'.join(self.horizontal_line)
        return '┌' + middle + '┐' + '\n'

    def middle_border(self):
        middle = '┼'.join(self.horizontal_line)
        return '\n' + '├' +  middle + '┤' + '\n'

    def bottom(self):
        middle = '┴'.join(self.horizontal_line)
        return '\n' +  '└' + middle + '┘'


