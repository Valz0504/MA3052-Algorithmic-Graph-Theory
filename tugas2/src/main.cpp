#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>
#include <cmath>
#include <cstddef>
#include <cstdio>
#include <deque>
#include <iomanip>
#include <ios>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <thread>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <climits>
#include <cctype>

using namespace std;

// Macros
#define ll int64_t
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define cinvi(va, n) for(int i = 0 ; i < n; i++) { cin >> va[i]; }

// Constants
const ll MOD = 1e9 + 7;
const ll INF = 1e18;

const int MAXN = 100005;

int dx[4] = {1,-1,0,0}, dy[4] = {0,0,1,-1};

int n,m,row,col;
vector<int> graph[MAXN];
vector<vector<int>> grid;

void dfsRec(vector<bool> &visited, int node, vector<int> &res)
{
    if (visited[node]) return;
    visited[node] = true;
    res.push_back(node);
    for (auto nxt : graph[node])
    {
        dfsRec(visited, nxt, res);
    }
}

vector<int> dfs(int startNode)
{
    vector<bool> visited(n + 5, false);
    vector<int> res;
    dfsRec(visited, startNode, res);
    return res;
}

vector<int> bfs(int startNode)
{
    vector<bool> visited(n + 5, false);
    vector<int> res;

    queue<int> q;
    visited[startNode] = true;
    q.push(startNode);

    while (!q.empty())
    {
        int curr = q.front();
        q.pop();
        res.push_back(curr);

        for (auto nxt : graph[curr])
        {
            if (!visited[nxt])
            {
                visited[nxt] = true;
                q.push(nxt);
            }
        }
    }
    return res;
}

void solve() {

    cout << "Pilih menu yang ingin diakses: \n";
    cout << "1. Penelusuran DFS\n";
    cout << "2. Penelusuran BFS\n";
    cout << "3. Cek Keberadaan Lintasan\n";
    cout << "4. Cek Keterhubungan Graf\n";
    cout << "5. Cari jumlah komponen dan komponen terbesar\n";
    cout << "6. Cari jumlah island\n";
    cout << "7. Exit\n";

    int type; cin >> type;

    if (type == 7) return;

    switch (type)
    {
        case 6: {
            cout << "Masukkan jumlah baris: ";
            cin>>row;
            cout << "Masukkan jumlah kolom: ";
            cin>>col;

            grid.assign(row + 5, vector<int> (col + 5));
            for (int i = 1; i <= row; i++) {
                for (int j = 1; j <= col; j++) cin >> grid[i][j];
            }
            break;
        }

        default: {
            cout << "Banyak Node: ";
            cin>>n;
            cout << "Banyak Edge: ";
            cin>>m;
            for (int i = 0; i < m; i++)
            {
                int u,v; cin>>u>>v;
                graph[u].push_back(v);
                graph[v].push_back(u);
            }
        }
    }
    if (type != 6)
    {
        switch (type)
        {
            case 1: {
                cout << "Masukkan node A: ";
                int A; cin >> A;
                cout << "\nPenelusuran menggunakan DFS dari A: ";
                vector<int> dfsTraversal = dfs(A);
                for (auto e : dfsTraversal)
                {
                    cout << e << " ";
                }
                cout << '\n';
                break;
            }
            case 2: {
                cout << "Masukkan node A: ";
                int A; cin >> A;
                cout << "\nPenelusuran menggunakan BFS dari A: ";
                vector<int> bfsTraversal = bfs(A);
                for (auto e : bfsTraversal)
                {
                    cout << e << " ";
                }
                cout << '\n';
                break;
            }
            case 3: {
                cout << "Masukkan node A: ";
                int A; cin >> A;
                cout << "Masukkan node B: ";
                int B; cin >> B;

                vector<int> dfsTraversal = dfs(A);
                bool ok = false;
                for (auto e : dfsTraversal)
                {
                    if (e == B)
                    {
                        ok = true;
                    }
                }
                if (ok)
                {
                    cout << "\nADA lintasan dari A ke B!\n";
                } else{
                    cout << "\nTIDAK ADA lintasan dari A ke B!\n";
                }
                break;
            }
            case 4: {
                cout << "Masukkan node A: ";
                int A; cin >> A;

                vector<int> dfsTraversal = dfs(A);
                if (dfsTraversal.size() == n)
                {
                    cout << "\nGraf ini terhubung!\n";
                } else{
                    cout << "\nGraf ini tidak terhubung!\n";
                }
                break;
            }
            case 5: {
                int cntComponent = 0;
                vector<int> largestComponent;
                vector<bool> mark(n + 5, false); 
                for (int i = 1; i <= n; i++)
                {
                    if (!mark[i])
                    {
                        cntComponent++;
                        vector<int> result = dfs(i);    
                        if (result.size() > largestComponent.size())
                        {
                            largestComponent = result;
                        }
                        for (auto e : result)
                        {
                            mark[e] = true;
                        }
                    }
                }
                cout << "\nJumlah component: " << cntComponent << '\n';
                cout << "Component terbesar berada di node-node berikut: ";
                for (auto e : largestComponent) cout << e << " ";
                cout << '\n';
                break;
            }
        }
    }
    else
    {
        vector<vector<bool>> gridVisit(row + 5, vector<bool>(col + 5, false));

        int cnt = 0;
        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= col; j++) {
                if (gridVisit[i][j] || grid[i][j] == 0) continue;

                cnt++;

                queue<pair<int, int>> q;
                gridVisit[i][j] = true;
                q.push({i, j});

                while (!q.empty()) {
                    auto [x, y] = q.front();
                    q.pop();

                    for (int d = 0; d < 4; d++) {
                        int newx = x + dx[d], newy = y + dy[d];
                        if (newx >= 1 && newx <= row && newy >= 1 && newy <= col && !gridVisit[newx][newy] && grid[newx][newy] != 0) {
                            gridVisit[newx][newy] = true;
                            q.push({newx, newy});
                        }
                    }
                }
            }
        }
        cout << "Jumlah island: " << cnt << '\n';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie();

    int tc = 1;
    // cin >> tc;
    while (tc--) {
        solve();
    }
    return 0;
}