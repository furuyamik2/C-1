// 選択肢を表示/非表示にする関数
function showChoices() {
    const choices = document.getElementById('choices');
    choices.style.display = choices.style.display === 'none' ? 'block' : 'none';
}

// 選択肢がクリックされた時の処理
function selectChoice(choice) {
    if (choice === 'Add+') {
        // 新しいページに遷移
        window.location.href = 'camera.html';
    }

    // 選択後に選択肢を非表示
    document.getElementById('choices').style.display = 'none';
}

