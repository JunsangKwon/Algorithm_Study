import Foundation

func solution(_ d:[Int], _ budget:Int) -> Int {
    var count:Int = 0
    var index:Int = 0
    var leftBudget:Int = budget
    var registerList:[Int] = d
    registerList.sort()

    while index < registerList.count {
        leftBudget -= registerList[index]
        if leftBudget < 0 { break }
        index += 1
        count += 1
    }

    return count
}