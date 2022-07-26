func solution(_ n: Int64) -> [Int] {
    var numList = String(n).map{Int(String($0))!}
    numList.reverse()

    return numList
}
