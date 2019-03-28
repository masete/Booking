
let uname = document.getElementById("sign-username");
let fname = document.getElementById("sign-firstname");
let lname = document.getElementById("sign-lastname");
let email = document.getElementById("sign-email");
let pwd = document.getElementById("sign-password");


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
        headers: {
            "content-type": "application/json",
        },
        body: JSON.stringify(newUser),
    })
        .then((response) => response.json())
        .then((data) => {
//
            document.getElementById("message").style.display = "block";
            document.getElementById("message").innerHTML = data["data"][0].success;
            window.setTimeout(function () {
                window.location.replace();
            }, 3000);
//
            })
//
//

        .catch((error) => console.log(error));

}