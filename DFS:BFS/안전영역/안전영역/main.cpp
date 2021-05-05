//
//  main.cpp
//  안전영역
//
//  Created by 권준상 on 2021/04/27.
//

#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, 1, 0, -1};
int map[102][102];
vector<int> v;
queue<pair<int, int>> q;

void bfs(int height) {
    bool visit[102][102] = {false,};
    int count = 0;
    
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            if(map[i][j] <= height) {
                visit[i][j] = true;
            }
        }
    }
    
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            if(visit[i][j]) continue;
            
            visit[i][j] = true;
            q.push({i,j});
            while(!q.empty()) {
                auto tmp = q.front();
                int ti = tmp.first;
                int tj = tmp.second;
                q.pop();
                
                for(int k=0; k<4; k++) {
                    int ki = ti + di[k];
                    int kj = tj + dj[k];
                    
                    if(ki<0 || ki>=n || kj<0 || kj>=n || visit[ki][kj]) continue;
                    visit[ki][kj] = true;
                    q.push({ki, kj});
                    
                }
            }
            count++;
        }
    }
    v.push_back(count);
}

int main(int argc, const char * argv[]) {
    int max = 0;
    int min = 101;
    
    cin >> n;
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            int tmp;
            cin >> tmp;
            map[i][j] = tmp;
            if(tmp > max) {
                max = tmp;
            }
            if(tmp < min) {
                min = tmp;
            }
        }
    }
    
    if(min == max) {
        cout << 1;
        return 0;
    }
    
    for(int i=min; i<=max; i++) {
        bfs(i);
    }
    
    sort(v.begin(), v.end(), greater<int>());
    cout << v[0];
    
    return 0;
}
