//
//  main.cpp
//  그림(1926)
//
//  Created by 권준상 on 2021/04/20.
//

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int n , m;
int map[502][502];
bool visit[502][502];
int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, 1, 0, -1};

void bfs() {
    queue<pair<int, int>> q;
    vector<int> v;
    int count = 0;
    bool flag = false;

    
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            if(map[i][j] == 0 || visit[i][j]) continue;
            visit[i][j] = true;
            q.push({i,j});
            count++;
            int area = 0;
            while(!q.empty()) {
                flag = true;
                auto tmp = q.front();
                int ti = tmp.first;
                int tj = tmp.second;
                q.pop();
                area++;
                
                for(int k = 0; k < 4; k++) {
                    int ki = ti + di[k];
                    int kj = tj + dj[k];
                    if(ki < 0 || ki >= n || kj <0 || kj >= m || map[ki][kj] == 0 || visit[ki][kj]) continue;
                    
                    visit[ki][kj] = true;
                    q.push({ki, kj});
                }
            }
            v.push_back(area);
        }
    }
    
    if(flag) {
        sort(v.begin(), v.end(), greater<int>());
        cout << count << "\n";
        cout << v[0];
    }
    else {
        cout << count << "\n";
        cout << 0;
    }
    
}

int main(int argc, const char * argv[]) {
    cin >> n >> m;
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            cin >> map[i][j];
        }
    }
    
    bfs();
    return 0;
}
