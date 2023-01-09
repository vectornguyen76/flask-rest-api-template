var input = document.getElementById("password");
input.addEventListener("keyup", function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("submit").click();
  }
});
var input2 = document.getElementById("username");
input2.addEventListener("keyup", function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("submit").click();
  }
});

function post_login(){
              
    let username = document.getElementById("username");
    let password = document.getElementById("password");
      
    // Creating a XHR object
    let xhr = new XMLHttpRequest();
    let url = "login";

    // open a connection
    xhr.open("POST", url, true);

    // Set the request header i.e. which type of content you are sending
    xhr.setRequestHeader("Content-Type", "application/json");

    // Create a state change callback
    xhr.onreadystatechange = function () {
        if (xhr.status === 200) {

            // Print received data from server
            console.log(this.responseText)
            window.location.href = "/";
        }
        else
        {
            document.getElementById("notify").innerHTML = "Tên đăng nhập hoặc mật khẩu không chính xác.";
        }
    };

    // Converting JSON data to string
    var data = JSON.stringify({"username": username.value, "password": password.value});

    // Sending data with the request
    xhr.send(data);
}