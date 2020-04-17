/*----------------Function to diaplay image on upload---------------------*/

function readURL(input) 
{
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah')
                .attr('src', e.target.result)
                .width(150)
                .height(200);
        };

        reader.readAsDataURL(input.files[0]);
    }
}


function downloadText(){
    var text = document.getElementById('textValue').value;
    var val = "data:x-application/text," + escape(text);
    window.open(val);
}


// /*----------Notifications------------*/

// 