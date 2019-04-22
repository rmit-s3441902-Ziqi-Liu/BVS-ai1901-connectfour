from connectfour.agents.agent import Agent

class StudentAgent(Agent):
    def __init__(self, name):
        super().__init__(name)
        self.MaxDepth = 4

    def get_move(self, board):
        """
        Args:
            board: An instance of `Board` that is the current state of the board.

        Returns:
            A tuple of two integers, (row, col)
        """

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            next_state = board.next_state(self.id, move[1])
            moves.append(move)
            vals.append(self.dfMiniMax(next_state, 1))

        bestMove = moves[vals.index(max(vals))]
        return bestMove

    def dfMiniMax(self, board, depth):
        # Goal return column with maximized scores of all possible next states

        if depth == self.MaxDepth:
            return self.evaluateBoardState(board)

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            if depth % 2 == 1:
                next_state = board.next_state(self.id % 2 + 1, move[1])
            else:
                next_state = board.next_state(self.id, move[1])

            moves.append(move)
            vals.append(self.dfMiniMax(next_state, depth + 1))

        if depth % 2 == 1:
            bestVal = min(vals)
        else:
            bestVal = max(vals)

        return bestVal

def evaluateBoardState(self, board):
    value = 0
        state = board.board
        for i in range(board.width):
            for j in range(board.height):
                #check horizontal token
                try:
                    if state[i][j] == state[i+1][j] == int(self.id):
                        value += 10
                    if state[i][j] == state[i+1][j] == state[i+2][j] == int(self.id):
                        value += 100
                    if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] == int(self.id):
                        value += 10000
                    if state[i][j] != int(self.id) and state[i][j] == state[i+1][j] != 0 :
                        value -= 10
                    if state[i][j] != int(self.id) and state[i][j] == state[i+1][j] == state[i+2][j] != 0:
                        value -= 1000
                    if state[i][j] != int(self.id) and state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] != 0:
                        value -= 10000
                except IndexError:
                    pass
    for i in range(board.width):
        for j in range(board.height):
            try:
                if state[i][j] == state[i][j+1] == int(self.id):
                    value += 10
                    if state[i][j] == state[i][j+1] == state[i][j+2] == int(self.id):
                        value += 100
                if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] == int(self.id):
                    value += 10000
                    if state[i][j] != int(self.id) and state[i][j] == state[i][j+1] != 0 :
                        value -= 10
                if state[i][j] != int(self.id) and state[i][j] == state[i][j+1] == state[i][j+2]!= 0:
                    value -= 1000
                    if state[i][j] != int(self.id) and state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] != 0:
                        value -= 10000
                        except IndexError:
                        pass
    for i in range(board.width):
        for j in range(board.height):
            try:
                if not j + 3  > board.height and state[i][j] == state[i+1][j+1] == int(self.id):
                    value += 10
                    if not j + 3 > board.height and state[i][j] == state[i+1][j+1] == state[i+2][j+2] == int(self.id):
                        value += 100
                if not j + 3 > board.height and state[i][j] == state[i+1][j+1] == state[i+2][j+2] == state[i+3][j+3] == int(self.id):
                    value += 10000
                    if not j + 3  > board.height and state[i][j] != int(self.id) and state[i][j] == state[i+1][j+1] != 0:
                        value -= 10
                if not j + 3 > board.height and state[i][j] != int(self.id) and state[i][j] == state[i+1][j+1] == state[i+2][j+2] != 0:
                    value -= 100
                    if not j + 3 > board.height and state[i][j] != int(self.id) and state[i][j] == state[i+1][j+1] == state[i+2][j+2] == state[i+3][j+3] != 0:
                        value -= 10000
                        except IndexError:
                        pass
for i in range(board.width):
    for j in range(board.height):
        try:
            if not j - 3  > board.height and state[i][j] == state[i+1][j-1] == int(self.id):
                value += 10
                    if not j - 3 > board.height and state[i][j] == state[i+1][j-1] == state[i+2][j-2] == int(self.id):
                        value += 100
                if not j - 3 > board.height and state[i][j] == state[i+1][j-1] == state[i+2][j-2] == state[i+3][j-3] == int(self.id):
                    value += 10000
                    if not j - 3  > board.height and state[i][j] != int(self.id) and state[i][j] == state[i+1][j-1] != 0:
                        value -= 10
                if not j - 3 > board.height and state[i][j] != int(self.id) and state[i][j] == state[i+1][j-1] == state[i+2][j-2] != 0:
                    value -= 100
                    if not j - 3 > board.height and state[i][j] != int(self.id) and state[i][j] == state[i+1][j-1] == state[i+2][j-2] == state[i+3][j-3] != 0:
                        value -= 10000
                        except IndexError:
                        pass
    return value


    def evaluate_window(self,window):
        score = 0
        piece = int(self.id)

        opp_piece = 1
        if piece == 1:
            opp_piece = 2

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(0) == 1:
            score -= 4

        return score
