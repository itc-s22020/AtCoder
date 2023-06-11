//提出コードの修正をc++に変更 TLE14 AC6
#include <iostream>
#include <vector>
 
int main() {
    int x;
    std::cin >> x;
 
    std::vector<int> sui(x);
    for (int i = 0; i < x; i++) {
        std::cin >> sui[i];
    }
 
    int q;
    std::cin >> q;
 
    std::vector<std::vector<int>> W(q, std::vector<int>(2));
    for (int i = 0; i < q; i++) {
        std::cin >> W[i][0] >> W[i][1];
    }
 
    std::vector<std::vector<int>> S;
    for (int i = 1; i < sui.size(); i += 2) {
        if (i % 2 != 0) {
            std::vector<int> temp{ sui[i], sui[i+1] };
            S.push_back(temp);
        }
    }
 
    for (const auto& v : W) {
        int total = 0;
        for (const auto& L : S) {
            int V1 = v[0], V2 = v[1];
            int L1 = L[0], L2 = L[1];
 
            // 時間時間がすべて睡眠時間の場合
            if (L1 < V1 && V1 < L2 && L1 < V2 && V2 < L2) {
                total += V2 - V1;
                break;
            }
            // 記録開始,終了時間が睡眠時間内の場合
            if (L1 < V1 && V1 < L2) {
                total += L2 - V1;
                continue;
            }
            else if (L1 < V2 && V2 < L2) {
                total += V2 - L1;
                continue;
            }
            // 上記のいずれも該当しないかつ、睡眠時間の全てが記録範囲内の場合
            if (L1 >= V1 && L2 <= V2) {
                total += L2 - L1;
            }
        }
        std::cout << total << std::endl;
    }
    return 0;
}

