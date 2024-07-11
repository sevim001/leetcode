class solution:
    def boredState(self,boared):
        dim=3
        row,col=3
        win=["xxx","ooo"]
        rowsum,colsum,primarydiag,secondrydiag="","","",""

        for i in range(dim):
            for j in range(dim):
                rowsum+=boared[i][j]
                colsum+=boared[j][i]
                primarydiag+=boared[i][i]
                secondrydiag+=boared[i][dim-1-i]

            if rowsum in win or colsum in win or primarydiag in win or secondrydiag in win:
                return [rowsum, colsum, primarydiag, secondrydiag]
            rowsum,colsum,primarydiag,secondrydiag="","","",""
            return ["-"]
        
        def tictactoe(self,moves:list[list[int]]) -> str:
            boared=[
                ["-","-",""],
                ["-","-",""],
                ["-","-",""]
            ]
            curr_player=0

            for m in moves:
                if curr_player == 0:
                    boared[m[0][m[1]]] == "x"
        
            
            