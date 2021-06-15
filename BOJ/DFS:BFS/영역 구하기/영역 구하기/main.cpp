//
//  main.cpp
//  영역 구하기
//
//  Created by 권준상 on 2021/04/27.
//

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int m,n,k;
int map[101][101];
bool visit[101][101];
int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, 1, 0, -1};

queue<vector<int>> q1;
vector<int> v;


void bfs() {
    queue<pair<int, int>> q2;
    vector<int> answer;
    
    for(int i=0; i<m; i++) {
        for(int j=0; j<n; j++) {
            if(map[i][j] == 1 || visit[i][j]) continue;
            visit[i][j] = true;
            q2.push({i,j});
            int area = 0;
            while(!q2.empty()) {
                auto tmp = q2.front();
                int ti = tmp.first;
                int tj = tmp.second;
                q2.pop();
                area++;
                
                for(int l=0; l<4; l++) {
                    int li = ti + di[l];
                    int lj = tj + dj[l];
                    
                    if(li < 0 || li >= m || lj < 0 || lj >= n || map[li][lj] == 1 || visit[li][lj]) continue;
                    
                    q2.push({li,lj});
                    visit[li][lj] = true;
                }
            }
            
            answer.push_back(area);
        }
    }
    
    cout << answer.size() << "\n";
    sort(answer.begin(), answer.end());
    for(int i=0; i<answer.size(); i++) {
        cout << answer[i] << " ";
    }
    
}

int main(int argc, const char * argv[]) {
    int count = 0;
    cin >> m >> n >> k;
    for(int i=0; i<k; i++) {
        int si, sj , fi, fj;
        cin >> sj >> si >> fj >> fi;
        v.push_back(si);
        v.push_back(sj);
        v.push_back(fi);
        v.push_back(fj);
        q1.push(v);
        v.clear();
    }
    
    while(count < k) {
        v = q1.front();
        q1.pop();
        for(int i=v[0]; i<v[2]; i++) {
            for(int j=v[1]; j<v[3]; j++) {
                map[i][j] = 1;
            }
        }
        v.clear();
        count++;
    }
    
    bfs();
    
    return 0;
}
