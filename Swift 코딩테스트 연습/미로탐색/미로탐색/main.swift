//
//  main.swift
//  미로탐색
//
//  Created by 권준상 on 2022/07/28.
//

import Foundation

let nm = readLine()!.split(separator:" ").map{Int(String($0))!}
let n = nm[0]
let m = nm[1]

var maze = [[Int]]()
var visited = Array(repeating: Array(repeating: false, count: m), count: n)

let di = [-1, 0, 1, 0]
let dj = [0, 1, 0, -1]
var q:[[Int]] = []

for _ in 0..<n {
    let nums = Array(readLine()!).map{Int(String($0))!}
    maze.append(nums)
}


q.append([0, 0, 1])
visited[0][0] = true

while !q.isEmpty {
    let ti = q[0][0]
    let tj = q[0][1]
    let tdepth = q[0][2]
    
    if ti == n-1 && tj == m-1 {
        print(tdepth)
        break
    }
    
    q.removeFirst()
    
    for k in 0..<4 {
        let ki = ti + di[k]
        let kj = tj + dj[k]
        let kdepth = tdepth + 1
        
        if (0..<n).contains(ki) && (0..<m).contains(kj) && maze[ki][kj] == 1 && !visited[ki][kj] {
            q.append([ki, kj, kdepth])
            visited[ki][kj] = true
        }
    }
}



