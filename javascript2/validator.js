export function isNotEmpty(value) {
    // 문자열의 앞뒤 공백을 제거하고 길이가 0이 아닌지 확인
    if(!value.trim()) {
        alert("값을 입력해주세요.");
        return false;
    }
    return true;
}
