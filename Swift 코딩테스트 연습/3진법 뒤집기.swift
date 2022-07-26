import Foundation

func solution(_ n: Int) -> Int {
    var numThree = Array(String(n, radix: 3)).map{Int(String($0))!}
    var answer: Int = numThree[0]

    for i in 1.. < numThree.count {
        var value = pow(3.0, i)
        var nsValue = NSDecimalNumber(decimal: value)
        answer += numThree[i] * Int(nsValue)
    }

    return answer
}
