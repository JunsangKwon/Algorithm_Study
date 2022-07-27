import Foundation

func solution(_ numbers:[Int]) -> Int {
    var zeroToTen:Set<Int> = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    var answer:Int = 0
    
    for n in numbers {
        zeroToTen.remove(n)
    }
    
    zeroToTen.forEach {
        answer += $0
    }
    
    return answer
}