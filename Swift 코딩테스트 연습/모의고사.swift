import Foundation

func solution(_ answers:[Int]) -> [Int] {
    var patternOne: [Int] = [1, 2, 3, 4, 5]
    var patternTwo: [Int] = [2, 1, 2, 3, 2, 4, 2, 5]
    var patternThree: [Int] = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    var answerOne: [Int] = []
    var answerTwo: [Int] = []
    var answerThree: [Int] = []
    var correct: [Int] = [0, 0, 0]
    var answer: [Int] = []
    
    while answerOne.count < 10000 {
        answerOne += patternOne
    }
    
    while answerTwo.count < 10000 {
        answerTwo += patternTwo
    }
    
    while answerThree.count < 10000 {
        answerThree += patternThree
    }
    
    for i in 0..<answers.count {
        if answerOne[i] == answers[i] {
            correct[0] += 1
        }
        
        if answerTwo[i] == answers[i] {
            correct[1] += 1
        }
        
        if answerThree[i] == answers[i] {
            correct[2] += 1
        }
    }
    
    var maxData = correct.max() ?? 0 
    
    for i in 0...2 {
        if correct[i] == maxData {
            answer.append(i+1)
        }
    }
    
    return answer
}