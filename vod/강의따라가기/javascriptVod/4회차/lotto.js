// 요소 선택 및 상수 선언
const todaySpan = document.querySelector("#today")
const numbersDiv = document.querySelector('.numbers')
const drawButton = document.querySelector('#draw')
const resetButton = document.querySelector('#reset')

const lottoNumbers = []
const colors = ['orange', 'skyblue', 'red', 'purple', 'green']

// 날짜 표시
const today = new Date()
let year = today.getFullYear()
let month = today.getMonth() + 1
let date = today.getDate()
todaySpan.textContent = `${year}년 ${month}월 ${date}일 `

// 추첨한 랜덤 숫자를 화면에 표출한다.
function paintNumber(number){
    const eachNumDiv = document.createElement('div')
    eachNumDiv.classList.add('eachnum')
    let colorIndex = Math.floor(number / 10)
    eachNumDiv.style.backgroundColor = colors[colorIndex]
    eachNumDiv.textContent = number
    numbersDiv.appendChild(eachNumDiv)
}

// 배열, 화면 초기화 함수
function clearNumbers() {
    lottoNumbers.splice(0, 6)
    numbersDiv.innerHTML = ""
}

// 추첨 버튼 클릭 이벤트
drawButton.addEventListener('click', function(){
    // 기존 숫자가 있으면 초기화
    clearNumbers()

    // 랜덤 숫자 여섯 개를 생성, 화면 표시
    while(lottoNumbers.length < 6){
        let rn = Math.floor(Math.random() * 45) + 1

        if(lottoNumbers.indexOf(rn) === -1){
            lottoNumbers.push(rn)
            paintNumber(rn)
        }
    }
})

// 다시 버튼 클릭 이벤트
resetButton.addEventListener('click', function() {
    clearNumbers()
});