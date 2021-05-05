//
//  main.cpp
//  감시
//
//  Created by 권준상 on 2021/04/28.
//

#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int map[9][9];
bool visit[9][9];
int n, m;
queue<pair<int, pair<int, int>>> q;


void search() {
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            if(map[i][j] == 0) continue;
            visit[i][j] = true;
            if(map[i][j] == 6) continue;
            
            switch(map[i][j]) {
                case 1:
                    q.push({i,{j,1}});
                    break;
                case 2:
                    q.push({i,{j,2}});
                    break;
                case 3:
                    q.push({i,{j,3}});
                    break;
                case 4:
                    q.push({i,{j,4}});
                    break;
                case 5:
                    q.push({i,{j,5}});
                    break;
            }
        }
    }
    
    while(!q.empty()) {
        auto tmp = q.front();
        int ti = tmp.first;
        int tj = tmp.second.first;
        int tnum = tmp.second.second;
        q.pop();
        
        if(tnum == 1) {
            for(int k = 0; k<4; k++) {
                if(k==0) {
                    
                }
            }
        } else if(tnum == 2) {
            for(int k = 0; k<2; k++) {
                
            }
        } else if(tnum == 3) {
            for(int k = 0; k<4; k++) {
                
            }
        } else if(tnum == 4) {
            for(int k = 0; k<4; k++) {
                
            }
        } else if(tnum == 5) {
            
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
    
    search();
    return 0;
}
