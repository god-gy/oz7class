// dog api 사용
const apiRandomDogs = "https://dog.ceo/api/breeds/image/random/42"
const apiAllBreeds = "https://dog.ceo/api/breeds/list/all"
const request1 = new XMLHttpRequest()
const request2 = new XMLHttpRequest()

const header = document.getElementById("header")
const main = document.getElementById("main")
const input = document.getElementById("filter-text")
const button = document.getElementById("filter-button")
const select = document.getElementById("filter-select")
const more = document.getElementById("more")
const tothetop = document.getElementById("tothetop")
const reset = document.getElementById("reset")

const currentDogs = []

function displayDogs(item){
    const dogImgDiv = document.createElement("div")
    dogImgDiv.classList.add("flex-item")
    dogImgDiv.innerHTML = `
        <img src = ${item}>
    `
    main.appendChild(dogImgDiv)
}

window.addEventListener("load", function(){
  // 강아지 사진 뿌리기
    request1.open("GET", apiRandomDogs)
    request1.addEventListener("load", function(){
        const response = JSON.parse(request1.response)
        response.message.forEach(function(item){
            currentDogs.push(item)
            displayDogs(item)
        });
    })
    request1.send()

    // 셀렉트에 견종 정보 뿌리기
    request2.open("GET", apiAllBreeds)
    request2.addEventListener("load", function(){
        const response = JSON.parse(request2.response)
        Object.keys(response.message).forEach(function(item){
            const option = document.createElement("option")
            option.textContent = item
            option.value = item
            select.appendChild(option)
        });
    })
    request2.send()
})

// 필터링 버튼 클릭시 필터링된 정보만 표시하기
button.addEventListener("click", function(){
    main.innerHTML = ""
    let filteredDogs = currentDogs.filter(function(item){
        return item.indexOf(input.value) !== -1
    })
    input.value = ""
    filteredDogs.forEach(function(item){
        displayDogs(item)
    });
})

// 셀렉트시 셀렉트된 정보만 표시하기
select.addEventListener("change", function(){
main.innerHTML = ""
    let filteredDogs = currentDogs.filter(function(item){
        return item.indexOf(select.value) !== -1
    })
    filteredDogs.forEach(function(item){
        displayDogs(item)
    });
})

// more 버튼 눌러서 강아지 사진 더 불러와서 추가하고 뿌리기
more.addEventListener("click", function(){
    request1.open("get", apiRandomDogs)
    request1.addEventListener("load", function(){
        const response = JSON.parse(request1.response)
        response.message.forEach(function(item){
            currentDogs.push(item)
            displayDogs(item)
        });
    })
    request1.send()
})

// top 버튼 눌러서 스크롤 맨 위로 올리기
tothetop.addEventListener("click", function(){
    // scrollTo : 주어진 위치로 스크롤을 이동한다.
    window.scrollTo({ top: 0 })
})

// reset 버튼 눌러서 기존 강아지는 모두 지우고 새로운 강아지로 채우기
reset.addEventListener("click", function(){
    // 1. 기존 사진 지우기
    main.innerHTML = ""
    currentDogs.length = 0  // 배열 비우기 (push된 모든 항목 제거)
    
    // 2. 새로운 request 생성 (request1과 분리해서 충돌 방지)
    const requestReset = new XMLHttpRequest()
    requestReset.open("GET", apiRandomDogs)
    requestReset.addEventListener("load", function(){
        const response = JSON.parse(requestReset.response)
        response.message.forEach(function(item){
            currentDogs.push(item)
            displayDogs(item)
        });
    })
    requestReset.send()
})
