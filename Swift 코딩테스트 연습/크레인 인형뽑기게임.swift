import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var newBoard = Array(repeating: Array(repeating: 0, count: board.count), count: board.count) 
    var busket: [Int] = []
    var count:Int = 0

    for i in 0..<board.count {
        for j in 0..<board.count {
            newBoard[j][i] = board[i][j]
        }
    }
    
    for i in 0..<board.count {
        newBoard[i].reverse()
    }
    
    for i in 0..<moves.count {
        while !newBoard[moves[i] - 1].isEmpty {
            var doll = newBoard[moves[i] - 1].removeLast()
            if doll != 0 {
                if !busket.isEmpty && busket.last == doll {
                    busket.removeLast()
                    count += 2
                } else {
                    busket.append(doll)
                }
                break
            }
        }  
    }
    
    return count
}