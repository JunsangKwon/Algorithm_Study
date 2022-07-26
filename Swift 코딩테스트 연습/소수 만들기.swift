import Foundation

func solution(_ nums:[Int]) -> Int {
    var answer = 0
    var sums: [Int] = []
    
    for i in 0..<nums.count {
        for j in i+1..<nums.count {
            for k in j+1..<nums.count {
                sums.append(nums[i] + nums[j] + nums[k])
            }
        }
    }
    
    for i in 0..<sums.count {
        var isPrimeNum:Bool = true
        for j in 2..<Int(sqrt(Double(sums[i])) + 1) {
            if sums[i] % j == 0 {
                isPrimeNum = false
                break
            }
        }
        if isPrimeNum {
            answer += 1
        }
    }
    
    return answer
}