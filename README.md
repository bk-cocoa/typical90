# typical90

てんけい９０ うめうめ2/90

1/3:星2着手開始
1/10:星2埋め(10/90)
1/10 14:47:星3着手

## 002 - Encyclopedia of Parentheses（★3）
* 制約の最大値であるN=20になった際、ありえる"("と")"の組合せは1048575通り
* 2進数で表現してあげれば良いかな
* 全部チェックしても10^6なので間に合いそう
  * 大丈夫でした

## 004 - Cross Sum（★2）
* 前処理とか、包除原理？とか
* そのセルが存在する行の合計 + そのセルが存在する列の合計 - そのセルの値
  * 行の合計と列の合計がパパッと出せたら嬉しいよね
    * じゃあ先に計算しておけば良いね

## 010 - Score Sum Queries（★2）
* 累積和
* 1組と2組で夫々累積和を作ってあげると、1つのクエリ(L,R)から
1組生徒の合計、2組生徒の合計がそれぞれO(1)で求められるね
* 学籍番号が重複しないことを踏まえてそれぞれの累積和を簡単に作れる点の理解が必要かもしれない…？

## 022 - Cubic Cake（★2）
* 最大公約数
* 直方体ではなく、2次元の平面から正方形を切り出したりする方法だったり、次元を落として考えるとわかりやすいかもしれない
* A,B,Cの最大公約数で割ったら良い
* カットするので、-1を忘れずに。

## 024 - Select +／- One（★2）
* 偶奇問題

## 027 - Sign Up Requests （★2）
* setで集合管理
* Nの最大値が10^5なので、listで持っちゃうと最大O(N^2)でTLEしちゃいそうな気配…？

## 033 - Not Too Bright（★2）
* 条件を完全に理解できるまで読み込もう
  * 「**完全に**含まれる」
後は、しっかりパターンと規則性考えるだけでOK

## 055 - Select 5（★2）
* 秒数に甘えて具直前探索
* O(N^5)だけど、処理自体は軽いのもあり。
* 数が大きくなると計算速度一気に遅くなるから積極的にmod取ろうね

## 061 - Deck（★2）
* dequeを使ってappendとappendleftで上下を表現
* dequeもスライスで欲しい位置の要素が取得可能なので、問題無し

## 067 - Base 8 to 9（★2）
* n進数の変換
* intを使えばn進数→10進数に直せるの便利
* 10進数→n進数への変換はライブラリ化しときたい :TODO

## 078 - Easy Graph Problem（★2）
* グラフ問題
* 隣接頂点に対して二分探索
* にぶたん前はソート忘れずに。