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

int n,m;
vector<int> graph[MAXN];

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

    cout << "Masukkan node A: ";
    int A; cin >> A;
    cout << "Masukkan node B: ";
    int B; cin >> B;
    cout << "\nPenelusuran menggunakan DFS dari A: ";
    vector<int> dfsTraversal = dfs(A);
    for (auto e : dfsTraversal)
    {
        cout << e << " ";
    }
    cout << '\n';

    cout << "\nPenelusuran menggunakan BFS dari A: ";
    vector<int> bfsTraversal = bfs(A);
    for (auto e : bfsTraversal)
    {
        cout << e << " ";
    }
    cout << '\n';

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

    if (dfsTraversal.size() == n)
    {
        cout << "\nGraf ini terhubung!\n";
    } else{
        cout << "\nGraf ini tidak terhubung!\n";
    }

    // ngecek jumlah component dan menentukan component terbesar
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
