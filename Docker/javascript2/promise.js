const drawButton = document.getElementById('drawButton');
 const messageDiv = document.getElementById('message');
 function drawLottery() {
 return new Promise((resolve, reject) => {
 setTimeout(() => {
 const isWinner = Math.random() < 0.5; // 50% 
isWinner ? resolve("당첨!") : reject("꽝!");
}, 1000);
 });
 }
 drawButton.addEventListener('click', () => {
 messageDiv.textContent = "1초 후 결과가 나옵니다...";
 messageDiv.className = 'message'; // 기본 메시지 클래스 추가
 drawLottery()
 .then(result => {
 messageDiv.textContent = result;
 messageDiv.classList.add('success'); // 
})
 .catch(error => {
 messageDiv.textContent = error;
 messageDiv.classList.add('failure'); // 
});
 }); //결과가 온전하게 전달되는지 확인하기 위해 사용