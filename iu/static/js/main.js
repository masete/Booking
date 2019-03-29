var lgn = document.getElementById("login-wrapper");
var sgn = document.getElementById("signup-wrapper");
lgn.style.display = "none";
sgn.style.display = "none";

function login(){
    lgn.style.display = "block";
}

function signin(){
    var username = document.getElementById("login-username");
    var password = document.getElementById("login-password");
    var error = document.getElementById("login-error");

    if( username.value == '' || password.value == ''){
        error.innerHTML = "<strong>Error! </strong> no empty field is allowed";
        error.style.display = "block";

        setTimeout(function(){
            error.style.display = "none";
        }, 3000)
    }else{

        payload = {
            username: username.value,
            password: password.value
        }

        fetch("https://bagzie-send-it-final.herokuapp.com/api/v2/auth/login", {
            method: 'POST',
            mode:'no-cors',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(payload)
        })
        .then(res => res.json())
        .then(function(data){
            if (data['status'] == 'failure'){
                error.innerHTML = "<strong>Error! </strong> " + data['error']['message'];
                error.style.display = "block";
            }else{
                localStorage.setItem('usertype', data['usertype'])
                localStorage.setItem('token', data['token'])
                localStorage.setItem('timer', new Date().getTime())

                if (data['usertype'] == 'admin'){
                    window.location.href = "pages/admin/home.html";
                }else{
                    window.location.href = "pages/user/order.html";
                }
            }
            setTimeout(function(){
                error.style.display = "none";
            }, 3000)
        })
    }
}

function signup(){
    sgn.style.display = "block";
}

function adduser(){
    var usr = document.getElementById("sign-username");
    var first = document.getElementById("sign-firstname");
    var last = document.getElementById("sign-lastname");
    var eml = document.getElementById("sign-email");
    var pas = document.getElementById("sign-password");
    var error = document.getElementById("sign-error");

    let url = "https://booing-373.herokuapp.com/api/auth/add_user";

    if(usr.value == '' && first.value == '' && last.value == '' && eml.value == '' && pas.value == ''){
        error.innerHTML = "<strong>Error! </strong> No empty field is allowed";
        error.style.display = "block";

        setTimeout(function(){
            error.style.display = "none";
        }, 3000)
    }else{
        payload = {
            username: usr.value,
            firstname: first.value,
            lastname: last.value,
            email: eml.value,
            password: pas.value
        }
        console.log(payload)

        fetch(url, {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(payload)
        })
        .then(res => res.json())
        .then(function(data){
            if (data['status'] == 'failure'){
                error.innerHTML = "<strong>Error! </strong> " + data['error']['message'];
                error.style.display = "block";
            }else{
                error.innerHTML = "<strong>Info! </strong> " + data['message'];
                error.style.background = "#16a085";
                error.style.display = "block";
            }
            setTimeout(function(){
                error.style.display = "none";
            }, 3000)
        })
    }
}

function cls(){
    lgn.style.display = "none";
    sgn.style.display = "none";
}

function changedesination(){
    lgn.style.display = "block";
}

function changelocation(){
    sgn.style.display = "block";
}