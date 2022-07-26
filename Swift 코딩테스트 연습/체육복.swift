import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    var clothStatus: [Int] = Array(repeating: 1, count: n)
    var answer: Int = 0
    
    for i in 0..<lost.count {
        clothStatus[lost[i] - 1] -= 1
    } 
    
    for i in 0..<reserve.count {
        clothStatus[reserve[i] - 1] += 1
    }

    for i in 0..<n {
        if clothStatus[i] == 0 {
            if i >= 1 && clothStatus[i-1] > 1 {
                clothStatus[i-1] -= 1
                clothStatus[i] += 1
            } else if i < n - 1 && clothStatus[i+1] > 1 {
                clothStatus[i+1] -= 1
                clothStatus[i] += 1
            } 
        }
    }

    for i in 0..<n {
        if clothStatus[i] != 0 {
            answer += 1
        }
    }
    
    return answer
}