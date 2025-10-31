// print("Hello World!")

console.log("Hello World!");

// 변수
const username = "갓거녕"; // const - 수정불가
let userage = 20; // let - 수정가능

// 함수

// 파이썬
// 함수 정의
// def hello():
//     print("hello")
// 함수 호출
// hello()

// 자바스크립트
// 함수 정의
const hello = () => {
    // 실행할 코드 작성
    console.log("Hello")
}
// 함수 호출
hello()

/**
 * 1. 버튼 태그 가져오기 v
 * 2. 가져온 버튼 태그의 클릭 이벤트 호출하기 v
 * 3. 사용자에게 바꿀 이름 입력받기 (prompt) v
 * 4. 이름 태그 가져오기 v
 * 5. 가져온 이름 태그에 입력 받은 이름으로 변경하기
 */

const buttonEl = document.querySelector('button');
const titleEl = document.querySelector('h2');

buttonEl.addEventListener("click", () => {
    const change_name = window.prompt("변경할 이름을 작성해주세요.");
    console.log("🚀 ~ change_name:", change_name);

    titleEl.innerText = change_name;
});
