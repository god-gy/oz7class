use mongodbtest;

db.createCollection("users", { capped: false});

// 단일 문서 삽입
db.users.insertOne({ name: "Alice", age: 30, address: "123 Maple St" })
db.users.insertOne({ name: "Alice", age: 30, address: ["123 Maple St","345 Maple St","678 Maple St"] })
db.users.insertOne({ name: "Alice", age: 30, city: "Callifornia" })

// 모든 문서 조회
db.users.find();

// 여러 문서 삽입
db.users.insertMany([
    { name: "Bob", age: 25, address: "456 Oak St" },
    { name: "Charlie", age: 35, address: "789 Pine St" }
])

// 특정 필드 조회
db.users.find({}, { name: 1 })
db.users.find({}, { name: 1, address: 1 })

// 조건에 맞는 문서 조회
db.users.find({}, { address: "Maple St" })

// 특정 문서 업데이트
db.users.updateOne({ name: "Alice" }, { $set: { age: 31 } })

// 여러 문서 업데이트
db.users.updateMany({ name: "Alice" }, { $set: { age: 100 } })

// 특정 문서 삭제
db.users.deleteOne({ name: "Alice" })

// 조건에 맞는 여러 문서 삭제
db.users.deleteMany({ name: "Bob" })
