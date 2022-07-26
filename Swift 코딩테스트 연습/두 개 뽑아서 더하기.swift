import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    var numSet:Set<Int> = Set()
    
    for i in 0..<numbers.count {
        for j in i+1..<numbers.count {
            numSet.insert(numbers[i] + numbers[j])
        }
    }
    
    var answer = Array(numSet)
    answer.sort()
    
    return answer
}