# typical90

てんけい９０ うめうめ2/90

1/3:星2着手開始 1/10:星2埋め(10/90)
1/10 14:47:星3着手

## 001 - Yokan Party（★4）

* 伝説の羊羹パーティ
* 答えを二分探索する
* 計算量はO(NlogN)…？で合ってる？？？



## 002 - Encyclopedia of Parentheses（★3）

* 制約の最大値であるN=20になった際、ありえる"("と")"の組合せは1048575通り
* 2進数で表現してあげれば良いかな
* 全部チェックしても10^6なので間に合いそう
    * 大丈夫でした
## 003 - Longest Circular Road（★4）

* 木の直径＝「適当な地点から一番遠いところ」から一番遠いところまでの長さ
* BFSとかDFSとか、後はお好きに感
* （queのBFSで逃げました）

## 004 - Cross Sum（★2）

* 前処理とか、包除原理？とか
* そのセルが存在する行の合計 + そのセルが存在する列の合計 - そのセルの値
    * 行の合計と列の合計がパパッと出せたら嬉しいよね
        * じゃあ先に計算しておけば良いね

## 007 - CP Classes（★3）

* クエリ処理問題
* にぶたんでOK
* インデックス気をつけてね！leftとか,rightとか
* 番兵作って処理してあげると良き

## 008 - AtCounter（★4）
* 久々の二次元DP
* DP定期的に書かないとインデックス処理とかわけわからなくなる…ひぃ…


## 010 - Score Sum Queries（★2）

* 累積和
* 1組と2組で夫々累積和を作ってあげると、1つのクエリ(L,R)から 1組生徒の合計、2組生徒の合計がそれぞれO(1)で求められるね
* 学籍番号が重複しないことを踏まえてそれぞれの累積和を簡単に作れる点の理解が必要かもしれない…？

## 012 - Red Painting（★4）
* BFS/DFSと思わせておいてのUnionFind
* 赤マスをグループとしてみなして、後は塗りつぶされた赤マスを追加していくだけ
* Gridの管理でちょっと悩んだ末の力技で乗り切った


## 014 - We Used to Sing a Song Together（★3）

* 所謂貪欲法
* 小学生iが通学路でクロスしてる時点で無駄が発生してる
* 縦に線を入れていくイメージ

## 016 - Minimum Coins（★3）

* 愚直な3重ループの全探索を高速化させる
    * a,bが決まればcはループ不要で勝手に決まるよね、というやつ
* O(N^2)で、N=10^4の時もpypyで軽い処理だから？か、通るんだなぁ…。

## 018 - Statue of Chokudai（★3）

* 三角関数、理解してますか？
* sin,cos,tam…ラジアン、ディグリーも。
* mathモジュール大活躍でござるな
    * 小数点以下が合ってないからローカルのテストだとWAになるのめっちゃ心に良くない

## 020 - Log Inequality（★3）

* 018に続いて数学問
* Logの大小比較、できますか？
* 解説ACだったので、忘れた頃に再チャレンジしたい

## 022 - Cubic Cake（★2）

* 最大公約数
* 直方体ではなく、2次元の平面から正方形を切り出したりする方法だったり、次元を落として考えるとわかりやすいかもしれない
* A,B,Cの最大公約数で割ったら良い
* カットするので、-1を忘れずに。

## 024 - Select +／- One（★2）
* 偶奇問題

## 026 - Independent Set on a Tree（★4）
* 二分グラフ？二部グラフ？とかいうやつらしい。
* 木構造の階層で、赤青塗っていくイメージで良かった
* 結局BFSが正義なんですよ

## 027 - Sign Up Requests （★2）

* setで集合管理
* Nの最大値が10^5なので、listで持っちゃうと最大O(N^2)でTLEしちゃいそうな気配…？

## 028 - Cluttered Paper（★4）
* 二次元いもす法
* 何か手順が垢抜けないと言うか…なんとなく、コードが汚い…
* 転置とかも考えると…ううん…処理がかっこわるーい…
* このくらいの処理はスタイリッシュに書きたいなぁ…


