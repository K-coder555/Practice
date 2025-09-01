import { isNotEmpty } from './validator.js';

const button = document.getElementById("button");
button.addEventListener("click", function() {
    event.preventDefault(); // 폼 제출 방지
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    console.log("이메일:", email);
    console.log("비밀번호:", password);

    if (!isNotEmpty(email) || !isNotEmpty(password)) {
        window.location.href = "https://google.com/"; // 에러 페이지로 리다이렉트
        return;
    }
});