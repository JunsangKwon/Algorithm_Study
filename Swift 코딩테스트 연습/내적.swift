import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    var innerProduct:Int = 0
    
    for i in 0..<a.count {
        innerProduct += a[i] * b[i]
    }
    
    return innerProduct
}