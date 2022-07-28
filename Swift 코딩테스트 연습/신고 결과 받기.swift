import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    let reportArr = Array(Set(report))
    var reportList:[[String]] = []
    var messageList:[String] = []
    var reporterDic = Dictionary<String, [String]>()
    var messageDic = Dictionary<String, Int>()
    var answer:[Int] = []
    
    for i in 0..<id_list.count {
        reporterDic[id_list[i]] = []
        messageDic[id_list[i]] = 0
    }
    
    reportArr.map {
        let tmpList = $0.components(separatedBy: " ")
        reportList.append(tmpList)
    }
    
    for i in 0..<reportList.count {
        reporterDic[reportList[i][1]]!.append(reportList[i][0])
    }
    
    for i in 0..<id_list.count {
        if reporterDic[id_list[i]]!.count >= k {
            reporterDic[id_list[i]]!.map {
                messageDic[$0]! += 1
            }
        }
    }
    
    for i in 0..<id_list.count {
        answer.append(messageDic[id_list[i]]!)
    }
    
    return answer
}