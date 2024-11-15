// 日付に基づいてサークルの色を変更する関数
function applyDateStyles() {
    // .tracker-item 要素をすべて取得
    const trackerItems = document.querySelectorAll('.tracker-item');
  
    trackerItems.forEach(item => {
        const dateText = item.querySelector('.date').textContent;  // 日付テキストを取得
        const targetDate = new Date(dateText);  // 目標日を Date オブジェクトに変換
        const currentDate = new Date();  // 現在の日付を取得
  
        // 日数の差を計算
        const diffTime = targetDate - currentDate;
        const remainingDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));  // ミリ秒から日数に変換
  
        // サークル要素を取得し、既存の色クラスを削除
        const circle = item.querySelector('.circle');
        circle.classList.remove('red', 'yellow', 'green');  // 色クラスの削除
  
        // 残り日数に応じて色クラスを追加
        if (remainingDays <= 5) {
            circle.classList.add('red');      // 5日以内
        } else if (remainingDays <= 10) {
            circle.classList.add('yellow');   // 6～10日以内
        } else {
            circle.classList.add('green');    // 10日以上
        }
  
        // 残り日数を日付テキストに追加表示
        item.querySelector('.date').textContent = `${dateText} - 残り${remainingDays}日`;
    });
  }
  
  // ページが読み込まれたときに applyDateStyles 関数を実行
  window.addEventListener('load', applyDateStyles);
  