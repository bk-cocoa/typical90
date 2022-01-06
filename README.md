# typical90

てんけい９０ うめうめ2/90

1/3:星2着手開始


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