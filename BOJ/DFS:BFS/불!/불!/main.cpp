//
//  main.cpp
//  불!
//
//  Created by 권준상 on 2021/04/27.
//

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int n , m;
char map[502][502];
bool visit[502][502];
int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, 1, 0, -1};

queue<pair<int, pair<int, int>>> jq;
queue<pair<int, int>> fq;
vector<int> ans;

void bfs() {
    
    bool flag = false;
    
    while(!jq.empty()) {
        flag = true;
        auto tmp = jq.front();
        int ti = tmp.first;
        int tj = tmp.second.first;
        int ttime = tmp.second.second;
        jq.pop();
        map[ti][tj] = '.';
        
        for(int k = 0; k < 4; k++) {
            int ki = ti + di[k];
            int kj = tj + dj[k];
            int ktime = ttime + 1;
            
            if(map[ki][kj] != '.' || visit[ki][kj]) continue;
            else if(ki == 0 || kj == 0 || ki == n-1 || kj == m-1) {
                
            }
            else if(ki < 0 || ki >= n || kj <0 || kj >= m || map[ki][kj] != '.' || visit[ki][kj]) continue;
            
            visit[ki][kj] = true;
            //jq.push({ki, kj});
        }
    }

}

int main(int argc, const char * argv[]) {
    cin >> n >> m;
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            cin >> map[i][j];
        }
    }
    
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            if(map[i][j] == 'J') {
                jq.push({i,{j,0}});
                visit[i][j] = true;
            }
            if(map[i][j] == 'F') {
                fq.push({i,j});
            }
        }
    }
    
    bfs();
    
    return 0;
}
