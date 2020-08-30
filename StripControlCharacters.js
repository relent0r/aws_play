//strip control characters

var bob = 'dsds\nreer\r'
console.log(bob)
var moobob = bob.replace(/\\r?\\n|\\r/, '').split('\n').join('')

var newbob = bob.replace(/[^\x20-\x7E]/gmi, "")

console.log(newbob)
console.log(moobob)