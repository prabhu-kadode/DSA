function execute() {
    console.log("##1")
    Promise.resolve(()=>{
        console.log("promise")
    }).then(()=>{
        console.log("i am promise")
    })
    setTimeout(()=>{
        console.log("timeout")
    },0)
    console.log("last#2")
}
//execute()

//Output
// ##1
// last#2
// i am promise
// timeout

for (var i=0;i<3;i++){
    console.log(i)
    setTimeout(()=>{
        console.log(i)
    },0)
    
}
// 333

// for (let i=0;i<3;i++){
//     setTimeout(()=>{
//         console.log(i)
//     },0)  
// }
//012