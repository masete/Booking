
let username = document.getElementById("sign-username");
let first_name = document.getElementById("sign-firstname");
let last_name = document.getElementById("sign-lastname");
let email = document.getElementById("sign-email");
let password = document.getElementById("sign-password");


function signUpAccount() {


    let url = "https://booing-373.herokuapp.com/api/auth/add_user";
    let newUser = {
        username: sign-username.value
        first_name: sign-firstname.value,
        last_name: sign-lastname.value,
        email: sign-email.value,
        password: sign-password.value
        };


    fetch(url, {
        method: "POST",
        headers: {
            "content-type": "application/json",
        },
        body: JSON.stringify(newUser),
    })
//        .then((response) => response.json())
        .then((data) => {
//
            document.getElementById("message").style.display = "block";
            document.getElementById("message").innerHTML = data["data"][0].success;
            window.setTimeout(function () {
                window.location.replace();
            }, 3000);
//
            }
//
//
//        })
//        .catch((error) => console.log(error));

}