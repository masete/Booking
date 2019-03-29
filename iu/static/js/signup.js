
let uname = document.getElementById("sign-username");
let fname = document.getElementById("sign-firstname");
let lname = document.getElementById("sign-lastname");
let email = document.getElementById("sign-email");
let pwd = document.getElementById("sign-password");
//let error = document.getElementById("message-error");


function validatePasswordStrength() {
    let passwordError = document.getElementById("password-error");

    if (/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/.test(pwd.value)) {
        passwordError.style.display = "none";
        pwd.setCustomValidity("");

    } else {
        passwordError.style.display = "block";
        passwordError.innerHTML = "Password Must contain a Minimum 8 characters" +
            " with atleast one upper case letter, atleast on lower case letter and atleast one number.";
        pwd.setCustomValidity("Weak Password.");

    }

}

pwd.onkeyup = validatePasswordStrength;
pwd.onchange = validatePasswordStrength;

function displayError(dataArray) {

    for (let key in dataArray) {

        if ({}.hasOwnProperty.call(dataArray, key)) {
            let fieldError = document.getElementById(key + "-error");
            fieldError.style.display = "block";
            fieldError.innerHTML = dataArray[key];
        }
    }
}

function signUpAccount() {


    let url = "https://booing-373.herokuapp.com/api/auth/add_user";
    let newUser = {
        username: uname.value,
        first_name: fname.value,
        last_name: lname.value,
        email: email.value,
        password: pwd.value
        };


    fetch(url, {
        method: "POST",
        mode: "no-cors",
        headers: {
            "content-type": "application/json",
        },
        body: JSON.stringify(newUser),
    })
        .then((response) => response.json())
        .then((data) => {
             if (data.status === 400) {
                //Bad format data
                displayError(data.error);

             }
              else if (data.status === 201) {
                document.getElementById("message-error").style.display = "block";
                 document.getElementById("message-error").innerHTML = "fuck off buddy.";
//                document.getElementById("message-error").innerHTML = data["data"][0].success;
                window.setTimeout(function () {
                window.location.replace("../index.html");
                }, 3000);

              }

            })
        .catch((error) => console.log(error));

}

function cls(){
    lgn.style.display = "none";
    sgn.style.display = "none";
}
