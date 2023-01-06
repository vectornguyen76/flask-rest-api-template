function readURL(input) {
    if (input.files && input.files[0]) {

      var reader = new FileReader();

      reader.onload = function(e) {
        $('.image-upload-wrap').hide();

        $('.file-upload-image').attr('src', e.target.result);
        $('.file-upload-content').show();

        $('.image-title').html(input.files[0].name);
      };

      reader.readAsDataURL(input.files[0]);

    } else {
      removeUpload();
    }
   }

   function removeUpload() {
    $('.file-upload-input').replaceWith($('.file-upload-input').clone());
    $('.file-upload-content').hide();
    $('.image-upload-wrap').show();
   }
   $('.image-upload-wrap').bind('dragover', function () {
      $('.image-upload-wrap').addClass('image-dropping');
    });
    $('.image-upload-wrap').bind('dragleave', function () {
      $('.image-upload-wrap').removeClass('image-dropping');
   });


      function ten() {
              //{#ẩn block 1,2#}
              document.getElementById('1').style.display = 'none';
              document.getElementById('2').style.display = 'none';
              //{#xoá và thêm tên class cho thẻ#}
              document.getElementById("img10").classList.add("active");
              document.getElementById("img20").classList.remove("active");
              document.getElementById("img30").classList.remove("active");
          }
      function twenty() {
              //{#ẩn block 2, hiện block 1#}
              document.getElementById('1').style.display = 'block';
              document.getElementById('2').style.display = 'none';
              //{#xoá và thêm tên class cho thẻ#}
              document.getElementById("img10").classList.remove("active");
              document.getElementById("img30").classList.remove("active");
              document.getElementById("img20").classList.add("active");
          }
      function thirty() {
              //{#hiện block 1,2#}
              document.getElementById('1').style.display = 'block';
              document.getElementById('2').style.display = 'block';
              //{#xoá và thêm tên class cho thẻ#}
              document.getElementById("img10").classList.remove("active");
              document.getElementById("img20").classList.remove("active");
              document.getElementById("img30").classList.add("active");
          }