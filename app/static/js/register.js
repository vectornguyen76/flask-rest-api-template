$(document).ready(function () {
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
            else
            {
                if (format.test(password) == true)
                {
                    document.getElementById("password-feedback").innerHTML  = "Mật khẩu không chưa kí tự đặc biệt!";
                } 
                else
                {
                    document.getElementById("password-feedback").innerHTML  = "";
                }
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
                $.get("/api/account", function (data) 
                {
                    var is_username = true;
                    for (var i in data) 
                    {
                        if (username == data[i].username) 
                        {
                            is_username = false;
                            break;
                        }
                    };
                    if (is_username == true)
                    {
                        document.getElementById("username-feedback").innerHTML  = "";
                        var password_feedback = document.getElementById("password-feedback").innerHTML;
                        var confirm_password_feedback = document.getElementById("confirm_password-feedback").innerHTML;
                        if ((password_feedback == "") && (confirm_password_feedback == ""))
                        {
                            $.post("/api/account", $("#form").serialize(), function () {
                                console.log("data sent");
                                alert('Đăng kí thành công!')
                            });
                        }
                    }
                    else
                    {
                        document.getElementById("username-feedback").innerHTML  = "Tên đăng nhập đã tồn tại!";
                    }
                });
            }
        }
        
        return false;
    }
});