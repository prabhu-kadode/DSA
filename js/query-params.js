function formQueryParams(obj) {
    let str = ''
    for (let item in obj) {
        console.log(item)
        str+=`${encodeURIComponent(item)}=${encodeURIComponent(obj[item])}&`
    }
    str = str.slice(0,-1)
    console.log(str)
}
const obj = {
    name:"prabhu",
    age:35,
    city:"Banglore"
}
formQueryParams(obj)