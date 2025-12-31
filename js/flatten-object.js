const data = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3,
            "lol":{
                "name":{
                    "abcd":{
                        "yes":"yes"
                    }
                }
            }
        }
    }
}
const newObject = {}
function flattenIt(item,parentkey="",sept=".") {
    
    for (const [key,values] of Object.entries(item)){
 
        const newKey = parentkey ? `${parentkey}${sept}${key}`:key
        if (typeof values ==='object'){
            flattenIt(values,newKey)
        } else {
            newObject[newKey]=values
        }
    }
}
flattenIt(data)
console.log(newObject)