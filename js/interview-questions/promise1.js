function mypromise(value){
    return  new Promise((reject,resolve)=>{
       if (value<=0) {
        reject("Value must be more than 0 ")
       } else {
       resolve(value*10)
       }
    })
}
mypromise(0).then((value)=>{
    console.log("value",value)
}).catch((error)=>{
    console.log(error)
})