// 요소 선택 및 배열 선언
const todoList = document.getElementById('todo-list')
const todoForm = document.getElementById('todo-form')
let todoArr = [];

// 1. 할일 추가하기
// 2. 할일 보여주기
// 3. 할일 수정하기
// 4. 할일 삭제하기


// 로컬 저장소에 저장하기
// saveTodos 함수
function saveTodos(){
    const todoSting = JSON.stringify(todoArr)
    localStorage.setItem('myTodos', todoSting)
}

// 로컬 저장소에서 가져오기
// loadTodos 함수
function loadTodos(){
    const myTodos = localStorage.getItem('myTodos') 
    todoArr = myTodos !== null ? JSON.parse(myTodos) : todoArr
    displayTodos()
}

// 4. 할일 삭제하기
// handleTodoDelBtnClick 함수
function handleTodoDelBtnClick(clickedId){
    todoArr = todoArr.filter(function(aTodo){
        return aTodo.todoId !== clickedId
    })
    displayTodos()
    saveTodos()
}

// 3. 할일 수정하기
// handleTodoItemClick 함수
function handleTodoItemClick(clickedId){
    todoArr = todoArr.map(function(aTodo){

        // if(aTodo.todoId === clickedId){
        //     return {
        //         ...aTodo, todoDone: !aTodo.todoDone
        //     }
        // }else{
        //     return aTodo
        // }
        //위 코드를 줄이면 아래의 두줄

        return aTodo.todoId !== clickedId ? 
        aTodo : { ...aTodo, todoDone: !aTodo.todoDone } 
    })
    displayTodos()
    saveTodos()
}

// 2. 할일 보여주기
// displayTodos 함수
function displayTodos(){
    todoList.innerHTML = ""
    todoArr.forEach((aTodo) => {
        const todoItem = document.createElement('li')
        const todoDelBtn = document.createElement('span')
        todoDelBtn.innerText = 'x'
        todoDelBtn.title = '클릭시 삭제됨'
        todoItem.innerText = aTodo.todoText
        todoItem.title = '클릭시 완료됨'

        // if(aTodo.todoDone){
        //     todoItem.classList.add('done')
        // }else{
        //    todoItem.classList.add('yet')
        // }
        // 위 코드를 줄이면 아래의 한줄로 쓸 수 있음.

        
        todoItem.classList.add(aTodo.todoDone ? 'done' : 'yet')
        
        // 1. 할일 추가하기
        todoItem.addEventListener('click', function(){
            handleTodoItemClick(aTodo.todoId)
        })
        
        // 4. 할일 삭제하기
        todoDelBtn.addEventListener('click', function(){
            handleTodoDelBtnClick(aTodo.todoId)
        })
        
        todoItem.appendChild(todoDelBtn)
        todoList.appendChild(todoItem)
    });
}

// 1. 할일 추가하기
// 할일 입력 후 제출하면 발생하는 이벤트 핸들링
todoForm.addEventListener('submit', function(e){
    e.preventDefault()
    const toBeAdded = {
        todoText: todoForm.todo.value,
        todoId: new Date().getTime(),
        todoDone: false // 할일 종료 여부
    }
    todoForm.todo.value = ""    // 할일 추가시 인풋 내 메시지 지우기
    todoArr.push(toBeAdded)
    displayTodos()
    saveTodos()
})

loadTodos() // 시작할 때 한번만!