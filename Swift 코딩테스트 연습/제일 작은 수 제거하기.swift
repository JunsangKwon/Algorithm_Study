func solution(_ arr:[Int]) -> [Int] {
    let minData = arr.min()
    var array: [Int] = arr
        
    for i in 0..<arr.count {
        if minData == arr[i] {
            array.remove(at: i)
        }
    }
    
    if array.count == 0 {
        return [-1]
    } else {
        return array
    }
}