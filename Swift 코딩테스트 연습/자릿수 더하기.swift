import Foundation

func solution(_ n:Int) -> Int
{
    var answer:Int = 0
    var numList = String(n).map {Int(String($0))!}
    
    numList.forEach { answer += $0 }
    
    return answer
}
