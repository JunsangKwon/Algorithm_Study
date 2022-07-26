import Foundation

func solution(_ price:Int, _ money:Int, _ count:Int) -> Int{
    var totalPrice:Int = 0
    
    for i in 1...count {
        totalPrice += i * price
    }
    
    if money > totalPrice {
        return 0    
    } else {
        return totalPrice - money
    }
}