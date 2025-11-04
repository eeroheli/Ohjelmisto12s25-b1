
let ye = confirm("Should I calculate the square root?")
if (ye == true) {
    const num = parseInt(prompt('give number'));
    if (num > 0 ){
        document.querySelector(".output").textContent = `square root is ${Math.sqrt(num)}`;
    }
    else {
        document.querySelector(".output").textContent = `The square root of a negative number is not defined`;
    }
}
else {
    document.querySelector(".output").textContent = `"The square root is not calculated."`;
}