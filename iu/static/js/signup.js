
function signUpAccount() {


    let url = "https://booing-373.herokuapp.com/api/auth/add_user";
    let newUser = {
        username: sign-username.value
        firstname: sign-firstname.value,
        lastname: sign-lastname.value,
        email: sign-email.value,
        password: sign-password.value,

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