## 032 - AtCoder Ekiden（★3）

* PythonはTLE,PyPyでAC通せた
* 無駄を減らしたらもしかしたらPythonでも…？
* ええと…順列を並び替えるやつ。全探索が通る(PyPyで)

## 033 - Not Too Bright（★2）

* 条件を完全に理解できるまで読み込もう
    * 「**完全に**含まれる」 後は、しっかりパターンと規則性考えるだけでOK

## 034 - There are few types of elements（★4）
* しゃくとり法
* 何か上手に組めなくて、変数増えた…
* そのうちリファクタリングしたい

## 038 - Large LCM（★3）

* また数学問題
* タイトル：大きな最小公倍数
* オーバーフローに注意すること
    * int()と、//と、/の違いでWAの数変わる…うーん。本番出たら怪しい

## 042 - Multiple of 9（★4）
* 割と単純な1次元DPに落とし込む
* 問題の解釈が難しかった問題
* modの値とかちゃんと！確認！しようね！

## 044 - Shift and Swapping（★3）

* やりたいことは分かる
* シフトした回数を覚えておいて、T=1,3の時のインデックスをシフトした回数で補正かける
    * dequeとPypyで殴ったら殴れた

## 046 - I Love 46（★3）

* 前処理：余りの数で纏めてあげる
* 一発ACできてよかった
* Counterとかlambdaとか使って綺麗にかけたらいいなぁ…

## 048 - I will not drop out（★3）

* ヒープキューで管理してあげた
* タプルでヒープキューに突っ込む
* 最大値から欲しいので-1かける
* 小技使う感じの問題でした

## 052 - Dice Product（★3）

* 全探索したくないから計算量減らす問題
* 総積を軽く考える問題
* パターンに落とし込む問題

## 055 - Select 5（★2）

* 秒数に甘えて具直前探索
* O(N^5)だけど、処理自体は軽いのもあり。
* 数が大きくなると計算速度一気に遅くなるから積極的にmod取ろうね

## 061 - Deck（★2）

* dequeを使ってappendとappendleftで上下を表現
* dequeもスライスで欲しい位置の要素が取得可能なので、問題無し

## 064 - Uplift（★3）

* 解説AC。悔しい。
* 階差と、状態保持と、変更箇所の差だけを持っていくイメージ

## 067 - Base 8 to 9（★2）

* n進数の変換
* intを使えばn進数→10進数に直せるの便利
* 10進数→n進数への変換はライブラリ化しときたい :TODO

## 069 - Colorful Blocks 2（★3）

* 制約から、ループは無理
* 1つ目のブロックから「何色使える」を考えて、総積を出すイメージ
* 初めてpow関数使った

## 075 - Magic For Balls（★3）

* 素因数分解問題
* 試し割り法で間に合った
    * 素因数分解が1回だったので
    * 複数回行うならエラトステネスの篩とかも要検討

## 076 - Cake Cut（★3）

* 尺取。que使おう。queじゃダメなときは、また何か考えよう
* 円形なので2週するのもワンポイント

## 078 - Easy Graph Problem（★2）

* グラフ問題
* 隣接頂点に対して二分探索
* にぶたん前はソート忘れずに。

## 079 - Two by Two（★3）

* 左上から1マスずつ確定させていくイメージ
* 鳩の巣原理？？？くるっぽー？よくわからない
* 何か、こう、パズルちっくな…。

## 082 - Counting Numbers（★3）

* 範囲で考えるのがしんどかったので、R-Lの累積和的に求めた
* ソースグッチャグチャになる…うぇ…桁数とか文字数とか苦手…
* なんとかAC通せてよかった…

## 084 - There are two types of characters（★3）

* ランレングス圧縮
* 頑張ってキューでしゃくとり的にどうにかなるかなぁと思ったけど難しそうだった