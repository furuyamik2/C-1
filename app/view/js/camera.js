window.addEventListener('load', startCamera);

function startCamera() {
    const video = document.getElementById('video');

    // 外カメラを優先する設定
    navigator.mediaDevices.getUserMedia({
        video: {
            facingMode: { exact: "environment" }
        }
    })
    .then((stream) => {
        video.srcObject = stream;
    })
    .catch((error) => {
        console.error("カメラのアクセスが拒否されました:", error);
        alert("カメラにアクセスできませんでした。ブラウザの設定を確認してください。");
    });
}

// 撮影ボタンを取得してクリックイベントを設定
document.getElementById('captureButton').addEventListener('click', captureImage);

function captureImage() {
    const video = document.getElementById('video');
    const canvas = document.createElement('canvas');
    const capturedImage = document.getElementById('capturedImage');

    // Canvasのサイズをビデオのサイズに合わせる
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    // Canvasにビデオの現在のフレームを描画
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    // CanvasをJPEG形式のデータURLに変換
    const imageDataUrl = canvas.toDataURL("image/jpeg");

    // 取得したデータURLをimg要素に設定して表示
    capturedImage.src = imageDataUrl;
    capturedImage.style.display = 'block';

    // 画像をダウンロードするためのリンクを作成して自動的にクリック
    const downloadLink = document.createElement('a');
    downloadLink.href = imageDataUrl;
    downloadLink.download = 'captured_image.jpg';
    downloadLink.click();

     // 撮影後にFood Trackerのページに戻る
     setTimeout(() => {
        window.location.href = 'index.html';  // Food TrackerページのURLを設定
    }, 1000); // 1秒の遅延を入れてページを遷移
}
