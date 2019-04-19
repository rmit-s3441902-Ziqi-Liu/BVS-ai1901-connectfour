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
                        




        """
        Your evaluation function should look at the current state and return a score for it. 
        As an example, the random agent provided works as follows:
            If the opponent has won this game, return -1.
            If we have won the game, return 1.
            If neither of the players has won, return a random number.
        """

        """
        These are the variables and functions for board objects which may be helpful when creating your Agent.
        Look into board.py for more information/descriptions of each, or to look for any other definitions which may help you.

        Board Variables:
            board.width 
            board.height
            board.last_move
            board.num_to_connect
            board.winning_zones
            board.score_array 
            board.current_player_score

        Board Functions:
            get_cell_value(row, col)
            try_move(col)
            valid_move(row, col)
            valid_moves()
            terminal(self)
            legal_moves()
            next_state(turn)
            winner()
        """
        return value
