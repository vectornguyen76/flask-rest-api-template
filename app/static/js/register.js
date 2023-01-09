document.getElementById("submit").onclick = fn_submit;
function fn_submit() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var confirm_password = document.getElementById("confirm_password").value;

    var format = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;
    
    if (password == "")
    {
        document.getElementById("password-feedback").innerHTML  = "Bạn chưa điền mật khẩu!";
    }
    else
    {
        var length = password.length;
        if (length < 6)
        {
            document.getElementById("password-feedback").innerHTML  = "Mật khẩu phải lớn hơn 6 kí tự!";
        }
    }
    
    if (confirm_password == "")
    {
        document.getElementById("confirm_password-feedback").innerHTML  = "Bạn chưa xác nhận mật khẩu!";
    }
    else
    {
        if(password != confirm_password)
        {
            document.getElementById("confirm_password-feedback").innerHTML  = "Mật khẩu xác nhận không đúng!";
        }
        else
        {
            document.getElementById("confirm_password-feedback").innerHTML  = "";
        }
    }
    
    if (username == "")
    {
        document.getElementById("username-feedback").innerHTML  = "Bạn chưa điền tên đăng nhập!";
    }
    else
    {
        if (format.test(username) == true)
        {
            document.getElementById("username-feedback").innerHTML  = "Tên đăng nhập không chưa kí tự đặc biệt!";
        }   
        else
        {
            post_register();
        }
    }
    
    return false;
}

function post_register(){
              
    let username = document.getElementById("username");
    let password = document.getElementById("password");
      
    // Creating a XHR object
    let xhr = new XMLHttpRequest();
    let url = "register";

    // open a connection
    xhr.open("POST", url, true);

    // Set the request header i.e. which type of content you are sending
    xhr.setRequestHeader("Content-Type", "application/json");

    // Create a state change callback
    xhr.onreadystatechange = function () {
        if (xhr.status === 200) {

            // Print received data from server
            console.log(this.responseText)
            document.getElementById("username-feedback").innerHTML  = "";
            document.getElementById("register-feedback").innerHTML  = "Đăng kí tài khoản thành công!";
        }
        else
        {
            document.getElementById("username-feedback").innerHTML  = "Tên đăng nhập đã tồn tại!";
        }
    };

    // Converting JSON data to string
    var data = JSON.stringify({"username": username.value, "password": password.value});

    // Sending data with the request
    xhr.send(data);
}