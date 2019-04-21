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
        score = 0
        state = board.board

        ## Score center column
        center_array = [int(i) for i in list(state[:][board.width//2])]
        center_count = center_array.count(int(self.id))
        score += center_count * 3

        ## Score Horizontal
        for r in range(board.height):
            row_array = [int(i) for i in list(state[r][:])]
            for c in range(board.width-3):
                window = row_array[c:c+4]
                score += self.evaluate_window(window)

        ## Score Vertical
        for c in range(board.width-1):
            col_array = [int(i) for i in list(state[:][c])]
            for r in range(board.height-3):
                window = col_array[r:r+4]
                score += self.evaluate_window(window)

        ## Score posiive sloped diagonal
        for r in range(board.height-3):
            for c in range(board.width-3):
                window = [state[r+i][c+i] for i in range(4)]
                score += self.evaluate_window(window)

        for r in range(board.height-3):
            for c in range(board.width-3):
                window = [state[r+3-i][c+i] for i in range(4)]
                score += self.evaluate_window(window)

        return score

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