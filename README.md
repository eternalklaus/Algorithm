# 면접 대비 문제 리스트

> 출처: GeeksforGeeks, LeetCode Discuss, Glassdoor, Parth Shah 블로그, Codeforces, 자체 피드백 분석

## 진행 현황

- [ ] 알고리즘 문제 (15)
- [ ] LLD/구현 문제 (5)
- [ ] 짧은 OA 문제 (10)

---

## A. 알고리즘 문제 (LeetCode 기반)

### 우선순위 1 — C사 실제 출제 확인

| 상태 | # | LeetCode | 문제 | 난이도 | 토픽 | 비고 |
|:----:|:-:|:--------:|------|:------:|------|------|
| ⬜ | 1 | [LC 5](https://leetcode.com/problems/longest-palindromic-substring/) | Longest Palindromic Substring | Medium | String / DP | C사 OA 2023 |
| ⬜ | 2 | [LC 256](https://leetcode.com/problems/paint-house/) | Paint House | Medium | DP | C사 OA |
| ⬜ | 3 | [LC 907](https://leetcode.com/problems/sum-of-subarray-minimums/) | Sum of Subarray Minimums | Medium | Monotonic Stack | C사 OA (≈max of windows) |
| ⬜ | 4 | [LC 460](https://leetcode.com/problems/lfu-cache/) | LFU Cache | Hard | Design / HashMap | C사 Round 3 |
| ⬜ | 5 | [LC 146](https://leetcode.com/problems/lru-cache/) | LRU Cache | Medium | Design / HashMap | 스토리지 도메인 단골 |
| ⬜ | 6 | [LC 55](https://leetcode.com/problems/jump-game/) | Jump Game | Medium | Greedy / DP | C사 SDET OA |
| ⬜ | 7 | [LC 64](https://leetcode.com/problems/minimum-path-sum/) | Minimum Path Sum | Medium | DP | C사 SDET OA |
| ⬜ | 8 | [LC 25](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Reverse Nodes in K-Group | Hard | Linked List | C사 Tech Round |
| ⬜ | 9 | [LC 21](https://leetcode.com/problems/merge-two-sorted-lists/) | Merge Two Sorted Lists | Easy | Linked List | C사 Tech Round |
| ⬜ | 10 | [LC 300](https://leetcode.com/problems/longest-increasing-subsequence/) | Longest Increasing Subsequence | Medium | DP | C사 Tech Round |

### 우선순위 2 — C사 특화

| 상태 | # | LeetCode | 문제 | 난이도 | 토픽 | 비고 |
|:----:|:-:|:--------:|------|:------:|------|------|
| ✅ | 11 | [LC 959](https://leetcode.com/problems/regions-cut-by-slashes/) | Regions Cut By Slashes | Medium | Graph / Union-Find | C사 SDE2 |
| ⬜ | 12 | [LC 403](https://leetcode.com/problems/frog-jump/) | Frog Jump | Hard | DP | C사 SDE2 |
| ⬜ | 13 | [LC 44](https://leetcode.com/problems/wildcard-matching/) | Wildcard Matching | Hard | DP / String | C사 SDE2 |
| ⬜ | 14 | [LC 1010](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/) | Pairs of Songs Divisible by K | Medium | HashMap / Math | C사 인도 캠퍼스 |
| ⬜ | 15 | [LC 124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Binary Tree Max Path Sum (DP on Tree) | Hard | Tree DP | **C사 1순위** |

### 우선순위 3 — 스냅샷 도메인 매핑 (면접 피드백 기반)

| 상태 | # | LeetCode | 문제 | 난이도 | 토픽 | 비고 |
|:----:|:-:|:--------:|------|:------:|------|------|
| ⬜ | 16 | [LC 303](https://leetcode.com/problems/range-sum-query-immutable/) | Range Sum Query - Immutable | Easy | Prefix Sum | **Feedback2 Q2 의심 1순위** |
| ⬜ | 17 | [LC 34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | First & Last Position in Sorted Array | Medium | Binary Search | **Feedback1 Q1 단서** |
| ⬜ | 18 | [LC 560](https://leetcode.com/problems/subarray-sum-equals-k/) | Subarray Sum Equals K | Medium | Prefix Sum + HashMap | O(N²)→O(N) 최적화 패턴 |
| ⬜ | 19 | [LC 210](https://leetcode.com/problems/course-schedule-ii/) | Course Schedule II | Medium | Graph / Topological Sort | 복구 순서 결정 |
| ✅ | 20 | [LC 215](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Kth Largest Element | Medium | Heap | 백업 스케줄러 priority queue |

---

## B. LLD / 구현 문제 (Round 2, 5~7시간)

| 상태 | # | 문제 | 핵심 요구사항 | 매핑 LeetCode |
|:----:|:-:|------|---------------|---------------|
| ⬜ | I-1 | **Incremental Snapshot File System** ⭐ | `commit()`, `read_file()`, 부모-자식 스냅샷 트리, leaf 검증, reference counting | [LC 588](https://leetcode.com/problems/design-in-memory-file-system/), [LC 1166](https://leetcode.com/problems/design-file-system/) |
| ⬜ | I-2 | **Versioned File System** | create / delete / copy / move + 버전 유지·롤백 | LC 588 변형 |
| ⬜ | I-3 | **Music Player Object Model** | user/playlist/song 메타데이터, add/delete/modify | [LC 359](https://leetcode.com/problems/logger-rate-limiter/) 풍 |
| ⬜ | I-4 | **LFU/LRU Cache (중복 키 지원)** | freq linked list, O(1) get/put, tie-breaking | [LC 460](https://leetcode.com/problems/lfu-cache/), [LC 146](https://leetcode.com/problems/lru-cache/) |
| ⬜ | I-5 | **Job Scheduler with Retry** | 우선순위 큐 + exponential backoff + 실패 재시도 | [LC 621](https://leetcode.com/problems/task-scheduler/), [LC 1834](https://leetcode.com/problems/single-threaded-cpu/) |

---

## C. 짧은 OA 문제 (Round 1)

| 상태 | # | 문제 | 출처 |
|:----:|:-:|------|------|
| ⬜ | C-1 | [Balanced Brackets (LC 20)](https://leetcode.com/problems/valid-parentheses/) | C사 OA 단골 |
| ⬜ | C-2 | [Longest Common Prefix (LC 14)](https://leetcode.com/problems/longest-common-prefix/) | C사 OA |
| ⬜ | C-3 | Right Shift `m` by `n` bits | C사 SDE 후기 |
| ⬜ | C-4 | Recursive Stack Reversal (no loops) | C사 SDE 후기 |
| ⬜ | C-5 | String mask 문자 제거 | C사 SDE 후기 |
| ⬜ | C-6 | 2D 행렬 90° 회전 + 중력 (`x`↓, `o`↑) | C사 SDE 후기 |
| ⬜ | C-7 | Preorder + Postorder → Inorder 트리 복원 | C사 SDE 후기 |
| ⬜ | C-8 | Polynomial Addition (Linked List) | C사 SDE 후기 |
| ⬜ | C-9 | Run-length Encoding `[1,2,2,2,3]→[1,[2,3],3]` | C사 SDET |
| ⬜ | C-10 | [Boundary / Left View / ZigZag (LC 545 / 103)](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | C사 Tech |

---

## 최우선 학습 순서 (TOP 5)

1. **LC 303** — Range Sum Query (Feedback2 Q2 패턴)
2. **LC 34** — Binary Search on sorted (Feedback1 Q1 단서)
3. **LC 588 / 1166** — Design File System (스냅샷 도메인 직결)
4. **LC 460** — LFU Cache (Round 3 단골 + reference counting 사고법)
5. **LC 124** — Binary Tree Max Path Sum (C사 1순위 패턴)

---

## 체크 방법

문제를 풀면 `⬜` → `✅` 로 변경:

```diff
- | ⬜ | 1 | LC 5 | Longest Palindromic Substring | ...
+ | ✅ | 1 | LC 5 | Longest Palindromic Substring | ...
```

커밋 메시지 예시:
```
solve: LC 303 Range Sum Query - Immutable
solve: LC 34 First & Last Position
study: I-1 Incremental Snapshot File System (1차 구현)
```

---

## Sources

- [Commvault Interview Experience (On-Campus) 2023 - LeetCode Discuss](https://leetcode.com/discuss/interview-question/4424820/Commvault-Interview-Experience-(On-Campus)-2023/)
- [Commvault Systems Interview Experience for SDE - GeeksforGeeks](https://www.geeksforgeeks.org/interview-experiences/commvault-systems-interview-experience-for-software-development-engineer/)
- [Commvault SDET Interview Experience - GeeksforGeeks](https://www.geeksforgeeks.org/commvault-interview-experience-for-sdet/)
- [CommVault OA SDE-1 2D Matrix and String - LeetCode Discuss](https://leetcode.com/discuss/interview-question/1744235/CommVault-or-OA-or-SDE-1-or-2-D-matrix-and-string-question-or)
- [Parth Shah's Commvault Interview Experience](https://parthvshah.me/blog/posts/commvault-interview-experience.html)
- [Clumio Interview Experience SDE2 - LeetCode Discuss](https://leetcode.com/discuss/interview-question/5061501/Clumio-Interview-Experience-or-SDE2-or-Reject/)
- [Clumio Shared Interest Problem - Codeforces](https://codeforces.com/blog/entry/85203)
- [Clumio Interview Questions - Glassdoor](https://www.glassdoor.com/Interview/Clumio-Interview-Questions-E3009099.htm)
- [Commvault Interview Questions - InterviewBit](https://www.interviewbit.com/commvault-interview-questions/)
