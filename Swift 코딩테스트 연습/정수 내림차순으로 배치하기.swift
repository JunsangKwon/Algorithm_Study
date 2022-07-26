func solution(_ n:Int64) -> Int64 {
    var strNum: String = String(n)
    var numList = Array(strNum).map{String($0)}
    
    numList.sort(by: >)
    
    var answer = numList.joined()
    
    return Int64(answer)!
}