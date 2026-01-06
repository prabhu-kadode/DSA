console.log("A")
setTimeout(()=>console.log("B"),0)
const promise = new Promise((resolve,reject)=>{
    console.log("D")
    resolve()
})
promise.then(()=>console.log("E"));
(async()=>{
    console.log("C")
    await promise
    console.log("F")
})()

console.log("G")
//ADCGEFB
