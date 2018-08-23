// function previewFile(){
//     var preview = document.querySelector("img");
//     var file = document.querySelector('input[type=file]').files[0]
//     var reader = new FileReader();

//     reader.onloadend = function (e) {
//         preview.src = e.target.result;
//     }
//     if(file){
//         reader.readAsDataURL(file);
//     }else{
//         preview.src = "";
//     }
// }

function previewFile(input) {
    var preview = input.nextElementSibling;
    var file = input.files[0];
    var reader = new FileReader();
  
    reader.onloadend = function() {
      preview.src = reader.result;
    }
  
    if (file) {
      reader.readAsDataURL(file);
    } else {
      preview.src = "";
    }
  }

function previewFileUpload(){
    var preview = document.getElementsByClassName("upload_image");
    var file = document.querySelector('input[type=file,name=upload]').files[0];
    console.log(file);
    var reader = new FileReader();

    reader.onloadend =function (e) {
        console.log(e);
        preview.src = reader.result;
    }
    console.log(file);
    if(file){
        reader.readAsDataURL(file);
    }else{
        console.log("This is Bad");
    }
}